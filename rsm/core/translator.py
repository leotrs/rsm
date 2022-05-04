"""
translator.py
-------------

RSM Translator: take a Manuscript and return a HTML string.

"""

import logging

logger = logging.getLogger('RSM').getChild('Translator')

from collections import namedtuple
from abc import ABC, abstractmethod
from typing import Iterable
from icecream import ic

from . import nodes
from .manuscript import AbstractTreeManuscript, HTMLManuscript
from .util import ShortenedString


class RSMTranslatorError(Exception):
    pass


def make_tag(tag, id, classes, newline=False):
    text = f'<{tag}'
    if id:
        text += f' id="{id}"'
    if classes:
        classes = ' '.join(classes)
        text += f' class="{classes}"'
    text += '>'
    if newline:
        text += '\n'
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

    def _edit_command_repr(self, members) -> str:
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
        ic(self)
        translator.body += self.text
        translator.deferred.append(AppendText(self.deferred_text))


class AppendText(EditCommand):
    def __init__(self, text: str):
        self.text = text

    def __repr__(self) -> str:
        return self._edit_command_repr(['text'])

    def execute(self, translator: 'Translator') -> None:
        ic(self)
        translator.body += self.text


class AppendOpenCloseTag(AppendText):
    def __init__(
        self,
        tag: str = 'div',
        content: str = '',
        *,
        id: str = '',
        classes: list = None,
        newline: bool = True,
    ):
        self.tag = tag
        self.content = content
        self.id = id
        self.classes = classes if classes else []
        self.newline = newline
        text = (
            make_tag(self.tag, self.id, self.classes, self.newline)
            + self.content
            + ('\n' if self.newline else '')
            + f'</{self.tag}>\n'
        )
        super().__init__(text)

    def __repr__(self) -> str:
        return self._edit_command_repr(['tag', 'content', 'id', 'classes', 'newline'])


class AppendOpenTag(AppendTextAndDefer):
    def __init__(
        self,
        tag: str = 'div',
        *,
        id: str = '',
        classes: list = None,
        newline: bool = True,
    ):
        self.tag = tag
        self.id = id
        self.classes = classes if classes else []
        self.newline = newline
        text = make_tag(self.tag, self.id, self.classes, self.newline)
        deferred_text = f'</{self.tag}>'
        if self.newline:
            deferred_text = '\n' + deferred_text
        super().__init__(text, deferred_text)

    def __repr__(self) -> str:
        return self._edit_command_repr(['tag', 'id', 'classes', 'newline'])


class AppendNodeTag(AppendOpenTag):
    def __init__(
        self,
        node: nodes.Node,
        tag: str = 'div',
        *,
        newline: bool = True,
    ):
        self.node = node
        classes = [node.__class__.__name__.lower()] + [str(t) for t in node.types]
        super().__init__(tag=tag, id=node.label, classes=classes, newline=newline)

    def __repr__(self) -> str:
        return self._edit_command_repr(['tag', 'node', 'newline'])


class AppendParagraph(AppendOpenCloseTag):
    def __init__(
        self,
        content: str = '',
        *,
        id: str = '',
        classes: list = None,
        newline: bool = True,
    ):
        super().__init__(
            tag='p', content=content, id=id, classes=classes, newline=newline
        )

    def __repr__(self) -> str:
        return self._edit_command_repr(['content', 'id', 'classes', 'newline'])


class AppendHeading(AppendOpenCloseTag):
    def __init__(
        self,
        level: int,
        content: str = '',
        *,
        id: str = '',
        classes: list = None,
        newline: bool = False,
    ):
        self.level = level
        super().__init__(
            tag=f'h{self.level}',
            content=content,
            id=id,
            classes=classes,
            newline=newline,
        )

    def __repr__(self) -> str:
        return self._edit_command_repr(['level', 'content', 'id', 'classes', 'newline'])


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
        s = f'executing batch of len {len(self)}'
        ic(s)
        deferred: list[AppendText] = []
        for item in self.items:
            if isinstance(item, AppendTextAndDefer):
                deferred.append(AppendText(item.deferred_text))
            AppendText(item.text).execute(translator)

        s = f'appending closing batch of len {len(deferred)}'
        ic(s)

        batch = AppendBatch(reversed(deferred))
        ic(batch.items)
        translator.deferred.append(batch)
        ic('finished batch')


