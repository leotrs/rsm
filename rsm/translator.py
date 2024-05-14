"""Input: abstract syntax tree -- Output: HTML body.

The translator takes the finished abstract manuscript tree and translates its content to
HTML.

Two main classes handle this process: :class:`Translator` and :class:`EditCommand`.
:class:`Translator` traverses the manuscript tree in depth-first order and implements a
generic visitor pattern.  That is, when a node ``n`` of class ``cls`` is visited, the
method ``visit_cls(n)`` is called.  Then, all of ``n``'s children are visited in order.
Finally, the method ``leave_cls(n)`` is called.

Each ``visit_*`` and ``leave_*`` method returns an object of type :class:`EditCommand`.
This class implements a command pattern whose sole purpose is to append text to the
underlying HTML string that is being built.  The simplest example is :class:`AppendText`
which simply appends an arbitrary string to the underlying HTML.  For example,
:meth:`~rsm.translator.Translator.visit_node` returns an :class:`AppendText` instance
which adds some basic information about the node to the HTML output.

The visit method ``visit_cls`` returns the HTML markup that needs to appear *before* the
node's children's markup, while ``leave_cls`` returns the HTML markup that appears
*after* all its children.

Suppose a new kind of node is created, called ``NewNodeClass``.  To implement the
translation step for this new class of node, implement a new method in
:class:`Translator` with signature

.. code-block:: python

   def visit_newnodeclass(self, node: NewNodeClass) -> EditCommand: ...

Optionally, also implement a leave method with signature

.. code-block:: python

   def leave_newnodeclass(self, node: NewNodeClass) -> EditCommand: ...

If a method of the appropriate name is not found, :class:`Translator` will look up the
inheritance tree of ``NewNodeClass`` until it finds a class with an existing method.
For example, if ``NewNodeClass`` inherits directly from :class:`~rsm.nodes.Span`, and a
``visit_newnodeclass`` method is not found, then ``visit_span`` will be called with the
visited instance of ``NewNodeClass``.  Since all nodes must subclass
:class:`~rsm.nodes.Node`, this process will ultimately end up calling
:meth:`~rsm.translator.Translator.visit_node` if no other bases of ``NewNodeClass`` have
a ``visit_*`` method.  The same is true for ``leave_*`` methods.

Since HTML has both opening and closing tags, the vast majority of which must be kept
balanced, care must be taken that the method ``leave_cls`` always closes any tags that
were left open in the corresponding ``visit_cls`` method.  RSM handles this
automatically in the following way.  Besides the basic :class:`AppendText` class, there
are other :class:`EditCommand` subclasses that accept some text that should be
*deferred* until the coresponding ``leave_*`` method is called on the same node.  This
deferred text is then automatically appended to the generated HTML *unless this process
is overridden* (see below).

For example, suppose nodes of class ``NewNodeClass`` should be translated to HTML by
wrapping their text contents in a ``div`` of class ``"wrapper"``.  We need only
implement a single method, namely

.. code-block:: python

   def visit_newnodeclass(self, node: NewNodeClass) -> EditCommand:
       content = f'<div class="wrapper">{node.text}'
       return AppendTextAndDefer(content, "</div>")

This tells the translator that when visiting a ``NewNodeClass`` node, the text ``"<div
class="wrapper">"``, followed by the text contents of the node, should be appended to
the generated HTML immediately, while the text ``"</div>"`` should be deferred and
appended only when ``leave_newnodeclass`` is called on that same node.  This will, as
usual, happen after the node's children have each been visited and exited.  Note there
is no need to manually implement a ``leave_newnodeclass`` method that will close the
``div`` tag.  In this way, all opening and closing HTMl tags may be specified in the
same method, and there is no need to manually coordinate the ``visit_*`` and ``leave_*``
methods of the same node class.  For this reason, most node classes do not implement a
``leave_*`` class at all.

If a ``leave_*`` method is implemented, this process will no longer work and manual
coordination must take place.  In the example above, if the node has some extra metadata
that needs to appear after its children's content, say in ``node.metadata``, then one
may implement a ``leave_*`` method such as

.. code-block:: python

   def leave_newnodeclass(self, node: NewNodeClass) -> EditCommand:
       return AppendText(f'{node.metadata}\\n</div>')

Note the need to manually close the ``</div>`` tag that was left open.

This example which manually specifies the text to be deferred (``</div>``) is for
illustration purposes only.  In reality, there exist subclasses of :class:`EditCommand`
that handle this automatically.  In fact, the example above where only the wrapper div
is necessary necessary (i.e. there is no ``node.text`` nor ``node.metadata``), could
instead be implemented simply as

.. code-block:: python

   def visit_newnodeclass(self, node: NewNodeClass) -> EditCommand:
       return AppendNodeTag(node, additional_classes="wrapper")

with no need of a ``leave`` method.  :class:`AppendNodeTag` knows to use the node's
attributes to generate the ``div``, as well as to defer its closing.  Indeed,
:class:`AppendNodeTag` is a sublcass of :class:`AppendTextAndDefer`.

There are two translator classes in this module.  The base translator
:class:`Translator` implements the visit and leave methods necessary to generate a
simple human-readable HTML output.  It is the translator class used by ``rsm-render``.
:class:`HandrailsTranslator` is a subclass of :class:`Translator` and overrides some
visit and leave methods to add handrails to the output.  It is the translator class used
by ``rsm-make``.

"""

import logging
import textwrap
from abc import ABC, abstractmethod
from collections import namedtuple
from typing import Any, Callable, Iterable, Optional

from icecream import ic

