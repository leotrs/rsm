"""
reader.py
---------

RSM Reader: take a file path and return a string.

"""

from pathlib import Path

from .manuscript import PlainTextManuscript


class Reader:

    def __init__(self):
        self.path: Path = Path()
        self.src: str = ''

    def read(self, path: Path | None) -> PlainTextManuscript:
        if not path:
            raise TypeError('Expected path, got None')
        self.path = Path(path)
        with open(path) as file:
            self.src = file.read()
        return PlainTextManuscript(self.src)
