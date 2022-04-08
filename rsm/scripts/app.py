"""
app.py
------

RSM Application: take a file path and output its contents as HTML.

"""

from ..core import manuscript
from ..core import reader
from ..core import parser
from ..core import transformer
from ..core import translator
from ..core import builder
from ..core import writer
from ..core.rsmlogger import RSMFormatter

from pathlib import Path
from icecream import ic
import logging
from logging.handlers import BufferingHandler
logger = logging.getLogger('RSM')


class RSMApplicationError(Exception):
    pass


class ParserApplication:

    def __init__(
            self,
            *,
            srcpath: Path | None = None,
            plain: manuscript.PlainTextManuscript = manuscript.PlainTextManuscript(),
            verbosity: int = 0
    ):
        if not srcpath and not plain:
            raise RSMApplicationError('Must specify exactly one of srcpath, plain')
        if srcpath and plain:
            raise RSMApplicationError('Must specify exactly one of srcpath, plain')
        self.srcpath: Path | None = srcpath
        self.plain: manuscript.PlainTextManuscript = plain
        self.dstpath: Path = Path()
        self.tree: manuscript.AbstractTreeManuscript | None = None
        self.reader: reader.Reader | None = None
        self.parser: parser.ManuscriptParser | None = None
        self.transformer: transformer.Transformer | None = None
        self.verbosity: int = verbosity

    def run(self) -> manuscript.AbstractTreeManuscript:
        self.configure()
        self.read()             # Path -> PlainTextManuscript
        self.parse()            # PlainTextManuscript -> AbstractTreeManuscript
        self.transform()        # AbstractTreeManuscript -> AbstractTreeManuscript
        self.wrapup()
        return self.tree

    def configure(self) -> None:
        level = logging.WARNING - self.verbosity * 10
        level = max(level, logging.DEBUG)
        if logger.level > level:
            logger.level = level
        for handler in logger.handlers:
            if handler.level > level:
                handler.setLevel(level)
        logger.info('Application started')
        logger.info('Configuring...')
        # self.config = self.config.configure()

    def read(self) -> None:
        if not self.plain:
            logger.info('Reading...')
            self.reader = reader.Reader()
            self.plain = self.reader.read(self.srcpath)

    def parse(self) -> None:
        logger.info('Parsing...')
        self.parser = parser.ManuscriptParser()
        self.tree = self.parser.parse(self.plain)

    def transform(self) -> None:
        logger.info('Transforming...')
        self.transformer = transformer.Transformer()
        self.tree = self.transformer.transform(self.tree)

    def wrapup(self) -> None:
        pass


class GatherHandler(BufferingHandler):

    def __init__(self, levels, target=None):
        super().__init__(capacity=float('inf'))
        self.gatherlevels = set(levels)
        self.buffer = []
        self.target = target

    def emit(self, record):
        if record.levelno in self.gatherlevels:
            self.buffer.append(record)

    def flush(self):
        self.acquire()
        try:
            if self.target:
                for record in self.buffer:
                    self.target.handle(record)
                self.buffer.clear()
        finally:
            self.release()


class Linter:

    def __init__(self):
        self.tree: manuscript.AbstractTreeManuscript | None = None
        logging.LINT = 25
        logging.addLevelName(logging.LINT, 'LINT')
        logger.lint = lambda msg, *args, **kwargs: logger.log(logging.LINT, msg, *args, **kwargs)
        if logger.level > logging.LINT:
           logger.level = logging.LINT
        target = logging.StreamHandler()
        target.setLevel(logging.LINT)
        # target.setFormatter(RSMFormatter())
        self.handler = GatherHandler([logging.WARNING, logging.LINT], target)
        self.handler.setLevel(logging.LINT)
        logger.addHandler(self.handler)

    def flush(self):
        if not self.handler.buffer:
            print('No linting messages')
            return
        print()
        print('------ Start of linting output ------ ')
        self.handler.flush()
        print('------ End of linting output ------')

    def lint(self, tree: manuscript.AbstractTreeManuscript):
        self.tree = tree
        logger.lint('this is a lint message')