from . import nodes
from .util import highlight_code

logger = logging.getLogger("RSM").getChild("tlate")


class RSMTranslatorError(Exception):
    pass


def _make_tag(
    tag: str,
    id_: str,
    classes: Iterable,
    is_selectable: bool = False,
    nodeid: int | None = None,
    **kwargs: Any,
) -> str:
    text = f"<{tag}"
    if id_:
        text += f' id="{id_}"'
    if classes:
        classes = " ".join(classes)
        text += f' class="{classes}"'
    tabindex = 0 if is_selectable else None
    items = []
    if kwargs or tabindex is not None:
        if kwargs:
            items += [f'{k}="{v}"' for k, v in kwargs.items() if v]
        if tabindex is not None:
            items += [f"tabindex={tabindex}"]
    if nodeid is not None:
        items += [f'data-nodeid="{nodeid}"']
    if items:
        text += " "
    text += " ".join(items)
    text += ">"
    return text


# FOR DOCUMENTATION: Classes that inherit from EditCommand are meant to encapsulate
# _reusable_ operations that convert a node into HTML text.  If an operation is not
# reusable on multiple node classes and is particular to just one node class, it should
# go into the visit_* method corresponding to that class.
class EditCommand(ABC):
    defers = False

    @abstractmethod
    def make_text(self) -> Any:
        pass

    @abstractmethod
    def execute(self, translator: "Translator") -> None:
        pass

    def _edit_command_repr(self, members: Iterable[str]) -> str:
        start = f"{self.__class__.__name__}("
        middles = []
        for key in members:
            s = f"{key}="
            value = getattr(self, key)
            if isinstance(value, str):
                value = repr(textwrap.shorten(value.strip(), 60))
            s += f"{value}"
            middles.append(s)
        middle = ", ".join(middles)
        end = ")"
        return start + middle + end

    def __repr__(self) -> str:
        return self._edit_command_repr([])


class AppendTextAndDefer(EditCommand):
    defers = True

    def __init__(self, text: str = "", deferred_text: str = ""):
        self._text = text
        self._deferred_text = deferred_text

    def __repr__(self) -> str:
        return self._edit_command_repr(["text", "deferred_text"])

    def execute(self, translator: "Translator") -> None:
        translator.body += self.make_text()
        translator.deferred.append(AppendText(self.make_deferred_text()))

    def make_text(self) -> str:
        return self._text

    def make_deferred_text(self) -> str:
        return self._deferred_text


class AppendText(EditCommand):
    def __init__(self, text: str = ""):
        self._text = text

    def __repr__(self) -> str:
        return self._edit_command_repr(["text"])

    def execute(self, translator: "Translator") -> None:
        translator.body += self.make_text()

    def make_text(self) -> str:
        return self._text


class AppendOpenCloseTag(AppendText):
    def __init__(
        self,
        tag: str = "div",
        content: str = "",
        *,
        id: str = "",
        classes: list = None,
        newline_inner: bool = True,
        newline_outer: bool = True,
        is_selectable: bool = False,
        **kwargs,
    ):
        self.tag = tag
        self.content = content
        self.id = id
        self.classes = classes if classes else []
        self.newline_inner = newline_inner
        self.newline_outer = newline_outer
        self.is_selectable = is_selectable
        self.custom_attrs = kwargs
        super().__init__()

    def make_text(self) -> str:
        outer = "\n" if self.newline_outer else ""
        inner = "\n" if self.newline_inner else ""
        tag = _make_tag(
            self.tag, self.id, self.classes, self.is_selectable, **self.custom_attrs
        )
        return outer + tag + inner + self.content + inner + f"</{self.tag}>" + outer

    def __repr__(self) -> str:
        return self._edit_command_repr(["tag", "content", "id", "classes"])


class AppendOpenTagManualClose(AppendText):
    def __init__(
        self,
        tag: str = "div",
        content: str = "",
        *,
        id: str = "",
        classes: list = None,
        newline_inner: bool = True,
        newline_outer: bool = True,
        is_selectable: bool = False,
        **kwargs,
    ):
        self.tag = tag
        self.content = content
        self.id = id
        self.classes = classes if classes else []
        self.newline_inner = newline_inner
        self.newline_outer = newline_outer
        self.is_selectable = is_selectable
        self.custom_attrs = kwargs
        super().__init__()

    def make_text(self) -> str:
        outer = "\n" if self.newline_outer else ""
        inner = "\n" if self.newline_inner else ""
        tag = _make_tag(
            self.tag, self.id, self.classes, self.is_selectable, *self.custom_attrs
        )
        return outer + tag + inner + self.content

    def __repr__(self) -> str:
        return self._edit_command_repr(["tag", "content", "id", "classes"])

    def close_command(self):
        return AppendText(
            ("\n" if self.newline_inner else "")
            + f"</{self.tag}>"
            + ("\n" if self.newline_outer else "")
        )


class AppendOpenTag(AppendTextAndDefer):
    def __init__(
        self,
        tag: str = "div",
        *,
        id: str = "",
        classes: list | None = None,
        newline_inner: bool = True,
        newline_outer: bool = True,
        is_selectable: bool = False,
        **kwargs,
    ):
        self.tag = tag
        self.id = id
        self.classes = classes if classes else []
        self.newline_inner = newline_inner
        self.newline_outer = newline_outer
        self.is_selectable = is_selectable
        self.custom_attrs = kwargs
        super().__init__()

    def make_text(self) -> str:
        outer = "\n" if self.newline_outer else ""
        inner = "\n" if self.newline_inner else ""
        tag = _make_tag(
            self.tag, self.id, self.classes, self.is_selectable, **self.custom_attrs
        )
        return outer + tag + inner

    def make_deferred_text(self) -> str:
        return (
            ("\n" if self.newline_inner else "")
            + f"</{self.tag}>"
            + ("\n" if self.newline_outer else "")
        )

    def __repr__(self) -> str:
        return self._edit_command_repr(["tag", "id", "classes", "newline_inner"])


