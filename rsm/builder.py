"""
builder.py
----------

RSM Builder: take a complete source string and output a Manuscript.

"""

from fs import open_fs
from fs.mountfs import MountFS
from fs.copy import copy_file

import re
from abc import ABC, abstractmethod
from textwrap import dedent
from pathlib import Path
import sass
from icecream import ic

from .manuscript import WebManuscript
from .parser import ManuscriptParser

import logging

logger = logging.getLogger('RSM').getChild('Builder')


class BaseBuilder(ABC):
    def __init__(self) -> None:
        self.body: str | None = None
        self.html: str | None = None
        self.web: WebManuscript | None = None
        self.outname: str = 'index.html'

    def build(self, body: str, src: Path = None) -> WebManuscript:
        logger.info("Building...")
        self.body = body
        self.web = WebManuscript(src)
        self.web.body = body

        logger.debug("Searching required static assets...")
        self.required_assets: list[Path] = []
        self.find_required_assets()

        logger.debug("Building main file...")
        self.make_main_file()
        return self.web

    @abstractmethod
    def make_main_file(self) -> None:
        pass

    def find_required_assets(self) -> None:
        self.required_assets = [
            Path(x) for x in re.findall(r'src="(.*?)"', str(self.body))
        ]


class SingleFileBuilder(BaseBuilder):
    body: str
    web: WebManuscript

    def make_main_file(self) -> None:
        html = str(
            '<html>\n\n'
            + self.make_html_header()
            + '\n'
            + self.body.strip()
            + '\n\n'
            + self.make_html_footer()
            + '</html>\n'
        )
        self.web.writetext(self.outname, html)
        self.web.html = html

    def make_html_header(self) -> str:
        return dedent(
            """\
        <head>
          <meta charset="utf-8" />
          <meta name="viewport" content="width=device-width, initial-scale=1.0" />
          <meta name="generator" content="RSM 0.0.1 https://github.com/leotrs/rsm" />

          <link rel="stylesheet" type="text/css" href="static/rsm.css" />
          <link rel="stylesheet" type="text/css" href="static/tooltipster.bundle.css" />

          <script src="static/jquery-3.6.0.js"></script>
          <script src="static/tooltipster.bundle.js"></script>
          <script type="module" src="static/tooltips.js"></script>
          <script type="module" src="static/classes.js"></script>
          <script type="module">
            import { loadMathJax } from '/static/tooltips.js';

            import { setupClassInteractions } from '/static/classes.js';


            window.addEventListener('load', function () {
                loadMathJax();
                setupClassInteractions();
            })

          </script>

          <title>{some_title}</title>
        </head>
        """
        )

    def make_html_footer(self) -> str:
        return ''


class FullBuilder(SingleFileBuilder):
    def build(self, body: str, src: Path = None) -> WebManuscript:
        super().build(body, src)
        logger.debug("Moving default RSM assets...")
        self.mount_static()
        if self.required_assets:
            logger.debug("Moving user assets...")
            self.mount_required_assets()
        return self.web

    def mount_static(self) -> None:
        working_path = Path(__file__).parent.absolute()
        source_path = (working_path / 'static').resolve()
        source = open_fs(str(source_path))

        filenames = [
            'jquery-3.6.0.js',
            'tooltips.js',
            'classes.js',
            'tooltipster.bundle.js',
            'tooltipster.bundle.css',
            'rsm.css',
        ]
        self.web.makedir('static')
        for fn in filenames:
            copy_file(source, fn, self.web, f'static/{fn}')

    def mount_required_assets(self) -> None:
        source = open_fs(str(Path().resolve()))

        for fn in self.required_assets:
            copy_file(source, str(fn), self.web, f'static/{fn.name}')
