import re
from markdown_it import MarkdownIt
from mdit_py_plugins.front_matter import front_matter_plugin
from mdit_py_plugins.footnote import footnote_plugin
from mdit_py_plugins.tasklists import tasklists_plugin


def page_break_plugin(md):
    r"""Plugin to handle \newpage and \pagebreak commands."""
    
    def page_break_rule(state, startLine, endLine, silent):
        """Block rule to detect page break commands."""
        pos = state.bMarks[startLine] + state.tShift[startLine]
        maximum = state.eMarks[startLine]
        
        # Get the line content
        line = state.src[pos:maximum].strip()
        
        # Check if line matches \newpage or \pagebreak
        if line in (r'\newpage', r'\pagebreak'):
            if silent:
                return True
            
            # Create token
            token = state.push('page_break', '', 0)
            token.markup = line
            token.map = [startLine, startLine + 1]
            
            state.line = startLine + 1
            return True
        
        return False
    
    # Register the block rule
    md.block.ruler.before('fence', 'page_break', page_break_rule)
    
    # Add renderer rule
    def render_page_break(tokens, idx, options, env, renderer):
        return '<div class="page-break"></div>\n'
    
    md.add_render_rule('page_break', render_page_break)


class MarkdownParser:
    def __init__(self):
        self.md = (
            MarkdownIt("commonmark", {"breaks": True, "html": True})
            .use(front_matter_plugin)
            .use(footnote_plugin)
            .use(tasklists_plugin)
            .use(page_break_plugin)
            .enable("image")
            .enable("link")
            .enable("table")
        )

    def parse(self, text: str):
        return self.md.parse(text)

    def render_html(self, text: str):
        return self.md.render(text)
