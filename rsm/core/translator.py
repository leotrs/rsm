"""
translator.py
-------------

RSM Translator: take a Manuscript and return a HTML string.

"""

from collections import namedtuple
from abc import ABC, abstractmethod
from typing import Iterable
from icecream import ic

from .nodes import Node
from .manuscript import AbstractTreeManuscript, HTMLBodyManuscript
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


class EditCommand(ABC):
    @abstractmethod
    def execute(self, translator: 'Translator') -> None:
        pass

    def _edit_command_repr(self, members) -> str:
        start = f'{self.__class__.__name__}('
        middle = []
        for key in members:
            s = f'{key}='
            value = getattr(self, key)
            if isinstance(value, str):
                value = repr(ShortenedString(value.strip()))
            s += f'{value}'
            middle.append(s)
        middle = ', '.join(middle)
        end = ')'
        return start + middle + end

    def __repr__(self) -> str:
        return self._edit_command_repr([])


class DummyCommand(EditCommand):
    def execute(self, translator: 'Translator') -> None:
        pass


class AppendTextAndDefer(EditCommand):

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
            newline: bool = True
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
        deferred_text = f'</{self.tag}>\n'
        super().__init__(text, deferred_text)

    def __repr__(self) -> str:
        return self._edit_command_repr(['tag', 'id', 'classes', 'newline'])


class AppendNodeTag(AppendOpenTag):
    """Most inherited fields are ignored and overwritten."""

    def __init__(
            self,
            node: Node,
            tag: str = 'div',
            *,
            newline: bool = True,
    ):
        self.node = node
        classes = [node.__class__.__name__.lower()] + node.types
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
            tag='p',
            content=content,
            id=id,
            classes=classes,
            newline=newline
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
            newline=newline
        )

    def __repr__(self) -> str:
        return self._edit_command_repr(['level', 'content', 'id', 'classes', 'node', 'newline'])


class EditCommandBatch(EditCommand):

    def __init__(self, items: Iterable):
        self.items = list(items)

    def __len__(self) -> int:
        return len(self.items)

    def __repr__(self) -> str:
        classname = self.__class__.__name__
        return f'{classname}({repr(self.items)})'


class AppendBatchAndDefer(EditCommandBatch):

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
        self.body: HTMLBodyManuscript = ''
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

    def translate(self, tree: AbstractTreeManuscript) -> HTMLBodyManuscript:
        self.tree = tree

        if self.deferred:
            raise RSMTranslatorError('Something went wrong')

        stack = TranslateActionStack()
        stack.push_visit(tree)
        while stack:
            ic(stack)
            node, action, method = stack.pop()
            if action == 'visit':
                stack.push_leave(node)
                for child in reversed(node.children):
                    stack.push_visit(child)
            append = method(self, node)

            ic('before executing')
            ic(len(self.deferred))
            append.execute(self)
            ic('after executing')
            ic(len(self.deferred))
            # ic([b.items if hasattr(b, 'items') else b for b in self.deferred ])
            ic(self.deferred)

        if self.deferred:
            raise RSMTranslatorError('Something went wrong')

        return self.body

    def visit_node(self, node: Node) -> None:
        return AppendText(str(node) + '\n')

    def leave_node(self, node: Node) -> None:
        s = f'leaving node of class {node.__class__.__name__}'
        ic(s)
        return self.deferred.pop()

    def visit_manuscript(self, node: Node) -> None:
        if not node.label:
            node.label = 'manuscript'
        return AppendBatchAndDefer([
            AppendOpenTag('body'),
            AppendNodeTag(node),
            AppendOpenTag('section', classes=['level-1']),
            AppendHeading(1, node.title)
        ])

    def visit_author(self, node: Node) -> None:
        return AppendBatchAndDefer([
            AppendNodeTag(node),
            AppendParagraph(f'{node.name}\n{node.affiliation}\n{node.email}'),
        ])

    def visit_abstract(self, node: Node) -> None:
        return AppendBatchAndDefer([
            AppendNodeTag(node),
            AppendHeading(3, 'Abstract'),
        ])

    def leave_abstract(self, node: Node) -> None:
        batch = AppendBatch([])

        if node.keywords:
            text = ', '.join(node.keywords)
            batch.items.append(AppendParagraph(f'Keywords: {text}', classes=['keywords']))
        if node.MSC:
            text = ', '.join(node.MSC)
            batch.items.append(AppendParagraph(f'MSC: {text}', classes=['MSC']))

        batch.items.append(self.leave_node(node))

        return batch

    def visit_paragraph(self, node: Node) -> None:
        return AppendNodeTag(node, tag='p', newline=False)

    def visit_section(self, node: None) -> None:
        node.types.insert(0, 'level-2')
        return AppendNodeTag(node, 'section')

    def visit_text(self, node: Node) -> None:
        return AppendText(node.text.strip())

    def leave_text(self, node: Node) -> None:
        return DummyCommand()
