"""
builder.py
----------

RSM Builder: take a complete source string and output a Manuscript.

"""

from fs import open_fs
from fs.mountfs import MountFS

from textwrap import dedent
from pathlib import Path

from .manuscript import HTMLManuscript, WebManuscript
from .parser import ManuscriptParser


class Builder:

    def __init__(self):
        self.body: HTMLManuscript = None
        self.html: HTMLManuscript = None
        self.web: WebManuscript = None
        self.outname: str = 'index.html'

    def build(self, body: HTMLManuscript, src: Path = None) -> WebManuscript:
        self.body = body
        self.web = WebManuscript(src)
        self.web.body = body

        # self.mount_static()
        self.make_main_file()

        return self.web

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
          <meta name="generator" content="Docutils 0.17.1: http://docutils.sourceforge.net/" />

          <title>{some_title}</title>
          <link rel="stylesheet" type="text/css" href="_static/rsm.css" />

          <script data-url_root="./" id="documentation_options" src="_static/documentation_options.js"></script>
          <script src="_static/jquery.js"></script>
        </head>
        """)

    def make_html_footer(self) -> str:
        return ''

    def mount_static(self) -> None:
        static1 = open_fs('~/code/rsm/rsm/core/rsm_theme/static')
        static2 = open_fs('~/research/small_graphs/results')
        self.web.mount('static1', static1)
        self.web.mount('static2', static2)
