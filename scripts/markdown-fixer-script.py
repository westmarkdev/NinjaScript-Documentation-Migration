import os
import re
from datetime import datetime
from pathlib import Path
import yaml
import html

def clean_content(content):
    # Remove table of contents and breadcrumb to avoid clutter and irrelevant information
    content = re.sub(r'\|.*?\[Click to Display Table of Contents\].*?\|', '', content, flags=re.DOTALL)
    
    # Remove garbage JavaScript at the bottom to prevent execution of unwanted scripts
    content = re.sub(r'var lastSlashPos.*$', '', content, flags=re.DOTALL)
    
    # Remove any BOM or other invisible characters at the start of the file to ensure clean parsing
    content = content.lstrip('\ufeff\u200b')
    
    # Remove unnecessary navigation links to streamline the content and focus on the main text
    content = re.sub(r'\[Previous page\].*\n\[Return to chapter overview\].*\n', '', content)
    
    # Convert HTML entities to Unicode to ensure proper rendering of special characters
    content = html.unescape(content)
    
    return content.strip()

def extract_title(content):
    # Extract the first non-empty line as the title and wrap in quotes
    # This approach ensures that the title is always the first meaningful line of the content,
    # which is typically the main heading in markdown files. Wrapping it in quotes helps to
    # avoid issues with special characters in YAML frontmatter.
    lines = content.split('\n')
    for line in lines:
        if line.strip():
            return f"{line.strip()}"
    return "Untitled"

def add_frontmatter(title, path):
    # Using a dictionary to structure the frontmatter ensures that the title and path are clearly defined.
    # This approach leverages YAML's readability and compatibility with many markdown processors.
    frontmatter = {
        "title": title,
        "path": path
    }
    # Dumping the dictionary to a YAML formatted string with default_flow_style=False for better readability.
    return yaml.dump(frontmatter, default_flow_style=False)

def fix_code_blocks(content):
    # Convert 'ns' and 'ns Best practice' code blocks to csharp to ensure proper syntax highlighting
    ns_block_pattern = r'\| ns(?: Best practice)? \|\n\| --- \|\n((?:.|\n)*?)(?=\n\n|\Z)'
    content = re.sub(ns_block_pattern, r'```csharp\n\1\n```', content, flags=re.DOTALL)

    # Convert other language code blocks (C#, XAML, etc.) to their respective languages for accurate rendering
    lang_block_pattern = r'\| (\w+) \|\n\| --- \|\n((?:.|\n)*?)(?=\n\n|\Z)'
    content = re.sub(lang_block_pattern, r'```\1\n\2\n```', content, flags=re.DOTALL)

    # Clean up remaining table-like structures in code blocks to avoid rendering issues
    code_block_pattern = r'```(\w*)\n((?:.|\n)*?)```'
    
    def clean_code_block(match):
        lang, code = match.groups()
        # Remove table headers and separators to ensure clean code blocks
        code = re.sub(r'\|[^|]*\|[\n\r]+\|[^|]*\|[\n\r]+', '', code)
        # Remove leading/trailing | characters and trim each line for consistency
        code = '\n'.join(line.strip('| ').strip() for line in code.split('\n'))
        return f'```{lang}\n{code.strip()}\n```'
    
    content = re.sub(code_block_pattern, clean_code_block, content, flags=re.DOTALL)

    # Final cleanup to fix any remaining formatting issues
    content = re.sub(r'}\|', '}\n```', content)  # Ensure closing brackets are properly formatted
    content = re.sub(r'```(\w*)\s*\|', r'```\1', content)  # Remove trailing | for clean code blocks
    content = re.sub(r'```;', '```', content)  # Remove trailing semicolons for proper code block closure

    return content

def convert_tables_to_callouts(content):
    # Using regex to match table-style callouts to ensure consistent formatting and easy identification.
    table_pattern = r'\|\s*\|\n\|\s*---\s*\|\n\|\s*(Note|Warning|Tip|Tips|Why|Critical):\s*((?:.|\n)*?)\s*\|(?=\n\n|\Z)'
    
    def replace_table_with_callout(match):
        callout_type = match.group(1).lower()
        callout_content = match.group(2).strip()
        
        # Mapping 'why' to 'note' and 'critical' to 'warning' for standardization across documents.
        if callout_type == 'why' or callout_type == 'tips' or callout_type == 'tip':
            callout_type = 'note'
        elif callout_type == 'critical':
            callout_type = 'warning'
        
        return f'{{% callout type="{callout_type}" %}}\n{callout_content}\n{{% /callout %}}'
    
    content = re.sub(table_pattern, replace_table_with_callout, content, flags=re.DOTALL)

    # Ensuring NS details are converted to callouts or headings for better readability and structure.
    ns_detail_pattern = r'\| ns (.*?) \|\n\| --- \|\n((?:.|\n)*?)(?=\n\n|\Z)'
    
    def replace_ns_detail(match):
        heading = match.group(1).strip()
        detail_content = match.group(2).strip()
        return f'### {heading}\n\n{detail_content}'
    
    content = re.sub(ns_detail_pattern, replace_ns_detail, content, flags=re.DOTALL)

    # Ensure there is one blank line before and after the callouts for proper separation and readability.
    content = re.sub(r'\n*{%', '\n\n{%', content)

    return content

