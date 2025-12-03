You are an expert Python engineer specializing in document generation pipelines.

Your task is to design a Python-based system that converts Markdown (.md) files into:
- PDF
- Microsoft Word (.docx)

The system must:
1. Preserve Markdown semantics (headers, lists, tables, code blocks, links, images).
2. Allow fine-grained control over layout and visual design, including:
   - Page size and margins
   - Font family, size, line spacing
   - Heading hierarchy styles
   - Table styling (borders, padding, column widths, header rows)
   - Image scaling, alignment, captions
   - Hyperlinks and internal document references
3. Support deterministic output (same input → same result), no creative drift.
4. Be controlled via structured configuration (YAML or JSON), NOT hardcoded styles.
5. Allow an LLM to modify only the configuration and templates, never raw document content.

Design the system architecture and provide:
- A clear module structure
- Recommended Python libraries and why they are chosen
- A sample configuration file
- A high-level rendering flow (Markdown → intermediate → PDF/Word)
- Example Python code snippets for the critical steps
- Notes on pitfalls (tables, page breaks, fonts, Unicode, images)

Assume this will run locally, not as a web app.
Assume the user wants professional, publication-ready documents.
