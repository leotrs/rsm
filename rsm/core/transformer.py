"""
transformer.py
--------------

Apply transforms to the AbstractTreeManuscript.

"""

from icecream import ic

from typing import Type
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

    def _label_to_node(self, label) -> Type[nodes.Node]:
        try:
            node = self.labels_to_nodes[label]
        except KeyError as e:
            raise RSMTransformerError(
                f'Reference to nonexistent label "{pending.targetlabel}"'
            ) from e
        return node

    def resolve_pending_references(self) -> None:
        condition = lambda n: type(n) in [nodes.PendingReference, nodes.PendingCite]
        for pending in self.tree.traverse(condition=condition):
            if isinstance(pending, nodes.PendingReference):
                target = self._label_to_node(pending.targetlabel)
                pending.replace_self(
                    nodes.Reference(
                        target=target,
                        overwrite_reftext=pending.overwrite_reftext,
                    )
                )
            elif isinstance(pending, nodes.PendingCite):
                targets = [self._label_to_node(label) for label in pending.targetlabels]
                pending.replace_self(nodes.Cite(targets=targets))

        node: nodes.PendingReference
        for node in self.tree.traverse(nodeclass=nodes.PendingReference):
            raise RSMTransformerError(
                f'Found unresolved referece to "{node.targetlabel}"'
            )

    def autonumber_nodes(self) -> None:
        counts = {
            nodes.Section: 0,
            nodes.DisplayMath: 0,
            nodes.Theorem: 0,
            nodes.Lemma: 0,
            nodes.Bibitem: 0,
        }
        for node in self.tree.traverse():
            nodeclass = type(node)
            if nodeclass in counts and not node.nonum:
                counts[nodeclass] += 1
                node.number = counts[nodeclass]
