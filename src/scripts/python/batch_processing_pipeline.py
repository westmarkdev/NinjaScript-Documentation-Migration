import json
import os
import sys
import pickle
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
from openai import OpenAI
from datetime import datetime
import logging

BATCH_SIZE = 2
MODEL = "gpt-4o-mini"

# project-root/
# ├── scripts/
# │   ├── python/
# │   │   ├── batch_processing_pipeline.py
# │   │   ├── markdown_fixer_script.py
# │   ├── js/
# │   │   ├── migrate.js
# │   │   ├── sanity.json
# ├── input/
# │   ├── raw/
# │   │   ├── *.md
# │   ├── linted/
# │   │   ├── *.md
# ├── output/
# │   ├── fixed/
# │   │   ├── *.md
# │   ├── final/
# │   │   ├── *.md
# ├── sanity/
# │   ├── schema.json
# ├── example_doc.md

# project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
project_root = "src"
input_dir = os.path.join(project_root, 'input', 'raw') # these are the files that are raw and need to be processed
intermediate_dir = os.path.join(project_root, 'output', 'fixed') # these are the files that are fixed by the markdown_fixer_script.py
final_output_dir = os.path.join(project_root, 'output', 'final') # these are the files that are the final output and are used for the website.

os.makedirs(intermediate_dir, exist_ok=True)
os.makedirs(final_output_dir, exist_ok=True)

schema_path = os.path.join(project_root, 'sanity', 'schema.json')
example_doc_path = os.path.join(project_root, 'example_doc.md')

with open(schema_path, 'r') as f:
    schema = f.read()

with open(example_doc_path, 'r') as f:
    example_doc = f.read()

def adaptive_batch_size(file_size):
    if file_size < 1000:
        return 50
    elif file_size < 10000:
        return 20
    else:
        return 10

def get_file_sizes(input_dir):
    file_info = []
    for root, dirs, filenames in os.walk(input_dir):
        for filename in filenames:
            file_path = os.path.join(root, filename)
            file_size = os.path.getsize(file_path)
            file_info.append((file_path, file_size))
    return file_info

def process_files_with_checkpointing(remote=False):
    # Separate checkpoints for local and remote processing
    local_checkpoint_file = os.path.join(project_root, 'scripts', 'local_processing_checkpoint.pkl')
    remote_checkpoint_file = os.path.join(project_root, 'scripts', 'remote_processing_checkpoint.pkl')

    # Initialize processed files
    processed_local_files = set()
    processed_remote_files = set()

    # Load local processing checkpoint
    if os.path.exists(local_checkpoint_file):
        with open(local_checkpoint_file, 'rb') as f:
            processed_local_files = pickle.load(f)
        logging.info(f"Resuming from local checkpoint. {len(processed_local_files)} files already processed locally.")
    else:
        logging.info("No local checkpoint found. Starting from the beginning.")

    # Load remote processing checkpoint
    if remote and os.path.exists(remote_checkpoint_file):
        with open(remote_checkpoint_file, 'rb') as f:
            processed_remote_files = pickle.load(f)
        logging.info(f"Resuming from remote checkpoint. {len(processed_remote_files)} files already processed remotely.")
    else:
        logging.info("No remote checkpoint found. Starting from the beginning.")

    files = get_file_sizes(input_dir)
    logging.info(f"Total files to process: {len(files)}")
    processing_logs.append(f"Total files to process: {len(files)}")

    for file, size in tqdm(files, desc="Processing files"):
        # Skip files already processed locally
        if file in processed_local_files:
            #logging.info(f"Skipping already processed local file: {file}")
            processing_logs.append(f"Skipping already processed local file: {file}")
            continue

        batch_size = adaptive_batch_size(size)
        #logging.info(f"Processing file: {file} (size: {size} bytes, batch size: {batch_size})")
        processing_logs.append(f"Processing file: {file} (size: {size} bytes, batch size: {batch_size})")
        error_occurred = process_file(file)

        if error_occurred:
            logging.error(f"Error occurred while processing {file}. Skipping remote processing.")
            continue

        # Save the local processing checkpoint
        processed_local_files.add(file)
        with open(local_checkpoint_file, 'wb') as f:
            pickle.dump(processed_local_files, f)

        # Remote processing only if specified and not already processed
        if remote and file not in processed_remote_files:
            #logging.info(f"Starting remote processing for file: {file}")
            processing_logs.append(f"Starting remote processing for file: {file}")
            process_remote(file, schema, example_doc)
            processed_remote_files.add(file)
            with open(remote_checkpoint_file, 'wb') as f:
                pickle.dump(processed_remote_files, f)

def process_file(file_path):
    file_name = os.path.basename(file_path)
    input_file_path = file_path
    intermediate_file_path = os.path.join(intermediate_dir, file_name)

    #logging.info(f"Processing file: {file_name}")
    processing_logs.append(f"Processing file: {file_name}")
    #logging.info(f"Input path: {input_file_path}")
    processing_logs.append(f"Input path: {input_file_path}")
    #logging.info(f"Intermediate path: {intermediate_file_path}")
    processing_logs.append(f"Intermediate path: {intermediate_file_path}")

    os.makedirs(os.path.dirname(intermediate_file_path), exist_ok=True)

    markdown_fixer_script_path = os.path.join(project_root, 'scripts', 'python', 'markdown_fixer_script.py')
    #logging.info(f"Running markdown_fixer_script.py on {input_file_path}")
    processing_logs.append(f"Running markdown_fixer_script.py on {input_file_path}")
    subprocess.run(['python', markdown_fixer_script_path, input_file_path, intermediate_file_path])

    if not os.path.exists(intermediate_file_path):
        log_message = f"Error: markdown_fixer_script.py did not create the expected output file: {intermediate_file_path}"
        #logging.error(log_message)
        processing_logs.append(log_message)
        return True  # Indicate an error occurred

    log_message = f"Processed {file_path} successfully."
    #logging.info(log_message)
    processing_logs.append(log_message)
    return False  # Indicate no error occurred

