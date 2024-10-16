import os
import re
import yaml
import html
from pathlib import Path
import sys
from datetime import datetime
import logging

# Configuration
LINT_CONFIG_PATH = '.markdownlint.json'
IMAGE_LOG_FILE = 'files_with_images.txt'
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# Add this after the imports
#logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def read_markdown_files(input_dir):
    """Reads all Markdown files in the specified directory."""
    markdown_files = []
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".md"):
                markdown_files.append(os.path.join(root, file))
    return markdown_files

def clean_content(content):
    """Cleans the content by removing unnecessary elements."""
    content = re.sub(r'\|.*?\[Click to Display Table of Contents\].*?\|', '', content, flags=re.DOTALL)
    content = re.sub(r'var lastSlashPos.*$', '', content, flags=re.DOTALL)
    content = content.lstrip('\ufeff\u200b')
    content = re.sub(r'\[Previous page\].*\n\[Return to chapter overview\].*\n', '', content)
    content = html.unescape(content)
    return content.strip()

def extract_title(content):
    """Extracts the title from the content."""
    lines = content.split('\n')
    for line in lines:
        if line.strip():
            return line.strip()
    return "Untitled"

def add_frontmatter(title, path):
    """Adds frontmatter to the content."""
    frontmatter = {
        "title": title,
        "path": path
    }
    return yaml.dump(frontmatter, default_flow_style=False)

def fix_code_blocks(content):
    """Fixes code blocks in the content."""
    ns_block_pattern = r'\| ns(?: Best practice)? \|\n\| --- \|\n((?:.|\n)*?)(?=\n\n|\Z)'
    content = re.sub(ns_block_pattern, r'```csharp\n\1\n```', content, flags=re.DOTALL)

    lang_block_pattern = r'\| (\w+) \|\n\| --- \|\n((?:.|\n)*?)(?=\n\n|\Z)'
    content = re.sub(lang_block_pattern, r'```\1\n\2\n```', content, flags=re.DOTALL)

    code_block_pattern = r'```(\w*)\n((?:.|\n)*?)```'
    
    def clean_code_block(match):
        lang, code = match.groups()
        code = re.sub(r'\|[^|]*\|[\n\r]+\|[^|]*\|[\n\r]+', '', code)
        code = '\n'.join(line.strip('| ').strip() for line in code.split('\n'))
        return f'```{lang}\n{code.strip()}\n```'
    
    content = re.sub(code_block_pattern, clean_code_block, content, flags=re.DOTALL)
    content = re.sub(r'}\|', '}\n```', content)
    content = re.sub(r'```(\w*)\s*\|', r'```\1', content)
    content = re.sub(r'```;', '```', content)
    return content

def convert_tables_to_callouts(content):
    """Converts tables to callouts in the content."""
    table_pattern = r'\|\s*\|\n\|\s*---\s*\|\n\|\s*(Note|Notes|Warning|Warnings|Tip|Tips|Why|Critical):\s*((?:.|\n)*?)\s*\|(?=\n\n|\Z)'
    
    def replace_table_with_callout(match):
        callout_type = match.group(1).lower()
        callout_content = match.group(2).strip()
        if callout_type == 'why' or callout_type == 'notes':
            callout_type = 'note'
        elif callout_type == 'critical':
            callout_type = 'warning'
        return f'{{% callout {callout_type} %}}\n\n{callout_content}\n\n{{% /callout %}}'
    
    content = re.sub(table_pattern, replace_table_with_callout, content, flags=re.DOTALL)
    ns_detail_pattern = r'\| ns (.*?) \|\n\| --- \|\n((?:.|\n)*?)(?=\n\n|\Z)'
    
    def replace_ns_detail(match):
        ns_type = match.group(1).lower()
        ns_content = match.group(2).strip()
        processing_logs.append(f"NS detail found")
        return f'## {ns_type.capitalize()}\n\n{ns_content}'
    
    content = re.sub(ns_detail_pattern, replace_ns_detail, content, flags=re.DOTALL)
    # content = re.sub(r'\n*{%', '\n\n{%', content)
    return content

def fix_relative_links(content):
    """Fixes relative links in the content."""
    content = re.sub(r'\[([^\]]+)\]\(([^)]+)\.htm\)', r'[\1](/docs/desktop/\2)', content)
    content = re.sub(r'\[([^\]]+)\]\(\.\./([^)]+)\)', r'[\1](/docs/desktop/../\2)', content)
    return content

