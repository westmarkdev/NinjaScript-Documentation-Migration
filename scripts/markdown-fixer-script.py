import os
import re
from datetime import datetime
from pathlib import Path
import yaml
import html

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
    # Step 1: Convert 'ns' code blocks to csharp
    ns_block_pattern = r'\| ns \|\n\| --- \|\n((?:.|\n)*?)(?=\n\n|\Z)'
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

def fix_markdown(input_dir, output_dir):
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    for filename in os.listdir(input_dir):
        if filename.endswith('.md'):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            
            with open(input_path, 'r', encoding='utf-8-sig') as file:
                content = file.read()
            
            # Clean up junk data
            content = clean_content(content)
            
            # Extract title and create path
            title = extract_title(content)
            path = os.path.splitext(filename)[0]
            
            # Remove the title from the content as it's now in the frontmatter
            content = re.sub(re.escape(title), '', content, count=1).strip()
            
            # IMPORTANT: The workflow can break the YAML front matter and adds a huge line instead, so we fix the heading styles
            # first, let's replace all the H2 headings and ignore the H1 headings
            content = re.sub(r'^(.+)\n-+\n', r'## \1\n\n', content, flags=re.MULTILINE)

            # Add frontmatter
            frontmatter = add_frontmatter(title, path)
            content = f"---\n{frontmatter}---\n\n{content}"
            
            # Fix code blocks
            content = fix_code_blocks(content)
            
            # Add blank lines around headings
            content = re.sub(r'(\n[#]+.*\n)', r'\n\1\n', content)
            
            # Remove extra blank lines
            content = re.sub(r'\n{3,}', '\n\n', content)
            
            # TODO: Replace table NOTE/WARNING/TIP with actual markdown syntax

            # Right now the calls are in tables:

            # ```markdown
            # |  |
            # | --- |
            # | Why:   The practice to avoid code below could work in some scenarios but would generate errors if other types were added to that collection that you were not anticipating. |
            # ```

            # OR
            # ```markdown
            # |  |
            # | --- |
            # | Note:  Information on this page focuses on supported (documented) NinjaTrader methods and properties shared between versions.  NinjaTrader 8 has seen a significant increase in supported NinjaTrader code, however if you were using previously undocumented NinjaTrader 7 methods or properties, they will NOT be covered in this topic.  You may be able to find more information on previously undocumented methods and properties in the NinjaTrader 8 Help Guide, or our support staff will also be happy to personally point you in the right direction. |

            # 

            # |  |
            # | --- |
            # | Critical:   If your product uses unsupported (undocumented) elements we strongly urge you to put your scripts through thorough testing to ensure they still behave as expected.  There is NO guarantee that previously undocumented method or property behavior has not changed in the new version of NinjaTrader 8. |            

            # In your Markdoc content, you can use the following syntax to create a “Note” callout:

            # ```markdown
            #   {% callout type="note" %} # or "warning" or "tip" (use "note" for "why")
            #   This is an important note for your readers.
            #   {% endcallout %}
            # ```

            # TODO: Use pymarkdownlnt for additional fixes on the CLI during development            
            
            with open(output_path, 'w', encoding='utf-8') as file:
                file.write(content)

    print(f"Markdown fixing complete. Check {output_dir} for updated files.")

# Create output directory with timestamp
folder_name = f'./output/fixed-{datetime.now().strftime("%Y-%m-%d--%H-%M")}'
os.makedirs(folder_name, exist_ok=True)

# Usage
fix_markdown('./input/', folder_name)