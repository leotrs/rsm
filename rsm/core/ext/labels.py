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

            # Because of the way ReST works, when we use the RSM syntax
            #
            # section title
            # -------------
            # :label`some-label`
            #
            # sphinx creates a paragraph whose only child is a pending_label node.  This
            # paragraph is the second child of the section node (the first child is the
            # title).  The following code checks if the current label is within an
            # otherwise empty paragraph that is the second child of the section.  If so,
            # we may assume that the current label is meant to label the entire section.
            # Otherwise, asume the user meant to label the paragraph it is part of.

            paragraph = node.parent
            section = node.parent.parent

            link_text = None
            if (
                    isinstance(node.parent.parent, nodes.section)
                    and paragraph.children == [node]
                    and section.children[1] == paragraph
            ):
                section['ids'].append(node.label)
                to_register = section
                paragraph.replace_self([])
                link_text = section.children[0].astext()

            else:
                paragraph['ids'].append(node.label)
                to_register = paragraph

            register_as_target(to_register, self.env, link_text)
            node.replace_self([])


def setup(app):
    app.add_role('label', label_role)
    app.add_transform(ResolvePendingLabels)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
