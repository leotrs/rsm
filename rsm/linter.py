"""
linter.py
---------

RSM Linter: analyze the manuscript tree and log linting messages.

"""

import logging
from typing import Optional

from . import nodes
from .rsmlogger import GatherHandler

logger = logging.getLogger("RSM")


class Linter:
    LINT_LVL = 25

    def __init__(self) -> None:
        self.tree: Optional[nodes.Manuscript] = None
        logging.LINT = self.LINT_LVL
        logging.addLevelName(self.LINT_LVL, "LINT")
        logger.lint = lambda msg, *args, **kwargs: logger.log(
            self.LINT_LVL, msg, *args, **kwargs
        )
        if logger.level > self.LINT_LVL:
            logger.level = self.LINT_LVL

    def lint(self, tree: nodes.Manuscript) -> nodes.Manuscript:
        logger.info("Linting...")
        self.tree = tree

        self.lint_manuscript_title()
        self.lint_section_label()

    def _extra(self, node):
        return {
            "start_row": node.start_point[0] + 1,
            "start_col": node.start_point[1] + 1,
        }

    def lint_manuscript_title(self):
        if not self.tree.title:
            logger.lint("Manuscript with no title", extra=self._extra(self.tree))
        return self.tree

    def lint_section_label(self):
        for section in self.tree.traverse(nodeclass=nodes.Section):
            if not section.label:
                logger.lint("Section with no label", extra=self._extra(section))
