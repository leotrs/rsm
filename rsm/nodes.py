"""Nodes that make up the manuscript tree.

The manuscript tree semantically represents each element in the manuscript such as
sections, paragraphs, special regions, figures, etc.

This is opposed to the syntax tree output by tree-sitter whose nodes represent elements
with syntactic meaning such as tags, delimiters, etc.

"""

from typing import Any, Type, Optional, Callable, ClassVar, TypeVar, cast, Union
from collections.abc import Iterable
from datetime import datetime
from icecream import ic
import textwrap
from pathlib import Path
import logging

logger = logging.getLogger("RSM").getChild("nodes")

NodeSubType = TypeVar("NodeSubType", bound="Node")


class RSMNodeError(Exception):
    pass


class Node:
    """A node in the manuscript tree.

    A node represents a semantically meaningful element of the manuscript.

    Parameters
    ----------

    label
        Unique identifier for this node.
    types
        Types of this node.
    number
        Node number.
    nonum
        Whether this node should be automatically given a number.
    reftext_template
        If not empty, replaces :attr:`classreftext`.

    See Also
    --------
    :class:`Manuscript` : The class of the root node of a manuscript tree.
    :class:`NodeWithChildren` : Subclass that implements methods to handle children.

    Notes
    -----
    An instance of Node cannot have children.  Only instances of (subclasses) of
    :class:`NodeWithChildren` may have them.  However, for the sake of having a uniform
    API, Node implements the property :attr:`children`, which always returns an empty
    tuple.

    """

    classreftext: ClassVar[str] = "{nodeclass} {number}"

    possible_parents: ClassVar[set[Type["NodeWithChildren"]]] = set()
    """Allowed types of parent Nodes.

    When setting the parent of a Node, this attribute is checked to see whether the
    intended parent has an admissible type.

    Examples
    --------
    This is a class variable

    >>> nodes.Item.possible_parents == {nodes.Itemize, nodes.Enumerate, nodes.Contents}
    True

    This variable is checked when setting the parent directly.

    >>> it = nodes.Item()
    >>> it.parent = nodes.Paragraph()
    Traceback (most recent call last):
    rsm.nodes.RSMNodeError: Node of type <class 'rsm.nodes.Item'> cannot have parent of type <class 'rsm.nodes.Paragraph'>

    This is also used when setting the parent in some other indirect way, for example
    when calling :meth:`~NodeWithChildren.append` on the desired parent.

    >>> nodes.Paragraph().append(it)
    Traceback (most recent call last):
    rsm.nodes.RSMNodeError: Node of type <class 'rsm.nodes.Item'> cannot have parent of type <class 'rsm.nodes.Paragraph'>

    Allowed parents proceed without raising.

    >>> nodes.Itemize().append(it)
    Itemize(parent=None, [Item])

    """

    autonumber: ClassVar[bool] = False
    """Whether to automatically assign a number to this node during transform step.

    Examples
    --------
    >>> msc, thm1, thm2 = nodes.Manuscript(), nodes.Theorem(), nodes.Theorem()
    >>> (thm1.number, thm2.number) == (None, None)
    True
    >>> tform = rsm.transformer.Transformer()
    >>> tform.transform(msc.append([thm1, thm2]))  # doctest: +IGNORE_RESULT
    >>> thm1.number, thm2.number
    (1, 2)

    """

    _number_within: ClassVar[Type["Node"] | None] = None
    # see property number_within for documentation

    _number_as: ClassVar[Type["Node"] | None] = None
    # see property number_as for documentation

    newmetakeys: ClassVar[set] = {"label", "types", "nonum", "reftext"}
    """Meta keys to add to those of the parent class.

    .. important::
       Only use this when defining a new Node subclass.  When dealing with Node
       isntances, do not access this attribute directly neither for reading nor writing.
       Always use :meth:`metakeys` in that case.

    See Also
    --------
    :meth:`metakeys`

    Examples
    --------
    The keys in `newmetakeys` are added to the meta keys of the parent class.

    >>> nodes.Heading.newmetakeys
    {'title'}
    >>> nodes.Heading.metakeys() == nodes.Node.metakeys() | {"title"}
    True

    The intended use, and only supported use, of `newmetakeys` is at the time of class
    definition.

    >>> class NewNode(nodes.Node):
    ...     newmetakeys = {"newkey"}
    >>> NewNode.metakeys() == nodes.Node.metakeys() | {"newkey"}
    True

    """

    def __init__(
        self,
        label: str = "",
        types: list[str] | None = None,
        number: int | None = None,
        nonum: bool = False,
        reftext_template: str = "",
    ) -> None:
        self.label = label
        self.types = types or []
        self.nonum = nonum
        self.number = number
        self.reftext_template = reftext_template or self.classreftext
        self._parent: "NodeWithChildren" | None = None

    def _attrs_for_repr_and_eq(self) -> list[str]:
        return ["label", "types", "nonum", "number", "parent"]

    def __repr__(self) -> str:
        cls = self.__class__.__name__
        d = {
            att: getattr(self, att)
            for att in self._attrs_for_repr_and_eq()
            if att != "children"
        }
        d["parent"] = (
            "None" if self.parent is None else f"{self.parent.__class__.__name__}"
        )
        d_str = ", ".join(f"{k}={v}" for k, v in d.items() if v)
        return f"{cls}({d_str})"

    def __eq__(self, other: Any) -> bool:
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

    def sexp(
        self,
        tab_width: int = 2,
        meta: bool = False,
        ignore_meta_keys: set | None = None,
    ) -> str:
        ignore_meta_keys = set() if ignore_meta_keys is None else set(ignore_meta_keys)
        exp = ""
        stack = [(0, self)]
        while stack:
            indent, node = stack.pop()
            if node is None:
                exp += ")"
                continue
            spaces = " " * indent
            exp += f"\n{spaces}({node.__class__.__name__}"
            if meta:
                meta_str = (
                    "{ "
                    + ", ".join(
                        [
                            f":{key}: {val}"
                            for key in sorted(node.metakeys())
                            if key not in ignore_meta_keys
                            and (val := getattr(node, key))
                        ]
                    )
                    + " }"
                )
                exp += f" {meta_str}"
            stack.append((None, None))
            if node.children:
                stack += [(indent + tab_width, c) for c in reversed(node.children)]
        return exp[1:]  # get rid of an extra newline at the start

    @classmethod
    def metakeys(cls: Type["Node"]) -> set[str]:
        """The valid meta keys of the given class.

        Returns
        -------
        The valid meta keys.

        Examples
        --------
        >>> all_nodes_meta = {"label", "types", "nonum", "reftext"}
        >>> nodes.Node.metakeys() == all_nodes_meta
        True
        >>> nodes.Span.metakeys() - all_nodes_meta == {"strong", "emphas", "little", "insert", "delete"}
        True
        >>> nodes.Author.metakeys()  - all_nodes_meta == {"name", "affiliation", "email"}
        True

        """
        return cls.newmetakeys.union(
            *[b.metakeys() for b in cls.__bases__ if hasattr(b, "metakeys")]
        )

    @property
    def parent(self) -> Optional["NodeWithChildren"]:
        """The parent of this Node, or None."""
        return self._parent

    @parent.setter
    def parent(self, node: Optional["NodeWithChildren"]) -> None:
        if node is None:
            self._parent = None
        elif not self.__class__.possible_parents:
            self._parent = node
        else:
            possible_parents = self.__class__.possible_parents
            if possible_parents and type(node) not in possible_parents:
                raise RSMNodeError(
                    f"Node of type {type(self)} cannot have parent of type {type(node)}"
                )
            self._parent = node

    @property
    def children(self) -> tuple:
        """Tuple with this Node's children."""
        return tuple()  # necessary for methods such as Nodes.traverse

    @property
    def number_within(self) -> Type["Node"]:
        return self.__class__._number_within or Manuscript

    @property
    def number_as(self) -> Type["Node"]:
        return self._number_as or self.__class__

    @property
    def full_number(self) -> str:
        if self.nonum:
            return None
        ancestor = self.first_ancestor_of_type(self.number_within)
        if not ancestor:
            logger.warning(
                f"{self.__class__.__name__} numbered within "
                f"{self.number_within.__name__} but no such ancestor was found; "
                "using root node instead"
            )
            ancestor = self.first_ancestor_of_type(Manuscript)
        if ancestor and ancestor.full_number:
            return f"{ancestor.full_number}.{self.number}"
        return f"{self.number}" if self.number else ""

    @property
    def reftext(self) -> str:
        return self.reftext_template.format(
            nodeclass=self.__class__.__name__, number=self.full_number
        )

    def traverse(
        self,
        *,
        condition: Callable = lambda n: True,
        nodeclass: NodeSubType | None = None,
    ) -> Iterable[NodeSubType]:
        if nodeclass is not None:
            if issubclass(nodeclass, Node):
                condition = lambda n: isinstance(n, nodeclass)
            else:
                raise RSMNodeError("nodeclass must inherit from Node")

        stack = [self]
        while stack:
            node = stack.pop()
            if condition(node):
                yield cast(NodeSubType, node)
            stack += node.children[::-1]

    def first_of_type(
        self, cls: Type["Node"] | tuple[Type["Node"]], return_idx: bool = False
    ) -> Optional["Node"] | tuple[Optional["Node"], Optional[int]]:
        """First child of the specified type.

        Parameters
        ----------
        cls
            Desired class of the child.
        return_idx
            Whether to return the index of the child among this node's children.

        Returns
        -------
        Node
            The first child of the specified type, or None.
        Node, int
            If `return_idx` is True, return (child, index), or (None, None).


        See Also
        --------
        :meth:`last_of_type`
        :meth:`first_ancestor_of_type`

        Examples
        --------
        >>> p = nodes.Paragraph().append([nodes.Text("one"), nodes.Text("two")])
        >>> p.first_of_type(nodes.Text)
        Text("one")
        >>> p.first_of_type(nodes.Text, return_idx=True)
        (Text("one"), 0)

        The index counts all existing children.

        >>> p.prepend(nodes.Span())
        Paragraph(parent=None, [Span, Text, Text])
        >>> p.first_of_type(nodes.Text, return_idx=True)
        (Text("one"), 1)

        """
        for idx, child in enumerate(self.children):
            if isinstance(child, cls):
                return (child, idx) if return_idx else child
        return (None, None) if return_idx else None

    def last_of_type(
        self, cls: Type["Node"] | tuple[Type["Node"]], return_idx: bool = False
    ) -> Optional["Node"] | tuple[Optional["Node"], int | None]:
        """Last child of the specified type.

        For details, see :meth:`first_of_type`.

        Examples
        --------
        >>> p = nodes.Paragraph().append([nodes.Span(), nodes.Text("one"), nodes.Text("two")])
        >>> p.last_of_type(nodes.Text, return_idx=True)
        (Text("two"), 2)

        """
        for idx, child in enumerate(reversed(self.children)):
            if isinstance(child, cls):
                return (child, len(self.children) - idx - 1) if return_idx else child

    def prev_sibling(
        self, cls: Union[Type["Node"], str, None] = None
    ) -> Optional["Node"]:
        """The previous sibling, optionally of a specified type.

        Parameters
        ----------
        cls
            The type of the desired sibling.  If "self", search for the previous sibling
            with the same type as this node.  If None, return the immediately preceding
            sibling, regardless of its type.

        Returns
        -------
            The desired sibling, or None.

        See Also
        --------
        :meth:`first_ancestor_of_type`
        :meth:`next_sibling`

        Examples
        --------
        >>> p, s, t1, t2 = nodes.Paragraph(), nodes.Span(), nodes.Text("one"), nodes.Text("two")
        >>> p.append([t1, s, t2])  # doctest: +IGNORE_RESULT
        >>> t2.prev_sibling()
        Span(parent=Paragraph)
        >>> t2.prev_sibling(nodes.Text)
        Text("one")
        >>> t1.prev_sibling() is None
        True

        """
        if self.parent is None:
            return None
        if cls is None:
            cls = self.__class__

        ids = [id(c) for c in self.parent.children]
        index = ids.index(id(self))
        prev_sibs = self.parent.children[:index]
        for node in reversed(prev_sibs):
            if isinstance(node, cls):
                return node
        return None

    def next_sibling(self, cls: Optional[Type["Node"]] = None) -> Optional["Node"]:
        if self.parent is None:
            return None
        if cls is None:
            cls = self.__class__

        ids = [id(c) for c in self.parent.children]
        index = ids.index(id(self))
        next_sibs = self.parent.children[index + 1 :]
        for node in reversed(next_sibs):
            if isinstance(node, cls):
                return node
        return None

    def first_ancestor_of_type(
        self, cls: Type["Node"] | tuple[Type["Node"]]
    ) -> Optional["Node"]:
        """First ancestor of the specified type.

        Parameters
        ----------
        cls
            Desired class of the ancestor.

        Returns
        -------
        The first ancestor of the specified type, or None.

        See Also
        --------
        :attr:`parent`
        :meth:`first_of_type`

        Examples
        --------
        Given the tree

        >>> t = nodes.Text('Hello')
        >>> p = nodes.Paragraph().append(nodes.Span().append(t))
        >>> print(p.sexp())
        (Paragraph
          (Span
            (Text)))

        Find an ancestor of a desired type.

        >>> t.first_ancestor_of_type(nodes.Paragraph)
        Paragraph(parent=None, [Span])

        Always check the return value against ``None``.

        >>> t.first_ancestor_of_type(nodes.Manuscript) is None
        True

        """
        ancestor = self.parent
        # We use `type is not cls` instead of the recommended `isinstance()` because we
        # are looking for an exact type, not a subtype.  For example, we may want to
        # find the enclosing Section of a Theorem, bypassing any Subsections that may
        # lie in between.
        while ancestor and (
            all(type(ancestor) is not c for c in cls)
            if isinstance(cls, tuple)
            else (type(ancestor) is not cls)
        ):
            ancestor = ancestor.parent
        return ancestor  # the root node has parent None

    def replace_self(self, replacement: Union["Node", Iterable["Node"]]) -> None:
        if not self.parent:
            raise RSMNodeError("Can only call replace_self on a node with parent")
        ids = [id(c) for c in self.parent.children]
        index = ids.index(id(self))
        parent = self.parent
        self.parent.remove(self)
        if not isinstance(replacement, Node):
            for idx, rep in enumerate(replacement):
                parent._children.insert(index + idx, rep)
                rep.parent = parent
        else:
            parent._children.insert(index, replacement)
            replacement.parent = parent

    def remove_self(self) -> None:
        """Remove this Node from its parent's children.

        See Also
        --------
        :meth:`replace_self`

        Examples
        --------
        >>> t = nodes.Text("remove me")
        >>> p = nodes.Paragraph().append(t)
        >>> p.children
        (Text("remove me"),)
        >>> t.remove_self()
        >>> p.children
        ()

        """
        if self.parent is not None:
            self.parent.remove(self)
            self.parent = None

    def ingest_dict_as_meta(self, meta: dict) -> None:
        if "reftext" in meta:
            meta["reftext_template"] = meta["reftext"]
            del meta["reftext"]
        for key, value in meta.items():
            setattr(self, str(key), value)


