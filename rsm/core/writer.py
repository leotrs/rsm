"""writer.py

Custom HTML writer for RSM.

"""

from sphinx.writers.html5 import HTML5Translator


class RSMTranslator(HTML5Translator):

    def visit_title(self, node):
        self.body.append('<div class="left-border left-offset">')
        super().visit_title(node)

    def depart_title(self, node):
        super().depart_title(node)
        self.body.append('</div>')


def setup(app):
    app.registry.add_translator('html', RSMTranslator)
