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


# def register_labels(app, document):
#     domain = app.env.get_domain('std')
#     for node in document.traverse(label):
#         docname = app.env.docname
#         labelid = node['ids'][0]

#         title = cast(nodes.title, node[0])
#         ref_name = getattr(title, 'rawsource', title.astext())
#         if app.config.autosectionlabel_prefix_document:
#             name = nodes.fully_normalize_name(docname + ':' + ref_name)
#         else:
#             name = nodes.fully_normalize_name(ref_name)
#         sectname = clean_astext(title)

#         if name in domain.labels:
#             logger.warning(__('duplicate label %s, other instance in %s'),
#                            name, app.env.doc2path(domain.labels[name][0]),
#                            location=node, type='autosectionlabel', subtype=docname)

#         domain.anonlabels[name] = docname, labelid
#         domain.labels[name] = docname, labelid, sectname


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
