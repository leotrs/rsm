"""
linter.py
---------

RSM Linter: analyze the manuscript tree and log linting messages.

"""

import logging
from typing import Optional

from . import nodes
from .rsmlogger import GatherHandler

main_logger = logging.getLogger("RSM")
logger = logging.getLogger("RSM").getChild("Linter")


class Linter:
    LINT_LVL = 25

    def __init__(self) -> None:
        self.tree: Optional[nodes.Manuscript] = None
        logging.LINT = self.LINT_LVL
        logging.addLevelName(self.LINT_LVL, "LINT")
        main_logger.lint = lambda msg, *args, **kwargs: main_logger.log(
            self.LINT_LVL, msg, *args, **kwargs
        )
        if main_logger.level > self.LINT_LVL:
            main_logger.level = self.LINT_LVL

    def lint(self, tree: nodes.Manuscript) -> nodes.Manuscript:
        main_logger.info("Linting...")
        self.tree = tree
        main_logger.lint("this is a lint message")
        return self.tree
