import { readdir, readFile, writeFile, mkdir } from "fs/promises";
import { join, extname } from "path";
import { createClient } from "@sanity/client";
import dotenv from "dotenv";
import path from "path";
import matter from "gray-matter";
import crypto from "crypto";

dotenv.config({ path: path.resolve(process.cwd(), ".env.local") });

const {
  NEXT_PUBLIC_SANITY_PROJECT_ID,
  NEXT_PUBLIC_SANITY_DATASET,
  NEXT_PUBLIC_SANITY_WRITE_TOKEN,
} = process.env;

if (
  !NEXT_PUBLIC_SANITY_PROJECT_ID ||
  !NEXT_PUBLIC_SANITY_DATASET ||
  !NEXT_PUBLIC_SANITY_WRITE_TOKEN
) {
  throw new Error("Missing required environment variables");
}

const client = createClient({
  projectId: NEXT_PUBLIC_SANITY_PROJECT_ID,
  dataset: NEXT_PUBLIC_SANITY_DATASET,
  token: NEXT_PUBLIC_SANITY_WRITE_TOKEN,
  useCdn: false,
  apiVersion: "2023-05-03",
});

const INPUT_DIR = "./";

function generateHash(keyword) {
  return crypto.createHash("sha256").update(keyword).digest("hex");
}

async function processMarkdownFiles(executeFlag, forceUpdate) {
  const timestamp = new Date()
    .toISOString()
    .replace(/:/g, "-")
    .replace(/\..+/, "");
  const uniqueSuffix = Math.random().toString(36).substring(2, 8);
  const outputFilePath = `./scripts/output/migration-plan-${timestamp}-${uniqueSuffix}.json`;
  let allDocs = [];

  async function processDirectory(dir) {
    const entries = await readdir(dir, { withFileTypes: true });

    for (const entry of entries) {
      const fullPath = join(dir, entry.name);

      if (entry.isDirectory()) {
        await processDirectory(fullPath);
      } else if (extname(entry.name) === ".md") {
        try {
          const fileContent = await readFile(fullPath, "utf8");
          const { data: frontmatter, content: markdownContent } =
            matter(fileContent);

          // Handle duplicate keys by using the last occurrence
          const cleanedFrontmatter = Object.entries(frontmatter).reduce(
            (acc, [key, value]) => {
              acc[key.toLowerCase()] = value; // Standardize to lowercase keys
              return acc;
            },
            {}
          );

          if (
            cleanedFrontmatter.status === "ready" ||
            cleanedFrontmatter.status === "updated"
          ) {
            const doc = {
              _id: `${generateHash(cleanedFrontmatter.pathname)}`,
              _type: "desktopSdkDoc",
              title: cleanedFrontmatter.title,
              pathName: cleanedFrontmatter.pathname,
              parent: cleanedFrontmatter.parent,
              order: cleanedFrontmatter.order
                ? parseInt(cleanedFrontmatter.order, 10)
                : 0,
              //status: cleanedFrontmatter.status, Don't include status in the migration
              section: cleanedFrontmatter.section,
              markdown: markdownContent.trim(),
            };

            allDocs.push(doc);
          }
        } catch (error) {
          console.error(`Error processing file ${fullPath}:`, error.message);
          // Continue to the next file instead of stopping the entire process
        }
      }
    }
  }

  await processDirectory(INPUT_DIR);

  await mkdir("./scripts/output", { recursive: true });
  await writeFile(outputFilePath, JSON.stringify(allDocs, null, 2));
  console.log(`Migration plan created at: ${outputFilePath}`);

  if (executeFlag) {
    console.log("Executing migration...");
    for (const doc of allDocs) {
      try {
        // Check if the document already exists
        const existingDoc = await client.getDocument(doc._id);

        if (existingDoc) {
          // Document exists, decide whether to update
          if (forceUpdate || doc.status === "updated") {
            await client
              .patch(doc._id)
              .set(doc)
              .commit()
              .then((updatedDoc) => {
                console.log(`Document updated: ${updatedDoc.title}`);
              })
              .catch((err) => {
                console.error(
                  `Document update failed for ${doc.title}:`,
                  err.message
                );
              });
          } else {
            console.log(`Skipping existing document: ${doc.title}`);
          }
        } else {
          // Document doesn't exist, create it
          await client.create(doc).then((createdDoc) => {
            console.log(`Created: ${createdDoc.title}`);
          });
        }
      } catch (error) {
        console.error(`Error processing ${doc.title}:`, error.message);
      }
    }
  }
}

const args = process.argv.slice(2);
const executeFlag = args.includes("--execute");
const forceUpdate = args.includes("--force");

processMarkdownFiles(executeFlag, forceUpdate)
  .then(() => console.log("Migration process completed"))
  .catch((error) => console.error("Migration failed:", error));
