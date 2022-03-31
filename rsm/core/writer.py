"""
writer.py
---------

RSM Writer: take a HTML string and write it to disk.

"""

from pathlib import Path


class Writer:
    """Take a HTML string and write to disk."""

    def __init__(self):
        self.html: str = ''
        self.dst_path: Path = Path()

    def write(self, html: str, dst_path: Path) -> str:
        self.html = html
        self.dst_path = dst_path
        with open(dst_path / 'index.hml', 'w+', encoding='utf-8') as file:
            file.write(html)
        return
