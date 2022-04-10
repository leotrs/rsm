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
        self.autonumber_nodes()

        return tree

    def collect_labels(self) -> None:
        for node in self.tree.traverse(lambda n: n.label):
            if node.label in self.labels_to_nodes:
                raise RSMTransformerError(f'Duplicate label {node.label}')
            self.labels_to_nodes[node.label] = node

    def resolve_pending_references(self) -> None:
        pending: nodes.PendingReference
        for pending in self.tree.traverse(nodeclass=nodes.PendingReference):
            try:
                target = self.labels_to_nodes[pending.targetlabel]
            except KeyError as e:
                raise RSMTransformerError(
                    f'Reference to nonexistent label "{pending.targetlabel}"'
                ) from e
            pending.replace_self(nodes.Reference(
                target=target,
                overwrite_reftext=pending.overwrite_reftext,
            ))

        node: nodes.PendingReference
        for node in self.tree.traverse(nodeclass=nodes.PendingReference):
            raise RSMTransformerError(f'Found unresolved referece to "{node.targetlabel}"')

    def autonumber_nodes(self) -> None:
        counts = {
            nodes.Section: 0,
            nodes.DisplayMath: 0,
            nodes.Theorem: 0,
            nodes.Lemma: 0,
        }
        for node in self.tree.traverse():
            nodeclass = type(node)
            if nodeclass in counts and not node.nonum:
                counts[nodeclass] += 1
                node.number = counts[nodeclass]
