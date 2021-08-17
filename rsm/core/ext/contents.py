"""contents.py

rsm-contents and rsm-tree directives.

"""

from docutils import nodes
from docutils.transforms.parts import Contents as ContentsTransform

from sphinx.util.docutils import SphinxDirective


class RSMContents(SphinxDirective):
    has_content = False

    def run(self):
        # container
        document = self.state_machine.document
        classes = ['contents'] + self.options.get('class', [])
        container = nodes.topic(classes=classes)
        title = nodes.title()
        title += nodes.Text('Contents')
        container += title
        document.note_implicit_target(container)

        # table
        self.options.update({'backlinks': None})
        pending = nodes.pending(RSMContentsTransform, rawsource=self.block_text)
        pending.details.update(self.options)
        document.note_pending(pending)
        table = nodes.topic(ids=['table-of-contents'])
        table += pending
        container += table

        # tree
        tree = nodes.topic(ids=['tree-of-contents'])
        container += tree

        return [container]


class RSMContentsTransform(ContentsTransform):
    pass



def setup(app):
    app.add_directive('rsm-contents', RSMContents)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
