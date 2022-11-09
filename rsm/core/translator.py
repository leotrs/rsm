"""
translator.py
-------------

RSM Translator: take a Manuscript and return a HTML string.

"""

import logging

logger = logging.getLogger('RSM').getChild('Translator')

from typing import Iterable, Callable
from collections import namedtuple
from abc import ABC, abstractmethod
from typing import Iterable
from icecream import ic

from . import nodes
from .manuscript import AbstractTreeManuscript, HTMLManuscript
from .util import ShortenedString


class RSMTranslatorError(Exception):
    pass


def make_tag(tag: str, id_: str, classes: Iterable) -> str:
    text = f'<{tag}'
    if id_:
        text += f' id="{id_}"'
    if classes:
        classes = ' '.join(classes)
        text += f' class="{classes}"'
    text += '>'
    return text


# FOR DOCUMENTATION: Classes that inherit from EditCommand are meant to encapsulate
# _reusable_ operations that convert a node into HTML text.  If an operation is not
# reusable on multiple node classes and is particular to just one node class, it should
# go into the visit_* method corresponding to that class.
class EditCommand(ABC):
    defers = False

    @abstractmethod
    def execute(self, translator: 'Translator') -> None:
        pass

    def _edit_command_repr(self, members: Iterable[str]) -> str:
        start = f'{self.__class__.__name__}('
        middles = []
        for key in members:
            s = f'{key}='
            value = getattr(self, key)
            if isinstance(value, str):
                value = repr(ShortenedString(value.strip()))
            s += f'{value}'
            middles.append(s)
        middle = ', '.join(middles)
        end = ')'
        return start + middle + end

    def __repr__(self) -> str:
        return self._edit_command_repr([])


class AppendTextAndDefer(EditCommand):
    defers = True

    def __init__(self, text: str, deferred_text: str):
        self.text = text
        self.deferred_text = deferred_text

    def __repr__(self) -> str:
        return self._edit_command_repr(['text', 'deferred_text'])

    def execute(self, translator: 'Translator') -> None:
        translator.body += self.text
        translator.deferred.append(AppendText(self.deferred_text))


class AppendText(EditCommand):
    def __init__(self, text: str):
        self.text = text

    def __repr__(self) -> str:
        return self._edit_command_repr(['text'])

    def execute(self, translator: 'Translator') -> None:
        translator.body += self.text


class AppendOpenCloseTag(AppendText):
    def __init__(
        self,
        tag: str = 'div',
        content: str = '',
        *,
        id: str = '',
        classes: list = None,
        newline_inner: bool = True,
        newline_outer: bool = True,
    ):
        self.tag = tag
        self.content = content
        self.id = id
        self.classes = classes if classes else []
        text = (
            ('\n' if newline_outer else '')
            + make_tag(self.tag, self.id, self.classes)
            + ('\n' if newline_inner else '')
            + self.content
            + ('\n' if newline_inner else '')
            + f'</{self.tag}>'
            + ('\n' if newline_outer else '')
        )
        super().__init__(text)

    def __repr__(self) -> str:
        return self._edit_command_repr(['tag', 'content', 'id', 'classes'])


class AppendOpenTagNoDefer(AppendText):
    def __init__(
        self,
        tag: str = 'div',
        content: str = '',
        *,
        id: str = '',
        classes: list = None,
        newline_inner: bool = True,
        newline_outer: bool = True,
    ):
        self.tag = tag
        self.content = content
        self.id = id
        self.classes = classes if classes else []
        self.newline_inner = newline_inner
        self.newline_outer = newline_outer
        text = (
            ('\n' if newline_outer else '')
            + make_tag(self.tag, self.id, self.classes)
            + ('\n' if newline_inner else '')
            + self.content
        )
        super().__init__(text)

    def __repr__(self) -> str:
        return self._edit_command_repr(['tag', 'content', 'id', 'classes'])

    def close_command(self):
        return AppendText(
            ('\n' if self.newline_inner else '')
            + f'</{self.tag}>'
            + ('\n' if self.newline_outer else '')
        )