def process_remote(file_path, schema, example_doc):
    file_name = os.path.basename(file_path)
    intermediate_file_path = os.path.join(intermediate_dir, file_name)
    final_file_path = os.path.join(final_output_dir, file_name)

    #logging.info(f"Remote processing file: {file_name}")
    processing_logs.append(f"Remote processing file: {file_name}")
    #logging.info(f"Intermediate path: {intermediate_file_path}")
    processing_logs.append(f"Intermediate path: {intermediate_file_path}")
    #logging.info(f"Final path: {final_file_path}")
    processing_logs.append(f"Final path: {final_file_path}")

    os.makedirs(os.path.dirname(final_file_path), exist_ok=True)

    if not os.path.exists(intermediate_file_path):
        log_message = f"Error: Intermediate file not found: {intermediate_file_path}"
        #logging.error(log_message)
        processing_logs.append(log_message)
        return True  # Indicate an error occurred
    
    with open(intermediate_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    logging.info(f"Sending content to OpenAI for processing (file: {file_path})")
    processing_logs.append(f"Sending content to OpenAI for processing (file: {file_path})")
    client = OpenAI()
    completion = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are an AI assistant that specializes in formatting markdown documents according to a defined schema. The goal is to ensure the document adheres strictly to the provided schema. Only respond with valid markdown content according to the schema and the example provided. Use markdownlint rules to ensure the output is correct markdown."},
            {"role": "system", "content": f"Here is the formatting schema you need to follow: {schema}. This schema includes proper YAML front matter and Markdown-specific rules."},
            {"role": "user", "content": f"""Here is an example of a correctly formatted document: {example_doc}. Pay close attention to how the formatting adheres to the schema, particularly in areas like headers, metadata, code blocks, and tables. Callouts are in the format `{{% callout type="callout_type" %}}...{{% /callout %}}` and support standard markdown. However Markdown tables containing nested bulleted lists do not support HTML tags like ordered lists or tables. To handle this, use `{{% <br> %}}` to insert line breaks within the table cells. For each bullet point, use `&bull;` followed by `{{% <br> %}}` to move to the next line. This ensures proper formatting without using nested HTML. Additionally, ensure the output content is NOT enclosed in triple backticks. Apply markdownlint rules to validate the markdown, especially ensuring the file ends with a single newline character (MD047/single-trailing-newline). Lists should be surrounded by blank lines. **Important: When encountering links in the format `[barsperiod.md](barsperiod.md)` or `[barsperiod](/barsperiod)`, they must be corrected to `[BarsPeriod](/docs/desktop/barsperiod)`**."""},
            {"role": "user", "content": f"Now, please format the following document according to the schema and the provided example. Ensure that the YAML front matter is properly structured, all Markdown content is valid, and formatting issues are corrected: {content}"},
            {"role": "system", "content": "After formatting the document, ensure that all content complies with the schema. If there are any parts that do not fit, apply corrections or suggest changes."}
        ]
    )

    formatted_content = completion.choices[0].message.content
    
    with open(final_file_path, 'w', encoding='utf-8') as file:
        file.write(formatted_content)

    log_message = f"Remote processed {file_path} successfully."
    #logging.info(log_message)
    processing_logs.append(log_message)
    return False  # Indicate no error occurred

def process_batch(batch, schema, example_doc):
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(process_file, file_path) for file_path in batch]
        for future in as_completed(futures):
            future.result()

def main():
    logging.info("Starting batch processing pipeline")
    files = get_file_sizes(input_dir)
    #logging.info(f"Total files to process: {len(files)}")
    processing_logs.append(f"Total files to process: {len(files)}")
    
    batch_size = BATCH_SIZE
    total_batches = (len(files) + batch_size - 1) // batch_size
    #logging.info(f"Batch size: {batch_size}, Total batches: {total_batches}")
    processing_logs.append(f"Batch size: {batch_size}, Total batches: {total_batches}")
    
    for i in tqdm(range(0, len(files), batch_size), total=total_batches, desc="Processing batches"):
        batch = [file[0] for file in files[i:i+batch_size]]
        #logging.info(f"Processing batch {i//batch_size + 1}/{total_batches}")
        processing_logs.append(f"Processing batch {i//batch_size + 1}/{total_batches}")
        process_batch(batch, schema, example_doc)

    #logging.info("Batch processing pipeline completed")
    processing_logs.append("Batch processing pipeline completed")
    generate_report()

processing_logs = []

def generate_report():
    logging.info("Generating report")
    with open(os.path.join(project_root, 'scripts', 'processing_report.txt'), 'w') as f:
        for log in processing_logs:
            f.write(log + '\n')
    logging.info("Report generated")

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    logging.info("Starting batch processing script")
    # get --remote flag
    remote = "--remote" in sys.argv
    if remote:
        logging.info("Running in remote mode")
    else:
        logging.info("Running in local mode")
    process_files_with_checkpointing(remote)
    logging.info("Batch processing script completed")