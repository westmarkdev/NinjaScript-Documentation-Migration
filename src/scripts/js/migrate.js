import { readdir, readFile, writeFile, mkdir } from 'fs/promises';
import { join, extname } from 'path';
import { createClient } from '@sanity/client';
import dotenv from 'dotenv';
import path from 'path';
import matter from 'gray-matter';

import yaml from 'js-yaml';

// Load environment variables from .env.local
dotenv.config({ path: path.resolve(process.cwd(), '.env.local') });

const {
  NEXT_PUBLIC_SANITY_PROJECT_ID,
  NEXT_PUBLIC_SANITY_DATASET,
  NEXT_PUBLIC_SANITY_WRITE_TOKEN,
} = process.env;

// TODO: We need to figure out how to handle the images before we can import the markdown files
// There are a few options -> The most straightforward would be to:
// 1. Upload the images to Sanity and update the markdown content to use the new URLs
// 1a. We could also update the markdown content to use relative URLs and then upload the images to Sanity

if (!NEXT_PUBLIC_SANITY_PROJECT_ID) {
  throw new Error('NEXT_PUBLIC_SANITY_PROJECT_ID is not set');
}
if (!NEXT_PUBLIC_SANITY_DATASET) {
  throw new Error('NEXT_PUBLIC_SANITY_DATASET is not set');
}
if (!NEXT_PUBLIC_SANITY_WRITE_TOKEN) {
  throw new Error('NEXT_PUBLIC_SANITY_WRITE_TOKEN is not set');
}

const client = createClient({
  projectId: NEXT_PUBLIC_SANITY_PROJECT_ID,
  dataset: NEXT_PUBLIC_SANITY_DATASET,
  token: NEXT_PUBLIC_SANITY_WRITE_TOKEN,
  useCdn: false,
  apiVersion: '2023-05-03',
});

const INPUT_DIR = '../../done/test-sm'; // Directory containing linted Markdown files

/**
 * Asynchronously imports Markdown files from a specified directory, extracts their content,
 * and creates or updates corresponding documents in Sanity.
 *
 * @async
 * @function importMarkdownFiles
 * @throws Will throw an error if there is an issue reading the directory or files, or if there is an issue with the Sanity client.
 *
 * @example
 * // Example usage:
 * importMarkdownFiles()
 *   .then(() => console.log('Import completed'))
 *   .catch(error => console.error('Import failed', error));
 */
async function importMarkdownFiles() {
  try {
    // Read all files in the input directory
    const files = await readdir(INPUT_DIR);
    for (const file of files) {
      // Process only Markdown files
      if (extname(file) === '.md') {
        const filePath = join(INPUT_DIR, file);
        const fileContent = await readFile(filePath, 'utf8');

        // Use gray-matter to parse the frontmatter and content
        const { data: frontmatter, content: markdownContent } =
          matter(fileContent);

        const title = frontmatter.title || '';
        const pathName = frontmatter.pathName
          ? `docs/desktop/${frontmatter.pathName}`
          : '';

        // title and pathName should be required
        if (!title) {
          console.warn(`No title found in file: ${file}`);
          continue;
        }
        if (!pathName) {
          console.warn(`No pathName found in file: ${file}`);
          continue;
        }

        // Construct the document to be sent to Sanity

        // TODO: Auto-generate a draft document ID, set _id to drafts. (nothing after the .).
        const doc = {
          _id: 'drafts.',
          _type: 'desktopSdkDocs',
          title: title,
          pathName: pathName,
          markdown: markdownContent.trim(), // Remove any leading/trailing whitespace
        };

        // Log the document to a unique file in its format for the test plan

        // first we need to make sure the output directory exists
        await mkdir('./output', { recursive: true });

        // Check if the output file already exists
        // BUG: Since the script takes mulitple seconds to run, the file name will be the same for multiple runs
        const outputFilePath = `./output/output-plan-${new Date()
          .toISOString()
          .slice(0, 13)
          .replace(/:/g, '-')}.json`;
        let existingDocs = [];

        try {
          const existingContent = await readFile(outputFilePath, 'utf8');
          existingDocs = JSON.parse(existingContent);

          // Add this check to ensure existingDocs is an array
          if (!Array.isArray(existingDocs)) {
            console.warn(
              'Existing content is not an array. Resetting to an empty array.'
            );
            existingDocs = [];
          }
        } catch (error) {
          // If the file does not exist, we can ignore the error
          if (error.code !== 'ENOENT') {
            console.error('Error reading existing output file:', error);
          }
        }

        // Add the new document to the existing documents array
        existingDocs.push(doc);

        await writeFile(outputFilePath, JSON.stringify(existingDocs, null, 2));

        // Check if the --execute flag is set
        const executeFlag = process.argv.includes('--execute');
        if (executeFlag) {
          // Create or update the document in Sanity
          await client.createOrReplace(doc);
          console.log(`Successfully imported: ${title}`);
        } else {
          console.log(`Test plan created for: ${title}`);
        }
      }
    }
  } catch (error) {
    // Log any errors that occur during the import process
    console.error('Error importing Markdown files:', error);
    throw error;
  }
}

importMarkdownFiles();
