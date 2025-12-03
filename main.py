import typer
from pathlib import Path
from core.parser import MarkdownParser
from core.utils import load_config
from renderers.pdf_renderer import render_pdf
from renderers.docx_renderer import render_docx

app = typer.Typer()

@app.command()
def convert(
    input_file: str = typer.Argument(..., help="Path to input Markdown file"),
    output_format: str = typer.Option("pdf", "--format", "-f", help="Output format (pdf or docx)"),
    config_file: str = typer.Option("config/default_config.yaml", "--config", "-c", help="Path to config file"),
    output_file: str = typer.Option(None, "--output", "-o", help="Path to output file")
):
    """
    Convert Markdown to PDF or DOCX.
    """
    input_path = Path(input_file)
    if not input_path.exists():
        typer.echo(f"Error: Input file '{input_file}' not found.")
        raise typer.Exit(code=1)

    try:
        config = load_config(config_file)
    except Exception as e:
        typer.echo(f"Error loading config: {e}")
        raise typer.Exit(code=1)

    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read()

    parser = MarkdownParser()
    
    if output_format.lower() == "pdf":
        typer.echo("Converting to PDF...")
        html = parser.render_html(text)
        if not output_file:
            output_file = input_path.with_suffix(".pdf")
        render_pdf(html, config, str(output_file))
        typer.echo(f"PDF saved to {output_file}")
    elif output_format.lower() == "docx":
        typer.echo("Converting to DOCX...")
        tokens = parser.parse(text)
        if not output_file:
            output_file = input_path.with_suffix(".docx")
        render_docx(tokens, config, str(output_file))
        typer.echo(f"DOCX saved to {output_file}")
    else:
        typer.echo(f"Error: Unsupported format '{output_format}'")
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()
