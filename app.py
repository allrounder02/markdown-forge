import streamlit as st
import os
from pathlib import Path
from core.parser import MarkdownParser
from core.utils import load_config
from renderers.pdf_renderer import render_pdf, generate_css
from renderers.docx_renderer import render_docx
import jinja2
from datetime import datetime

st.set_page_config(page_title="Markdown Forge", layout="wide")

st.title("Markdown Forge Preview")

# Initialize session state for content management
if 'md_content' not in st.session_state:
    st.session_state.md_content = ""
if 'insert_image' not in st.session_state:
    st.session_state.insert_image = None

# Sidebar: File Selection
st.sidebar.header("Configuration")
files = [f for f in os.listdir(".") if f.endswith(".md")]
selected_file = st.sidebar.selectbox("Select Markdown File", files)

config_path = st.sidebar.text_input("Config File", "config/default_config.yaml")

# Image Upload Section
st.sidebar.markdown("---")
st.sidebar.header("Image Upload")

# Initialize session state for tracking uploaded files
if 'uploaded_files' not in st.session_state:
    st.session_state.uploaded_files = set()

uploaded_file = st.sidebar.file_uploader(
    "Upload Image", 
    type=['png', 'jpg', 'jpeg'],
    help="Upload an image to insert into your markdown document"
)

if uploaded_file is not None:
    # Create a unique identifier for this upload
    file_id = f"{uploaded_file.name}_{uploaded_file.size}"
    
    # Only save if this is a new upload
    if file_id not in st.session_state.uploaded_files:
        # Create images directory if it doesn't exist
        images_dir = Path("images")
        images_dir.mkdir(exist_ok=True)
        
        # Sanitize filename
        original_filename = uploaded_file.name
        safe_filename = "".join(c for c in original_filename if c.isalnum() or c in ('.', '_', '-'))
        
        # Check if file exists and add timestamp if needed
        image_path = images_dir / safe_filename
        if image_path.exists():
            stem = image_path.stem
            suffix = image_path.suffix
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            safe_filename = f"{stem}_{timestamp}{suffix}"
            image_path = images_dir / safe_filename
        
        # Save the uploaded file
        with open(image_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Mark this file as uploaded
        st.session_state.uploaded_files.add(file_id)
        
        # Store the filename for this session
        st.session_state.last_uploaded_image = safe_filename
        st.sidebar.success(f"✓ Saved as {safe_filename}")
    
    # Use the stored filename if available
    if 'last_uploaded_image' in st.session_state:
        safe_filename = st.session_state.last_uploaded_image
    else:
        # Fallback to sanitized name
        safe_filename = "".join(c for c in uploaded_file.name if c.isalnum() or c in ('.', '_', '-'))
    
    # Show preview
    st.sidebar.image(uploaded_file, caption=safe_filename, use_container_width=True)
    
    # Generate markdown syntax
    relative_path = f"images/{safe_filename}"
    markdown_code = f"![Image description]({relative_path})"
    
    # Show markdown code
    st.sidebar.code(markdown_code, language="markdown")
    
    # Line number for insertion
    st.sidebar.markdown("**Insert at line number** (leave empty to append at end):")
    insert_line = st.sidebar.number_input(
        "Line number",
        min_value=1,
        value=None,
        step=1,
        label_visibility="collapsed"
    )
    
    # Insert button
    if st.sidebar.button("Insert into Document", type="primary"):
        st.session_state.insert_image = {
            'markdown': markdown_code,
            'line': insert_line
        }
        st.rerun()

if selected_file:
    file_path = Path(selected_file)
    
    # Load initial content from file if not in session state or file changed
    if 'current_file' not in st.session_state or st.session_state.current_file != selected_file:
        with open(file_path, "r", encoding="utf-8") as f:
            st.session_state.md_content = f.read()
        st.session_state.current_file = selected_file

    try:
        config = load_config(config_path)
    except Exception as e:
        st.error(f"Error loading config: {e}")
        st.stop()

    # Parse Markdown
    parser = MarkdownParser()
    
    # Layout: Dual Window
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("Editor")
        
        # Handle image insertion
        if st.session_state.insert_image:
            lines = st.session_state.md_content.split('\n')
            insert_data = st.session_state.insert_image
            
            if insert_data['line'] is None:
                # Append at end
                st.session_state.md_content += f"\n\n{insert_data['markdown']}\n"
            else:
                # Insert at specified line
                line_idx = insert_data['line'] - 1  # Convert to 0-indexed
                if line_idx < 0:
                    line_idx = 0
                if line_idx > len(lines):
                    line_idx = len(lines)
                
                lines.insert(line_idx, insert_data['markdown'])
                st.session_state.md_content = '\n'.join(lines)
            
            # Clear the insert trigger
            st.session_state.insert_image = None
        
        # Editor
        edited_content = st.text_area(
            "Markdown Input", 
            st.session_state.md_content, 
            height=800, 
            label_visibility="collapsed",
            key="markdown_editor"
        )
        
        # Update session state if content changed
        if edited_content != st.session_state.md_content:
            st.session_state.md_content = edited_content

    # Render logic based on edited content
    html_content = parser.render_html(st.session_state.md_content)
    tokens = parser.parse(st.session_state.md_content)
    css_content = generate_css(config)

    with col2:
        st.subheader("Preview (PDF)")
        # Generate PDF bytes
        try:
            pdf_bytes = render_pdf(html_content, config)
            
            if pdf_bytes:
                import base64
                base64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')
                # Use <embed> instead of <iframe> to avoid auto-download issues and improve rendering
                pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" type="application/pdf">'
                st.markdown(pdf_display, unsafe_allow_html=True)
            else:
                st.error("Failed to generate PDF preview.")
        except Exception as e:
            st.error(f"Error generating preview: {e}")

    # Conversion Actions
    st.sidebar.markdown("---")
    st.sidebar.header("Actions")
    
    # Save changes to file
    if st.sidebar.button("💾 Save Changes"):
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(st.session_state.md_content)
        st.sidebar.success(f"Saved to {selected_file}")
    
    if st.sidebar.button("Convert to PDF"):
        output_pdf = file_path.with_suffix(".pdf")
        with st.spinner("Converting to PDF..."):
            try:
                render_pdf(html_content, config, str(output_pdf))
                st.sidebar.success(f"Saved to {output_pdf}")
            except Exception as e:
                st.sidebar.error(f"Error: {e}")

    if st.sidebar.button("Convert to DOCX"):
        output_docx = file_path.with_suffix(".docx")
        with st.spinner("Converting to DOCX..."):
            try:
                render_docx(tokens, config, str(output_docx))
                st.sidebar.success(f"Saved to {output_docx}")
            except Exception as e:
                st.sidebar.error(f"Error: {e}")