class AppendNodeTag(AppendOpenTag):
    def __init__(
        self,
        node: nodes.Node,
        tag: str = "div",
        *,
        additional_classes: Optional[list[str]] = None,
        newline_inner: bool = True,
        newline_outer: bool = True,
        is_selectable: bool = False,
    ):
        self.node = node
        classes = [node.__class__.__name__.lower()] + [str(t) for t in node.types]
        classes = list(dict.fromkeys(classes + (additional_classes or [])))
        super().__init__(
            tag=tag,
            id=node.label,
            classes=classes,
            newline_inner=newline_inner,
            newline_outer=newline_outer,
            is_selectable=is_selectable,
            nodeid=node.nodeid,
        )

    def __repr__(self) -> str:
        return self._edit_command_repr(["tag", "node"])


class AppendParagraph(AppendOpenCloseTag):
    def __init__(
        self,
        content: str = "",
        *,
        id: str = "",
        classes: list = None,
        newline_inner: bool = False,
        newline_outer: bool = True,
    ):
        super().__init__(
            tag="p",
            content=content,
            id=id,
            classes=classes,
            newline_inner=newline_inner,
            newline_outer=newline_outer,
        )

    def __repr__(self) -> str:
        return self._edit_command_repr(["content", "id", "classes"])


class AppendHeading(AppendOpenCloseTag):
    def __init__(
        self,
        level: int,
        content: str = "",
        *,
        id: str = "",
        classes: list = None,
        newline_inner: bool = False,
        newline_outer: bool = True,
    ):
        self.level = level
        super().__init__(
            tag=f"h{self.level}",
            content=content,
            id=id,
            classes=classes,
            newline_inner=newline_inner,
            newline_outer=newline_outer,
        )

    def __repr__(self) -> str:
        return self._edit_command_repr(["level", "content", "id", "classes"])


class AppendKeyword(AppendOpenCloseTag):
    def __init__(
        self,
        keyword: str,
        *,
        id: str = "",
        classes: list = None,
        newline_inner: bool = False,
        newline_outer: bool = False,
    ):
        classes = ["keyword"] + (classes or [])
        super().__init__(
            tag="span",
            content=keyword,
            id=id,
            classes=classes,
            newline_inner=newline_inner,
            newline_outer=newline_outer,
        )

    def __repr__(self) -> str:
        return self._edit_command_repr(["level", "content", "id", "classes"])


class AppendHalmos(AppendOpenCloseTag):
    def __init__(
        self,
        *,
        id: str = "",
        classes: list = None,
    ):
        super().__init__(
            tag="div",
            content="",
            id=id,
            classes=["halmos"] + (classes or []),
            newline_inner=False,
            newline_outer=True,
        )

    def __repr__(self) -> str:
        return self._edit_command_repr(["classes"])


class AppendExternalTree(AppendText):
    def __init__(self, root: nodes.Node):
        super().__init__()
        self.root = root

    def make_text(self) -> str:
        return Translator(quiet=True).translate(self.root)


class EditCommandBatch(EditCommand):
    def __init__(self, items: Iterable):
        self.items = list(items)

    def __len__(self) -> int:
        return len(self.items)

    def __repr__(self) -> str:
        classname = self.__class__.__name__
        return f"{classname}({repr(self.items)})"

    def make_text(self) -> str:
        raise RSMTranslatorError("Why are we here?")


class AppendBatchAndDefer(EditCommandBatch):
    defers = True

    def execute(self, translator: "Translator") -> None:
        deferred: list[EditCommand] = []
        for item in self.items:
            if isinstance(item, AppendTextAndDefer):
                deferred.append(AppendText(item.make_deferred_text()))
            AppendText(item.make_text()).execute(translator)

        batch = AppendBatch(reversed(deferred))
        translator.deferred.append(batch)


class AppendBatch(EditCommandBatch):
    def execute(self, translator: "Translator") -> None:
        for item in self.items:
            item.execute(translator)