class AppendOpenTag(AppendTextAndDefer):
    def __init__(
        self,
        tag: str = 'div',
        *,
        id: str = '',
        classes: list = None,
        newline_inner: bool = True,
        newline_outer: bool = True,
    ):
        self.tag = tag
        self.id = id
        self.classes = classes if classes else []
        text = (
            ('\n' if newline_outer else '')
            + make_tag(self.tag, self.id, self.classes)
            + ('\n' if newline_inner else '')
        )
        deferred_text = (
            ('\n' if newline_inner else '')
            + f'</{self.tag}>'
            + ('\n' if newline_outer else '')
        )
        super().__init__(text, deferred_text)

    def __repr__(self) -> str:
        return self._edit_command_repr(['tag', 'id', 'classes', 'newline_inner'])


class AppendNodeTag(AppendOpenTag):
    def __init__(
        self,
        node: nodes.Node,
        tag: str = 'div',
        *,
        newline_inner: bool = True,
        newline_outer: bool = True,
    ):
        self.node = node
        classes = [node.__class__.__name__.lower()] + [str(t) for t in node.types]
        super().__init__(
            tag=tag,
            id=node.label,
            classes=classes,
            newline_inner=newline_inner,
            newline_outer=newline_outer,
        )

    def __repr__(self) -> str:
        return self._edit_command_repr(['tag', 'node'])


class AppendParagraph(AppendOpenCloseTag):
    def __init__(
        self,
        content: str = '',
        *,
        id: str = '',
        classes: list = None,
        newline_inner: bool = False,
        newline_outer: bool = True,
    ):
        super().__init__(
            tag='p',
            content=content,
            id=id,
            classes=classes,
            newline_inner=newline_inner,
            newline_outer=newline_outer,
        )

    def __repr__(self) -> str:
        return self._edit_command_repr(['content', 'id', 'classes'])


class AppendHeading(AppendOpenCloseTag):
    def __init__(
        self,
        level: int,
        content: str = '',
        *,
        id: str = '',
        classes: list = None,
        newline_inner: bool = False,
        newline_outer: bool = True,
    ):
        self.level = level
        super().__init__(
            tag=f'h{self.level}',
            content=content,
            id=id,
            classes=classes,
            newline_inner=newline_inner,
            newline_outer=newline_outer,
        )

    def __repr__(self) -> str:
        return self._edit_command_repr(['level', 'content', 'id', 'classes'])


class AppendTombstone(AppendOpenCloseTag):
    def __init__(
        self,
        *,
        id: str = '',
        classes: list = None,
    ):
        super().__init__(
            tag='div',
            content='',
            id=id,
            classes=['tombstone'],
            newline_inner=False,
            newline_outer=True,
        )

    def __repr__(self) -> str:
        return self._edit_command_repr(['classes'])


class EditCommandBatch(EditCommand):
    def __init__(self, items: Iterable):
        self.items = list(items)

    def __len__(self) -> int:
        return len(self.items)

    def __repr__(self) -> str:
        classname = self.__class__.__name__
        return f'{classname}({repr(self.items)})'


class AppendBatchAndDefer(EditCommandBatch):
    defers = True

    def execute(self, translator: 'Translator') -> None:
        deferred: list[EditCommand] = []
        for item in self.items:
            if isinstance(item, AppendTextAndDefer):
                deferred.append(AppendText(item.deferred_text))
            AppendText(item.text).execute(translator)

        batch = AppendBatch(reversed(deferred))
        translator.deferred.append(batch)


class AppendBatch(EditCommandBatch):
    def execute(self, translator: 'Translator') -> None:
        for item in self.items:
            item.execute(translator)


