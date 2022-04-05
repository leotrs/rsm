"""
writer.py
---------

RSM Writer: take a HTML string and write it to disk.

"""

from fs.copy import copy_fs
from pathlib import Path

from .manuscript import WebManuscript


class Writer:
    """Take a HTML string and write to disk."""

    def __init__(self):
        self.web: WebManuscript | None = None
        self.dstpath: Path = Path()

    def write(self, web: WebManuscript, dstpath: Path):
        self.web = web
        self.dstpath = dstpath
        copy_fs(web, './')
