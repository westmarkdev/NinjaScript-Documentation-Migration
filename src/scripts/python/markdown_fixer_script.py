import os
import re
import yaml
import html
from pathlib import Path

# Configuration
LINT_CONFIG_PATH = '.markdownlint.json'
IMAGE_LOG_FILE = 'files_with_images.txt'

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
    table_pattern = r'\|\s*\|\n\|\s*---\s*\|\n\|\s*(Note|Warning|Tip|Tips|Why|Critical):\s*((?:.|\n)*?)\s*\|(?=\n\n|\Z)'
    
    def replace_table_with_callout(match):
        callout_type = match.group(1).lower()
        callout_content = match.group(2).strip()
        if callout_type == 'why':
            callout_type = 'note'
        elif callout_type == 'critical':
            callout_type = 'warning'
        return f'{{% callout {callout_type} %}}\n{callout_content}\n{{% /callout %}}'
    
    content = re.sub(table_pattern, replace_table_with_callout, content, flags=re.DOTALL)
    ns_detail_pattern = r'\| ns (.*?) \|\n\| --- \|\n((?:.|\n)*?)(?=\n\n|\Z)'
    
    def replace_ns_detail(match):
        ns_type = match.group(1).lower()
        ns_content = match.group(2).strip()
        return f'## {ns_type.capitalize()}\n\n{ns_content}'
    
    content = re.sub(ns_detail_pattern, replace_ns_detail, content, flags=re.DOTALL)
    content = re.sub(r'\n*{%', '\n\n{%', content)
    return content

def fix_relative_links(content):
    """Fixes relative links in the content."""
    content = re.sub(r'\[([^\]]+)\]\(([^)]+)\.htm\)', r'[\1](\2)', content)
    content = re.sub(r'\[([^\]]+)\]\(\.\./([^)]+)\)', r'[\1](../\2)', content)
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
        else:
            if blank_line_count > 1:
                fixed_lines.append('')
            blank_line_count = 0
            fixed_lines.append(line)

    return '\n'.join(fixed_lines)

def fix_md022(content):
    """Fixes MD022 (Headers should be surrounded by blank lines) issues."""
    lines = content.split('\n')
    fixed_lines = []

    for line in lines:
        if line.startswith('#'):
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
                fixed_lines.append('')
                in_table = True
            fixed_lines.append(line)
        else:
            if in_table:
                fixed_lines.append('')
                in_table = False
            fixed_lines.append(line)

    return '\n'.join(fixed_lines)

def fix_syntax_section(content):
    """Fixes the syntax section in the content."""
    syntax_pattern = r'(?<=\n\n)Syntax\n(.+?)(?=\n\n|\Z)'

    if not re.search(syntax_pattern, content, flags=re.DOTALL):
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

def process_markdown_file(input_file, output_dir, image_log):
    """Processes a single Markdown file."""
    with open(input_file, 'r', encoding='utf-8-sig') as file:
        content = file.read()
    
    content = clean_content(content)
    title = extract_title(content)
    path = Path(input_file).stem
    content = re.sub(re.escape(title.strip('"')), '', content, count=1).strip()
    content = re.sub(r'^(.+)\n-+\n', r'## \1\n\n', content, flags=re.MULTILINE)
    frontmatter = add_frontmatter(title, path)
    content = f"---\n{frontmatter}---\n\n{content}"
    content = fix_code_blocks(content)
    content = convert_tables_to_callouts(content)
    content = fix_relative_links(content)
    content = clean_trailing_spaces_and_blank_lines(content)
    content = fix_syntax_section(content)
    
    # Check for images
    images = extract_image_references(content)
    if images:
        image_log.write(f"{input_file}: {', '.join(images)}\n")
    
    output_file = os.path.join(output_dir, os.path.basename(input_file))
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(content)

def process_markdown_directory(input_dir, output_dir):
    """Processes all Markdown files in a directory."""
    files = read_markdown_files(input_dir)
    with open(IMAGE_LOG_FILE, 'w') as image_log:
        for file in files:
            process_markdown_file(file, output_dir, image_log)
    
    print(f"Processing complete. Check {IMAGE_LOG_FILE} for a list of files containing images.")

if __name__ == "__main__":
    input_directory = '../input/raw'
    output_directory = '../output/fixed'
    os.makedirs(output_directory, exist_ok=True)
    process_markdown_directory(input_directory, output_directory)