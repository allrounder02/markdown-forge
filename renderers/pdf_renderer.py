import jinja2
from config.schema import Config
from pathlib import Path

def generate_css(config: Config) -> str:
    css = []
    
    # Page setup
    css.append(f"""
    @page {{
        size: {config.document.page_size};
        margin-top: {config.document.margins.top};
        margin-bottom: {config.document.margins.bottom};
        margin-left: {config.document.margins.left};
        margin-right: {config.document.margins.right};
    }}
    """)
    
    # Fonts
    css.append(f"""
    body {{
        font-family: "{config.fonts.body}", sans-serif;
        font-size: {config.fonts.base_size};
        line-height: {config.fonts.line_height};
    }}
    h1, h2, h3, h4, h5, h6 {{
        font-family: "{config.fonts.heading}", serif;
    }}
    code, pre {{
        font-family: "{config.fonts.code}", monospace;
    }}
    """)
    
    # Headings
    for level, style in config.styles.dict().items():
        if not level.startswith("h"):
            continue
        
        style_css = []
        if style.get("size"): style_css.append(f"font-size: {style['size']};")
        if style.get("weight"): style_css.append(f"font-weight: {style['weight']};")
        if style.get("color"): style_css.append(f"color: {style['color']};")
        
        if style_css:
            css.append(f"{level} {{ {' '.join(style_css)} }}")
            
    # Tables
    css.append("""
    table {
        border-collapse: collapse;
        width: 100%;
        max-width: 100%;
        margin-bottom: 1em;
        font-size: 0.9em;  /* Slightly smaller font for tables */
        table-layout: auto;
    }
    th, td {
        border: 1px solid #ddd;
        padding: 6px 8px;
        text-align: left;
        word-wrap: break-word;
        word-break: break-word;
        hyphens: auto;
        overflow-wrap: break-word;
    }
    th {
        background-color: #f2f2f2;
        font-weight: bold;
    }
    /* For very wide tables, reduce font size further */
    @media print {
        table {
            font-size: 0.85em;
        }
    }
    """)
    
    # Images
    css.append("""
    img {
        max-width: 100%;
        height: auto;
    }
    """)
    
    # Hyperlinks
    css.append("""
    a {
        color: #0066cc;
        text-decoration: underline;
    }
    a:visited {
        color: #800080;
    }
    """)
    
    # Text alignment support
    css.append("""
    /* Support for align attribute (deprecated but still used) */
    [align="center"] {
        text-align: center;
    }
    [align="right"] {
        text-align: right;
    }
    [align="left"] {
        text-align: left;
    }
    [align="justify"] {
        text-align: justify;
    }
    
    /* Utility classes for alignment */
    .text-center {
        text-align: center;
    }
    .text-right {
        text-align: right;
    }
    .text-left {
        text-align: left;
    }
    .text-justify {
        text-align: justify;
    }
    
    /* Center block elements */
    .center {
        margin-left: auto;
        margin-right: auto;
        display: block;
    }
    """)
    
    # Page breaks
    css.append("""
    .page-break {
        page-break-after: always;
        break-after: page;
        height: 0;
        display: block;
    }
    """)

    return "\n".join(css)

def render_pdf(html_content: str, config: Config, output_path: str = None):
    import os
    # Add GTK3 to PATH for Windows
    gtk_paths = [
        r"C:\Program Files\GTK3-Runtime Win64\bin",
        r"C:\Program Files\GTK3-Runtime\bin",
        r"C:\Program Files (x86)\gtk-3.8.1\bin", # 32-bit fallback (might fail on 64-bit Python)
        r"C:\Program Files (x86)\gtk-3.8.1",
    ]
    for path in gtk_paths:
        if os.path.exists(path):
            os.environ['PATH'] = path + os.pathsep + os.environ['PATH']
            break
    
    try:
        from weasyprint import HTML, CSS
    except OSError as e:
        print(f"Error: WeasyPrint dependencies not found. Please install GTK3 for Windows. Details: {e}")
        return None

    # Load template
    template_loader = jinja2.FileSystemLoader(searchpath=str(Path(__file__).parent.parent / "templates"))
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template("base.html")
    
    # Generate CSS
    css_content = generate_css(config)
    
    # Render HTML
    full_html = template.render(content=html_content, css=css_content)
    
    # Get the base directory for resolving relative paths (like images/)
    # Use the current working directory as the base
    base_url = Path.cwd().as_uri() + '/'
    
    # Generate PDF with base_url so images can be found
    if output_path:
        HTML(string=full_html, base_url=base_url).write_pdf(output_path)
        return None
    else:
        return HTML(string=full_html, base_url=base_url).write_pdf()
