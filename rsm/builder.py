"""
builder.py
----------

RSM Builder: take a complete source string and output a Manuscript.

"""

from fs import open_fs
from fs.mountfs import MountFS
from fs.copy import copy_file

from abc import ABC, abstractmethod
from textwrap import dedent
from pathlib import Path
import sass
from icecream import ic

from .manuscript import HTMLManuscript, WebManuscript
from .parser import ManuscriptParser

import logging

logger = logging.getLogger('RSM').getChild('Builder')


class BaseBuilder(ABC):
    def __init__(self):
        self.body: HTMLManuscript = None
        self.html: HTMLManuscript = None
        self.web: WebManuscript = None
        self.outname: str = 'index.html'

    def build(self, body: HTMLManuscript, src: Path = None) -> WebManuscript:
        logger.info("Building...")
        self.body = body
        self.web = WebManuscript(src)
        self.web.body = body
        self.make_main_file()
        return self.web

    @abstractmethod
    def make_main_file(self) -> None:
        pass


class SingleFileBuilder(BaseBuilder):
    def make_main_file(self) -> None:
        html = HTMLManuscript(
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
            loadMathJax();
            import { setupClassInteractions } from '/static/classes.js';
            setupClassInteractions();
          </script>

          <title>{some_title}</title>
        </head>
        """
        )

    def make_html_footer(self) -> str:
        return ''


class FullBuilder(SingleFileBuilder):
    def build(self, body: HTMLManuscript, src: Path = None) -> WebManuscript:
        super().build(body, src)
        self.mount_static()
        return self.web

    def mount_static(self) -> None:
        self.web.makedir('static')

        cur_path = Path(__file__).parent.absolute()
        source_path = (cur_path / 'static').resolve()
        source = open_fs(str(source_path))

        # # compile sass into css
        # content = source.readtext('rsm.scss')
        # css = sass.compile(string=content, output_style='nested')
        # self.web.writetext('static/rsm.css', css)

        # # leave an updated version in the source dir
        # source.writetext('rsm.css', css)

        # copy JS files
        filenames = [
            'jquery-3.6.0.js',
            'tooltips.js',
            'classes.js',
            'tooltipster.bundle.js',
            'tooltipster.bundle.css',
            'rsm.css',
        ]
        for fn in filenames:
            copy_file(source, fn, self.web, f'static/{fn}')

        # self.web.tree()