class NodeWithChildren(Node):
    """A :class:`Node` that may have children Nodes."""

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._children: list[Node] = []

    def _attrs_for_repr_and_eq(self) -> list[str]:
        return super()._attrs_for_repr_and_eq() + ["children"]

    def __repr__(self) -> str:
        if not self._children:
            return super().__repr__()
        children_repr = ", ".join(f"{c.__class__.__name__}" for c in self._children)
        children_repr = "[" + children_repr + "]"
        ret = super().__repr__()
        return ret[:-1] + ", " + children_repr + ")"

    @property
    def children(self) -> tuple[Node, ...]:
        """Tuple with this Node's children."""
        return tuple(self._children)

    def clear(self) -> None:
        """Remove all children."""
        for c in self._children:
            c.parent = None
        self._children = []

    def append(self, child: Node | Iterable[Node]) -> "NodeWithChildren":
        """Add a child or children after all current children.

        Parameters
        ----------
        child
            Node or iterable or nodes to append.

        Returns
        -------
        self

        Raises
        ------
        RSMNodeError
            When attempting to add as a child a node that already has a parent.

        See Also
        --------
        :meth:`prepend`

        Examples
        --------

        Append one or many children.

        >>> p, t1, t2, t3 = nodes.Paragraph(), nodes.Text("one"), nodes.Text("two"), nodes.Text("three")
        >>> p.append(t1)        # doctest: +IGNORE_RESULT
        >>> p.append([t2, t3])  # doctest: +IGNORE_RESULT
        >>> p.children
        (Text("one"), Text("two"), Text("three"))

        Calls can be chained.

        >>> p, t1, t2, t3 = nodes.Paragraph(), nodes.Text("one"), nodes.Text("two"), nodes.Text("three")
        >>> p.append(t1).append([t2, t3])  # doctest: +IGNORE_RESULT
        >>> p.children
        (Text("one"), Text("two"), Text("three"))

        Will raise when trying to append a node that already has a parent.

        >>> p2 = nodes.Paragraph()
        >>> p2.append(t1)
        Traceback (most recent call last):
        rsm.nodes.RSMNodeError: Attempting to append child to a new parent

        This is the case even when appending to the same parent.

        >>> t4 = nodes.Text("four")
        >>> p2.append(t4)       # doctest: +IGNORE_RESULT
        >>> p2.append(t4)
        Traceback (most recent call last):
        rsm.nodes.RSMNodeError: Attempting to append child to a new parent

        """
        if isinstance(child, Iterable):
            for c in child:
                self.append(c)
        elif isinstance(child, Node):
            if child.parent:
                raise RSMNodeError("Attempting to append child to a new parent")
            self._children.append(child)
            child.parent = self
        else:
            raise TypeError("Can only append a Node or iterable of Nodes as children")
        return self

    def prepend(self, child: Node | Iterable[Node]) -> None:
        """Add a child or children before all current children.

        For details, see :meth:`append`.

        See Also
        --------
        :meth:`append`

        """
        if isinstance(child, list):
            for c in reversed(child):
                self.prepend(c)
        elif isinstance(child, Node):
            if child.parent and child.parent is not self:
                raise RSMNodeError("Attempting to prepend child to a different parent")
            self._children.insert(0, child)
            child.parent = self
        else:
            raise TypeError("Can only prepend a Node or iterable of Nodes as children")
        return self

    def remove(self, child: "Node") -> None:
        """Remove child."""
        ids = [id(c) for c in self._children]
        index = ids.index(id(child))
        del self._children[index]
        child.parent = None