def clean_trailing_spaces_and_blank_lines(content):
    """Cleans trailing spaces and blank lines in the content."""
    content = re.sub(r'[ \t]+$', '', content, flags=re.MULTILINE)
    content = fix_md009(content)
    content = fix_md012(content)
    content = fix_md022(content)
    content = fix_md047(content)
    content = fix_md058(content)
    return content

def fix_md009(content):
    """Fixes MD009 (Trailing spaces) issues."""
    return re.sub(r'[ \t]+$', '', content, flags=re.MULTILINE)

def fix_md012(content):
    """Fixes MD012 (Multiple consecutive blank lines) issues."""
    lines = content.split('\n')
    fixed_lines = []
    blank_line_count = 0

    for line in lines:
        if not line.strip():
            blank_line_count += 1
            #processing_logs.append(f"Multiple consecutive blank lines found.")
        else:
            if blank_line_count > 1:
                fixed_lines.append('')
            blank_line_count = 0
            fixed_lines.append(line)

    if blank_line_count > 1:
        processing_logs.append(f"Multiple consecutive blank lines found")
    return '\n'.join(fixed_lines)

def fix_md022(content):
    """Fixes MD022 (Headers should be surrounded by blank lines) issues."""
    lines = content.split('\n')
    fixed_lines = []

    for line in lines:
        if line.startswith('#'):
            processing_logs.append(f"Headers should be surrounded by blank lines found")
            fixed_lines.append('')
            fixed_lines.append(line)
            fixed_lines.append('')
        else:
            fixed_lines.append(line)

    return '\n'.join(fixed_lines)

def fix_md047(content):
    """Fixes MD047 (Files should end with a single newline character) issues."""
    return content.strip() + '\n'

def fix_md058(content):
    """Fixes MD058 (Multiple blank lines inside tables) issues."""
    lines = content.split('\n')
    fixed_lines = []
    in_table = False

    for line in lines:
        if line.startswith('|'):
            if not in_table:
                processing_logs.append(f"Multiple blank lines inside tables found")
                fixed_lines.append('')
                in_table = True
            fixed_lines.append(line)
        else:
            if in_table:
                processing_logs.append(f"Multiple blank lines inside tables found")
                fixed_lines.append('')
                in_table = False
            fixed_lines.append(line)

    return '\n'.join(fixed_lines)

def fix_syntax_section(content):
    """Fixes the syntax section in the content."""
    syntax_pattern = r'(?<=\n\n)Syntax\n(.+?)(?=\n\n|\Z)'

    if not re.search(syntax_pattern, content, flags=re.DOTALL):
        processing_logs.append(f"Syntax section not found")
        return content
    
    def replace_syntax(match):
        syntax_content = match.group(1).strip()
        return f'### Syntax\n\n```\n{syntax_content}\n```'
    
    content = re.sub(syntax_pattern, replace_syntax, content, flags=re.DOTALL)
    return content

def extract_image_references(content):
    """Extracts image references from the content."""
    image_pattern = r'!\[.*?\]\((.*?)\)'

    return re.findall(image_pattern, content)

