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
from .builder import BaseBuilder, BodyOnlyBuilder, FullBuilder
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
        self.reader: Reader | None = None
        self.parser: ManuscriptParser | None = None
        self.transformer: Transformer | None = None
        self.translator: Translator | None = None
        self.builder: BaseBuilder | None = None
        self.writer: Writer | None = None

    def run(self, body_only: bool = False, write: bool = True) -> WebManuscript:
        logger.info('Application started')

        self.configure()
        self.read()             # Path -> PlainTextManuscript
        self.parse()            # PlainTextManuscript -> AbstractTreeManuscript
        self.transform()        # AbstractTreeManuscript -> AbstractTreeManuscript
        ic.disable()
        self.translate()        # AbstractTreeManuscript -> HTMLManuscript
        self.build(body_only)   # HTMLManuscript -> WebManuscript
        self.write(write)       # WebManuscript -> HDD

        logger.info('Done.')
        return self.web

    def configure(self) -> None:
        logger.info('Configuring...')
        # self.config = self.config.configure()

    def read(self) -> None:
        if not self.plain:
            logger.info('Reading...')
            self.reader = Reader()
            self.plain = self.reader.read(self.srcpath)

    def parse(self) -> None:
        logger.info('Parsing...')
        self.parser = ManuscriptParser()
        self.tree = self.parser.parse(self.plain)

    def transform(self) -> None:
        logger.info('Transforming...')
        self.transformer = Transformer()
        self.tree = self.transformer.transform(self.tree)

    def translate(self) -> None:
        logger.info('Translating...')
        self.translator = Translator()
        self.body = self.translator.translate(self.tree)

    def build(self, body_only: bool = False) -> None:
        logger.info('Building...')
        self.builder = BodyOnlyBuilder() if body_only else FullBuilder()
        self.web = self.builder.build(self.body, self.srcpath)
        self.html = self.web.html

    def write(self, write: bool = True) -> None:
        if write:
            logger.info('Writing...')
            self.writer = Writer()
            self.writer.write(self.web, self.dstpath)
