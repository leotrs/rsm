"""
nodes.py
--------

Nodes that make up the Manuscript tree.

"""

from dataclasses import dataclass, field
from typing import Any, ClassVar, Type, Optional
from collections.abc import Iterable
from datetime import datetime
from icecream import ic

from .util import ShortenedString, short_repr


class RSMNodeError(Exception):
    pass


@dataclass
class Node:
    label: str = ''
    types: list[str] = field(default_factory=list)
    comment: str = ''
    parent: Optional['NodeWithChildren'] = None
    globalmetakeys = {'label', 'types', 'comment'}
    _newmetakeys: ClassVar[set] = set()

    @classmethod
    def metakeys(cls: Type['Node']):
        return cls._newmetakeys.union(
            *[b._newmetakeys for b in cls.__bases__]
        )

    @property
    def children(self) -> tuple:
        return tuple()

    def traverse(self, condition=lambda n: True, *, nodeclass=None) -> Iterable['Node']:
        if nodeclass:
            if issubclass(nodeclass, Node):
                condition = lambda n: isinstance(n, nodeclass)
            else:
                raise RSMNodeError('nodeclass must inherit from Node')

        stack = [self]
        while stack:
            node = stack.pop()
            if condition(node):
                yield node
            stack += node.children[::-1]

    def replace_self(self, replace) -> None:
        if not self.parent:
            raise RSMNodeError('Can only call replace_self on a node with parent')
        index = self.parent.children.index(self)
        self.parent.remove(self)
        self.parent._children.insert(index, replace)

    def ingest_dict_as_meta(self, meta: dict) -> None:
        for key, value in meta.items():
            setattr(self, key, value)


@dataclass
class NodeWithChildren(Node):
    def __post_init__(self):
        self._children: list[Node] = []

    def add(self, child: Node | list) -> None:
        if isinstance(child, list):
            for c in child:
                self.add(c)
        elif isinstance(child, Node):
            if child.parent and child.parent is not self:
                raise RSMNodeError('Attempting to add child to a different parent')
            self._children.append(child)
            child.parent = self
        else:
            raise RSMNodeError('Attempting to add a non-Node object as a child of a Node')

    def remove(self, child: 'Node') -> None:
        self._children.remove(child)

    @property
    def children(self) -> tuple:
        return tuple(self._children)


@dataclass
class Text(Node):
    text: ShortenedString = field(default_factory=ShortenedString)

    def __repr__(self):
        return short_repr(self.text, self.__class__.__name__)


@dataclass
class Span(NodeWithChildren):
    strong: bool = field(kw_only=True, default=False)
    emphas: bool = field(kw_only=True, default=False)
    little: bool = field(kw_only=True, default=False)
    insert: bool = field(kw_only=True, default=False)
    delete: bool = field(kw_only=True, default=False)
    _newmetakeys: ClassVar[set] = {'strong', 'emphas', 'little', 'insert', 'delete'}
    attr_to_tag: ClassVar[dict] = {
        'strong': 'strong',
        'emphas': 'em',
        'little': 'small',
        'insert': 'ins',
        'delete': 'del',
    }


@dataclass
class Heading(NodeWithChildren):
    title: str = ''
    _newmetakeys: ClassVar[set] = {'title'}


@dataclass
class Manuscript(Heading):
    src: ShortenedString = field(default_factory=ShortenedString, repr=False)
    date: datetime | None = None
    _newmetakeys: ClassVar[set] = {'date'}

    def __post_init__(self):
        super().__post_init__()
        self.src = ShortenedString(self.src)


@dataclass
class Author(Node):
    name: str = ''
    affiliation: str = ''
    email: str = ''
    _newmetakeys: ClassVar[set] = {'name', 'affiliation', 'email'}


@dataclass
class Abstract(NodeWithChildren):
    keywords: list[str] = field(default_factory=list)
    MSC: list[str] = field(default_factory=list)
    _newmetakeys: ClassVar[set] = {'keywords', 'MSC'}


@dataclass
class Section(Heading):
    pass


@dataclass
class Paragraph(Heading):
    pass


@dataclass
class Enumerate(NodeWithChildren):
    pass


@dataclass
class Itemize(NodeWithChildren):
    pass


@dataclass
class Item(Paragraph):
    pass


@dataclass
class Math(NodeWithChildren):
    display: bool = field(kw_only=True, default=False)
    number: bool = field(kw_only=True, default=False)
    _newmetakeys: ClassVar[set] = {'number'}


@dataclass
class PendingReference(Node):
    targetlabel: str = field(kw_only=True, default='')


@dataclass
class Reference(Node):
    target: Node | None = field(kw_only=True, default=None)