class Action(namedtuple('Action', 'node action method')):
    def __repr__(self) -> str:
        classname = self.node.__class__.__name__
        return f'Action(node={classname}(), action="{self.action}")'


class Translator:
    def __init__(self):
        self.tree: AbstractTreeManuscript = None
        self.body: HTMLManuscript = ''
        self.deferred: list[EditCommand] = []

    @classmethod
    def get_action_method(cls, node: nodes.Node, action: str) -> Callable:
        ogclass = node.__class__
        nodeclass = node.__class__
        method = f'{action}_{nodeclass.__name__.lower()}'
        while not hasattr(cls, method):
            nodeclass = nodeclass.__bases__[0]
            method = f'{action}_{nodeclass.__name__.lower()}'
        if action == 'visit' and ogclass is not nodeclass:
            logger.debug(f'Using {method} for node of class {ogclass}')
        return getattr(cls, method)

    def push_visit(self, stack, node: nodes.Node) -> None:
        stack.append(Action(node, 'visit', self.get_action_method(node, 'visit')))

    def push_leave(self, stack, node: nodes.Node) -> None:
        stack.append(Action(node, 'leave', self.get_action_method(node, 'leave')))

    def translate(self, tree: AbstractTreeManuscript) -> HTMLManuscript:
        logger.info('Translating...')
        # ic.enable()
        self.tree = tree

        if self.deferred:
            raise RSMTranslatorError('Something went wrong')

        stack = []
        self.push_visit(stack, tree)
        while stack:
            node, action, method = stack.pop()
            command = method(self, node)
            if action == 'visit':
                if command.defers:
                    self.push_leave(stack, node)
                for child in reversed(node.children):
                    self.push_visit(stack, child)
            command.execute(self)

        if self.deferred:
            raise RSMTranslatorError('Something went wrong')

        return self.body

    def visit_node(self, node: nodes.Node) -> EditCommand:
        return AppendText(str(node) + '\n')

    def leave_node(self, node: nodes.Node) -> EditCommand:
        try:
            return self.deferred.pop()
        except IndexError as e:
            classname = node.__class__.__name__
            raise RSMTranslatorError(
                'Cannot finish translation; did you forget to write '
                'a visit_* or leave_* method?'
            ) from e

    def visit_manuscript(self, node: nodes.Manuscript) -> EditCommand:
        if not node.label:
            node.label = 'manuscript'
        return AppendBatchAndDefer(
            [
                AppendOpenTag('body'),
                AppendOpenTag(classes=['manuscriptwrapper']),
                AppendNodeTag(node),
                AppendOpenTag('section', classes=['level-1']),
                AppendHeading(1, node.title),
            ]
        )

    def visit_author(self, node: nodes.Author) -> EditCommand:
        lines = [str(x) for x in [node.name, node.affiliation, node.email] if x]
        line = '\n'.join(lines)
        if line:
            return AppendBatchAndDefer([AppendNodeTag(node), AppendParagraph(line)])
        else:
            return AppendNodeTag(node)

    def visit_abstract(self, node: nodes.Abstract) -> EditCommand:
        return AppendBatchAndDefer(
            [
                AppendNodeTag(node),
                AppendHeading(3, 'Abstract'),
            ]
        )

    def leave_abstract(self, node: nodes.Abstract) -> EditCommand:
        batch = AppendBatch([])

        if node.keywords:
            text = ', '.join(node.keywords)
            batch.items.append(
                AppendParagraph(f'Keywords: {text}', classes=['keywords'])
            )
        if node.MSC:
            text = ', '.join(node.MSC)
            batch.items.append(AppendParagraph(f'MSC: {text}', classes=['MSC']))

        # For documentation: if a visit_* method returns a command with defers = True,
        # then the corresponding leave_* method MUST MUST MUST call leave_node(node) and
        # add it to the returned batch!!!
        batch.items.append(self.leave_node(node))
        return batch

    def visit_paragraph(self, node: nodes.Paragraph) -> EditCommand:
        return AppendNodeTag(node, tag='p', newline_inner=False)

    def visit_step(self, node: nodes.Step) -> EditCommand:
        return AppendNodeTag(node)

    def visit_section(self, node: nodes.Section) -> EditCommand:
        node.types.insert(0, f'level-{node.level}')
        heading = f'{node.number}. {node.title}' if not node.nonum else f'{node.title}'
        return AppendBatchAndDefer(
            [
                AppendNodeTag(node, 'section'),
                AppendHeading(node.level, heading),
            ]
        )

    def visit_enumerate(self, node: nodes.Enumerate) -> EditCommand:
        return AppendNodeTag(node, 'ol')

    def visit_itemize(self, node: nodes.Itemize) -> EditCommand:
        return AppendNodeTag(node, 'ul')

    def visit_item(self, node: nodes.Item) -> EditCommand:
        return AppendNodeTag(node, 'li')

    def visit_comment(self, node: nodes.Item) -> EditCommand:
        return AppendNodeTag(node)

    def visit_math(self, node: nodes.Math) -> EditCommand:
        # the strings r'\(' and r'\)' are MathJax's delimiters for inline math
        return AppendBatchAndDefer(
            [
                AppendNodeTag(node, 'span', newline_inner=False, newline_outer=False),
                AppendTextAndDefer(r'\(', r'\)'),
            ]
        )

    def visit_displaymath(self, node: nodes.DisplayMath) -> EditCommand:
        # the strings '$$' and '$$' are MathJax's delimiters for inline math
        return AppendBatchAndDefer(
            [AppendNodeTag(node, 'div'), AppendTextAndDefer('$$\n', '$$')]
        )

    def visit_code(self, node: nodes.Code) -> EditCommand:
        return AppendNodeTag(node, 'span', newline_inner=False, newline_outer=False)

    def visit_displaycode(self, node: nodes.Code) -> EditCommand:
        return AppendNodeTag(node, 'div', newline_inner=True, newline_outer=True)

    def visit_text(self, node: nodes.Text) -> EditCommand:
        return AppendText(node.text)

    def visit_span(self, node: nodes.Span) -> EditCommand:
        commands = [
            AppendOpenTag(tag, newline_inner=False, newline_outer=False)
            for attr, tag in nodes.Span.attr_to_tag.items()
            if getattr(node, attr)
        ]
        return AppendBatchAndDefer(
            [
                AppendNodeTag(
                    node, tag='span', newline_inner=False, newline_outer=False
                ),
                *commands,
            ]
        )

    def visit_reference(self, node: nodes.Reference) -> EditCommand:
        if not node.target:
            raise RSMTranslatorError('Found a reference without a target')
        tgt = node.target
        if node.overwrite_reftext:
            reftext = node.overwrite_reftext
        else:
            reftext = tgt.reftext.format(
                nodeclass=tgt.__class__.__name__, number=tgt.number
            )
        classes = " ".join(['reference'] + node.types)
        text = f'<a class="{classes}" href="#{node.target.label}">{reftext}</a>'
        return AppendText(text)

    def visit_claim(self, node: nodes.Claim) -> EditCommand:
        return AppendNodeTag(node, tag='span', newline_inner=False, newline_outer=False)

    def visit_theorem(self, node: nodes.Theorem) -> EditCommand:
        paragraph = node.first_of_type(nodes.Paragraph)
        if paragraph is not None:
            paragraph: nodes.Paragraph
            classname = node.__class__.__name__.capitalize()
            span = nodes.Span(strong=True)
            span.append(nodes.Text(text=f'{classname} {node.number}. '))
            paragraph.prepend(span)
        return AppendNodeTag(node)

    def visit_proof(self, node: nodes.Proof) -> EditCommand:
        para = nodes.Paragraph()
        span = nodes.Span(strong=True)
        text = nodes.Text(text='Proof.')
        span.append(text)
        para.append(span)
        node.prepend(para)
        return AppendNodeTag(node)

    def leave_proof(self, node: nodes.Proof) -> EditCommand:
        batch = AppendBatch([AppendTombstone()])
        # For documentation: if a visit_* method returns a command with defers = True,
        # then the corresponding leave_* method MUST MUST MUST call leave_node(node) and
        # add it to the returned batch!!!
        batch.items.append(self.leave_node(node))
        return batch

    def visit_cite(self, node: nodes.Cite) -> EditCommand:
        text = ', '.join([str(bibitem.number) for bibitem in node.targets])
        return AppendText(f'[{text}]')

    def visit_bibliography(self, node: nodes.Bibliography) -> EditCommand:
        return AppendBatchAndDefer(
            [
                AppendOpenTag('section', classes=['level-2']),
                AppendHeading(2, 'References'),
                AppendNodeTag(node, 'ol'),
            ]
        )

    def visit_bibitem(self, node: nodes.Bibitem) -> EditCommand:
        text = f'{node.author}. "{node.title}".'
        if node.kind == 'article':
            text += f' {node.journal}.'
        elif node.kind == 'book':
            text += f' {node.publisher}.'
        text += f' {node.year}.'
        return AppendBatchAndDefer([AppendNodeTag(node, 'li'), AppendText(text)])


