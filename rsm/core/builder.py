"""
builder.py
----------

RSM Builder: take a complete source string and output a Manuscript.

"""

from fs import open_fs
from fs.mountfs import MountFS

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
        html = self.make_html_header()
        html += self.body
        html += self.make_html_footer()
        self.web.writetext(self.outname, html)
        self.web.html = html

    def make_html_header(self) -> str:
        return ''

    def make_html_footer(self) -> str:
        return ''

    def mount_static(self) -> None:
        static1 = open_fs('~/code/rsm/rsm/core/rsm_theme/static')
        static2 = open_fs('~/research/small_graphs/results')
        self.web.mount('static1', static1)
        self.web.mount('static2', static2)
