"""
app.py
------

RSM Application: take a file path and output its contents as HTML.

"""

from ..core import nodes
from ..core import manuscript
from ..core import reader
from ..core import parser
from ..core import transformer
from ..core import linter
from ..core import translator
from ..core import builder
from ..core import writer
from ..core.rsmlogger import RSMFormatter

from pathlib import Path
from icecream import ic
from typing import NamedTuple, Any, Callable
import logging


logger = logging.getLogger('RSM')


class RSMApplicationError(Exception):
    pass


class Task(NamedTuple):
    name: str
    obj: Any
    run: Callable


class Pipeline:
    def __init__(self, tasks: list[Task]):
        self.tasks = []
        for t in tasks:
            self.add_task(t)

    def add_task(self, task):
        self.tasks.append(task)
        setattr(self, task.name, task.obj)

    def pop_task(self):
        task = self.tasks.pop()
        delattr(self, task.name)
        return task

    def run(self, initial_args=None):
        res = initial_args
        for _, _, call in self.tasks:
            if isinstance(res, dict):
                res = call(**res)
            elif isinstance(res, (list, tuple)):
                res = call(*res)
            elif res is None:
                res = call()
            else:
                res = call(res)
        return res


def validate(srcpath, plain) -> None:
    if not srcpath and not plain:
        raise RSMApplicationError('Must specify exactly one of srcpath, plain')
    if srcpath and plain:
        raise RSMApplicationError('Must specify exactly one of srcpath, plain')


def configure(verbosity) -> None:
    level = logging.WARNING - verbosity * 10
    level = max(level, logging.DEBUG)
    logger.level = min(logger.level, level)
    for handler in logger.handlers:
        if handler.level > level:
            handler.setLevel(level)
    logger.info('Application started')
    logger.info('Configuring...')
    # self.config = self.config.configure()


class ParserApplication(Pipeline):
    def __init__(
        self, srcpath: Path | None = None, plain: str = '', verbosity: int = 0
    ):
        validate(srcpath, plain)
        configure(verbosity)

        tasks = []
        if not plain:
            r = reader.Reader()
            tasks.append(Task("reader", r, lambda: r.read(srcpath)))
        else:
            tasks.append(Task("dummy", None, lambda: plain))
        tasks += [
            Task("parser", p := parser.MainParser(), p.parse),
            Task("transformer", t := transformer.Transformer(), t.transform),
        ]
        super().__init__(tasks)


class LinterApplication(ParserApplication):
    def __init__(
        self,
        srcpath: Path | None = None,
        plain: str = '',
        verbosity: int = 0,
    ):
        super().__init__(srcpath, plain, verbosity)
        mylinter = linter.Linter()
        self.add_task(Task("linter", mylinter, mylinter.lint))
        self.add_task(Task("linter", mylinter, mylinter.flush))
        self.add_task(Task("linter", mylinter, lambda: mylinter.flush))


class RSMProcessorApplication(ParserApplication):
    def __init__(
        self,
        srcpath: Path | None = None,
        plain: str = '',
        verbosity: int = 0,
        run_linter: bool = False,
    ):
        super().__init__(srcpath, plain, verbosity)
        if run_linter:
            self.add_task(Task("linter", l := linter.Linter(), l.lint))
        self.add_task(Task("translator", t := translator.Translator(), t.translate))
        if run_linter:
            self.add_task(Task("linter", l, l.flush))


class FullBuildApplication(RSMProcessorApplication):
    def __init__(
        self,
        srcpath: Path | None = None,
        plain: str = '',
        run_linter: bool = False,
        verbosity: int = 0,
    ):
        super().__init__(srcpath, plain, verbosity, run_linter)
        if run_linter:
            wrapup = self.pop_task()
        self.add_task(Task("builder", b := builder.FullBuilder(), b.build))
        self.add_task(Task("writer", w := writer.Writer(), w.write))
        if run_linter:
            self.add_task(wrapup)
