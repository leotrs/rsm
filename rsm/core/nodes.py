"""
nodes.py
--------

Nodes that make up the Manuscript tree.

"""

from typing import Any, Type, Optional, Callable, ClassVar
from collections.abc import Iterable
from datetime import datetime
from icecream import ic

from .util import ShortenedString, short_repr


class RSMNodeError(Exception):
    pass


class Node:
    classreftext: ClassVar[str] = '{nodeclass} {number}'
    possible_parents: ClassVar[set[Type['NodeWithChildren']]] = set()
    _newmetakeys: ClassVar[set] = {'label', 'types', 'nonum', 'reftext'}

    def __init__(
        self,
        label: str = '',
        types: list[str] | None = None,
        number: int | None = None,
        nonum: bool = False,
        customreftext: str = '',
    ) -> None:
        self.label = label
        self.types = types or []
        self.nonum = nonum
        self.number = number
        self.reftext = customreftext or self.classreftext
        self._parent = None

    def _attrs_for_repr_and_eq(self):
        return ['label', 'types', 'nonum', 'number', 'parent']

    def __repr__(self):
        cls = self.__class__.__name__
        d = {att: getattr(self, att) for att in self._attrs_for_repr_and_eq()}
        d['parent'] = (
            'None' if self.parent is None else f'{self.parent.__class__.__name__}(...)'
        )
        return f'{cls}({d})'

    def __eq__(self, other):
        attrs = self._attrs_for_repr_and_eq()
        try:
            return all(
                (mine is getattr(other, a))
                if isinstance(mine := getattr(self, a), Node)
                else (mine == getattr(other, a))
                for a in attrs
            )
        except AttributeError:
            return False

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

    def prev_sibling(self, cls: Optional[Type['Node']] = None) -> Optional['Node']:
        if self.parent is None:
            return None
        if cls is None:
            cls = self.__class__

        index = self.parent.children.index(self)
        prev_sibs = self.parent.children[:index]
        ic(index)
        ic(prev_sibs)
        for node in reversed(prev_sibs):
            if isinstance(node, cls):
                return node
        return None

    def first_ancestor_of_type(self, cls: Type['Node']) -> Optional['Node']:
        ancestor = self.parent
        while not isinstance(ancestor, cls):
            ancestor = ancestor.parent
        return ancestor  # the root node has parent None

    def replace_self(self, replacement: 'Node') -> None:
        if not self.parent:
            raise RSMNodeError('Can only call replace_self on a node with parent')
        ids = [id(c) for c in self.parent.children]
        index = ids.index(id(self))
        self.parent.remove(self)
        self.parent._children.insert(index, replacement)
        replacement.parent = self.parent
        self.parent = None

    def ingest_dict_as_meta(self, meta: dict) -> None:
        for key, value in meta.items():
            setattr(self, str(key), value)


class NodeWithChildren(Node):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self._children = []

    def _attrs_for_repr_and_eq(self):
        return super()._attrs_for_repr_and_eq() + ['children']

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
        ids = [id(c) for c in self._children]
        index = ids.index(id(child))
        del self._children[index]


class Text(Node):
    def __init__(self, text: str = '', **kwargs):
        super().__init__(**kwargs)
        self.text = text

    def __repr__(self) -> str:
        return short_repr(self.text, self.__class__.__name__)