class AppendBatch(EditCommandBatch):
    def execute(self, translator: 'Translator') -> None:
        s = f'executing closing batch of len {len(self)}'
        ic(s)
        for item in self.items:
            ic(item.__class__.__name__)
            item.execute(translator)
        ic('finished closing batch')


class Action(namedtuple('Action', 'node action method')):
    def __repr__(self) -> str:
        classname = self.node.__class__.__name__
        return f'Action(node={classname}(), action="{self.action}")'


class TranslateActionStack(list):
    def push_visit(self, node):
        self.append(Action(node, 'visit', Translator.get_visit_method(node)))

    def push_leave(self, node):
        self.append(Action(node, 'leave', Translator.get_leave_method(node)))


class Translator:
    def __init__(self):
        self.tree: AbstractTreeManuscript = None
        self.body: HTMLManuscript = ''
        self.deferred: list = []

    @classmethod
    def _get_action_method(cls, node, action):
        nodeclass = node.__class__
        method = f'{action}_{nodeclass.__name__.lower()}'
        while not hasattr(cls, method):
            nodeclass = nodeclass.__bases__[0]
            method = f'{action}_{nodeclass.__name__.lower()}'
        return getattr(cls, method)

    @classmethod
    def get_visit_method(cls, node):
        return cls._get_action_method(node, 'visit')

    @classmethod
    def get_leave_method(cls, node):
        return cls._get_action_method(node, 'leave')

    def translate(self, tree: AbstractTreeManuscript) -> HTMLManuscript:
        # ic.enable()
        self.tree = tree

        if self.deferred:
            raise RSMTranslatorError('Something went wrong')

        stack = TranslateActionStack()
        stack.push_visit(tree)
        while stack:
            ic(stack)
            node, action, method = stack.pop()
            command = method(self, node)
            if action == 'visit':
                if command.defers:
                    stack.push_leave(node)
                for child in reversed(node.children):
                    stack.push_visit(child)

            ic('before executing')
            ic(len(self.deferred))
            command.execute(self)
            ic('after executing')
            ic(len(self.deferred))
            ic(self.deferred)

        if self.deferred:
            raise RSMTranslatorError('Something went wrong')

        return self.body

    def visit_node(self, node: nodes.Node) -> EditCommand:
        return AppendText(str(node) + '\n')

    def leave_node(self, node: nodes.Node) -> EditCommand:
        s = f'leaving node of class {node.__class__.__name__}'
        ic(s)
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
        return AppendNodeTag(node, tag='p', newline=False)

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
            [AppendNodeTag(node, 'span'), AppendTextAndDefer(r'\(', r'\)')]
        )

    def visit_displaymath(self, node: nodes.DisplayMath) -> EditCommand:
        # the strings '$$' and '$$' are MathJax's delimiters for inline math
        return AppendBatchAndDefer(
            [AppendNodeTag(node, 'div'), AppendTextAndDefer('$$\n', '$$')]
        )

    def visit_text(self, node: nodes.Text) -> EditCommand:
        return AppendText(node.text)

    def visit_span(self, node: nodes.Span) -> EditCommand:
        commands = [
            AppendOpenTag(tag, newline=False)
            for attr, tag in nodes.Span.attr_to_tag.items()
            if getattr(node, attr)
        ]
        return AppendBatchAndDefer(
            [
                AppendNodeTag(node, tag='span', newline=False),
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
        text = f'<a href="#{node.target.label}">{reftext}</a>'
        return AppendText(text)

    def visit_claim(self, node: nodes.Claim) -> EditCommand:
        return AppendNodeTag(node, tag='span', newline=False)

    def visit_theorem(self, node: nodes.Theorem) -> EditCommand:
        paragraph: nodes.Paragraph = node.first_of_type(nodes.Paragraph)
        classname = node.__class__.__name__.capitalize()
        span = nodes.Span(strong=True)
        span.append(nodes.Text(text=f'{classname} {node.number}. '))
        paragraph.prepend(span)
        return AppendNodeTag(node)

    def visit_cite(self, node: nodes.Cite) -> EditCommand:
        text = ','.join([str(bibitem.number) for bibitem in node.targets])
        return AppendText(f'[{text}]')

    def visit_bibliography(self, node: nodes.Bibliography) -> EditCommand:
        # ic.enable()
        # ic(node.children)
        # ic.disable()
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
