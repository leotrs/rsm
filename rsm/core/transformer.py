"""
transformer.py
--------------

Apply transforms to the AbstractTreeManuscript.

"""

from icecream import ic

from typing import Type
import warnings
from .manuscript import AbstractTreeManuscript
from . import nodes

import logging

logger = logging.getLogger('RSM').getChild('Transformer')


class RSMTransformerError(Exception):
    pass


class Transformer:
    def __init__(self) -> None:
        self.tree: AbstractTreeManuscript | None = None
        self.labels_to_nodes: dict[str, nodes.Node] = {}

    def transform(self, tree: AbstractTreeManuscript) -> AbstractTreeManuscript:
        logger.info("Transforming...")
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

    def _label_to_node(self, label: str, default=None) -> nodes.Node:
        try:
            return self.labels_to_nodes[label]
        except KeyError as e:
            if default is None:
                raise RSMTransformerError(
                    f'Reference to nonexistent label "{label}" and no default given'
                )
            else:
                warnings.warn(f'Reference to nonexistent label "{label}"')
                return default()

    def resolve_pending_references(self) -> None:
        classes = [
            nodes.PendingReference,
            nodes.PendingCite,
            nodes.PendingPrev,
        ]

        for pending in self.tree.traverse(condition=lambda n: type(n) in classes):
            if isinstance(pending, nodes.PendingReference):
                target = self._label_to_node(pending.target)
                pending.replace_self(
                    nodes.Reference(
                        target=target,
                        overwrite_reftext=pending.overwrite_reftext,
                    )
                )
            elif isinstance(pending, nodes.PendingCite):
                targets = [
                    self._label_to_node(label, nodes.UnknownBibitem)
                    for label in pending.targetlabels
                ]
                pending.replace_self(nodes.Cite(targets=targets))
            elif isinstance(pending, nodes.PendingPrev):
                step = pending.first_ancestor_of_type(nodes.Step)
                li = step.parent.children
                if step is None:
                    raise RSMTransformerError('Found :prev: tag outside proof step')
                target = step.prev_sibling(nodes.Step)
                ic(target)
                if target is None:
                    raise RSMTransformerError(f'No previous step found')
                pending.replace_self(
                    nodes.Reference(
                        target=target, overwrite_reftext=pending.overwrite_reftext
                    )
                )

    def autonumber_nodes(self) -> None:
        counts = {
            nodes.Section: 0,
            nodes.Subsection: 0,
            nodes.Subsubsection: 0,
            nodes.DisplayMath: 0,
            nodes.Theorem: 0,
            nodes.Lemma: 0,
            nodes.Bibitem: 0,
            nodes.Step: 0,
        }
        for node in self.tree.traverse():
            nodeclass = type(node)
            if nodeclass in counts and not node.nonum:
                counts[nodeclass] += 1
                node.number = counts[nodeclass]
            if nodeclass is nodes.Section:
                counts[nodes.Subsubsection] = 0
                counts[nodes.Subsection] = 0
                counts[nodes.Theorem] = 0
                counts[nodes.Lemma] = 0
            if nodeclass is nodes.Subsection:
                counts[nodes.Subsubsection] = 0
                counts[nodes.Theorem] = 0
                counts[nodes.Lemma] = 0
            if nodeclass is nodes.Proof:
                counts[nodes.Step] = 0
