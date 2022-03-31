"""
app.py
------

RSM Application: take a file path and output its contents as HTML.

"""

from pathlib import Path

from .reader import Reader
from .builder import Builder
from .writer import Writer


class Application:

    def __init__(self):
        self.path = None
        self.src = None
        self.tree = None
        self.html = None
        self.reader = Reader()
        self.builder = Builder()
        self.writer = Writer()

    def run(self, path: Path | str) -> str:
        self.path = Path(path)
        self.src = self.reader.read(path)
        self.tree = self.builder.build(self.src)
        self.html = self.writer.write(self.tree)
        return self.html