def fix_relative_links(content):
    # Convert .htm links to .md to ensure compatibility with markdown processors
    # This is necessary because the original documentation uses .htm extensions,
    # which need to be converted to .md for proper linking in markdown files.
    content = re.sub(r'\[([^\]]+)\]\(([^)]+)\.htm\)', r'[\1](\2)', content)
    
    # Adjust relative links to maintain correct paths after migration
    # This ensures that links pointing to parent directories are correctly formatted
    # to reflect the new markdown structure.
    content = re.sub(r'\[([^\]]+)\]\(\.\./([^)]+)\)', r'[\1](../\2)', content)
    
    return content

def clean_trailing_spaces_and_blank_lines(content):
    # Removing trailing spaces to ensure clean and consistent formatting.
    # This helps in avoiding unnecessary whitespace that can cause rendering issues or make the content look untidy.
    content = re.sub(r'[ \t]+$', '', content, flags=re.MULTILINE)
    
    # Reducing multiple consecutive blank lines to a maximum of two.
    # This ensures that the content remains readable and avoids excessive whitespace that can disrupt the flow of the document.
    # Disabled because it's not working as expected and putting double line breaks in the middle of tables and code blocks.
    # content = re.sub(r'\n{3,}', '\n\n', content)
    content = fix_md009(content)
    content = fix_md012(content)
    content = fix_md022(content)
    content = fix_md047(content)
    content = fix_md058(content)
    
    return content

# MD009/no-trailing-spaces: Trailing spaces [Expected: 0 or 2; Actual: 1]
def fix_md009(content):
    return re.sub(r'[ \t]+$', '', content, flags=re.MULTILINE)

# MD012/no-multiple-blanks: Multiple consecutive blank lines [Expected: 1; Actual: 2]
def fix_md012(content):
    lines = content.split('\n')
    fixed_lines = []
    blank_line_count = 0
    in_table = False

    for line in lines:
        if re.match(r'^\s*\|', line):
            in_table = True
        elif in_table and not re.match(r'^\s*\|', line):
            in_table = False

        if not in_table:
            if line.strip() == '':
                blank_line_count += 1
            else:
                blank_line_count = 0

            if blank_line_count > 1:
                continue

        fixed_lines.append(line)

    return '\n'.join(fixed_lines)

# MD022/blanks-around-headings: Headings should be surrounded by blank lines [Expected: 1; Actual: 0; Above]
def fix_md022(content):
    lines = content.split('\n')
    fixed_lines = []
    in_table = False

    for line in lines:
        if re.match(r'^\s*\|', line):
            in_table = True
        elif in_table and not re.match(r'^\s*\|', line):
            in_table = False

        if not in_table:
            if re.match(r'^#+\s', line):
                if not fixed_lines or fixed_lines[-1].strip() != '':
                    fixed_lines.append('')

        fixed_lines.append(line)

    return '\n'.join(fixed_lines)

# MD047/single-trailing-newline: Files should end with a single newline character
def fix_md047(content):
    return content.strip() + '\n'

# MD058/blanks-around-tables: Tables should be surrounded by blank lines
def fix_md058(content):
    lines = content.split('\n')
    fixed_lines = []
    in_table = False

    for line in lines:
        if re.match(r'^\s*\|', line):
            in_table = True
        elif in_table and not re.match(r'^\s*\|', line):
            in_table = False

        if in_table:
            if line.strip() == '':
                continue

        fixed_lines.append(line)

    return '\n'.join(fixed_lines)

def fix_syntax_section(content):
    # Converting "Syntax" to H3 and wrapping the following code in inline code to ensure
    # that the syntax section is clearly identified and the code is properly formatted.
    # This approach improves readability and ensures that the syntax is highlighted correctly.
    syntax_pattern = r'(?<=\n\n)Syntax\n(.+?)(?=\n\n|\Z)'

    # if there is no pattern, maybe it's already in a heading 2?
    if not re.search(syntax_pattern, content, flags=re.DOTALL):
        syntax_pattern = r'(?<=\n\n)## Syntax\n(.+?)(?=\n\n|\Z)'
    
    def replace_syntax(match):
        syntax_code = match.group(1).strip()
        return f'## Syntax\n\n`{syntax_code}`'
    
    content = re.sub(syntax_pattern, replace_syntax, content, flags=re.DOTALL)
    return content

def fix_markdown(input_file, output_dir):
    with open(input_file, 'r', encoding='utf-8-sig') as file:
        content = file.read()
    
    # Clean content
    content = clean_content(content)
    
    # Extract title for frontmatter
    title = extract_title(content)
    path = Path(input_file).stem
    
    # Remove the title from the content to avoid duplication
    content = re.sub(re.escape(title.strip('"')), '', content, count=1).strip()
    
    # Standardize heading styles
    content = re.sub(r'^(.+)\n-+\n', r'## \1\n\n', content, flags=re.MULTILINE)

    # Add frontmatter
    frontmatter = add_frontmatter(title, path)
    content = f"---\n{frontmatter}---\n\n{content}"
    
    # Apply fixes
    content = fix_code_blocks(content)
    content = convert_tables_to_callouts(content)
    content = fix_relative_links(content)
    content = clean_trailing_spaces_and_blank_lines(content)
    content = fix_syntax_section(content)
    
    # Write the cleaned and formatted content to the output directory
    output_file = os.path.join(output_dir, os.path.basename(input_file))
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(content)

    print(f"Markdown fixing complete for {os.path.basename(input_file)}.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python markdown_fixer_script.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, 'output', 'fixed-latest')
    os.makedirs(output_dir, exist_ok=True)

    fix_markdown(input_file, output_dir)