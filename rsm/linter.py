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
        if not tree.title:
            logger.lint(
                "Manuscript with no title",
                extra=dict(start_row=1, start_col=12),
            )
        return self.tree