class Text(Node):
    def __init__(self, text: str = "", asis: bool = False, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.text = text
        self.asis = asis

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}("{textwrap.shorten(self.text, 60)}")'


class Error(Text):
    pass


class Span(NodeWithChildren):
    newmetakeys: ClassVar[set] = {"strong", "emphas", "little", "insert", "delete"}
    attr_to_tag: ClassVar[dict] = {
        "strong": "strong",
        "emphas": "em",
        "little": "small",
        "insert": "ins",
        "delete": "del",
    }

    def __init__(
        self,
        strong: bool = False,
        emphas: bool = False,
        little: bool = False,
        insert: bool = False,
        delete: bool = False,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.strong = strong
        self.emphas = emphas
        self.little = little
        self.insert = insert
        self.delete = delete


class Heading(NodeWithChildren):
    newmetakeys: ClassVar[set] = {"title"}

    def __init__(self, title: str = "", **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.title = title


class Manuscript(Heading):
    newmetakeys: ClassVar[set] = {"date"}
    nonum = True

    def __init__(
        self, src: str = "", date: datetime | None = None, **kwargs: Any
    ) -> None:
        super().__init__(**kwargs)
        self.src = src
        self.date = date

    @property
    def full_number(self) -> str:
        return ""


class Author(Node):
    newmetakeys: ClassVar[set] = {"name", "affiliation", "email"}

    def __init__(
        self, name: str = "", affiliation: str = "", email: str = "", **kwargs: Any
    ) -> None:
        super().__init__(**kwargs)
        self.name = name
        self.affiliation = affiliation
        self.email = email


class Abstract(NodeWithChildren):
    newmetakeys: ClassVar[set] = {"keywords", "MSC"}

    def __init__(
        self,
        keywords: list[str] | None = None,
        MSC: list[str] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.keywords = keywords or []
        self.MSC = MSC or []


class Section(Heading):
    autonumber = True
    level: ClassVar[int] = 2


class Subsection(Section):
    _number_within = Section
    level: ClassVar[int] = 3
    classreftext: ClassVar[str] = "Section {number}"


class Subsubsection(Section):
    _number_within = Subsection
    level: ClassVar[int] = 4
    classreftext: ClassVar[str] = "Section {number}"


class BaseParagraph(Heading):
    pass


class Paragraph(BaseParagraph):
    pass


class Note(BaseParagraph):
    pass


class Enumerate(NodeWithChildren):
    pass


class Itemize(NodeWithChildren):
    pass


class Keyword(Span):
    pass


class Construct(NodeWithChildren):
    kind_to_keyword: dict[str, str] = {
        "let": "LET",
        "define": "DEFINE",
        "write": "WRITE",
        "case": "CASE",
        "then": "THEN",
        "new": "NEW",
        "assume": "ASSUME",
        "prove": "PROVE",
        "claim": "⊢",
        "claimblock": "⊢",
        "qed": "QED",
    }

    def __init__(self, kind: str = "", **kwargs: Any):
        super().__init__(**kwargs)
        self.kind = kind

    @property
    def keyword(self):
        return self.kind_to_keyword[self.kind]


class ClaimBlock(Construct):
    def __init__(self, **kwargs: Any):
        super().__init__(kind="claimblock", **kwargs)


class Math(NodeWithChildren):
    pass


class Code(NodeWithChildren):
    pass


class MathBlock(NodeWithChildren):
    autonumber = True
    _number_within = Section
    classreftext: ClassVar[str] = "({number})"
    newmetakeys: ClassVar[set] = {"isclaim"}

    def __init__(self, isclaim: bool = False, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.isclaim = isclaim


class CodeBlock(NodeWithChildren):
    classreftext: ClassVar[str] = "Code Listing {number}"


class Algorithm(NodeWithChildren):
    autonumber = True


class Appendix(Node):
    pass


class BaseReference(Node):
    def __init__(
        self,
        target: str | Node | None = None,
        overwrite_reftext: str = "",
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.overwrite_reftext = overwrite_reftext
        self.target = target

    def _attrs_for_repr_and_eq(self) -> list[str]:
        return super()._attrs_for_repr_and_eq() + ["target", "overwrite_reftext"]


class PendingReference(BaseReference):
    def __init__(self, target: str = "", **kwargs: Any) -> None:
        super().__init__(target, **kwargs)


class Reference(BaseReference):
    def __init__(self, target: Node | None = None, **kwargs: Any) -> None:
        super().__init__(target, **kwargs)


class PendingPrev(BaseReference):
    def __init__(self, target: str = "", **kwargs: Any) -> None:
        super().__init__(target, **kwargs)


class URL(BaseReference):
    def __init__(self, target: str = "", **kwargs: Any) -> None:
        super().__init__(target, **kwargs)


class PendingCite(Node):
    def __init__(self, targetlabels: list[str] = None, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.targetlabels = targetlabels or []


class Cite(Node):
    def __init__(self, targets: list[Node] | None = None, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.targets = targets or []


class Statement(NodeWithChildren):
    pass


class Proof(NodeWithChildren):
    pass


class Subproof(NodeWithChildren):  # importantly, NOT a subclass of Proof!
    pass


class Sketch(NodeWithChildren):
    possible_parents: ClassVar[set[Type["NodeWithChildren"]]] = {Proof}


class Step(Paragraph):
    autonumber = True
    possible_parents: ClassVar[set[Type["NodeWithChildren"]]] = {Proof, Subproof}


Step.possible_parents.add(Step)
Step._number_within = (Step, Proof)


class Theorem(Heading):
    autonumber = True
    title = ""
    _number_within = Section
    newmetakeys: ClassVar[set] = {"title", "goals", "stars", "clocks"}

    def __init__(
        self,
        title: str = "",
        goals: list[BaseReference] | None = None,
        stars: int = 0,
        clocks: int = 0,
        **kwargs: Any,
    ):
        super().__init__(*kwargs)
        self.title = title
        self.goals = goals or []
        self.stars = stars
        self.clocks = clocks


class Lemma(Theorem):
    _number_as = Theorem


class Proposition(Theorem):
    _number_as = Theorem


class Remark(Theorem):
    _number_as = Theorem


class Definition(Theorem):
    _number_as = Theorem


class Bibliography(NodeWithChildren):
    pass


class Bibitem(Node):
    autonumber = True
    classreftext: ClassVar[str] = "{number}"
    newmetakeys: ClassVar[set] = {
        "kind",
        "author",
        "title",
        "year",
        "journal",
        "volume",
        "number",
        "publisher",
        "doi",
    }

    def __init__(
        self,
        kind: str = "",
        author: str = "",
        title: str = "",
        year: int = -1,
        journal: str = "",
        volume: int = -1,
        number: int = -1,
        publisher: str = "",
        doi: str = "",
        **kwargs: Any,
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
        self.doi = doi
        self.backlinks = []


class UnknownBibitem(Bibitem):
    def __init__(self, number: str | int = "?", **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.number = number


class Figure(NodeWithChildren):
    autonumber = True
    _number_within = Section
    newmetakeys: ClassVar[set] = {"path", "scale"}

    def __init__(
        self, path: Path | str = "", scale: float = 1.0, **kwargs: Any
    ) -> None:
        super().__init__(**kwargs)
        self.path = Path(path)
        self.scale = scale


class Draft(NodeWithChildren):
    pass


class Table(NodeWithChildren):
    autonumber = True


class TableHead(NodeWithChildren):
    pass


class TableBody(NodeWithChildren):
    pass


class TableRow(NodeWithChildren):
    pass


class TableDatum(NodeWithChildren):
    pass


class Caption(Paragraph):
    possible_parents: ClassVar[set[Type["NodeWithChildren"]]] = {Figure, Table}


class Contents(Itemize):
    pass


class Item(BaseParagraph):
    possible_parents: ClassVar[set[Type["NodeWithChildren"]]] = {
        Itemize,
        Enumerate,
        Contents,
    }
