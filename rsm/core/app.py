"""
app.py
------

RSM Application: take a file path and output its contents as HTML.

"""

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('RSM')

from pathlib import Path

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


class RSMApplicationError(Exception):
    pass


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

    def run(self, data: Path | PlainTextManuscript, write: bool = True) -> str:
        logger.info('Application started')

        logger.info('Configuring...')
        # self.config = self.config.configure()

        logger.info('Reading...')
        if type(data) in [Path, str]:
            self.src_path = Path(data)
            # Path -> PlainTextManuscript
            self.plain = self.reader.read(self.src_path)

        elif isinstance(data, PlainTextManuscript):
            self.src_path = None
            self.plain = data

        else:
            raise RSMApplicationError(
                'Application.run() expects a path to a .rsm file, or a string'
                ' of type PlainTextManuscript'
            )

        # PlainTextManuscript -> AbstractTreeManuscript
        logger.info('Parsing...')
        self.tree = self.parser.parse(self.plain)

        from icecream import ic
        ic.disable()

        # AbstractTreeManuscript -> AbstractTreeManuscript
        logger.info('Transforming...')
        self.tree = self.transformer.transform(self.tree)

        # AbstractTreeManuscript -> HTMLBodyManuscript
        logger.info('Translating...')
        self.body = self.translator.translate(self.tree)

        # AbstractTreeManuscript -> WebManuscript
        logger.info('Building...')
        self.web = self.builder.build(self.body)

        if write:
            # write WebManuscript to disk
            logger.info('Writing...')
            self.writer.write(self.web, self.dst_path)

        return self.web
