#!/usr/bin/env python3
"""Test script to verify page break functionality."""

from core.parser import MarkdownParser

# Test markdown with page breaks
test_md = """# Page 1
Content on page 1.

\\newpage

# Page 2
Content on page 2.

\\pagebreak

# Page 3
Content on page 3.
"""

parser = MarkdownParser()

# Test 1: Check tokens
print("=== Token Test ===")
tokens = parser.parse(test_md)
page_break_count = sum(1 for token in tokens if token.type == 'page_break')
print(f"Found {page_break_count} page_break tokens")
for i, token in enumerate(tokens):
    if token.type == 'page_break':
        print(f"  Token {i}: {token.type} - {token.markup}")

# Test 2: Check HTML output
print("\n=== HTML Rendering Test ===")
html = parser.render_html(test_md)
div_count = html.count('<div class="page-break"></div>')
print(f"Found {div_count} page-break divs in HTML")
print("\nHTML Output:")
print(html)

# Test 3: Verify both commands work
print("\n=== Command Recognition Test ===")
for cmd in [r'\newpage', r'\pagebreak']:
    test = f"Before\n\n{cmd}\n\nAfter"
    tokens = parser.parse(test)
    has_pagebreak = any(t.type == 'page_break' for t in tokens)
    print(f"{cmd}: {'✓ Recognized' if has_pagebreak else '✗ NOT recognized'}")
