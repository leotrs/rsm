"""
builder.py
----------

RSM Builder: take a complete source string and output a Manuscript.

"""

from .manuscript import PlainTextManuscript, AbstractTreeManuscript, WebManuscript
from .parser import ManuscriptParser


class Builder:

    def __init__(self):
        self.src: str = None
        self.plain: PlainTextManuscript = None
        self.tree: AbstractTreeManuscript = None
        self.parser: ManuscriptParser = None

    def build(self, plain: PlainTextManuscript) -> WebManuscript:
        self.plain = plain
        self.parser = ManuscriptParser(plain)
        self.tree = self.parser.parse()
        # apply transforms and resolve references
        return self.tree
