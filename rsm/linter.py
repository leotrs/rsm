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


LINT_LVL = 25


class Linter:
    def __init__(self) -> None:
        self.tree: Optional[nodes.Manuscript] = None
        logging.LINT = LINT_LVL
        logging.addLevelName(LINT_LVL, "LINT")
        main_logger.lint = lambda msg, *args, **kwargs: main_logger.log(
            LINT_LVL, msg, *args, **kwargs
        )
        if main_logger.level > LINT_LVL:
            main_logger.level = LINT_LVL
        target = logging.StreamHandler()
        target.setLevel(LINT_LVL)
        # target.setFormatter(RSMFormatter())
        self.handler = GatherHandler([logging.WARNING, LINT_LVL], target)
        self.handler.setLevel(LINT_LVL)
        main_logger.addHandler(self.handler)

    def flush(self) -> None:
        if not self.handler.buffer:
            print("No linting messages")
            return
        print()
        print("------ Start of linting output ------ ")
        self.handler.flush()
        print("------ End of linting output ------")

    def lint(self, tree: nodes.Manuscript) -> nodes.Manuscript:
        main_logger.info("Linting...")
        self.tree = tree
        main_logger.lint("this is a lint message")
        return self.tree
