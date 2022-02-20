"""
util.py
-------

Utilities for RSM extensions.

"""

import re

from docutils import nodes
from sphinx.util.docutils import SphinxDirective

from misc import claim_start


# -- Directives ----------------------------------------------------------------------

class NodeClassDirective(SphinxDirective):
    """Directive that simply parses its contents and returns a specific node."""

    has_content = True
    nodeclass = None

    def run(self):
        node = self.nodeclass('\n'.join(self.content))
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class LabeledDirective:
    """Directive that admits a label option."""

    @property
    def label(self):
        return self.options['label'] if 'label' in self.options else None


class GoalDirective:
    """Directive that contains a claim that is the goal of a theorem or step."""

    def find_goal(self, node):
        """Find the claim that is the goal of node.

        Must be called after the contents of node have been parsed, usually with
        nested_parse.

        """
        for start in node.traverse(lambda n: isinstance(n, claim_start)):
            start.goal_set_by = node
            node.goal_for_substeps = start
            break


# -- References ----------------------------------------------------------------------

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


# -- Keywords ----------------------------------------------------------------------

KEYWORDS = {'LET', 'ASSUME', 'SUFFICES', 'DEFINE', 'PROVE', 'QED'}
SYMBOLS = {'⊢', '■'}
REGEX = re.compile(
    '|'.join(r'\b' + kw + r'\b ?' for kw in KEYWORDS)
    + '|'
    + '|'.join(SYMBOLS),
    re.UNICODE
)


def parse_keywords(source):
    for pattern in KEYWORDS | SYMBOLS:
        source = re.sub(pattern, f':kw:`{pattern}`', source)
    return source
