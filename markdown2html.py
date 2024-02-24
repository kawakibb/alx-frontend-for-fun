#!/usr/bin/python3
"""
Script to convert Markdown to HTML.
Usage: ./markdown2html.py README.md README.html
"""

import sys
import markdown

def convert_markdown_to_html(markdown_file, output_file):
    """
    Convert Markdown file to HTML.
    """
    try:
        with open(markdown_file, 'r') as f:
            markdown_content = f.read()
    except FileNotFoundError:
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    html_content = markdown.markdown(markdown_content)

    with open(output_file, 'w') as f:
        f.write(html_content)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_markdown_to_html(markdown_file, output_file)