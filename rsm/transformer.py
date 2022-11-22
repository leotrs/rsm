"""
transformer.py
--------------

Apply transforms to the nodes.Manuscript.

"""

from icecream import ic

from collections import defaultdict
from typing import Type
from . import nodes

import logging

logger = logging.getLogger('RSM').getChild('tform')


class RSMTransformerError(Exception):
    pass


class Transformer:
    def __init__(self) -> None:
        self.tree: nodes.Manuscript | None = None
        self.labels_to_nodes: dict[str, nodes.Node] = {}

    def transform(self, tree: nodes.Manuscript) -> nodes.Manuscript:
        logger.info("Transforming...")
        self.tree = tree

        self.collect_labels()
        self.resolve_pending_references()
        self.add_necessary_subproofs()
        self.autonumber_nodes()

        return tree

    def collect_labels(self) -> None:
        for node in self.tree.traverse(condition=lambda n: n.label):
            if node.label in self.labels_to_nodes:
                logger.warning(f'Duplicate label {node.label}, using first encountered')
                node.label = ''
                continue
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
                logger.warning(f'Reference to nonexistent label "{label}"')
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
                try:
                    step = pending.first_ancestor_of_type(nodes.Step)
                except AttributeError:
                    step = None
                if step is None:
                    raise RSMTransformerError('Found :prev: tag outside proof step')

                target = step
                for _ in range(int(str(pending.target))):
                    target = target.prev_sibling(nodes.Step)
                    if target is None:
                        raise RSMTransformerError(
                            f'Did not find previous {pending.target} step(s)'
                        )
                pending.replace_self(
                    nodes.Reference(
                        target=target, overwrite_reftext=pending.overwrite_reftext
                    )
                )

        for pending in self.tree.traverse(condition=lambda n: type(n) in classes):
            raise RSMTransformerError('Found unresolved pending reference')

    def add_necessary_subproofs(self) -> None:
        for step in self.tree.traverse(nodeclass=nodes.Step):
            if not step.children:
                continue

            _, split_at_idx = step.first_of_type(
                (nodes.Step, nodes.Subproof), return_idx=True
            )
            if split_at_idx is None:
                split_at_idx = len(step.children)

            children = step.children[::]
            step.clear()

            statement = nodes.Statement()
            statement.append(children[:split_at_idx])

            if split_at_idx == len(children):
                step.append(statement)
                continue

            if isinstance(children[split_at_idx], nodes.Step):
                subproof = nodes.Subproof()
                subproof.append(children[split_at_idx:])
            elif isinstance(children[split_at_idx], nodes.Subproof):
                assert split_at_idx == len(children) - 1
                subproof = children[split_at_idx]
            else:
                raise RSMTransformerError('How did we get here?')
            step.append([statement, subproof])

    def autonumber_nodes(self) -> None:
        counts: dict[Type[nodes.Node], dict[Type[nodes.Node], int]] = defaultdict(
            lambda: defaultdict(int)
        )
        for node in self.tree.traverse():
            if isinstance(node, (nodes.Proof, nodes.Subproof)):
                self._autonumber_steps(node)
                continue
            if isinstance(node, (nodes.Step, nodes.Subproof)):
                continue

            if node.autonumber and not node.nonum:
                counts[type(node)] = defaultdict(int)
                num = counts[node.number_within][node.number_as]
                node.number = num + 1
                counts[node.number_within][node.number_as] = num + 1

    def _autonumber_steps(self, proof: nodes.Proof) -> None:
        step_gen = (s for s in proof.children if isinstance(s, nodes.Step))
        for idx, step in enumerate(step_gen, start=1):
            step.number = idx
