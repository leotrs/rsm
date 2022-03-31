"""
writer.py
---------

RSM Writer: take a document tree and output an HTML string.

"""

from .nodes import Manuscript


class Writer:

    def __init__(self):
        self.tree = None
        self.html = None

    def write(self, tree: Manuscript) -> str:
        self.tree = tree
        self.html = str(tree)
        return self.html
