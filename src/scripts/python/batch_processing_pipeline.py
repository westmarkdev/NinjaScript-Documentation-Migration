import json
import os
import pickle
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
from openai import OpenAI

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
python_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
project_root = os.path.dirname(python_root)
input_dir = os.path.join(project_root, 'input', 'raw')
intermediate_dir = os.path.join(project_root, 'output', 'fixed')
final_output_dir = os.path.join(project_root, 'output', 'final')

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

def process_files_with_checkpointing():
    checkpoint_file = os.path.join(project_root, 'scripts', 'processing_checkpoint.pkl')
    
    # Check if this is the first run
    if not os.path.exists(checkpoint_file):
        print("First-time run detected. Starting from the beginning.")
        processed_files = set()
    else:
        # Load the checkpoint if it exists
        with open(checkpoint_file, 'rb') as f:
            processed_files = pickle.load(f)
        print(f"Resuming from checkpoint. {len(processed_files)} files already processed.")

    files = get_file_sizes(input_dir)
    
    for file, size in tqdm(files, desc="Processing files"):
        if file in processed_files:
            continue
        
        batch_size = adaptive_batch_size(size)
        process_file(file, schema, example_doc)
        
        processed_files.add(file)
        
        with open(checkpoint_file, 'wb') as f:
            pickle.dump(processed_files, f)

    print(f"Processing complete. Checkpoint saved.")

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def get_file_sizes(directory):
    file_sizes = []
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            file_path = os.path.join(directory, filename)
            file_sizes.append((filename, os.path.getsize(file_path)))
    return sorted(file_sizes, key=lambda x: x[1])

def process_file(file_name, schema, example_doc):
    input_file_path = os.path.join(input_dir, file_name)
    intermediate_file_path = os.path.join(intermediate_dir, file_name)
    final_file_path = os.path.join(final_output_dir, file_name)

    os.makedirs(intermediate_dir, exist_ok=True)
    os.makedirs(final_output_dir, exist_ok=True)

    markdown_fixer_script_path = os.path.join(project_root, 'scripts', 'python', 'markdown_fixer_script.py')
    subprocess.run(['python', markdown_fixer_script_path, input_file_path])
    
    if not os.path.exists(intermediate_file_path):
        print(f"markdown_fixer_script.py did not create the expected output file: {intermediate_file_path}")
        return
    
    with open(intermediate_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    completion = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are an AI assistant that specializes in formatting markdown documents according to a defined schema. The goal is to ensure the document adheres strictly to the provided schema. Only respond with valid markdown content according to the schema and the example provided. Use markdownlint rules to ensure the output is correct markdown."},
            {"role": "system", "content": f"Here is the formatting schema you need to follow: {schema}. This schema includes proper YAML front matter and Markdown-specific rules."},
            {"role": "user", "content": f"Here is an example of a correctly formatted document: {example_doc}. Take note of how the formatting follows the schema, especially in areas like headers, metadata, and code blocks. Note: The output content must NOT be wrapped in triple backticks. Use markdownlint rules to ensure the output is correct markdown. MD047/single-trailing-newline: Files should end with a single newline character"},
            {"role": "user", "content": f"Now, please format the following document according to the schema and the provided example. Ensure that the YAML front matter is properly structured, all Markdown content is valid, and formatting issues are corrected: {content}"},
            {"role": "system", "content": "After formatting the document, ensure that all content complies with the schema. If there are any parts that do not fit, apply corrections or suggest changes."}
        ]
    )
    
    formatted_content = completion.choices[0].message.content
    
    with open(final_file_path, 'w', encoding='utf-8') as file:
        file.write(formatted_content)

    print(f"Processed {file_name} successfully.")

def process_batch(batch, schema, example_doc):
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(process_file, file_name, schema, example_doc) for file_name in batch]
        for future in as_completed(futures):
            future.result()

def main():
    files = get_file_sizes(input_dir)
    
    batch_size = BATCH_SIZE
    total_batches = (len(files) + batch_size - 1) // batch_size
    
    for i in tqdm(range(0, len(files), batch_size), total=total_batches, desc="Processing batches"):
        batch = [file[0] for file in files[i:i+batch_size]]
        process_batch(batch, schema, example_doc)

if __name__ == "__main__":
    process_files_with_checkpointing()