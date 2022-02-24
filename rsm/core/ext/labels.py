"""labels.py

Define label nodes that allow the user to drop labels anywhere on the document.

"""

from docutils import nodes

from sphinx.transforms import SphinxTransform

from util import register_as_target


class pending_label(nodes.Element):
    def __init__(self, lbl, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = lbl


def label_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    return [pending_label(text)], []


class ResolvePendingLabels(SphinxTransform):
    default_priority = 100

    def apply(self, **kwargs):
        for node in self.document.traverse(pending_label):
            assert isinstance(node.parent, nodes.Element)
            node.parent['ids'].append(node.label)
            register_as_target(node.parent, self.env)
            node.replace_self([])


def setup(app):
    # app.connect('doctree-read', register_labels)
    app.add_role('label', label_role)
    app.add_transform(ResolvePendingLabels)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
