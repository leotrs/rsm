"""
manuscript.py
-------------

Classes that represent the manuscript at different stages.

"""

from . import nodes


class PlainTextManuscript(str):
    pass


AbstractTreeManuscript = nodes.Manuscript


class HTMLBodyManuscript(str):
    pass


class WebManuscript:
    def __init__(self, body: HTMLBodyManuscript):
        self.body = body
