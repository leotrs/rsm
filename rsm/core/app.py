"""
app.py
------

RSM Application: take a file path and output its contents as HTML.

"""

from pathlib import Path

from .manuscript import PlainTextManuscript, AbstractTreeManuscript, WebManuscript
from .reader import Reader
from .builder import Builder
from .translator import Translator
from .writer import Writer


class Application:

    def __init__(self):
        self.src_path: Path = Path()
        self.dst_path: Path = Path()
        self.plain: PlainTextManuscript = None
        self.tree: AbstractTreeManuscript = None
        self.web: WebManuscript = None
        self.reader = Reader()
        self.builder = Builder()
        self.translator = Translator()
        self.writer = Writer()

    def run(self, src_path: Path | str) -> str:
        self.src_path = Path(src_path)

        # Path -> PlainTextManuscript
        self.plain = self.reader.read(self.src_path)

        # PlainTextManuscript -> AbstractTreeManuscript
        self.tree = self.builder.build(self.plain)

        # AbstractTreeManuscript -> WebManuscript
        self.web = self.translator.translate(self.tree)

        # write WebManuscript to disk
        self.writer.write(self.web, self.dst_path)

        return self.web
