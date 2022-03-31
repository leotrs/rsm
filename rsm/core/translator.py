"""
translator.py
-------------

RSM Translator: take a Manuscript and return a HTML string.

"""

from collections import namedtuple
from icecream import ic

from .nodes import Manuscript


Action = namedtuple('Action', 'node action method')


class ActionStack(list):

    def push_visit(self, node):
        self.append(Action(node, 'visit', Translator.get_visit_method(node)))

    def push_leave(self, node):
        self.append(Action(node, 'leave', Translator.get_leave_method(node)))


class Translator:

    def __init__(self):
        self.tree: Manuscript | None = None
        self.html: str = ''

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

    def translate(self, tree: Manuscript) -> str:
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

        return self.html

    def visit_node(self, node):
        self.html += str(node) + '\n'

    def leave_node(self, node):
        pass

    def visit_manuscript(self, node):
        self.visit_node(node)
        self.html += f"""
<!DOCTYPE html>

<html>
  <head>
    <meta charset="utf-8" />
    <title>{node.title}</title>
    <script crossorigin="anonymous" src="https://kit.fontawesome.com/0e1aa62e6e.js"></script>
  </head>

  <body>
"""

    def leave_manuscript(self, node):
        self.html += """
   </body>
</html>
"""
