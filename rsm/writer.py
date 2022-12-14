"""Input: WebManuscript -- Output: None (writes to disk)."""

from fs.copy import copy_fs
from pathlib import Path

from .manuscript import WebManuscript

import logging

logger = logging.getLogger("RSM").getChild("write")


class Writer:
    """Take a WebManuscript and write to disk."""

    def __init__(self, dstpath: Path | None = None) -> None:
        self.web: WebManuscript | None = None
        self.dstpath = Path() if dstpath is None else dstpath

    def write(self, web: WebManuscript) -> None:
        self.web = web
        copy_fs(web, "./")
