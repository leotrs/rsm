"""
reader.py
---------

RSM Reader: take a file path and return a string.

"""

from pathlib import Path


class Reader:

    def __init__(self):
        self.path = None
        self.src = None

    def read(self, path: Path) -> str:
        self.path = path
        with open(path) as file:
            self.src = file.read()
        return self.src
