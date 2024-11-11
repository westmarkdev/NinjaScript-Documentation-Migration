const fs = require("fs");
const path = require("path");
const https = require("https");
const async = require("async");

const docsFolder = "./docs";
const baseUrl = "https://ninjatrader.com/support/helpguides/nt8/";
const attachmentsFolder = "./attachments";
const reportFile = "./scripts/output/image-report.txt";
const requestTimeout = 10000; // 10 seconds
const downloadDelay = 2000; // 2 seconds delay between downloads
const downloadQueue = async.queue((task, callback) => {
  setTimeout(() => {
    downloadImage(task.url, task.dest)
      .then(() => {
        if (!callback.called) {
          callback.called = true;
          callback();
        }
      })
      .catch((error) => {
        logError(`Failed to download ${task.url}: ${error.message}`);
        // Retry logic
        if (task.retries && task.retries < 3) {
          console.log(
            `Retrying download for ${task.url} (attempt ${task.retries + 1})`
          );
          downloadQueue.push({ ...task, retries: (task.retries || 0) + 1 });
        } else {
          console.log(`Max retries reached for ${task.url}`);
        }
        if (!callback.called) {
          callback.called = true;
          callback();
        }
      });
  }, downloadDelay);
}, 1); // Limit to 1 concurrent download

function logError(message) {
  fs.appendFileSync(reportFile, `${message}\n`);
}

function logSuccess(message) {
  fs.appendFileSync(reportFile, `${message}\n`);
}

function downloadImage(url, dest) {
  return new Promise((resolve, reject) => {
    console.log(`Requesting: ${url}`);
    const file = fs.createWriteStream(dest);

    const options = {
      headers: {
        "User-Agent":
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
      },
    };

    const request = https.get(url, options, (response) => {
      if (response.statusCode === 429) {
        // Too Many Requests - implement exponential backoff
        const retryAfter = parseInt(response.headers["retry-after"]) || 60;
        fs.unlink(dest, () => {});
        reject(new Error(`Rate limited. Retry after ${retryAfter} seconds`));
        return;
      }

      if (response.statusCode !== 200) {
        fs.unlink(dest, () => {});
        reject(new Error(`HTTP status code: ${response.statusCode}`));
        return;
      }

      response.pipe(file);

      file.on("finish", () => {
        file.close();
        console.log(`Downloaded: ${url}`);
        logSuccess(`Downloaded: ${url} to ${dest}`);
        resolve();
      });

      file.on("error", (err) => {
        fs.unlink(dest, () => {});
        reject(err);
      });
    });

    request.on("error", (err) => {
      fs.unlink(dest, () => {});
      reject(err);
    });

    request.setTimeout(requestTimeout, () => {
      request.destroy();
      fs.unlink(dest, () => {});
      reject(new Error("Request timeout"));
    });
  });
}

function processFile(filePath) {
  console.log(`Processing file: ${filePath}`);
  const data = fs.readFileSync(filePath, "utf8");
  
  // Updated regex to handle more image path patterns
  const regex = /!\[.*?\]\(((?:\.\.\/)?[^)]+\.(?:png|jpeg|jpg))\)/gi;
  
  // Add debug logging
  console.log(`File contents: ${data.substring(0, 200)}...`); // Show first 200 chars
  
  let match;
  const fileName = path.basename(filePath, ".md");
  const fileAttachmentsFolder = path.join(attachmentsFolder, fileName);
  let imageFound = false;

  while ((match = regex.exec(data)) !== null) {
    // Add debug logging
    console.log(`Found match: ${JSON.stringify(match)}`);
    
    const imageUrl = match[1];
    console.log(`Extracted image URL: ${imageUrl}`);
    
    if (!imageUrl.match(/\.(png|jpeg|jpg)$/i)) {
      console.log(`Skipping non-image URL: ${imageUrl}`);
      continue;
    }
    
    if (!imageFound) {
      fs.mkdirSync(fileAttachmentsFolder, { recursive: true });
      console.log(`Created directory: ${fileAttachmentsFolder}`);
      imageFound = true;
    }
    
    const imageName = path.basename(imageUrl);
    const fullUrl = `${baseUrl}${imageUrl.replace(/^\.\.?\//, "")}`;
    const dest = path.join(fileAttachmentsFolder, imageName);
    
    console.log(`Processing image:
      Original URL: ${imageUrl}
      Full URL: ${fullUrl}
      Destination: ${dest}
    `);

    if (!fs.existsSync(dest)) {
      console.log(`Found image: ${imageUrl}, queuing download to: ${dest}`);
      downloadQueue.push({
        url: fullUrl,
        dest: dest,
        retries: 0,
      });
    } else {
      console.log(`File already exists: ${dest}, skipping download.`);
    }
  }

  if (!imageFound) {
    fs.promises
      .readdir(fileAttachmentsFolder)
      .then((files) => {
        if (files.length === 0) {
          return fs.promises.rmdir(fileAttachmentsFolder);
        }
      })
      .then(() => {
        console.log(`Deleted empty directory: ${fileAttachmentsFolder}`);
      })
      .catch(() => {});
    console.log(`No images found in file: ${filePath}`);
    logSuccess(`No images found in file: ${filePath}`);
  }
}

function processDirectory(directory) {
  console.log(`Processing directory: ${directory}`);
  fs.readdir(directory, (err, files) => {
    if (err) {
      const errorMessage = `Error reading directory ${directory}: ${err.message}`;
      console.error(errorMessage);
      logError(errorMessage);
      return;
    }
    files.forEach((file) => {
      const filePath = path.join(directory, file);
      try {
        const stats = fs.statSync(filePath);
        if (stats.isDirectory()) {
          processDirectory(filePath);
        } else if (filePath.endsWith(".md")) {
          processFile(filePath);
        }
      } catch (statErr) {
        const errorMessage = `Error processing file/directory ${filePath}: ${statErr.message}`;
        console.error(errorMessage);
        logError(errorMessage);
      }
    });
  });
}

// Clear the report file before starting
fs.writeFileSync(reportFile, "Image Download Report\n====================\n\n");

processDirectory(docsFolder);

downloadQueue.drain(() => {
  console.log("All downloads complete.");
  logSuccess("All downloads complete.");
});
