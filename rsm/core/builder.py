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


class BaseBuilder(ABC):

    def __init__(self):
        self.body: HTMLManuscript = None
        self.html: HTMLManuscript = None
        self.web: WebManuscript = None
        self.outname: str = 'index.html'

    def build(self, body: HTMLManuscript, src: Path = None) -> WebManuscript:
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
            + self.make_html_header() + '\n'
            + self.body.strip() + '\n\n'
            + self.make_html_footer()
            + '</html>\n'
        )
        self.web.writetext(self.outname, html)
        self.web.html = html

    def make_html_header(self) -> str:
        return dedent("""\
        <head>
          <meta charset="utf-8" />
          <meta name="viewport" content="width=device-width, initial-scale=1.0" />
          <meta name="generator" content="RSM 0.0.1 https://github.com/leotrs/rsm" />

          <link rel="stylesheet" type="text/css" href="static/rsm.css" />

          <script src="static/jquery-3.6.0.js"></script>
          <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
          <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

          <title>{some_title}</title>
        </head>
        """)

    def make_html_footer(self) -> str:
        return ''


class FullBuilder(SingleFileBuilder):

    def build(self, body: HTMLManuscript, src: Path = None) -> WebManuscript:
        super().build(body, src)
        self.mount_static()
        return self.web

    def mount_static(self) -> None:
        self.web.makedir('static')

        # compile sass into css
        cur_path = Path(__file__).parent.absolute()
        source_path = (cur_path / 'static').resolve()
        source = open_fs(str(source_path))
        content = source.readtext('rsm.scss')
        css = sass.compile(string=content, output_style='nested')
        self.web.writetext('static/rsm.css', css)

        # copy JS files
        copy_file(source, 'jquery-3.6.0.js', self.web, 'static/jquery-3.6.0.js')

        self.web.tree()
