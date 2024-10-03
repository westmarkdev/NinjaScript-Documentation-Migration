import json
from openai import OpenAI
import os
import pickle
import subprocess
import shutil
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

BATCH_SIZE = 20
MODEL="gpt-4o-mini"

script_dir = os.path.dirname(os.path.abspath(__file__))
input_dir = os.path.join(script_dir, 'input')
intermediate_dir = os.path.join(script_dir, 'output', 'fixed-latest')
final_output_dir = os.path.join(script_dir, 'output', 'final')

os.makedirs(intermediate_dir, exist_ok=True)
os.makedirs(final_output_dir, exist_ok=True)

schema = open(os.path.join(script_dir, 'schema.json'), 'r').read()
example_doc = open(os.path.join(script_dir, 'example_doc.md'), 'r').read()

def adaptive_batch_size(file_size):
    if file_size < 1000:  # Small files
        return 50
    elif file_size < 10000:  # Medium files
        return 20
    else:  # Large files
        return 10

def process_files_with_checkpointing():
    checkpoint_file = os.path.join(script_dir, 'processing_checkpoint.pkl')
    
    if os.path.exists(checkpoint_file):
        with open(checkpoint_file, 'rb') as f:
            processed_files = pickle.load(f)
    else:
        processed_files = set()

    files = get_file_sizes(input_dir)
    
    for file, size in tqdm(files, desc="Processing files"):
        if file in processed_files:
            continue
        
        batch_size = adaptive_batch_size(size)
        process_file(file, schema, example_doc)
        
        processed_files.add(file)
        
        # Checkpoint after each file
        with open(checkpoint_file, 'wb') as f:
            pickle.dump(processed_files, f)

    # Clean up checkpoint file after successful completion
    os.remove(checkpoint_file)

# Set your OpenAI API key in the environment variable OPENAI_API_KEY
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
    intermediate_dir_path = os.path.join(script_dir, 'output', 'fixed-latest')
    intermediate_file_path = os.path.join(intermediate_dir_path, file_name)
    final_output_dir_path = os.path.join(script_dir, 'output', 'final')
    final_file_path = os.path.join(final_output_dir_path, file_name)

    # Ensure directories exist
    os.makedirs(intermediate_dir_path, exist_ok=True)
    os.makedirs(final_output_dir_path, exist_ok=True)

    # Step 1: Run Python script
    # Ensure the markdown_fixer_script is correctly referenced from the ./scripts directory
    print(f"Running markdown_fixer_script.py on {input_file_path}")
    markdown_fixer_script_path = os.path.join(script_dir, 'scripts', 'markdown-fixer-script.py')
    subprocess.run(['python', markdown_fixer_script_path, input_file_path])
    
    # Check if the markdown_fixer_script.py created the output file
    if not os.path.exists(intermediate_file_path):
        print(f"markdown_fixer_script.py did not create the expected output file: {intermediate_file_path}")
        print("Copying original file to intermediate directory for further processing.")
        shutil.copy2(input_file_path, intermediate_file_path)
    
    # Step 2: Process with OpenAI
    # FIXME: The output content should NOT be wrapped in triple backticks. Process these files as if they are markdown with YAML front matter.
    if os.path.exists(intermediate_file_path):
        with open(intermediate_file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    else:
        print(f"File not found: {intermediate_file_path}")
        return
    
    completion = client.chat.completions.create(
        model=MODEL,
        messages = [
            {"role": "system", "content": "You are an AI assistant that specializes in formatting markdown documents according to a defined schema. The goal is to ensure the document adheres strictly to the provided schema. Only respond with valid markdown content according to the schema and the example provided. Use markdownlint rules to ensure the output is correct markdown."},
            
            # Step 1: Present the Schema
            {"role": "system", "content": f"Here is the formatting schema you need to follow: {schema}. This schema includes proper YAML front matter and Markdown-specific rules."},
            
            # Step 2: Provide a Reference Example
            {"role": "user", "content": f"Here is an example of a correctly formatted document: {example_doc}. Take note of how the formatting follows the schema, especially in areas like headers, metadata, and code blocks. Note: The output content must NOT be wrapped in triple backticks. Use markdownlint rules to ensure the output is correct markdown. MD047/single-trailing-newline: Files should end with a single newline character"},

            # Step 3: Format the Provided Content
            {"role": "user", "content": f"Now, please format the following document according to the schema and the provided example. Ensure that the YAML front matter is properly structured, all Markdown content is valid, and formatting issues are corrected: {content}"},
            
            # Step 4: Validate Against Schema
            {"role": "system", "content": "After formatting the document, ensure that all content complies with the schema. If there are any parts that do not fit, apply corrections or suggest changes."}
        ]

            )
    
    formatted_content = completion.choices[0].message.content
    
    with open(final_file_path, 'w', encoding='utf-8') as file:
        file.write(formatted_content)

    # Step 3: CLI linting (using Prettier and markdownlint)
    # subprocess.run(['npx', 'prettier', '--write', final_file_path])
    # subprocess.run(['npx', 'markdownlint', '--fix', final_file_path])

    print(f"Processed {file_name} successfully.")

def process_batch(batch, schema, example_doc):
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(process_file, file_name, schema, example_doc) for file_name in batch]
        for future in as_completed(futures):
            future.result()  # This will raise any exceptions that occurred during processing

def main():
    files = get_file_sizes(input_dir)
    
    batch_size = BATCH_SIZE
    total_batches = (len(files) + batch_size - 1) // batch_size
    
    for i in tqdm(range(0, len(files), batch_size), total=total_batches, desc="Processing batches"):
        batch = [file[0] for file in files[i:i+batch_size]]
        process_batch(batch, schema, example_doc)

if __name__ == "__main__":
    process_files_with_checkpointing()