def process_markdown(input_file, output_file):
    """Processes a single Markdown file."""
    changes_made = False
    images_found = False
    # logging.info(f"Processing file: {input_file}")
    processing_logs.append(f"Processing file: {input_file}")
    
    with open(input_file, 'r', encoding='utf-8-sig') as file:
        content = file.read()
    

    # We can check if the file is already processed by looking for the presence of --- at the beginning of the file
    if content.startswith('---\ntitle:'):
        logging.info(f"File {input_file} is already processed. Skipping.")
        return False, False

    # ENHANCEMENT: We could return a flag in each one of these function to let us know specifically what changes were made... 
    # But that requires detecting that changes need to be made in the first place... let's just process everything for now.
    changes_made = True

    #logging.info("Cleaning content")
    content = clean_content(content)
    processing_logs.append(f"Content cleaned")
    
    
    title = extract_title(content)
    #logging.info(f"Extracted title: {title}")
    processing_logs.append(f"Title extracted: {title}")
    
    path = Path(input_file).stem
    #logging.info(f"File path: {path}")
    processing_logs.append(f"File path: {path}")
    
    content = re.sub(re.escape(title.strip('"')), '', content, count=1).strip()
    content = re.sub(r'^(.+)\n-+\n', r'## \1\n', content, flags=re.MULTILINE)
    
    #logging.info("Adding frontmatter")
    processing_logs.append(f"Frontmatter added")
    frontmatter = add_frontmatter(title, path)
    content = f"---\n{frontmatter}---\n\n{content}"
    
    #logging.info("Fixing code blocks")
    content = fix_code_blocks(content)
    processing_logs.append(f"Code blocks fixed")
    
    #logging.info("Converting tables to callouts")
    content = convert_tables_to_callouts(content)
    processing_logs.append(f"Tables converted to callouts")
    
    #logging.info("Fixing relative links")
    content = fix_relative_links(content)
    processing_logs.append(f"Relative links fixed")
    
    #logging.info("Cleaning trailing spaces and blank lines")
    content = clean_trailing_spaces_and_blank_lines(content)
    processing_logs.append(f"Trailing spaces and blank lines cleaned")
    
    #logging.info("Fixing syntax section")
    content = fix_syntax_section(content)
    processing_logs.append(f"Syntax section fixed")
    
    #logging.info("Extracting image references")
    images = extract_image_references(content)
    if images:
        images_found = True
        logging.info(f"Found {len(images)} image references")
        with open("files_with_images.txt", "a") as f:
            f.write(f"{input_file}\n")
    
    #logging.info(f"Writing processed content to: {output_file}")
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(content)

    return changes_made, images_found

def process_markdown_directory(input_dir, output_dir):
    """Processes all Markdown files in a directory."""
    files = read_markdown_files(input_dir)
    with open(IMAGE_LOG_FILE, 'w') as image_log:
        for file in files:
            process_markdown_file(file, output_dir, image_log)
    
    print(f"Processing complete. Check {IMAGE_LOG_FILE} for a list of files containing images.")

def main():
    if len(sys.argv) != 3:
        logging.error("Usage: python markdown_fixer_script.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.exists(input_file):
        logging.error(f"Input file does not exist: {input_file}")
        sys.exit(1)

    #logging.info(f"Starting processing of {input_file}")
    try:
        changes_made, images_found = process_markdown(input_file, output_file)

        if changes_made:
            #logging.info(f"Processed {input_file} successfully with changes.")
            processing_logs.append(f"{input_file}: Changes made.")
        else:
            #logging.info(f"Processed {input_file} successfully. No changes needed.")
            processing_logs.append(f"{input_file}: No changes needed.")
        
        if images_found:
            #logging.info(f"Found images in {input_file}. Adding to files_with_images.txt")
            processing_logs.append(f"{input_file}: Found images. Adding to files_with_images.txt")
            # Avoid duplicate logging in files_with_images.txt
            with open("files_with_images.txt", "a+") as f:
                f.seek(0)
                existing_files = f.read().splitlines()
                if input_file not in existing_files:
                    f.write(f"{input_file}\n")

    except Exception as e:
        logging.error(f"Error processing {input_file}: {str(e)}")
        processing_logs.append(f"{input_file}: Error - {str(e)}")

    #logging.info("Processing completed")
    processing_logs.append(f"Processing completed")
def generate_report():
    if not processing_logs:
        return

    report_dir = os.path.join(PROJECT_ROOT, 'output', 'reports')
    os.makedirs(report_dir, exist_ok=True)

    report_file = os.path.join(report_dir, "markdown_fixer_report.txt")

    with open(report_file, 'a', encoding='utf-8') as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"\n\n--- Processing Session: {timestamp} ---\n")
        f.write("=" * 50 + "\n\n")
        
        for log in processing_logs:
            f.write(f"{log}\n")
        
        f.write("\n" + "=" * 50 + "\n")

    processing_logs.clear()  # Clear the logs after writing to the file

    #print(f"Processing report appended to: {report_file}")

processing_logs = []

if __name__ == "__main__":
    # logging.info("Starting markdown fixer script")
    processing_logs.append(f"Starting markdown fixer script")
    main()
    if processing_logs:  # Only generate a report if there's something to report
        generate_report()
    # logging.info("Markdown fixer script completed")
    processing_logs.append(f"Markdown fixer script completed")