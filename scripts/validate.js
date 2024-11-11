// Import required libraries
import { createClient } from "@sanity/client";
import { promisify } from "util";
import dotenv from "dotenv";
import path from "path";
import async from "async";
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

// Define the document type and field to check
const DOCUMENT_TYPE = "desktopSdkDoc"; // Replace with your document type
const FIELD_NAME = "markdown"; // Replace with the field that contains the links

// Enhanced link pattern matching
const INVALID_LINK_PATTERN = /\[(.*?)\]\((.*?\.(?:md|htm))\)/g;

// Function to extract and validate links from markdown content
const validateLinks = (markdownContent) => {
  if (typeof markdownContent !== "string") {
    return [];
  }

  const matches = [...markdownContent.matchAll(INVALID_LINK_PATTERN)];
  return matches.map((match) => ({
    linkText: match[1],
    invalidUrl: match[2],
  }));
};

const validateDocumentsInBatches = async () => {
  try {
    console.log("\n🔍 Starting document validation...\n");

    // Fetch all documents of the specified type
    const query = `*[_type == "${DOCUMENT_TYPE}"]{_id, title, ${FIELD_NAME}}`;
    const documents = await client.fetch(query);

    console.log(`📚 Found ${documents.length} documents to validate`);
    console.log(`🔄 Processing in batches of 10...\n`);

    let processedCount = 0;
    let documentsWithInvalidLinks = 0;

    // Create a queue to process documents in batches
    const queue = async.queue(async (doc, callback) => {
      processedCount++;
      const markdownContent = doc[FIELD_NAME];

      console.log(
        `\n📄 Processing document ${processedCount}/${documents.length}`
      );
      console.log(`   ID: ${doc._id}`);
      console.log(`   Title: ${doc.title || "Untitled"}`);

      if (!markdownContent) {
        console.log("   ⚠️  No markdown content found");
        callback();
        return;
      }

      const invalidLinks = validateLinks(markdownContent);

      if (invalidLinks.length > 0) {
        documentsWithInvalidLinks++;
        console.log("   ❌ Invalid links found:");
        invalidLinks.forEach(({ linkText, invalidUrl }) => {
          console.log(`      - "${linkText}": ${invalidUrl}`);
        });
      } else {
        console.log("   ✅ No invalid links found");
      }

      // Add a small delay to prevent rate limiting
      setTimeout(callback, 100);
    }, 10);

    // Add completion handler
    queue.drain(() => {
      console.log("\n✨ Validation complete!");
      console.log(`📊 Summary:`);
      console.log(`   - Total documents processed: ${processedCount}`);
      console.log(
        `   - Documents with invalid links: ${documentsWithInvalidLinks}`
      );
      console.log(
        `   - Documents with valid links: ${
          processedCount - documentsWithInvalidLinks
        }\n`
      );
    });

    // Push all documents to the queue
    queue.push(documents);

    // Wait for the queue to drain
    await promisify(queue.drain.bind(queue))();
  } catch (error) {
    console.error("\n❌ Error validating documents:", error);
  }
};

validateDocumentsInBatches();
