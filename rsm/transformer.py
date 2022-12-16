"""Input: abstract syntax tree -- Output: (transformed) abstract syntax tree."""

import logging
from collections import defaultdict
from itertools import count
from string import ascii_uppercase
from typing import Generator, Optional, Type

from icecream import ic

from . import nodes

logger = logging.getLogger("RSM").getChild("tform")


class RSMTransformerError(Exception):
    pass


class Transformer:
    """Apply transformations to the abstract syntax tree."""

    def __init__(self) -> None:
        self.tree: Optional[nodes.Manuscript] = None
        self.labels_to_nodes: dict[str, nodes.Node] = {}

    def transform(self, tree: nodes.Manuscript) -> nodes.Manuscript:
        logger.info("Transforming...")
        self.tree = tree

        self.collect_labels()
        self.resolve_pending_references()
        self.add_necessary_subproofs()
        self.autonumber_nodes()
        self.make_toc()
        self.add_keywords_to_constructs()
        return tree

    def collect_labels(self) -> None:
        for node in self.tree.traverse(condition=lambda n: n.label):
            if node.label in self.labels_to_nodes:
                logger.warning(f"Duplicate label {node.label}, using first encountered")
                node.label = ""
                continue
            self.labels_to_nodes[node.label] = node

    def _label_to_node(self, label: str, default=nodes.Error) -> nodes.Node:
        try:
            return self.labels_to_nodes[label]
        except KeyError as e:
            logger.warning(f'Reference to nonexistent label "{label}"')
            return default(f'[unknown label "{label}"]')

    def resolve_pending_references(self) -> None:
        classes = [
            nodes.PendingReference,
            nodes.PendingCite,
            nodes.PendingPrev,
        ]

        counter = count()
        for pending in self.tree.traverse(condition=lambda n: type(n) in classes):
            if isinstance(pending, nodes.PendingReference):
                target = self._label_to_node(pending.target)
                if isinstance(target, nodes.Error):
                    pending.replace_self(target)
                else:
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
                cite = nodes.Cite(targets=targets)
                cite.label = f"cite-{next(counter)}"
                pending.replace_self(cite)
                for tgt in targets:
                    tgt.backlinks.append(cite.label)
            elif isinstance(pending, nodes.PendingPrev):
                try:
                    step = pending.first_ancestor_of_type(nodes.Step)
                except AttributeError:
                    step = None
                if step is None:
                    raise RSMTransformerError("Found :prev: tag outside proof step")

                target = step
                for _ in range(int(str(pending.target))):
                    target = target.prev_sibling(nodes.Step)
                    if target is None:
                        raise RSMTransformerError(
                            f"Did not find previous {pending.target} step(s)"
                        )
                pending.replace_self(
                    nodes.Reference(
                        target=target, overwrite_reftext=pending.overwrite_reftext
                    )
                )

        for pending in self.tree.traverse(condition=lambda n: type(n) in classes):
            raise RSMTransformerError("Found unresolved pending reference")

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
                raise RSMTransformerError("How did we get here?")
            step.append([statement, subproof])

    def autonumber_nodes(self) -> None:
        counts: dict[Type[nodes.Node], dict[Type[nodes.Node], Generator]] = defaultdict(
            lambda: defaultdict(lambda: count(start=1))
        )
        within_appendix = False
        for node in self.tree.traverse():

            if isinstance(node, nodes.Appendix):
                counts[nodes.Manuscript] = defaultdict(lambda: iter(ascii_uppercase))
                within_appendix = True
                continue
            if isinstance(node, (nodes.Proof, nodes.Subproof)):
                self._autonumber_steps(node)
                continue
            if isinstance(node, nodes.Step):
                continue

            if node.autonumber and not node.nonum:
                counts[type(node)] = defaultdict(lambda: count(start=1))
                num = next(counts[node.number_within][node.number_as])
                node.number = num
                if within_appendix and isinstance(node, nodes.Section):
                    node.reftext_template = node.reftext_template.replace(
                        "{nodeclass}", "Appendix"
                    )

    def _autonumber_steps(self, proof: nodes.Proof) -> None:
        step_gen = (s for s in proof.children if isinstance(s, nodes.Step))
        for idx, step in enumerate(step_gen, start=1):
            step.number = idx

    def make_toc(self) -> None:
        toc = None
        for node in self.tree.traverse(nodeclass=nodes.Contents):
            if toc is None:
                toc = node
            else:
                logger.warning("Multiple Tables of Content found, using only first one")
                node.remove_self()
        if toc is None:
            return

        current_parent = toc
        for sec in self.tree.traverse(nodeclass=nodes.Section):
            item = nodes.Item()

            # Sections with no number are still displayed in the TOC, while sub- or
            # subsubsections are simply ignored
            if sec.nonum and isinstance(node, nodes.Subsection):
                continue
            reftext = f"{sec.title}" if sec.nonum else f"{sec.full_number}. {sec.title}"

            item.append(nodes.Reference(target=sec, overwrite_reftext=reftext))
            if type(sec) is nodes.Section:
                toc.append(item)
                if sec.first_of_type(nodes.Subsection):
                    itemize = nodes.Itemize()
                    item.append(itemize)
                    current_parent = itemize
            elif type(sec) is nodes.Subsection:
                current_parent.append(item)
                if sec.first_of_type(nodes.Subsubsection):
                    itemize = nodes.Itemize()
                    item.append(itemize)
                    current_parent = itemize
            else:
                current_parent.append(item)

    def add_keywords_to_constructs(self) -> None:
        for construct in self.tree.traverse(nodeclass=nodes.Construct):
            keyword = nodes.Keyword()
            keyword.append(nodes.Text(f"{construct.keyword} "))
            construct.prepend(keyword)

            kind = construct.kind
            assert kind
            construct.types.append(kind)
            if kind not in {"then", "suffices", "claim", "claimblock", "qed"}:
                construct.types.append("assumption")
