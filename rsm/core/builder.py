"""
builder.py
----------

RSM Builder: take a complete source string and output a Manuscript.

"""

from .nodes import Manuscript
from .parser import ManuscriptParser


class Builder:

    def __init__(self):
        self.src: str = None
        self.tree: Manuscript | None = None
        self.parser: ManuscriptParser | None = None

    def build(self, src: str) -> Manuscript:
        self.src = src
        self.parser = ManuscriptParser(src)
        self.tree = self.parser.parse()
        return self.tree
