import os
import re
from datetime import datetime
from pathlib import Path
import yaml
import html

# Can we fix these errors?
# MD009/no-trailing-spaces: Trailing spaces [Expected: 0 or 2; Actual: 1] markdownlintMD009
# MD012/no-multiple-blanks: Multiple consecutive blank lines [Expected: 1; Actual: 2] 

def clean_content(content):
    # Remove table of contents and breadcrumb
    content = re.sub(r'\|.*?\[Click to Display Table of Contents\].*?\|', '', content, flags=re.DOTALL)
    
    # Remove garbage JavaScript at the bottom
    content = re.sub(r'var lastSlashPos.*$', '', content, flags=re.DOTALL)
    
    # Remove any BOM or other invisible characters at the start of the file
    content = content.lstrip('\ufeff\u200b')
    
    # Remove unnecessary navigation links
    content = re.sub(r'\[Previous page\].*\n\[Return to chapter overview\].*\n', '', content)
    
    # Convert HTML entities to Unicode
    content = html.unescape(content)
    
    return content.strip()

def extract_title(content):
    # Extract the first non-empty line as the title
    lines = content.split('\n')
    for line in lines:
        if line.strip():
            return line.strip()
    return "Untitled"

def add_frontmatter(title, path):
    frontmatter = {
        "title": title,
        "path": path
    }
    return yaml.dump(frontmatter, default_flow_style=False)

# FIXME: We also need to look for | ns Best practice | and convert it to ```csharp
def fix_code_blocks(content):
    # Step 1: Convert 'ns' and 'ns Best practice' code blocks to csharp
    ns_block_pattern = r'\| ns(?: Best practice)? \|\n\| --- \|\n((?:.|\n)*?)(?=\n\n|\Z)'
    content = re.sub(ns_block_pattern, r'```csharp\n\1\n```', content, flags=re.DOTALL)

    # Step 2: Convert other language code blocks (C#, XAML, etc.)
    lang_block_pattern = r'\| (\w+) \|\n\| --- \|\n((?:.|\n)*?)(?=\n\n|\Z)'
    content = re.sub(lang_block_pattern, r'```\1\n\2\n```', content, flags=re.DOTALL)

    # Step 3: Clean up remaining table-like structures in code blocks
    code_block_pattern = r'```(\w*)\n((?:.|\n)*?)```'
    
    def clean_code_block(match):
        lang, code = match.groups()
        # Remove table headers and separators
        code = re.sub(r'\|[^|]*\|[\n\r]+\|[^|]*\|[\n\r]+', '', code)
        # Remove leading/trailing | characters and trim each line
        code = '\n'.join(line.strip('| ').strip() for line in code.split('\n'))
        return f'```{lang}\n{code.strip()}\n```'
    
    content = re.sub(code_block_pattern, clean_code_block, content, flags=re.DOTALL)

    # Step 4: Final cleanup
    content = re.sub(r'}\|', '}\n```', content)  # Fix closing brackets
    content = re.sub(r'```(\w*)\s*\|', r'```\1', content)  # Remove trailing |
    content = re.sub(r'```;', '```', content)  # Remove trailing semicolons

    return content

def convert_tables_to_callouts(content):
    # Pattern to match table-style callouts
    table_pattern = r'\|\s*\|\n\|\s*---\s*\|\n\|\s*(Note|Warning|Tip|Why|Critical):\s*((?:.|\n)*?)\s*\|(?=\n\n|\Z)'
    
    def replace_table_with_callout(match):
        callout_type = match.group(1).lower()
        callout_content = match.group(2).strip()
        
        # Map 'why' to 'note' and 'critical' to 'warning'
        if callout_type == 'why':
            callout_type = 'note'
        elif callout_type == 'critical':
            callout_type = 'warning'
        
        return f'{{% callout type="{callout_type}" %}}\n{callout_content}\n{{% /callout %}}'
    
    return re.sub(table_pattern, replace_table_with_callout, content, flags=re.DOTALL)

def fix_markdown(input_dir, output_dir):
    input_path = Path(input_dir).resolve()
    output_path = Path(output_dir).resolve()
    
    # Create input and output directories if they don't exist
    input_path.mkdir(parents=True, exist_ok=True)
    output_path.mkdir(parents=True, exist_ok=True)
    
    for filename in input_path.glob('*.md'):
        with open(filename, 'r', encoding='utf-8-sig') as file:
            content = file.read()
        
        # Clean up junk data
        content = clean_content(content)
        
        # Extract title and create path
        title = extract_title(content)
        # FIXME: We need to convert to just the filename without the path or extension
        # path = os.path.splitext(filename)[0]
        path = filename.stem
        
        # Remove the title from the content as it's now in the frontmatter
        content = re.sub(re.escape(title), '', content, count=1).strip()
        
        # Fix heading styles
        content = re.sub(r'^(.+)\n-+\n', r'## \1\n\n', content, flags=re.MULTILINE)

        # Add frontmatter
        frontmatter = add_frontmatter(title, path)
        content = f"---\n{frontmatter}---\n\n{content}"
        
        # Fix code blocks
        content = fix_code_blocks(content)
        
        # Convert tables to callouts
        content = convert_tables_to_callouts(content)
        
        # Add blank lines around headings
        content = re.sub(r'(\n[#]+.*\n)', r'\n\1\n', content)
        
        # Remove extra blank lines
        content = re.sub(r'\n{3,}', '\n\n', content)
        
        output_file = output_path / filename.name
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(content)

    print(f"Markdown fixing complete. Check {output_path} for updated files.")

# Create output directory with timestamp
script_dir = Path(__file__).parent.resolve()
folder_name = f'output/fixed-{datetime.now().strftime("%Y-%m-%d--%H-%M")}'
output_dir = script_dir / folder_name
output_dir.mkdir(parents=True, exist_ok=True)

# Usage
input_dir = script_dir / 'input'
fix_markdown(input_dir, output_dir)