"""
nodes.py
--------

Nodes that make up the Manuscript tree.

"""

from dataclasses import dataclass, field
from typing import Any, ClassVar
from datetime import datetime
from icecream import ic

from .util import ShortenedString, short_repr


@dataclass
class Node:
    label: str = field(default_factory=str)
    types: list[str] = field(default_factory=list)
    children: list['Node'] = field(default_factory=list, repr=False)
    _newmetakeys: ClassVar[set] = set()

    def add(self, child: 'Node') -> None:
        self.children.append(child)

    @classmethod
    def metakeys(cls):
        return cls._newmetakeys.union(*[b._newmetakeys for b in cls.__bases__])


@dataclass
class Text(Node):
    text: ShortenedString = field(default_factory=ShortenedString)

    def __repr__(self):
        return short_repr(self.text, self.__class__.__name__)


@dataclass
class Heading(Node):
    title: str = ''
    _newmetakeys: ClassVar[set] = {'title'}


@dataclass
class Manuscript(Heading):
    src: ShortenedString = field(default_factory=ShortenedString, repr=False)
    date: datetime = None
    _newmetakeys: ClassVar[set] = {'date'}

    def __post_init__(self):
        self.src = ShortenedString(self.src)


@dataclass
class Author(Node):
    name: str = None
    affiliation: str = None
    email: str = None
    _newmetakeys: ClassVar[set] = {'name', 'affiliation', 'email'}


@dataclass
class Abstract(Node):
    keywords: list[str] = field(default_factory=list)
    MSC: list[str] = field(default_factory=list)
    _newmetakeys: ClassVar[set] = {'keywords', 'MSC'}


@dataclass
class Section(Heading):
    pass


@dataclass
class Paragraph(Heading):
    pass
