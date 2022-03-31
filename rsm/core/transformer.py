"""
transformer.py
--------------

Apply transforms to the AbstractTreeManuscript.

"""

from .manuscript import AbstractTreeManuscript

class Transformer:

    def __init__(self):
        self.tree: AbstractTreeManuscript = None

    def transform(self, tree: AbstractTreeManuscript) -> AbstractTreeManuscript:
        self.tree = tree
        return tree
