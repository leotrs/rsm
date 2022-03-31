"""
manuscript.py
-------------

Classes that represent the manuscript at different stages.

"""

from . import nodes


class PlainTextManuscript(str):
    pass


AbstractTreeManuscript = nodes.Manuscript


class WebManuscript:
    pass