class Translator:
    """Translate an abstract syntax tree into HTML.

    Examples
    --------
    This is an example doctest.

    >>> [1, 2, 3]
    [1, 2, 3]

    """

    class Action(namedtuple("Action", "node action method")):
        def __repr__(self) -> str:
            classname = self.node.__class__.__name__
            return f'Action(node={classname}(), action="{self.action}")'

    def __init__(self, quiet: bool = False):
        self.tree: nodes.Manuscript = None
        self.body: str = ""
        self.deferred: list[EditCommand] = []
        self.quiet = quiet

    @classmethod
    def get_action_method(cls, node: nodes.Node, action: str) -> Callable:
        ogclass = node.__class__
        nodeclass = node.__class__
        method = f"{action}_{nodeclass.__name__.lower()}"
        while not hasattr(cls, method):
            nodeclass = nodeclass.__bases__[0]
            method = f"{action}_{nodeclass.__name__.lower()}"
        if action == "visit" and ogclass is not nodeclass:
            logger.debug(f"Using {method} for node of class {ogclass}")
        return getattr(cls, method)

    def push_visit(self, stack: list[Action], node: nodes.Node) -> None:
        stack.append(self.Action(node, "visit", self.get_action_method(node, "visit")))

    def push_leave(self, stack: list[Action], node: nodes.Node) -> None:
        stack.append(self.Action(node, "leave", self.get_action_method(node, "leave")))

    def translate(self, tree: nodes.Manuscript, new: bool = True) -> str:
        if not self.quiet:
            logger.info("Translating...")
        if new:
            self.body = ""
        self.tree = tree

        if self.deferred:
            raise RSMTranslatorError("Something went wrong")

        stack: list[Translator.Action] = []
        self.push_visit(stack, tree)
        while stack:
            node, action, method = stack.pop()
            command = method(self, node)
            if action == "visit":
                if command.defers:
                    self.push_leave(stack, node)
                for child in reversed(node.children):
                    self.push_visit(stack, child)
            command.execute(self)

        if self.deferred:
            raise RSMTranslatorError("Something went wrong")

        return self.body

    def visit_node(self, node: nodes.Node) -> EditCommand:
        return AppendBatchAndDefer(
            [
                AppendOpenTag(classes=["node-with-no-class"]),
                AppendText(str(node) + "\n"),
            ]
        )

    def leave_node(self, node: nodes.Node) -> EditCommand:
        try:
            return self.deferred.pop()
        except IndexError as ex:
            raise RSMTranslatorError(
                "Cannot finish translation; did you forget to write "
                "a visit_* or leave_* method?"
            ) from ex

    def visit_manuscript(self, node: nodes.Manuscript) -> EditCommand:
        batch = AppendBatchAndDefer(
            [
                AppendOpenTag("body"),
                AppendOpenTag(classes=["manuscriptwrapper"]),
                AppendNodeTag(node),
                AppendOpenTag("section", classes=["level-1"]),
            ]
        )
        if node.title:
            batch.items.append(AppendHeading(1, node.title))
        return batch

    def visit_author(self, node: nodes.Author) -> EditCommand:
        if [node.name, node.affiliation, node.email]:
            if node.email:
                email = (
                    _make_tag("a", id_="", classes="", href=f"mailto:{node.email}")
                    + node.email
                    + "</a>"
                )
            else:
                email = ""
            return AppendBatchAndDefer(
                [
                    AppendNodeTag(node),
                    *[
                        AppendParagraph(str(x))
                        for x in [node.name, node.affiliation, email]
                        if x
                    ],
                ]
            )
        else:
            return AppendNodeTag(node)

    def visit_abstract(self, node: nodes.Abstract) -> EditCommand:
        return AppendBatchAndDefer(
            [
                AppendNodeTag(node),
                AppendHeading(3, "Abstract"),
            ]
        )

    def leave_abstract(self, node: nodes.Abstract) -> EditCommand:
        batch = AppendBatch([])

        if node.keywords:
            text = ", ".join(node.keywords)
            batch.items.append(
                AppendParagraph(f"Keywords: {text}", classes=["keywords"])
            )
        if node.msc:
            text = ", ".join(node.msc)
            batch.items.append(AppendParagraph(f"MSC: {text}", classes=["msc"]))

        # For documentation: if a visit_* method returns a command with defers = True,
        # then the corresponding leave_* method MUST MUST MUST call leave_node(node) and
        # add it to the returned batch!!!
        batch.items.append(self.leave_node(node))
        return batch

    def visit_paragraph(self, node: nodes.Paragraph) -> EditCommand:
        return AppendNodeTag(node, tag="p", newline_inner=False)

    def visit_step(self, node: nodes.Step) -> EditCommand:
        return AppendNodeTag(node)

    def visit_section(self, node: nodes.Section) -> EditCommand:
        node.types.insert(0, f"level-{node.level}")
        heading = (
            f"{node.full_number}. {node.title}" if not node.nonum else f"{node.title}"
        )
        return AppendBatchAndDefer(
            [
                AppendNodeTag(node, "section"),
                AppendHeading(node.level, heading),
            ]
        )

    def visit_enumerate(self, node: nodes.Enumerate) -> EditCommand:
        return AppendNodeTag(node, "ol")

    def visit_itemize(self, node: nodes.Itemize) -> EditCommand:
        return AppendNodeTag(node, "ul")

    def visit_item(self, node: nodes.Item) -> EditCommand:
        return AppendNodeTag(node, "li")

    def visit_contents(self, node: nodes.Contents) -> EditCommand:
        return AppendBatchAndDefer(
            [
                AppendOpenTag(classes=["toc"]),
                AppendHeading(3, "Table of Contents"),
                AppendNodeTag(node, "ul"),
            ]
        )

    def visit_note(self, node: nodes.Note) -> EditCommand:
        return AppendBatchAndDefer(
            [
                AppendOpenTag("span", classes=["note"]),
                AppendOpenCloseTag(
                    "sup",
                    content=f'<a class="note__link">{node.full_number}</a>',
                    classes=["note__number"],
                    newline_inner=False,
                ),
                AppendOpenTag(
                    "span",
                    id=node.label,
                    classes=["note__content"],
                    newline_inner=False,
                ),
            ]
        )

    def visit_math(self, node: nodes.Math) -> EditCommand:
        # the strings r'\(' and r'\)' are MathJax's delimiters for inline math
        return AppendBatchAndDefer(
            [
                AppendNodeTag(node, "span", newline_inner=False, newline_outer=False),
                AppendTextAndDefer(r"\(", r"\)"),
            ]
        )

    def visit_mathblock(self, node: nodes.MathBlock) -> EditCommand:
        # the strings '$$' and '$$' are MathJax's delimiters for inline math
        return AppendBatchAndDefer(
            [
                AppendNodeTag(node, "div"),
                AppendTextAndDefer("$$\n", "\n$$"),
            ]
        )

    def leave_mathblock(self, node: nodes.MathBlock) -> EditCommand:
        # For documentation: if a visit_* method returns a command with defers = True,
        # then the corresponding leave_* method MUST MUST MUST call leave_node(node) and
        # add it to the returned batch!!!
        if node.nonum:
            return self.leave_node(node)

        batch = self.leave_node(node)
        batch.items.insert(
            1,
            AppendOpenCloseTag(
                content=f"({node.full_number})",
                classes=["mathblock__number"],
                newline_inner=False,
            ),
        )
        batch = AppendBatch(batch.items)
        return batch

    def visit_sourcecode(self, node: nodes.SourceCode) -> EditCommand:
        classes = []
        if node.lang:
            classes = ["highlight", node.lang]
            code = highlight_code(node.text, node.lang)
        else:
            code = node.text
        return AppendBatchAndDefer(
            [
                AppendOpenTag(
                    "code",
                    classes=classes,
                    newline_outer=False,
                    newline_inner=False,
                ),
                AppendText(code),
            ]
        )

    def visit_code(self, node: nodes.Code) -> EditCommand:
        return AppendNodeTag(node, tag="span", newline_inner=False)

    def visit_codeblock(self, node: nodes.CodeBlock) -> EditCommand:
        return AppendBatchAndDefer(
            [
                AppendNodeTag(node, "div", newline_inner=True, newline_outer=True),
                AppendOpenTag("pre"),
            ]
        )

    def visit_algorithm(self, node: nodes.Algorithm) -> EditCommand:
        return AppendBatchAndDefer(
            [
                AppendOpenTag(id=node.label, classes=["algorithm"]),
                AppendOpenTag("pre", classes=["pseudocode"]),
            ]
        )

    def visit_text(self, node: nodes.Text) -> EditCommand:
        return AppendText(node.text)

    def visit_error(self, node: nodes.Error) -> EditCommand:
        return AppendBatchAndDefer(
            [
                AppendNodeTag(node, "span", newline_inner=False, newline_outer=False),
                AppendText(node.text),
            ]
        )

    def visit_span(self, node: nodes.Span) -> EditCommand:
        commands = [
            AppendOpenTag(tag, newline_inner=False, newline_outer=False)
            for attr, tag in nodes.Span.attr_to_tag.items()
            if getattr(node, attr)
        ]
        return AppendBatchAndDefer(
            [
                AppendNodeTag(
                    node, tag="span", newline_inner=False, newline_outer=False
                ),
                *commands,
            ]
        )

    def visit_construct(self, node: nodes.Construct) -> EditCommand:
        return AppendNodeTag(node, tag="span", newline_inner=False, newline_outer=False)

    def _make_ahref_tag_text(
        self,
        node: nodes.BaseReference,
        target: nodes.Node,
        href_text: str,
        label: str = "",
        id_: str = "",
    ) -> str:
        if not target:
            raise RSMTranslatorError(f"Found a {node.__class__} without a target")
        tgt = target
        if hasattr(node, "overwrite_reftext") and node.overwrite_reftext:
            reftext = node.overwrite_reftext
        else:
            reftext = getattr(tgt, "reftext", tgt)
        classes = node.types
        if not isinstance(node, nodes.URL) and "reference" not in classes:
            classes.insert(0, "reference")
        tag = (
            _make_tag("a", id_=id_, classes=classes, href=href_text) + reftext + "</a>"
        )
        return tag

    def visit_reference(self, node: nodes.Reference) -> EditCommand:
        return AppendText(
            self._make_ahref_tag_text(node, node.target, f"#{node.target.label}")
        )

    def visit_url(self, node: nodes.URL) -> EditCommand:
        return AppendText(
            self._make_ahref_tag_text(node, node.target, f"{node.target}")
        )

    def visit_claimblock(self, node: nodes.ClaimBlock) -> EditCommand:
        return AppendNodeTag(node)

    def _make_title_node(
        self, text: str, types: list, paragraph: bool = True
    ) -> nodes.Node:
        if paragraph:
            para = nodes.Paragraph(types=types)
        span = nodes.Span(strong=True)
        text = nodes.Text(text=text)
        span.append(text)
        if paragraph:
            para.append(span)
            return para
        else:
            return span

    def visit_theorem(self, node: nodes.Theorem) -> EditCommand:
        classname = node.__class__.__name__.lower()
        title = self._make_title_node(
            f"{classname.capitalize()}"
            + (f" {node.full_number}" if not node.nonum and node.number else "")
            + (f": {node.title}." if node.title else "."),
            ["theorem__title", f"{classname}__title"],
        )
        classes = ["theorem-contents"]
        if classname != "theorem":
            classes.append(f"{classname}-contents")
        return AppendBatchAndDefer(
            [
                AppendNodeTag(node, additional_classes=["theorem"]),
                AppendOpenTag(classes=classes),
                AppendExternalTree(title),
            ]
        )

    def visit_statement(self, node: nodes.Statement) -> EditCommand:
        return AppendNodeTag(node)

    def visit_subproof(self, node: nodes.Subproof) -> EditCommand:
        classname = node.__class__.__name__.lower()
        return AppendBatchAndDefer(
            [
                AppendNodeTag(node),
                AppendOpenTag(classes=[f"{classname}-contents"]),
            ]
        )

    def visit_proof(self, node: nodes.Proof) -> EditCommandBatch:
        last = node.last_of_type(nodes.Step)
        if last:
            last.types.append("last")

        classname = node.__class__.__name__.lower()
        title = self._make_title_node(
            f"{classname.capitalize()}. ", [f"{classname}__title"]
        )
        return AppendBatchAndDefer(
            [
                AppendNodeTag(node),
                AppendExternalTree(title),
                AppendOpenTag(classes=[f"{classname}-contents"]),
            ]
        )

    def visit_sketch(self, node: nodes.Sketch) -> EditCommand:
        return AppendNodeTag(node)

    def leave_proof(self, node: nodes.Proof) -> EditCommand:
        # For documentation: if a visit_* method returns a command with defers = True,
        # then the corresponding leave_* method MUST MUST MUST call leave_node(node) and
        # add it to the returned batch!!!
        batch = self.leave_node(node)
        batch.items.insert(1, AppendHalmos())
        batch = AppendBatch(batch.items)
        return batch

    def visit_cite(self, node: nodes.Cite) -> EditCommand:
        if len(node.targets) == 1:
            t = node.targets[0]
            text = self._make_ahref_tag_text(node, t, f"#{t.label}", id_=node.label)
        else:
            tags = [
                self._make_ahref_tag_text(
                    node, t, f"#{t.label}", id_=f"{node.label}-{idx}"
                )
                for idx, t in enumerate(node.targets)
            ]
            text = ", ".join(tags)
            text = f'<span id="{node.label}">{text}</span>'
        return AppendText(f"[{text}]")

    def visit_bibliography(self, node: nodes.Bibliography) -> EditCommand:
        return AppendBatchAndDefer(
            [
                AppendOpenTag("section", classes=["level-2"]),
                AppendHeading(2, "References"),
                AppendNodeTag(node, "ol"),
            ]
        )

    def visit_bibitem(self, node: nodes.Bibitem) -> EditCommand:
        items = [node.author, f'"{node.title}"']
        if node.kind == "article":
            if node.journal:
                items.append(node.journal)
            else:
                logger.warning(f"Bibitem {node.label} has no journal")
        elif node.kind == "book":
            if node.publisher:
                items.append(node.publisher)
            else:
                logger.warning(f"Bibitem {node.label} has no publisher")
        if node.year:
            items.append(node.year)
        else:
            logger.warning(f"Bibitem {node.label} has no year")
        text = ". ".join([i.strip(".") for i in items]) + "."
        if node.doi:
            a_tag = _make_tag(
                "a",
                id_=f"{node.label}-doi",
                classes=["bibitem-doi"],
                href=f"https://doi.org/{node.doi}",
                target="_blank",
            )
            text = f"{text} {a_tag}[link]</a>"
        else:
            logger.warning(f"Bibitem {node.label} has no DOI")

        if node.backlinks:
            text += "<br />"
            backs = [
                _make_tag(
                    "a",
                    id_="",
                    classes=["reference", "backlink"],
                    href=f"#{link_lbl}",
                )
                + f"^{idx}"
                + "</a>"
                for idx, link_lbl in enumerate(node.backlinks, start=1)
            ]
            text += "[" + ",".join(backs) + "]"

        return AppendBatchAndDefer([AppendNodeTag(node, "li"), AppendText(text)])

    def visit_draft(self, node: nodes.Draft) -> EditCommand:
        return AppendBatchAndDefer(
            [AppendNodeTag(node, "span"), AppendTextAndDefer("[ ", " ]")]
        )

    def visit_figure(self, node: nodes.Figure) -> EditCommand:
        return AppendBatchAndDefer(
            [
                AppendNodeTag(node, "figure"),
                AppendText(
                    _make_tag(
                        "img",
                        id_=node.label,
                        classes=[],
                        src=node.path,
                        alt=f"{node.__class__.__name__} {node.full_number}.",
                        onload=""
                        if node.scale == 1.0
                        else f"this.width*={node.scale};",
                    )
                ),
            ]
        )

    def visit_caption(self, node: nodes.Caption) -> EditCommand:
        parent = node.parent
        title = self._make_title_node(
            f"{parent.__class__.__name__} {parent.full_number}. ",
            types=[],
            paragraph=False,
        )
        return AppendBatchAndDefer(
            [
                AppendOpenTag(
                    "figcaption" if isinstance(parent, nodes.Figure) else "caption"
                ),
                AppendExternalTree(title),
            ]
        )

    def visit_appendix(self, node: nodes.Appendix) -> EditCommand:
        # Appendix nodes are used during the transform phase, but do not apear in the
        # output in any way.
        return AppendText("")

    def visit_table(self, node: nodes.Table) -> EditCommand:
        return AppendNodeTag(node, "table")

    def visit_tablehead(self, node: nodes.TableHead) -> EditCommand:
        return AppendNodeTag(node, "thead")

    def visit_tablebody(self, node: nodes.TableBody) -> EditCommand:
        return AppendNodeTag(node, "tbody")

    def visit_tablerow(self, node: nodes.TableRow) -> EditCommand:
        return AppendNodeTag(node, "tr")

    def visit_tabledatum(self, node: nodes.TableDatum) -> EditCommand:
        return AppendNodeTag(node, "td", newline_inner=False)


