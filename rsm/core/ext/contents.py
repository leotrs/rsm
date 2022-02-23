"""contents.py

rsm-contents and rsm-tree directives.

"""

from docutils import nodes
from docutils.transforms.parts import Contents as ContentsTransform

from sphinx.util.docutils import SphinxDirective


class contents_title(nodes.title):
    pass


class abstract_title(nodes.title):
    pass


class RSMContents(SphinxDirective):
    has_content = False

    def run(self):
        # container
        document = self.state_machine.document
        classes = ['contents'] + self.options.get('class', [])
        container = nodes.topic(ids=['contents'], classes=classes)

        title = contents_title()
        title += nodes.Text('Contents')
        container += title
        document.note_implicit_target(container)

        # table
        self.options.update({'backlinks': None})
        pending = nodes.pending(RSMContentsTransform, rawsource=self.block_text)
        pending.details.update(self.options)
        document.note_pending(pending)
        table = nodes.topic(ids=['table-of-contents'], classes=['hide'])
        table += pending
        container += table

        # tree
        tree = nodes.topic(ids=['tree-of-contents'])
        container += tree

        return [container]


class RSMContentsTransform(ContentsTransform):

    def copy_and_filter(self, node):
        text = super().copy_and_filter(node)
        if text[0].startswith(':no-num:'):
            text[0] = nodes.Text(text[0][8:])
        return text


class Abstract(SphinxDirective):

    has_content = True

    def run(self):
        self.assert_has_content()
        abstract = nodes.topic(ids=['abstract'])
        title = abstract_title()
        title += nodes.Text('Abstract')
        abstract += title
        self.state.nested_parse(self.content, self.content_offset, abstract)
        return [abstract]


def setup(app):
    app.add_directive('abstract', Abstract)
    app.add_directive('rsm-contents', RSMContents)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
