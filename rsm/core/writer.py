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
        self.web: WebManuscript = None
        self.dst_path: Path = Path()

    def write(self, web: WebManuscript, dst_path: Path) -> str:
        self.web = web
        self.dst_path = dst_path
        copy_fs(web, './')
        return
