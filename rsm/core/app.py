"""
app.py
------

RSM Application: take a file path and output its contents as HTML.

"""

from icecream import ic

import logging
from . import rsmlogger
logger = logging.getLogger('RSM')

from pathlib import Path

from .manuscript import (
    PlainTextManuscript,
    HTMLManuscript,
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

    def __init__(
            self,
            *,
            srcpath: Path | None = None,
            plain: PlainTextManuscript = PlainTextManuscript(),
    ):
        if not srcpath and not plain:
            raise RSMApplicationError('Must specify exactly one of srcpath, plain')
        if srcpath and plain:
            raise RSMApplicationError('Must specify exactly one of srcpath, plain')
        self.srcpath: Path | None = srcpath
        self.plain: PlainTextManuscript = plain
        self.dstpath: Path = Path()
        self.tree: AbstractTreeManuscript | None = None
        self.body: HTMLManuscript | None = None
        self.html: HTMLManuscript | None = None
        self.web: WebManuscript | None = None
        self.reader: Reader = Reader()
        self.parser: ManuscriptParser = ManuscriptParser()
        self.transformer: Transformer = Transformer()
        self.translator: Translator = Translator()
        self.builder: Builder = Builder()
        self.writer: Writer = Writer()

    def run(self, write: bool = True) -> WebManuscript:
        logger.info('Application started')

        logger.info('Configuring...')
        # self.config = self.config.configure()

        if not self.plain:
            logger.info('Reading...')
            # Path -> PlainTextManuscript
            self.plain = self.reader.read(self.srcpath)

        # PlainTextManuscript -> AbstractTreeManuscript
        logger.info('Parsing...')
        self.tree = self.parser.parse(self.plain)

        ic.disable()

        # AbstractTreeManuscript -> AbstractTreeManuscript
        logger.info('Transforming...')
        self.tree = self.transformer.transform(self.tree)

        # AbstractTreeManuscript -> HTMLManuscript
        logger.info('Translating...')
        self.body = self.translator.translate(self.tree)

        # AbstractTreeManuscript -> WebManuscript
        logger.info('Building...')
        self.web = self.builder.build(self.body, self.srcpath)
        self.html = self.web.html

        if write:
            # write WebManuscript to disk
            logger.info('Writing...')
            self.writer.write(self.web, self.dstpath)

        logger.info('Done.')
        return self.web
