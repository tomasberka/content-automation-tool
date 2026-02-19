#!/usr/bin/env python3
"""
Script to remove <strong> tags that wrap or are wrapped by <a> links.
Keeps standalone <strong> tags that are not associated with links.
"""

import re
import sys
from pathlib import Path


def fix_strong_in_html(html_content):
    """
    Remove <strong> tags that are associated with <a> links.
    
    Handles two patterns:
    1. <strong><a href="...">text</a></strong> -> <a href="...">text</a>
    2. <a href="..."><strong>text</strong></a> -> <a href="...">text</a>
    """
    
    # Pattern 1: <strong><a ...>...</a></strong>
    # Remove <strong> wrapper around <a> tags
    pattern1 = r'<strong>(<a\s+[^>]*>.*?</a>)</strong>'
    html_content = re.sub(pattern1, r'\1', html_content, flags=re.DOTALL)
    
    # Pattern 2: <a ...><strong>...</strong></a>
    # Remove <strong> tags inside <a> tags
    pattern2 = r'(<a\s+[^>]*>)<strong>(.*?)</strong>(</a>)'
    html_content = re.sub(pattern2, r'\1\2\3', html_content, flags=re.DOTALL)
    
    return html_content


def process_file(file_path):
    """Process a single HTML file."""
    print(f"Processing: {file_path}")
    
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        original_content = f.read()
    
    # Fix the content
    fixed_content = fix_strong_in_html(original_content)
    
    # Check if any changes were made
    if original_content != fixed_content:
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(fixed_content)
        print(f"  ✓ Fixed {file_path}")
        return True
    else:
        print(f"  - No changes needed for {file_path}")
        return False


def main():
    """Main function to process all HTML files."""
    base_path = Path(__file__).parent
    
    # Find all HTML files
    html_files = list(base_path.glob('**/*.html'))
    
    if not html_files:
        print("No HTML files found!")
        return 1
    
    print(f"Found {len(html_files)} HTML files\n")
    
    changed_count = 0
    for html_file in sorted(html_files):
        if process_file(html_file):
            changed_count += 1
    
    print(f"\n✓ Processed {len(html_files)} files")
    print(f"✓ Modified {changed_count} files")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
