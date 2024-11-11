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

const DOCUMENT_TYPE = "desktopSdkDoc";
const FIELD_NAME = "markdown";

// Regex patterns for table validation
const TABLE_PATTERNS = {
  tableStart: /{% table %}/g,
  tableEnd: /{% \/table %}/g,
  headerRow: /^\* .*$/gm,
  divider: /^---$/gm,
  dataRow: /^\* .*$/gm,
};

const validateTable = (tableContent) => {
  const issues = [];

  // Remove leading/trailing whitespace
  const trimmedContent = tableContent.trim();

  // Split into lines
  const lines = trimmedContent.split("\n").map((line) => line.trim());

  // Basic structure checks
  if (!lines[0].includes("{% table %}")) {
    issues.push("Table must start with {% table %}");
  }

  if (!lines[lines.length - 1].includes("{% /table %}")) {
    issues.push("Table must end with {% /table %}");
  }

  // Find header section
  const headerLines = lines.filter(
    (line) =>
      line.startsWith("* ") && lines.indexOf(line) < lines.indexOf("---")
  );

  if (headerLines.length === 0) {
    issues.push("No header row found");
  }

  // Count columns in header
  const headerColumnCount =
    headerLines.length > 0
      ? headerLines.map((line) => line.split("* ")[1]).length
      : 0;

  // Check data rows
  let foundDivider = false;
  let currentRow = [];

  lines.forEach((line, index) => {
    if (line === "---") {
      foundDivider = true;
      if (currentRow.length > 0) {
        if (currentRow.length !== headerColumnCount) {
          issues.push(
            `Row ${index} has ${currentRow.length} columns, expected ${headerColumnCount}`
          );
        }
        currentRow = [];
      }
    } else if (line.startsWith("* ") && foundDivider) {
      currentRow.push(line);
    }
  });

  if (!foundDivider) {
    issues.push("No divider (---) found between header and data");
  }

  return issues;
};

const extractTables = (markdownContent) => {
  const tables = [];
  let currentTable = "";
  let insideTable = false;

  markdownContent.split("\n").forEach((line) => {
    if (line.includes("{% table %}")) {
      insideTable = true;
      currentTable = line + "\n";
    } else if (line.includes("{% /table %}")) {
      insideTable = false;
      currentTable += line;
      tables.push(currentTable);
      currentTable = "";
    } else if (insideTable) {
      currentTable += line + "\n";
    }
  });

  return tables;
};

const validateDocumentsInBatches = async () => {
  try {
    console.log("\n🔍 Starting table validation...\n");

    const query = `*[_type == "${DOCUMENT_TYPE}"]{_id, title, ${FIELD_NAME}}`;
    const documents = await client.fetch(query);

    console.log(`📚 Found ${documents.length} documents to validate`);
    console.log(`🔄 Processing in batches of 10...\n`);

    let processedCount = 0;
    let documentsWithTables = 0;
    let documentsWithTableIssues = 0;

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

      const tables = extractTables(markdownContent);

      if (tables.length > 0) {
        documentsWithTables++;
        console.log(`   📊 Found ${tables.length} tables`);

        tables.forEach((table, index) => {
          const issues = validateTable(table);

          if (issues.length > 0) {
            documentsWithTableIssues++;
            console.log(`   ❌ Issues in table ${index + 1}:`);
            issues.forEach((issue) => {
              console.log(`      - ${issue}`);
            });
            // Log problematic table for inspection
            console.log("   Table content:");
            console.log(table);
          } else {
            console.log(`   ✅ Table ${index + 1} is valid`);
          }
        });
      } else {
        console.log("   ℹ️  No tables found in document");
      }

      setTimeout(callback, 100);
    }, 10);

    queue.drain(() => {
      console.log("\n✨ Validation complete!");
      console.log(`📊 Summary:`);
      console.log(`   - Total documents processed: ${processedCount}`);
      console.log(`   - Documents with tables: ${documentsWithTables}`);
      console.log(
        `   - Documents with table issues: ${documentsWithTableIssues}`
      );
      console.log(
        `   - Documents with valid tables: ${
          documentsWithTables - documentsWithTableIssues
        }\n`
      );
    });

    queue.push(documents);
    await promisify(queue.drain.bind(queue))();
  } catch (error) {
    console.error("\n❌ Error validating documents:", error);
  }
};

validateDocumentsInBatches();
