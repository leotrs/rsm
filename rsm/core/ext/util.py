"""
util.py
-------

Utilities for RSM extensions.

"""

from docutils import nodes


class LabeledDirective:
    @property
    def label(self):
        return self.options['label'] if 'label' in self.options else None


class Targetable:

    def default_link_text(self):
        raise NotImplementedError

    def register_as_target(self, env):
        # Makes :ref:`this_thm_id` work. Call only after self.number, self.label, and
        # self['ids'] have all been finalized. This usually happens during
        # AutoNumberTheoremLike.
        return register_as_target(self, env, self.default_link_text())


def register_as_target(node, env, link_text=None):
    domain = env.get_domain('std')
    for _id in node['ids']:
        name = nodes.fully_normalize_name(_id)
        domain.anonlabels[name] = env.docname, _id
        if link_text is not None:
            domain.labels[name] = env.docname, _id, link_text
