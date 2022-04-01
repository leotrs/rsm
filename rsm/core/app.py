"""
app.py
------

RSM Application: take a file path and output its contents as HTML.

"""

from pathlib import Path
from icecream import ic

from .manuscript import (
    PlainTextManuscript,
    HTMLBodyManuscript,
    AbstractTreeManuscript,
    WebManuscript,
)
from .reader import Reader
from .parser import ManuscriptParser
from .transformer import Transformer
from .translator import Translator
from .builder import Builder
from .writer import Writer


class Application:

    def __init__(self):
        self.src_path: Path = Path()
        self.dst_path: Path = Path()
        self.plain: PlainTextManuscript = None
        self.tree: AbstractTreeManuscript = None
        self.body: HTMLBodyManuscript = None
        self.web: WebManuscript = None
        self.reader: Reader = Reader()
        self.parser: ManuscriptParser = ManuscriptParser()
        self.transformer: Transformer = Transformer()
        self.translator: Translator = Translator()
        self.builder: Builder = Builder()
        self.writer: Writer = Writer()

    def run(self, src_path: Path | str) -> str:
        self.src_path = Path(src_path)

        # Path -> PlainTextManuscript
        self.plain = self.reader.read(self.src_path)

        # PlainTextManuscript -> AbstractTreeManuscript
        self.tree = self.parser.parse(self.plain)

        # AbstractTreeManuscript -> AbstractTreeManuscript
        self.tree = self.transformer.transform(self.tree)

        # AbstractTreeManuscript -> HTMLBodyManuscript
        self.body = self.translator.translate(self.tree)

        # AbstractTreeManuscript -> WebManuscript
        self.web = self.builder.build(self.body)

        # write WebManuscript to disk
        self.writer.write(self.web, self.dst_path)

        return self.web