class LinterApplication(ParserApplication):

    def __init__(
            self,
            *,
            srcpath: Path | None = None,
            plain: manuscript.PlainTextManuscript = manuscript.PlainTextManuscript(),
            verbosity: int = 0,
    ):
        super().__init__(srcpath=srcpath, plain=plain, verbosity=verbosity)
        self.linter: Linter = Linter()

    def run(self) -> manuscript.AbstractTreeManuscript:
        self.configure()
        self.read()             # Path -> PlainTextManuscript
        self.parse()            # PlainTextManuscript -> AbstractTreeManuscript
        self.transform()        # AbstractTreeManuscript -> AbstractTreeManuscript
        self.lint()
        self.wrapup()
        return self.tree

    def lint(self) -> None:
        logger.info('Linting...')
        self.linter.lint(self.tree)

    def wrapup(self) -> None:
        self.linter.flush()


class RSMProcessorApplication(ParserApplication):

    def __init__(
            self,
            *,
            srcpath: Path | None = None,
            plain: manuscript.PlainTextManuscript = manuscript.PlainTextManuscript(),
            verbosity: int = 0,
            run_linter: bool = False,
    ):
        super().__init__(srcpath=srcpath, plain=plain, verbosity=verbosity)
        self.translator: translator.Translator | None = None
        self.run_linter: bool = run_linter
        self.linter: Linter | None = Linter() if run_linter else None

    def run(self) -> manuscript.HTMLManuscript:
        self.configure()
        self.read()             # Path -> PlainTextManuscript
        self.parse()            # PlainTextManuscript -> AbstractTreeManuscript
        self.transform()        # AbstractTreeManuscript -> AbstractTreeManuscript
        self.lint()
        self.translate()        # AbstractTreeManuscript -> HTMLManuscript
        self.wrapup()
        return self.body

    def lint(self) -> None:
        if self.run_linter:
            logger.info('Linting...')
            self.linter.lint(self.tree)

    def translate(self) -> None:
        logger.info('Translating...')
        self.translator = translator.Translator()
        self.body = self.translator.translate(self.tree)

    def wrapup(self) -> None:
        if self.run_linter:
            self.linter.flush()


class FullBuildApplication(RSMProcessorApplication):

    def __init__(
            self,
            *,
            srcpath: Path | None = None,
            plain: manuscript.PlainTextManuscript = manuscript.PlainTextManuscript(),
            run_linter: bool = False,
            verbosity: int = 0
    ):
        super().__init__(srcpath=srcpath, plain=plain, run_linter=run_linter, verbosity=verbosity)
        self.html: manuscript.HTMLManuscript | None = None
        self.web: manuscript.WebManuscript | None = None
        self.builder: builder.BaseBuilder | None = None
        self.writer: writer.Writer | None = None

    def run(self) -> manuscript.HTMLManuscript:
        self.configure()
        self.read()             # Path -> PlainTextManuscript
        self.parse()            # PlainTextManuscript -> AbstractTreeManuscript
        self.transform()        # AbstractTreeManuscript -> AbstractTreeManuscript
        self.lint()
        self.translate()        # AbstractTreeManuscript -> HTMLManuscript
        self.build()            # HTMLManuscript -> WebManuscript
        self.write()            # WebManuscript -> HDD
        self.wrapup()
        return self.web

    def build(self) -> None:
        logger.info('Building...')
        self.builder = builder.FullBuilder()
        self.web = self.builder.build(self.body, self.srcpath)
        self.html = self.web.html

    def write(self, write: bool = True) -> None:
        if write:
            logger.info('Writing...')
            self.writer = writer.Writer()
            self.writer.write(self.web, self.dstpath)

    def wrapup(self) -> None:
        if self.run_linter:
            self.linter.flush()
