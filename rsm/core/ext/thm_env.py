"""envs.py

This file defines a number of ReST directives that provide theorem-like environments.

"""

from icecream import ic

from docutils import nodes
from docutils.statemachine import StringList

from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective
from sphinx.transforms import SphinxTransform

from util import Targetable, LabeledDirective, GoalDirective, parse_keywords
from misc import claim_start, claim_end


# -- Nodes ---------------------------------------------------------------------------

class theorem_like_title(nodes.strong):
    pass


# Main node class for all theorem-like environments
class theorem_like(nodes.Element, Targetable):

    def __init__(self, content,  label=None, stars=0, clocks=0, *args, **kwargs):
        super().__init__(content, *args, **kwargs)
        self._number = None      # will be filled by AutoNumberTheoremLike
        self.label = label
        if self.label is not None:
            self['ids'] = [label]
        self.stars = stars
        self.clocks = clocks
        self.goal_for_substeps = None

        # The contents of self.attributes['classes'] are added as html tag class (for
        # example '<div class="...">').
        html_class = self.__class__.__name__
        self.attributes['classes'] += ['theorem-env', html_class]

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        self._number = number
        if self.children:
            name = self.__class__.__name__.capitalize()
            self.title = theorem_like_title(text=f'{name} {number}. ')
            self.children[0].insert(0, self.title)

    def default_link_text(self):
        cls = self.__class__.__name__.capitalize()
        return f'{cls} {self.number}'


class theorem(theorem_like): pass
class proposition(theorem_like): pass
class remark(theorem_like): pass
class sketch(theorem_like): pass
class lemma(theorem_like): pass
class corollary(theorem_like): pass


# -- Directives ----------------------------------------------------------------------

# DO NOT use this directive! Subclass it and change the node_class.
class TheoremLikeDirective(SphinxDirective, LabeledDirective, GoalDirective):
    node_class = None
    has_content = True
    option_spec = {
        'label': str,
        'stars': int,
        'clocks': int,
    }

    def run(self):
        content = parse_keywords('\n'.join(self.content))
        node = self.node_class(
            content=content,
            label=self.label,
            stars=self.options.get('stars', 0),
            clocks=self.options.get('clocks', 0),
        )
        self.content = StringList(
            content.split('\n'),
            parent=self.content.parent, parent_offset=self.content_offset
        )
        self.state.nested_parse(self.content, self.content_offset, node)
        assert len(node.children), 'Theorem-like environment cannot be empty'
        assert isinstance(node.children[0], nodes.paragraph), 'First child of theorem-like must be paragraph'
        self.find_goal(node)
        return [node]


# DO use these directives, each must subclass TheoremLikeDirective and use the correct
# node class.
class TheoremDirective(TheoremLikeDirective):
    node_class = theorem
class PropositionDirective(TheoremLikeDirective):
    node_class = proposition
class RemarkDirective(TheoremLikeDirective):
    node_class = remark
class SketchDirective(TheoremLikeDirective):
    node_class = sketch
class LemmaDirective(TheoremLikeDirective):
    node_class = lemma
class CorollaryDirective(TheoremLikeDirective):
    node_class = corollary


# -- Transforms ----------------------------------------------------------------------

class AutoNumberTheoremLike(SphinxTransform):
    default_priority = 600
    prefix = {
        theorem: 'thm',
        proposition: 'prp',
        lemma: 'lem',
        remark: 'rmk',
        sketch: 'skc',
        corollary: 'cor',
    }
    counts = {
        theorem: 1,
        proposition: 1,
        lemma: 1,
        remark: 1,
        sketch: 1,
        corollary: 1,
    }
    page_counts = {}

    def apply(self, **kwargs):
        src = self.document['source']
        if src not in self.page_counts:
            self.page_counts[src] = self.counts.copy()

        for node in self.document.traverse(theorem_like):
            cls = type(node)
            number = self.page_counts[src][cls]
            label = f'{self.prefix[cls]}-{number}'
            if not node.label:
                node.label = label
            node['ids'].append(label)
            node.number = number # MUST set number after setting label
            self.page_counts[src][cls] += 1
            node.register_as_target(self.env)


# -- Setup ----------------------------------------------------------------------

def setup(app):
    app.add_transform(AutoNumberTheoremLike)

    for node_class in [theorem, proposition, remark, sketch, lemma, corollary]:
        name = node_class.__name__
        app.add_node(node_class)
        app.add_directive(name, globals()[f'{name.capitalize()}Directive'])

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
