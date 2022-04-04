"""
builder.py
----------

RSM Builder: take a complete source string and output a Manuscript.

"""

from fs import open_fs
from fs.mountfs import MountFS

from pathlib import Path

from .manuscript import HTMLBodyManuscript, WebManuscript
from .parser import ManuscriptParser


class Builder:

    def __init__(self):
        self.body: HTMLBodyManuscript = None
        self.web: WebManuscript = None

    def build(self, body: HTMLBodyManuscript, src: Path = None) -> WebManuscript:
        self.body = body
        self.web = WebManuscript(self.body, src)

        # self.mount_static()
        self.make_main_file()

        return self.web

    def make_main_file(self) -> None:
        self.web.writetext('index.html', self.body)

    def mount_static(self) -> None:
        static1 = open_fs('~/code/rsm/rsm/core/rsm_theme/static')
        static2 = open_fs('~/research/small_graphs/results')
        self.web.mount('static1', static1)
        self.web.mount('static2', static2)
