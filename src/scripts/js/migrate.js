const { readdir, readFile } = require('fs').promises;
const { join, extname, basename } = require('path');
const sanityClient = require('@sanity/client');

const {
  NEXT_PUBLIC_SANITY_PROJECT_ID,
  NEXT_PUBLIC_SANITY_DATASET,
  NEXT_PUBLIC_SANITY_WRITE_TOKEN,
} = process.env;

// TODO: We need to figure out how to handle the images before we can import the markdown files
// There are a few options -> The most straightforward would be to:
// 1. Upload the images to Sanity and update the markdown content to use the new URLs
// 1a. We could also update the markdown content to use relative URLs and then upload the images to Sanity

const client = sanityClient({
  projectId: NEXT_PUBLIC_SANITY_PROJECT_ID,
  dataset: NEXT_PUBLIC_SANITY_DATASET,
  token: NEXT_PUBLIC_SANITY_WRITE_TOKEN,
  useCdn: false,
});

const INPUT_DIR = '../output/linted'; // Directory containing linted Markdown files

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
        // Read the content of the Markdown file
        const markdownContent = await readFile(filePath, 'utf8');

        // Extract title from the file name (assuming it matches H1 heading)
        // This is done to use the file name as the document title in Sanity
        const title = basename(file, '.md');

        // Construct the document to be sent to Sanity
        // The pathName is generated based on the title to create a URL-friendly path
        const doc = {
          _type: 'sdkDoc',
          title: title,
          pathName: `/docs/${title.toLowerCase()}`, // Adjust as needed
          markdown: markdownContent,
        };

        // Create or update the document in Sanity
        // This ensures that the document is either created if it doesn't exist or updated if it does
        await client.createOrReplace(doc);
        console.log(`Successfully imported: ${title}`);
      }
    }
  } catch (error) {
    // Log any errors that occur during the import process
    console.error('Error importing Markdown files:', error);
    throw error;
  }
}

importMarkdownFiles();
