"""
transformer.py
--------------

Apply transforms to the AbstractTreeManuscript.

"""

from icecream import ic

from .manuscript import AbstractTreeManuscript
from . import nodes


class RSMTransformerError(Exception):
    pass


class Transformer:

    def __init__(self):
        self.tree: AbstractTreeManuscript = None
        self.labels_to_nodes: dict = {}

    def transform(self, tree: AbstractTreeManuscript) -> AbstractTreeManuscript:
        self.tree = tree

        self.collect_labels()
        self.resolve_pending_references()

        return tree

    def collect_labels(self):
        for node in self.tree.traverse(lambda n: n.label):
            self.labels_to_nodes[node.label] = node

    def resolve_pending_references(self):
        for node in self.tree.traverse(nodeclass=nodes.PendingReference):
            try:
                target = self.labels_to_nodes[node.targetlabel]
                node.replace_self(nodes.Reference(target=target))
            except KeyError as e:
                raise RSMTransformerError(
                    f'Reference to nonexistent label "{node.targetlabel}"'
                ) from e

        for node in self.tree.traverse(nodeclass=nodes.PendingReference):
            raise RSMTransformerError(f'Found unresolved referece to "{node.targetlabel}"')