class HandrailsTranslator(Translator):

    svg = {
        "rarrow": """<svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-chevron-right" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
        <polyline points="9 6 15 12 9 18"></polyline>
        </svg>""",
        "vdots": """<svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-dots-vertical" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
        <circle cx="12" cy="12" r="1"></circle>
        <circle cx="12" cy="19" r="1"></circle>
        <circle cx="12" cy="5" r="1"></circle>
        </svg>""",
        "link": """<svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-link" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
        <path d="M10 14a3.5 3.5 0 0 0 5 0l4 -4a3.5 3.5 0 0 0 -5 -5l-.5 .5"></path>
        <path d="M14 10a3.5 3.5 0 0 0 -5 0l-4 4a3.5 3.5 0 0 0 5 5l.5 -.5"></path>
        </svg>""",
        "tree": """<svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-binary-tree" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
        <path d="M6 20a2 2 0 1 0 -4 0a2 2 0 0 0 4 0z"></path>
        <path d="M16 4a2 2 0 1 0 -4 0a2 2 0 0 0 4 0z"></path>
        <path d="M16 20a2 2 0 1 0 -4 0a2 2 0 0 0 4 0z"></path>
        <path d="M11 12a2 2 0 1 0 -4 0a2 2 0 0 0 4 0z"></path>
        <path d="M21 12a2 2 0 1 0 -4 0a2 2 0 0 0 4 0z"></path>
        <path d="M5.058 18.306l2.88 -4.606"></path>
        <path d="M10.061 10.303l2.877 -4.604"></path>
        <path d="M10.065 13.705l2.876 4.6"></path>
        <path d="M15.063 5.7l2.881 4.61"></path>
        </svg>""",
        "source": """<svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-source-code" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
        <path d="M14.5 4h2.5a3 3 0 0 1 3 3v10a3 3 0 0 1 -3 3h-10a3 3 0 0 1 -3 -3v-5"></path>
        <path d="M6 5l-2 2l2 2"></path>
        <path d="M10 9l2 -2l-2 -2"></path>
        </svg>""",
        "vars": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-tabler icons-tabler-outline icon-tabler-variable">
        <path stroke="none" d="M0 0h24v24H0z" fill="none" />
        <path d="M5 4c-2.5 5 -2.5 10 0 16m14 -16c2.5 5 2.5 10 0 16m-10 -11h1c1 0 1 1 2.016 3.527c.984 2.473 .984 3.473 1.984 3.473h1" />
        <path d="M8 16c1.5 0 3 -2 4 -3.5s2.5 -3.5 4 -3.5" />
        </svg>""",
        "widen": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-tabler icons-tabler-outline icon-tabler-viewport-wide">
        <path stroke="none" d="M0 0h24v24H0z" fill="none" />
        <path d="M10 12h-7l3 -3m0 6l-3 -3" />
        <path d="M14 12h7l-3 -3m0 6l3 -3" />
        <path d="M3 6v-3h18v3" />
        <path d="M3 18v3h18v-3" />
        </svg>""",
        "narrow": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-tabler icons-tabler-outline icon-tabler-viewport-narrow">
        <path stroke="none" d="M0 0h24v24H0z" fill="none" />
        <path d="M3 12h7l-3 -3m0 6l3 -3" />
        <path d="M21 12h-7l3 -3m0 6l-3 -3" />
        <path d="M9 6v-3h6v3" />
        <path d="M9 18v3h6v-3" />
        </svg>
        """,
    }

    def __init__(
        self,
        quiet: bool = False,
        hidden_handrails: bool = True,
        sidebar: bool = True,
        add_source: bool = True,
    ):
        super().__init__(quiet)
        self.hidden_handrails = hidden_handrails
        self.sidebar = sidebar
        self.add_source = add_source

    @staticmethod
    def _make_option_tag(name: str, svg: str) -> AppendOpenCloseTag:
        return AppendOpenCloseTag(
            "span",
            svg,
            classes=["option", f"option__{name}"],
            newline_inner=False,
        )

    def _replace_items_with_handrails(self, index, items, cls, include_content=False):
        classes = ["handrail", "handrail--offset"]
        if include_content:
            handrail = AppendOpenTag(classes=classes, is_selectable=True)
        else:
            handrail = AppendOpenTagManualClose(classes=classes, is_selectable=True)
        btn_cont = AppendOpenTagManualClose(classes=["handrail__btn-container"])
        btn_togg = AppendOpenTagManualClose(
            classes=["handrail__btn", "handrail__btn-toggle"], newline_inner=False
        )
        btn_menu = AppendOpenTagManualClose(
            classes=["handrail__btn", "handrail__btn-menu", "handrail__btn--relative"],
            newline_inner=False,
        )
        opt_tag = AppendOpenTagManualClose(
            classes=["options", "hide"], newline_inner=True, newline_outer=True
        )
        options = [
            self._make_option_tag(opt, self.svg[opt])
            for opt in ["link", "tree", "source"]
        ]
        newitems = [
            handrail,
            btn_cont,
            # btn_togg,
            # AppendOpenCloseTag(
            #     "span",
            #     # self.svg["rarrow"],
            #     newline_inner=False,
            #     newline_outer=False,
            # ),
            # btn_togg.close_command(),
            btn_menu,
            AppendOpenCloseTag(
                "span",
                self.svg["vdots"],
                newline_inner=False,
                newline_outer=False,
            ),
            opt_tag,
            *options,
            opt_tag.close_command(),
            btn_menu.close_command(),
            btn_cont.close_command(),
            items[index],
        ]
        if not include_content:
            newitems.append(handrail.close_command())
        # else:
        #    nothing to do here since when include_content is True, handrail will defer
        #    its close command
        newitems = items[:index] + newitems + items[index + 1 :]
        return cls(newitems)

    def _replace_batch_with_handrails(self, index, batch, include_content=False):
        return self._replace_items_with_handrails(
            index, batch.items, batch.__class__, include_content
        )

    def _replace_cmd_with_handrails(self, cmd, include_content=False):
        return self._replace_items_with_handrails(
            0, [cmd], AppendBatchAndDefer, include_content
        )

    def _make_tools_sidebar(self):
        html = f"""
        <div class="tools-sidebar">
          <div class="tools-sidebar__btn">{self.svg["vars"]}</div>
          <div class="vars-list hide"><ul class="vars-list-ul"><li>Nothing here...</li></ul></div>
        </div>
        """
        return AppendText(text=html)

    def _make_source_div(self):
        return AppendText(text=f'<div class="rsm-source hide">{self.tree.src}</div>')

    def visit_manuscript(self, node: nodes.Manuscript) -> EditCommand:
        batch = super().visit_manuscript(node)
        if node.title:
            batch = self._replace_batch_with_handrails(4, batch)
        if self.sidebar:
            batch.items.insert(2, self._make_tools_sidebar())
        if self.add_source:
            batch.items.insert(1, self._make_source_div())
        return batch

    def visit_section(self, node: nodes.Section) -> EditCommand:
        batch = super().visit_section(node)
        return self._replace_batch_with_handrails(1, batch)

    def visit_abstract(self, node: nodes.Abstract) -> EditCommand:
        batch = super().visit_abstract(node)
        return self._replace_batch_with_handrails(1, batch)

    def visit_contents(self, node: nodes.Contents) -> EditCommand:
        batch = super().visit_contents(node)
        return self._replace_batch_with_handrails(1, batch)

    def visit_bibliography(self, node: nodes.Bibliography) -> EditCommand:
        batch = super().visit_bibliography(node)
        return self._replace_batch_with_handrails(1, batch)

    def visit_paragraph(self, node: nodes.Paragraph) -> EditCommand:
        cmd = super().visit_paragraph(node)
        if self.hidden_handrails:
            batch = self._replace_cmd_with_handrails(cmd, include_content=True)
            batch.items[0].classes.append("handrail--hide")
            return batch
        else:
            return cmd

    def visit_theorem(self, node: nodes.Theorem) -> EditCommand:
        batch = super().visit_theorem(node)
        batch.items[1].classes.append("handrail__collapsible")
        batch = self._replace_batch_with_handrails(1, batch, include_content=True)
        batch.items[1].classes += [
            f"stars-{node.stars}",
            f"clocks-{node.clocks}",
        ]
        batch.items[-1].root.types.append("do-not-hide")
        return batch

    def visit_proof(self, node: nodes.Proof) -> EditCommand:
        batch = super().visit_proof(node)
        batch.items[2].classes.append("handrail__collapsible")

        # the last element is the proof title, we pop it as it will be inserted into the
        # proof header div
        tree = batch.items[1]
        batch.items = [batch.items[0], batch.items[2]]
        tree.root.types.append("do-not-hide")

        if any(type(c) is nodes.Sketch for c in node.children):
            self._add_proof_header_with_sketch(batch, tree)
            for c in node.children:
                if type(c) is not nodes.Sketch:
                    c.types.append("hide")
        else:
            self._add_proof_header_sans_sketch(batch, tree)
        return self._replace_batch_with_handrails(1, batch, include_content=True)

    def _add_proof_header_with_sketch(
        self, batch: EditCommandBatch, tree: nodes.Node
    ) -> None:
        header = AppendOpenTagManualClose(classes=["proof__header"])
        tabs = AppendOpenTagManualClose(classes=["proof__tabs"])
        batch.items[1:1] = [
            header,
            tree,
            tabs,
            AppendOpenCloseTag(
                "button",
                content="sketch",
                classes=["sketch", "active"],
                newline_inner=False,
            ),
            AppendOpenCloseTag(
                "button", content="full", classes=["full"], newline_inner=False
            ),
            tabs.close_command(),
            header.close_command(),
        ]

    def _add_proof_header_sans_sketch(
        self, batch: EditCommandBatch, tree: nodes.Node
    ) -> None:
        header = AppendOpenTagManualClose(classes=["proof__header"])
        batch.items[1:1] = [header, tree, header.close_command()]

    def visit_subproof(self, node: nodes.Subproof) -> EditCommand:
        batch = super().visit_subproof(node)
        batch.items[1].classes += ["handrail", "handrail--hug", "handrail__collapsible"]
        return batch

    def visit_step(self, node: nodes.Step) -> EditCommand:
        cmd = super().visit_step(node)
        batch = self._replace_cmd_with_handrails(cmd, include_content=True)
        batch.items[0].classes.append("handrail__collapsible")
        batch.items.insert(
            -1,
            AppendOpenCloseTag(
                classes=["step__number"],
                content=f"({node.full_number})",
                newline_inner=False,
                newline_outer=False,
            ),
        )
        return batch

    def leave_step(self, node: nodes.Step) -> EditCommand:
        # For documentation: if a visit_* method returns a command with defers = True,
        # then the corresponding leave_* method MUST MUST MUST call leave_node(node) and
        # add it to the returned batch!!!
        batch = self.leave_node(node)
        batch.items.insert(1, AppendHalmos(classes=["hide"]))
        batch = AppendBatch(batch.items)
        return batch

    def visit_mathblock(self, node: nodes.MathBlock) -> EditCommand:
        batch = super().visit_mathblock(node)
        if node.nonum:
            return batch

        batch.items.insert(
            -1,
            AppendOpenCloseTag(
                content=f"({node.full_number})",
                classes=["mathblock__number mathblock__number--phantom"],
                newline_inner=False,
            ),
        )
        return batch
