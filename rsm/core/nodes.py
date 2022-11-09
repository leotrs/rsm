"""
nodes.py
--------

Nodes that make up the Manuscript tree.

"""

from dataclasses import dataclass, field, InitVar, KW_ONLY
from typing import Any, ClassVar, Type, Optional, Callable
from collections.abc import Iterable
from datetime import datetime
from icecream import ic

from .util import ShortenedString, short_repr


class RSMNodeError(Exception):
    pass


@dataclass
class Node:
    classreftext: ClassVar[str] = '{nodeclass} {number}'
    possible_parents: ClassVar[set[Type['NodeWithChildren']]] = set()

    # meta keys
    label: str = ''
    types: list[str] = field(default_factory=list)
    nonum: bool = False
    customreftext: InitVar[str] = ''
    _newmetakeys: ClassVar[set] = {'label', 'types', 'nonum', 'reftext'}

    # non-meta instance variables
    number: int | None = None
    # we need parent to be a property, see https://stackoverflow.com/a/61480946/14157230
    # for how this works
    _parent: Optional['NodeWithChildren'] = field(init=False, repr=False, default=None)
    parent: Optional['NodeWithChildren'] = None

    def __post_init__(self, customreftext: str) -> None:
        self._reftext = customreftext

    @classmethod
    def metakeys(cls: Type['Node']) -> set:
        return cls._newmetakeys.union(
            *[b.metakeys() for b in cls.__bases__ if hasattr(b, 'metakeys')]
        )

    @property
    def parent(self) -> Optional['NodeWithChildren']:
        return self._parent

    @parent.setter
    def parent(self, node: 'Node') -> None:
        if isinstance(node, property):
            node = self._parent  # initial value not specified, use default
        if node is None:
            self._parent = node
            return
        possible_parents = self.__class__.possible_parents
        if possible_parents and type(node) not in possible_parents:
            raise RSMNodeError(
                f'Node of type {type(self)} cannot have parent of type {type(node)}'
            )
        self._parent = node

    @property
    def children(self) -> tuple:
        # necessary for methods such as Nodes.traverse
        return tuple()

    @property
    def full_number(self) -> str:
        node = self
        numbers = []
        while node.number is not None:
            numbers.append(str(node.number))
            node = node.parent
        return '.'.join(reversed(numbers))

    def traverse(
        self,
        condition: Callable = lambda n: True,
        *,
        nodeclass: Type['Node'] | None = None,
    ) -> Iterable['Node']:
        if nodeclass is not None:
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

    def first_of_type(self, cls: Type['Node']) -> Optional['Node']:
        for child in self.children:
            if isinstance(child, cls):
                return child
        return None

    def last_of_type(self, cls: Type['Node']) -> Optional['Node']:
        last = None
        for child in self.children:
            if isinstance(child, cls):
                last = child
        return last

    @property
    def reftext(self) -> str:
        return self._reftext or self.classreftext

    @reftext.setter
    def reftext(self, value: str) -> None:
        self._reftext = value

    def replace_self(self, replace: 'Node') -> None:
        if not self.parent:
            raise RSMNodeError('Can only call replace_self on a node with parent')
        index = self.parent.children.index(self)
        self.parent.remove(self)
        self.parent._children.insert(index, replace)
        replace.parent = self.parent

    def ingest_dict_as_meta(self, meta: dict) -> None:
        for key, value in meta.items():
            setattr(self, str(key), value)


@dataclass
class NodeWithChildren(Node):
    def __post_init__(self, customreftext: str) -> None:
        self._reftext = customreftext
        self._children: list[Node] = []

    @property
    def children(self) -> tuple:
        return tuple(self._children)

    def append(self, child: Node | list) -> None:
        if isinstance(child, list):
            for c in child:
                self.append(c)
        elif isinstance(child, Node):
            if child.parent and child.parent is not self:
                raise RSMNodeError('Attempting to append child to a different parent')
            self._children.append(child)
            child.parent = self
        else:
            raise TypeError('Can only append a Node or iterable of Nodes as children')

    def prepend(self, child: Node | list) -> None:
        if isinstance(child, list):
            for c in child:
                self.prepend(c)
        elif isinstance(child, Node):
            if child.parent and child.parent is not self:
                raise RSMNodeError('Attempting to prepend child to a different parent')
            self._children.insert(0, child)
            child.parent = self
        else:
            raise TypeError('Can only prepend a Node or iterable of Nodes as children')

    def remove(self, child: 'Node') -> None:
        self._children.remove(child)