class HandrailsTranslator(Translator):
    @staticmethod
    def _replace_items_with_handrails(index, items, cls):
        handrail = AppendOpenTagNoDefer(classes=['handrail', 'handrail--offset'])
        btn_cont = AppendOpenTagNoDefer(classes=['handrail__btn-container'])
        btn_menu = AppendOpenTagNoDefer(
            classes=["handrail__btn handrail__btn-menu handrail__btn--relative"],
            newline_inner=False,
        )
        btn_togg = AppendOpenTagNoDefer(
            classes=["handrail__btn handrail__btn-toggle"], newline_inner=False
        )
        newitems = [
            handrail,
            btn_cont,
            btn_menu,
            AppendOpenCloseTag('span', '⋮', newline_inner=False, newline_outer=False),
            btn_menu.close_command(),
            btn_togg,
            AppendOpenCloseTag('span', '〉', newline_inner=False, newline_outer=False),
            btn_togg.close_command(),
            btn_cont.close_command(),
            items[index],
            handrail.close_command(),
        ]
        newitems = items[:index] + newitems + items[index + 1 :]
        return cls(newitems)

    @classmethod
    def _replace_batch_with_handrails(cls, index, batch):
        return cls._replace_items_with_handrails(index, batch.items, batch.__class__)

    @classmethod
    def _replace_cmd_with_handrails(cls, cmd):
        return cls._replace_items_with_handrails(0, [cmd], AppendBatchAndDefer)

    def visit_manuscript(self, node: nodes.Manuscript) -> EditCommand:
        batch = super().visit_manuscript(node)
        return self._replace_batch_with_handrails(4, batch)

    def visit_section(self, node: nodes.Section) -> EditCommand:
        batch = super().visit_section(node)
        return self._replace_batch_with_handrails(1, batch)

    def visit_abstract(self, node: nodes.Abstract) -> EditCommand:
        batch = super().visit_abstract(node)
        return self._replace_batch_with_handrails(1, batch)

    def visit_bibliography(self, node: nodes.Bibliography) -> EditCommand:
        batch = super().visit_bibliography(node)
        return self._replace_batch_with_handrails(1, batch)

    def visit_theorem(self, node: nodes.Theorem) -> EditCommand:
        cmd = super().visit_theorem(node)
        return self._replace_cmd_with_handrails(cmd)

    def visit_proof(self, node: nodes.Proof) -> EditCommand:
        cmd = super().visit_proof(node)
        return self._replace_cmd_with_handrails(cmd)
