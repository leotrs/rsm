"""
builder.py
----------

RSM Builder: take a complete source string and output a Manuscript.

"""

from .manuscript import HTMLBodyManuscript, WebManuscript
from .parser import ManuscriptParser


class Builder:

    def __init__(self):
        self.body: HTMLBodyManuscript = None
        self.web: WebManuscript = None

    def build(self, body: HTMLBodyManuscript) -> WebManuscript:
        self.body = body
        self.web = WebManuscript(self.body)
        return self.web
