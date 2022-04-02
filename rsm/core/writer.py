"""
writer.py
---------

RSM Writer: take a HTML string and write it to disk.

"""

from pathlib import Path

from .manuscript import WebManuscript

class Writer:
    """Take a HTML string and write to disk."""

    def __init__(self):
        self.html: str = ''
        self.dst_path: Path = Path()

    def write(self, web: WebManuscript, dst_path: Path) -> str:
        self.web = web
        self.dst_path = dst_path
        with open(dst_path / 'index.html', 'w+', encoding='utf-8') as file:
            file.write(self.web.body)
        return
