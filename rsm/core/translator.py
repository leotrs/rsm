"""
translator.py
-------------

RSM Translator: take a Manuscript and return a HTML string.

"""

from collections import namedtuple
from icecream import ic

from .nodes import Node
from .manuscript import AbstractTreeManuscript, HTMLBodyManuscript


Action = namedtuple('Action', 'node action method')


class ActionStack(list):

    def push_visit(self, node):
        self.append(Action(node, 'visit', Translator.get_visit_method(node)))

    def push_leave(self, node):
        self.append(Action(node, 'leave', Translator.get_leave_method(node)))


class Translator:

    def __init__(self):
        self.tree: AbstractTreeManuscript = None
        self.body: HTMLBodyManuscript = ''

    @classmethod
    def _get_action_method(cls, node, action):
        nodeclass = node.__class__
        method = f'{action}_{nodeclass.__name__.lower()}'
        while not hasattr(cls, method):
            nodeclass = nodeclass.__bases__[0]
            method = f'{action}_{nodeclass.__name__.lower()}'
        return getattr(cls, method)

    @classmethod
    def get_visit_method(cls, node):
        return cls._get_action_method(node, 'visit')

    @classmethod
    def get_leave_method(cls, node):
        return cls._get_action_method(node, 'leave')

    def translate(self, tree: AbstractTreeManuscript) -> HTMLBodyManuscript:
        self.tree = tree

        stack = ActionStack()
        stack.push_visit(tree)
        while stack:
            node, action, method = stack.pop()
            if action == 'visit':
                stack.push_leave(node)
                for child in reversed(node.children):
                    stack.push_visit(child)
            method(self, node)

        return self.body

    def start_tag(self, node: Node, tag: str = 'div') -> str:
        html = f'<{tag}'
        if node.label:
            html += f' id="{node.label}"'
        classname = node.__class__.__name__.lower()
        classes = ' '.join([classname] + node.types)
        html += f' class="{classes}"'
        html += '>'
        return html

    def visit_node(self, node: Node) -> None:
        self.body += str(node) + '\n'

    def leave_node(self, node: Node) -> None:
        pass

    def visit_manuscript(self, node: Node) -> None:
        if not node.label:
            node.label = 'manuscript'
        self.body += '<body>\n'
        self.body += self.start_tag(node) + '\n'
        self.body += '<section class="level-1">\n'
        self.body += f'<h1>{node.title}</h1>\n'

    def leave_manuscript(self, node: Node) -> None:
        self.body += '</section>\n</div>\n</body>\n'

    def visit_author(self, node: Node) -> None:
        self.body += self.start_tag(node) + '\n'
        self.body += f'{node.name}\n{node.affiliation}\n{node.email}\n'

    def leave_author(self, node: Node) -> None:
        self.body += '</div>\n'

    def visit_abstract(self, node: Node) -> None:
        self.body += self.start_tag(node) + '\n'
        self.body += '<h3>Abstract</h3>\n'

    def leave_abstract(self, node: Node) -> None:
        if node.keywords:
            text = ', '.join(node.keywords)
            self.body += f'<p class="abstract keywords">\nKeywords: {text}\n</p>\n'
        if node.MSC:
            text = ', '.join(node.MSC)
            self.body += f'<p class="MSC">\nMSC: {text}</p>\n'
        self.body += '</div>\n'

    def visit_paragraph(self, node: Node) -> None:
        self.body += self.start_tag(node, 'p') + '\n'

    def leave_paragraph(self, node: None) -> None:
        self.body += '</p>\n'

    def visit_section(self, node: None) -> None:
        node.types.insert(0, 'level-2')
        self.body += self.start_tag(node, 'section') + '\n'

    def leave_section(self, node: Node) -> None:
        self.body += '</section>\n'

    def visit_text(self, node: Node) -> None:
        self.body += node.text