class Span(NodeWithChildren):
    _newmetakeys: ClassVar[set] = {'strong', 'emphas', 'little', 'insert', 'delete'}
    attr_to_tag: ClassVar[dict] = {
        'strong': 'strong',
        'emphas': 'em',
        'little': 'small',
        'insert': 'ins',
        'delete': 'del',
    }

    def __init__(
        self,
        strong: bool = False,
        emphas: bool = False,
        little: bool = False,
        insert: bool = False,
        delete: bool = False,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.strong = strong
        self.emphas = emphas
        self.little = little
        self.insert = insert
        self.delete = delete


class Claim(NodeWithChildren):
    pass


class BlockClaim(Claim):
    pass


class Heading(NodeWithChildren):
    _newmetakeys: ClassVar[set] = {'title'}

    def __init__(self, title: str = '', **kwargs):
        super().__init__(**kwargs)
        self.title = title


class Manuscript(Heading):
    _newmetakeys: ClassVar[set] = {'date'}

    def __init__(self, src: str = '', date: datetime | None = None, **kwargs):
        super().__init__(**kwargs)
        self.src = ShortenedString(src)
        self.date = date


class Author(Node):
    _newmetakeys: ClassVar[set] = {'name', 'affiliation', 'email'}

    def __init__(
        self, name: str = '', affiliation: str = '', email: str = '', **kwargs
    ):
        super().__init__(**kwargs)
        self.name = name
        self.affiliation = affiliation
        self.email = email


class Abstract(NodeWithChildren):
    _newmetakeys: ClassVar[set] = {'keywords', 'MSC'}

    def __init__(
        self, keywords: list[str] | None = None, MSC: list[str] | None = None, **kwargs
    ):
        super().__init__(**kwargs)
        self.keywords = keywords or []
        self.MSC = MSC or []


class Section(Heading):
    level: ClassVar[int] = 2


class Subsection(Section):
    level: ClassVar[int] = 3


class Subsubsection(Section):
    level: ClassVar[int] = 4


class BaseParagraph(Heading):
    pass


class Paragraph(BaseParagraph):
    pass


class Comment(BaseParagraph):
    pass


class Enumerate(NodeWithChildren):
    pass


class Itemize(NodeWithChildren):
    pass


class Item(BaseParagraph):
    possible_parents: ClassVar[set[Type['NodeWithChildren']]] = {Itemize, Enumerate}


class Keyword(Span):
    pass


class Math(NodeWithChildren):
    pass


class Code(NodeWithChildren):
    pass


class DisplayMath(NodeWithChildren):
    classreftext: str = 'Equation {number}'


class DisplayCode(NodeWithChildren):
    classreftext: str = 'Code Listing {number}'


class BaseReference(Node):
    def __init__(
        self, target: str | Node | None = None, overwrite_reftext: str = '', **kwargs
    ):
        super().__init__(**kwargs)
        self.overwrite_reftext = overwrite_reftext
        self.target = target

    def _attrs_for_repr_and_eq(self):
        return super()._attrs_for_repr_and_eq() + ['target', 'overwrite_reftext']


class PendingReference(BaseReference):
    def __init__(self, target: str = '', **kwargs):
        super().__init__(target, **kwargs)


class Reference(BaseReference):
    def __init__(self, target: Node | None = None, **kwargs):
        super().__init__(target, **kwargs)


class PendingPrev(BaseReference):
    def __init__(self, target: str = '', **kwargs):
        super().__init__(target, **kwargs)


class URL(BaseReference):
    def __init__(self, target: str = '', **kwargs):
        super().__init__(target, **kwargs)


class PendingCite(Node):
    def __init__(self, targetlabels: list[str] = None, **kwargs):
        super().__init__(**kwargs)
        self.targetlabels = targetlabels or []


class Cite(Node):
    def __init__(self, targets: list[Node] | None = None, **kwargs):
        super().__init__(**kwargs)
        self.targets = targets or []


class Proof(NodeWithChildren):
    _newmetakeys: ClassVar[set] = set()


class Subproof(NodeWithChildren):
    _newmetakeys: ClassVar[set] = set()


class Sketch(Paragraph):
    possible_parents: ClassVar[set[Type['NodeWithChildren']]] = {Proof}


class Step(Paragraph):
    possible_parents: ClassVar[set[Type['NodeWithChildren']]] = {Proof}


Step.possible_parents.add(Step)


class Theorem(Heading):
    _newmetakeys: ClassVar[set] = {'goals', 'stars', 'clocks'}

    def __init__(
        self,
        goals: list[BaseReference] | None = None,
        stars: int = 0,
        clocks: int = 0,
        **kwargs,
    ):
        super().__init__(*kwargs)
        self.goals = goals or []
        self.stars = stars
        self.clocks = clocks


class Lemma(Theorem):
    _newmetakeys: ClassVar[set] = set()


class Remark(Theorem):
    _newmetakeys: ClassVar[set] = set()


class Bibliography(NodeWithChildren):
    pass


class Bibitem(Node):
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

    def __init__(
        self,
        kind: str = '',
        author: str = '',
        title: str = '',
        year: int = -1,
        journal: str = '',
        volume: int = -1,
        number: int = -1,
        publisher: str = '',
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.kind = kind
        self.author = author
        self.title = title
        self.year = year
        self.journal = journal
        self.volume = volume
        self.number = number
        self.publisher = publisher


class UnknownBibitem(Bibitem):
    def __init__(self, number: str | int = '?', **kwargs):
        super().__init__(**kwargs)
        self.number = number
