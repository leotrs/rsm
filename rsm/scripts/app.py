"""
app.py
------

RSM Application: take a file path and output its contents as HTML.

"""

import logging
from pathlib import Path
from typing import Any, Callable, NamedTuple, Optional, Union

from icecream import ic

from .. import builder, linter, reader, transformer, translator, tsparser, writer

logger = logging.getLogger("RSM")


class RSMApplicationError(Exception):
    pass


class Task(NamedTuple):
    """A step in a :class:`Pipeline`."""

    name: str
    obj: Any
    run: Callable


class Pipeline:
    """A sequence of :class:`Task`s."""

    def __init__(self, tasks: list[Task]):
        self.tasks: list[Task] = []
        for t in tasks:
            self.add_task(t)

    def add_task(self, task: Task) -> None:
        """Add a task at the end of the current pipeline."""
        self.tasks.append(task)
        setattr(self, task.name, task.obj)

    def pop_task(self) -> Task:
        """Remove and return the last task."""
        task = self.tasks.pop()
        delattr(self, task.name)
        return task

    def run(self, initial_args: Any = None) -> Any:
        """Execute every task in the pipeline serially."""
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


class RSMApp(Pipeline):
    def __init__(self, tasks: Optional[list[Task]] = None, verbosity: int = 0):
        self._config_logger(verbosity)
        logger.info("Application started")
        logger.info("Configuring...")
        # self.config = self.config.configure()
        super().__init__(tasks or [])

    def run(self, initial_args: Any = None) -> Optional[str]:
        result = super().run(initial_args)
        logger.info("Done.")
        return result

    @staticmethod
    def _config_logger(verbosity: int):
        level = logging.WARNING - verbosity * 10
        level = max(level, logging.DEBUG)
        logger.level = min(logger.level, level)
        for handler in logger.handlers:
            if handler.level > level:
                handler.setLevel(level)


class ParserApp(RSMApp):
    def __init__(
        self,
        srcpath: Optional[Path] = None,
        plain: str = "",
        verbosity: int = 0,
    ):
        self._validate_srcpath_and_plain(srcpath, plain)

        tasks = []
        if not plain:
            tasks.append(Task("reader", r := reader.Reader(), lambda: r.read(srcpath)))
        else:
            tasks.append(Task("dummy", None, lambda: plain))

        tasks += [
            Task("parser", p := tsparser.TSParser(), p.parse),
            Task("transformer", t := transformer.Transformer(), t.transform),
        ]
        super().__init__(tasks, verbosity=verbosity)

    @staticmethod
    def _validate_srcpath_and_plain(
        srcpath: Union[Path, str, None], plain: str
    ) -> None:
        if (not srcpath and not plain) or (srcpath and plain):
            raise RSMApplicationError("Must specify exactly one of srcpath, plain")


class LinterApp(ParserApp):
    def __init__(
        self,
        srcpath: Optional[Path] = None,
        plain: str = "",
        verbosity: int = 0,
    ):
        super().__init__(srcpath, plain, verbosity)
        mylinter = linter.Linter()
        self.add_task(Task("linter", mylinter, mylinter.lint))
        self.add_task(Task("linter", mylinter, lambda _: mylinter.flush()))


class ProcessorApp(ParserApp):
    def __init__(
        self,
        srcpath: Optional[Path] = None,
        plain: str = "",
        verbosity: int = 0,
        handrails: bool = False,
        run_linter: bool = False,
    ):
        super().__init__(srcpath, plain, verbosity)
        if run_linter:
            self.add_task(Task("linter", l := linter.Linter(), l.lint))

        tr = translator.HandrailsTranslator() if handrails else translator.Translator()
        self.add_task(Task("translator", tr, tr.translate))
        if run_linter:
            self.add_task(Task("linter", l, l.flush))


class FullBuildApp(ProcessorApp):
    def __init__(
        self,
        srcpath: Optional[Path] = None,
        plain: str = "",
        verbosity: int = 0,
        handrails: bool = True,
        run_linter: bool = False,
    ):
        super().__init__(srcpath, plain, verbosity, handrails, run_linter)
        if run_linter:
            wrapup = self.pop_task()
        self.add_task(Task("builder", b := builder.FullBuilder(), b.build))
        self.add_task(Task("writer", w := writer.Writer(), w.write))
        if run_linter:
            self.add_task(wrapup)


def render(source: str, handrails: bool = False, verbosity: int = 0) -> str:
    return ProcessorApp(plain=source, handrails=handrails, verbosity=verbosity).run()


def lint(source: str, handrails: bool = False, verbosity: int = 0):
    return LinterApp(plain=source, verbosity=verbosity).run()


def make(source: str, lint: bool = True, verbose: int = 0) -> str:
    return FullBuildApp(plain=source, run_linter=lint, verbosity=verbose).run()
