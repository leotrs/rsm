"""
app.py
------

RSM Application: take a file path and output its contents as HTML.

"""

from icecream import ic

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
from .builder import BaseBuilder, FullBuilder
from .writer import Writer

import logging
logger = logging.getLogger('RSM')

from pathlib import Path


class RSMApplicationError(Exception):
    pass


class ParserApplication:

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
        self.reader: Reader | None = None
        self.parser: ManuscriptParser | None = None
        self.transformer: Transformer | None = None

    def run(self) -> AbstractTreeManuscript:
        self.configure()
        self.read()             # Path -> PlainTextManuscript
        self.parse()            # PlainTextManuscript -> AbstractTreeManuscript
        self.transform()        # AbstractTreeManuscript -> AbstractTreeManuscript
        return self.tree

    def configure(self) -> None:
        logger.info('Application started')
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


class LinterApplication(ParserApplication):

    def __init__(
        self,
        *,
        srcpath: Path | None = None,
        plain: PlainTextManuscript = PlainTextManuscript(),
    ):
        super().__init__(srcpath=srcpath, plain=plain)
        self.linter = None

    def run(self) -> AbstractTreeManuscript:
        self.configure()
        self.read()             # Path -> PlainTextManuscript
        self.parse()            # PlainTextManuscript -> AbstractTreeManuscript
        self.transform()        # AbstractTreeManuscript -> AbstractTreeManuscript
        self.lint()
        return self.tree

    def configure(self) -> None:
        # self.linter: Linter = Linter()
        # instantiate handler
        # register everything
        super().configure()

    def lint(self) -> None:
        pass


class RSMProcessorApplication(LinterApplication):

    def __init__(
            self,
            *,
            srcpath: Path | None = None,
            plain: PlainTextManuscript = PlainTextManuscript(),
            run_linter: bool = False,
    ):
        super().__init__(srcpath=srcpath, plain=plain)
        self.translator: Translator | None = None
        self.run_linter: bool = run_linter

    def run(self) -> HTMLManuscript:
        self.configure()
        self.read()             # Path -> PlainTextManuscript
        self.parse()            # PlainTextManuscript -> AbstractTreeManuscript
        self.transform()        # AbstractTreeManuscript -> AbstractTreeManuscript
        self.lint()
        self.translate()        # AbstractTreeManuscript -> HTMLManuscript
        return self.body

    def lint(self) -> None:
        if self.run_linter:
            super().lint()

    def translate(self) -> None:
        logger.info('Translating...')
        self.translator = Translator()
        self.body = self.translator.translate(self.tree)


class Application(RSMProcessorApplication):

    def __init__(
            self,
            *,
            srcpath: Path | None = None,
            plain: PlainTextManuscript = PlainTextManuscript(),
            run_linter: bool = False,
    ):
        super().__init__(srcpath=srcpath, plain=plain, run_linter=run_linter)
        self.html: HTMLManuscript | None = None
        self.web: WebManuscript | None = None
        self.builder: BaseBuilder | None = None
        self.writer: Writer | None = None

    def run(self) -> HTMLManuscript:
        self.configure()
        self.read()             # Path -> PlainTextManuscript
        self.parse()            # PlainTextManuscript -> AbstractTreeManuscript
        self.transform()        # AbstractTreeManuscript -> AbstractTreeManuscript
        self.lint()
        self.translate()        # AbstractTreeManuscript -> HTMLManuscript
        self.build()            # HTMLManuscript -> WebManuscript
        self.write()            # WebManuscript -> HDD
        return self.web

    def build(self) -> None:
        logger.info('Building...')
        self.builder = FullBuilder()
        self.web = self.builder.build(self.body, self.srcpath)
        self.html = self.web.html

    def write(self, write: bool = True) -> None:
        if write:
            logger.info('Writing...')
            self.writer = Writer()
            self.writer.write(self.web, self.dstpath)