@dataclass
class Text(Node):
    text: str = ''

    def __repr__(self) -> str:
        return short_repr(self.text, self.__class__.__name__)


@dataclass
class Span(NodeWithChildren):
    _: KW_ONLY
    strong: bool = False
    emphas: bool = False
    little: bool = False
    insert: bool = False
    delete: bool = False
    _newmetakeys: ClassVar[set] = {'strong', 'emphas', 'little', 'insert', 'delete'}
    attr_to_tag: ClassVar[dict] = {
        'strong': 'strong',
        'emphas': 'em',
        'little': 'small',
        'insert': 'ins',
        'delete': 'del',
    }


@dataclass
class Claim(NodeWithChildren):
    pass


@dataclass
class Heading(NodeWithChildren):
    title: str = ''
    _newmetakeys: ClassVar[set] = {'title'}


@dataclass
class Manuscript(Heading):
    src: str = field(repr=False, default='')
    date: datetime | None = None
    _newmetakeys: ClassVar[set] = {'date'}

    def __post_init__(self, customreftext: str) -> None:
        super().__post_init__(customreftext)
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
    level: ClassVar[int] = 2


@dataclass
class Subsection(Section):
    level: ClassVar[int] = 3


@dataclass
class Subsubsection(Section):
    level: ClassVar[int] = 4


@dataclass
class BaseParagraph(Heading):
    pass


@dataclass
class Paragraph(BaseParagraph):
    pass


@dataclass
class Comment(BaseParagraph):
    pass


@dataclass
class Enumerate(NodeWithChildren):
    pass


@dataclass
class Itemize(NodeWithChildren):
    pass


@dataclass
class Item(BaseParagraph):
    possible_parents: ClassVar[set[Type['NodeWithChildren']]] = {Itemize, Enumerate}


@dataclass
class Keyword(Span):
    pass


@dataclass
class Math(NodeWithChildren):
    pass


@dataclass
class Code(NodeWithChildren):
    pass


@dataclass
class DisplayMath(NodeWithChildren):
    reftext: str = 'Equation {number}'


@dataclass
class DisplayCode(NodeWithChildren):
    reftext: str = 'Code Listing {number}'


@dataclass
class BaseReference(Node):
    overwrite_reftext: str | None = field(kw_only=True, default=None)


@dataclass
class PendingReference(BaseReference):
    target: str = field(kw_only=True, default='')


@dataclass
class Reference(BaseReference):
    target: Node | None = field(kw_only=True, default=None)


@dataclass
class URL(BaseReference):
    target: str = field(kw_only=True, default='')


@dataclass
class PendingCite(Node):
    targetlabels: list[str] = field(kw_only=True, default_factory=list)


@dataclass
class Cite(Node):
    targets: list[Node] = field(kw_only=True, default_factory=list)


@dataclass
class Proof(NodeWithChildren):
    _newmetakeys: ClassVar[set] = set()


@dataclass
class Subproof(NodeWithChildren):
    _newmetakeys: ClassVar[set] = set()


@dataclass
class Sketch(Paragraph):
    possible_parents: ClassVar[set[Type['NodeWithChildren']]] = {Proof}


@dataclass
class Step(Paragraph):
    possible_parents: ClassVar[set[Type['NodeWithChildren']]] = {Proof}


@dataclass
class Theorem(Heading):
    goals: list[BaseReference] = field(kw_only=True, default_factory=list)
    _newmetakeys: ClassVar[set] = {'goals'}


@dataclass
class Lemma(Theorem):
    _newmetakeys: ClassVar[set] = set()


@dataclass
class Remark(Theorem):
    _newmetakeys: ClassVar[set] = set()


@dataclass
class Bibliography(NodeWithChildren):
    pass


@dataclass
class Bibitem(Node):
    _: KW_ONLY
    kind: str = ''
    author: str = ''
    title: str = ''
    year: int = -1
    journal: str = ''
    volume: int = -1
    number: int = -1
    publisher: str = ''
    _newmetakeys: ClassVar[set] = {
        'kind',
        'author',
        'title',
        'year',
        'journal',
        'volume',
        'number',
        'publisher',
    }


@dataclass
class UnknownBibitem(Bibitem):
    number: str = "?"
