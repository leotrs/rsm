"""envs.py

This file defines a number of ReST directives that provide theorem-like environments.

"""

from icecream import ic

from docutils import nodes

from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective
from sphinx.transforms import SphinxTransform

from util import Targetable, LabeledDirective


class theorem_like_title(nodes.strong): pass


# Main node class for all theorem-like environments
class theorem_like(nodes.Element, Targetable):

    def __init__(self, content,  label=None, *args, **kwargs):
        super().__init__(content, *args, **kwargs)
        self._number = None      # will be filled by AutoNumberTheoremLike
        self.label = label
        if self.label is not None:
            self['ids'] = [label]

        # The contents of self.attributes['classes'] are added as html tag class (for
        # example '<div class="...">').
        html_class = self.__class__.__name__
        classes = ['theorem-env', 'handrail', html_class]
        self.attributes['classes'] += classes

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


# DO NOT use this directive!
# Subclass it and change the node_class
class TheoremLikeDirective(SphinxDirective, LabeledDirective):
    node_class = None
    option_spec = {'label': str}
    has_content = True

    def run(self):
        node = self.node_class(
            content='\n'.join(self.content),
            label=self.label
        )
        self.state.nested_parse(self.content, self.content_offset, node)
        assert len(node.children), 'Theorem-like environment cannot be empty'
        assert isinstance(node.children[0], nodes.paragraph), 'First child of theorem-like must be paragraph'
        return [node]


# DO use these directives, each must subclass TheoremLikeDirective and use the correct
# node class.
class theorem(theorem_like): pass
class proposition(theorem_like): pass
class remark(theorem_like): pass
class sketch(theorem_like): pass
class lemma(theorem_like): pass
class corollary(theorem_like): pass

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

    def apply(self, **kwargs):
        for node in self.document.traverse(theorem_like):
            cls = type(node)
            number = self.counts[cls]
            label = f'{self.prefix[cls]}-{number}'
            if not node.label:
                node.label = label
            node['ids'].append(label)
            node.number = number # MUST set number after setting label
            self.counts[cls] += 1
            node.register_as_target(self.env)


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


# -- UI -----------------------------------------------------------------
# tooltips
# table of contents
# auto number sections
# refactor handrail--hug (almost all handrails are hug...)
#
# -- MVC ----------------------------------------------------------------
# the doctree is my model, the html/css is my view
# only use JS for complex selectors and adding/removing classes
# anything more complicated goes to rsm-read (exception tooltips)

# Remember
#
# as much as possible, only use margin-bottom
# Use margins when pushing blocks away from each other
# Use padding when pushing things into their own block




# Use something similar to the following in order to reduce boilerplate:
#
# class GenericRole(object):
#     def __init__(self, role_name, node_class):
#         self.name = role_name
#         self.node_class = node_class
#     def __call__(self, role, rawtext, text, lineno, inliner,
#                  options={}, content=[]):
#         set_classes(options)
#         return [self.node_class(rawtext, text, **options)], []
