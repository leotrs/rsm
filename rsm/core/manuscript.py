"""
manuscript.py
-------------

Classes that represent the manuscript at different stages.

"""

from pathlib import Path

from fs.mountfs import MountFS
from . import nodes


class PlainTextManuscript(str):
    pass


AbstractTreeManuscript = nodes.Manuscript


class HTMLManuscript(str):
    pass


class WebManuscript(MountFS):
    def __init__(self, src: Path = None):
        super().__init__()
        self.src = Path(src) if src else None
        self.body: HTMLManuscript = HTMLManuscript('')
        self.html: HTMLManuscript = HTMLManuscript('')

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        classname = self.__class__.__name__
        return f"{classname}(src='{self.src}')"
