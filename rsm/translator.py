"""
translator.py
-------------

RSM Translator: take a Manuscript and return a HTML string.

"""

import logging
from typing import Iterable, Callable, Any
from collections import namedtuple
from abc import ABC, abstractmethod
from typing import Iterable
from icecream import ic
import textwrap

from . import nodes

logger = logging.getLogger('RSM').getChild('Translator')


class RSMTranslatorError(Exception):
    pass


def make_tag(tag: str, id_: str, classes: Iterable, **kwargs: Any) -> str:
    text = f'<{tag}'
    if id_:
        text += f' id="{id_}"'
    if classes:
        classes = ' '.join(classes)
        text += f' class="{classes}"'
    if kwargs:
        text += ' '
    text += ' '.join(f'{k}="{v}"' for k, v in kwargs.items())
    text += '>'
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
    def execute(self, translator: 'Translator') -> None:
        pass

    def _edit_command_repr(self, members: Iterable[str]) -> str:
        start = f'{self.__class__.__name__}('
        middles = []
        for key in members:
            s = f'{key}='
            value = getattr(self, key)
            if isinstance(value, str):
                value = repr(textwrap.shorten(value.strip(), 60))
            s += f'{value}'
            middles.append(s)
        middle = ', '.join(middles)
        end = ')'
        return start + middle + end

    def __repr__(self) -> str:
        return self._edit_command_repr([])


class AppendTextAndDefer(EditCommand):
    defers = True

    def __init__(self, text: str = '', deferred_text: str = ''):
        self._text = text
        self._deferred_text = deferred_text

    def __repr__(self) -> str:
        return self._edit_command_repr(['text', 'deferred_text'])

    def execute(self, translator: 'Translator') -> None:
        translator.body += self.make_text()
        translator.deferred.append(AppendText(self.make_deferred_text()))

    def make_text(self) -> str:
        return self._text

    def make_deferred_text(self) -> str:
        return self._deferred_text


class AppendText(EditCommand):
    def __init__(self, text: str = ''):
        self._text = text

    def __repr__(self) -> str:
        return self._edit_command_repr(['text'])

    def execute(self, translator: 'Translator') -> None:
        translator.body += self.make_text()

    def make_text(self) -> str:
        return self._text


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
        self.newline_inner = newline_inner
        self.newline_outer = newline_outer
        super().__init__()

    def make_text(self) -> str:
        return (
            ('\n' if self.newline_outer else '')
            + make_tag(self.tag, self.id, self.classes)
            + ('\n' if self.newline_inner else '')
            + self.content
            + ('\n' if self.newline_inner else '')
            + f'</{self.tag}>'
            + ('\n' if self.newline_outer else '')
        )

    def __repr__(self) -> str:
        return self._edit_command_repr(['tag', 'content', 'id', 'classes'])


class AppendOpenTagManualClose(AppendText):
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

        super().__init__()

    def make_text(self) -> str:
        return (
            ('\n' if self.newline_outer else '')
            + make_tag(self.tag, self.id, self.classes)
            + ('\n' if self.newline_inner else '')
            + self.content
        )

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
        self.newline_inner = newline_inner
        self.newline_outer = newline_outer
        super().__init__()

    def make_text(self) -> str:
        return (
            ('\n' if self.newline_outer else '')
            + make_tag(self.tag, self.id, self.classes)
            + ('\n' if self.newline_inner else '')
        )

    def make_deferred_text(self) -> str:
        return (
            ('\n' if self.newline_inner else '')
            + f'</{self.tag}>'
            + ('\n' if self.newline_outer else '')
        )

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


class AppendKeyword(AppendOpenCloseTag):
    def __init__(
        self,
        keyword: str,
        *,
        id: str = '',
        classes: list = None,
        newline_inner: bool = False,
        newline_outer: bool = False,
    ):
        classes = ['keyword'] + (classes or [])
        super().__init__(
            tag='span',
            content=keyword,
            id=id,
            classes=classes,
            newline_inner=newline_inner,
            newline_outer=newline_outer,
        )

    def __repr__(self) -> str:
        return self._edit_command_repr(['level', 'content', 'id', 'classes'])


class AppendHalmos(AppendOpenCloseTag):
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
            classes=['halmos'] + (classes or []),
            newline_inner=False,
            newline_outer=True,
        )

    def __repr__(self) -> str:
        return self._edit_command_repr(['classes'])


class AppendExternalTree(AppendText):
    def __init__(self, root: nodes.Node):
        super().__init__()
        self.root = root

    def make_text(self) -> str:
        return Translator().translate(self.root)


class EditCommandBatch(EditCommand):
    def __init__(self, items: Iterable):
        self.items = list(items)

    def __len__(self) -> int:
        return len(self.items)

    def __repr__(self) -> str:
        classname = self.__class__.__name__
        return f'{classname}({repr(self.items)})'

    def make_text(self) -> str:
        raise RSMTranslatorError('Why are we here?')


class AppendBatchAndDefer(EditCommandBatch):
    defers = True

    def execute(self, translator: 'Translator') -> None:
        deferred: list[EditCommand] = []
        for item in self.items:
            if isinstance(item, AppendTextAndDefer):
                deferred.append(AppendText(item.make_deferred_text()))
            AppendText(item.make_text()).execute(translator)

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
        self.tree: nodes.Manuscript = None
        self.body: str = ''
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

    def translate(self, tree: nodes.Manuscript) -> str:
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
        return AppendBatchAndDefer(
            [
                AppendOpenTag(classes=['node-with-no-class']),
                AppendText(str(node) + '\n'),
            ]
        )

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
        heading = (
            f'{node.full_number}. {node.title}' if not node.nonum else f'{node.title}'
        )
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

    def visit_note(self, node: nodes.Note) -> EditCommand:
        return AppendNodeTag(node)

    def visit_math(self, node: nodes.Math) -> EditCommand:
        # the strings r'\(' and r'\)' are MathJax's delimiters for inline math
        return AppendBatchAndDefer(
            [
                AppendNodeTag(node, 'span', newline_inner=False, newline_outer=False),
                AppendTextAndDefer(r'\(', r'\)'),
            ]
        )

    def visit_mathblock(self, node: nodes.MathBlock) -> EditCommand:
        # the strings '$$' and '$$' are MathJax's delimiters for inline math
        return AppendBatchAndDefer(
            [
                AppendNodeTag(node, 'div'),
                AppendTextAndDefer('$$\n', '$$'),
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
                content=f'({node.full_number})',
                classes=['mathblock__number'],
                newline_inner=False,
            ),
        )
        batch = AppendBatch(batch.items)
        return batch

    def visit_code(self, node: nodes.Code) -> EditCommand:
        return AppendNodeTag(node, 'span', newline_inner=False, newline_outer=False)

    def visit_codeblock(self, node: nodes.Code) -> EditCommand:
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

    def _make_ahref_tag_text(
        self, node: nodes.BaseReference, target: nodes.Node, href_text: str
    ) -> str:
        if not target:
            raise RSMTranslatorError(f'Found a {node.__class__} without a target')
        tgt = target
        if hasattr(node, 'overwrite_reftext') and node.overwrite_reftext:
            reftext = node.overwrite_reftext
        else:
            if hasattr(tgt, 'reftext'):
                reftext = tgt.reftext.format(
                    nodeclass=tgt.__class__.__name__, number=tgt.number
                )
            else:
                reftext = tgt
        classes = node.types
        if not isinstance(node, nodes.URL) and 'reference' not in classes:
            classes.insert(0, 'reference')
        tag = make_tag('a', id_='', classes=classes, href=href_text) + reftext + '</a>'
        return tag

    def visit_reference(self, node: nodes.Reference) -> EditCommand:
        return AppendText(
            self._make_ahref_tag_text(node, node.target, f"#{node.target.label}")
        )

    def visit_url(self, node: nodes.URL) -> EditCommand:
        return AppendText(
            self._make_ahref_tag_text(node, node.target, f"{node.target}")
        )

    def visit_claim(self, node: nodes.Claim) -> EditCommand:
        return AppendBatchAndDefer(
            [
                AppendNodeTag(
                    node, tag='span', newline_inner=False, newline_outer=False
                ),
                AppendKeyword('⊢ '),
            ]
        )

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
            f'{classname.capitalize()} {node.full_number}. ',
            [f'{classname}__title'],
        )
        return AppendBatchAndDefer(
            [
                AppendNodeTag(node),
                AppendOpenTag(classes=[f'{classname}-contents']),
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
                AppendOpenTag(classes=[f'{classname}-contents']),
            ]
        )

    def visit_proof(self, node: nodes.Proof) -> EditCommandBatch:
        last = node.last_of_type(nodes.Step)
        if last:
            last.types.append('last')

        classname = node.__class__.__name__.lower()
        title = self._make_title_node(
            f'{classname.capitalize()}. ', [f'{classname}__title']
        )
        return AppendBatchAndDefer(
            [
                AppendNodeTag(node),
                AppendExternalTree(title),
                AppendOpenTag(classes=[f'{classname}-contents']),
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
        tags = [self._make_ahref_tag_text(node, t, f'#{t.label}') for t in node.targets]
        text = ', '.join(tags)
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

    def visit_draft(self, node: nodes.Draft) -> EditCommand:
        return AppendBatchAndDefer(
            [AppendNodeTag(node, 'span'), AppendTextAndDefer('[ ', ' ]')]
        )

    def visit_figure(self, node: nodes.Figure) -> EditCommand:
        figcaption = AppendOpenTagManualClose('figcaption')
        title = self._make_title_node(
            f'{node.__class__.__name__} {node.full_number}. ', types=[], paragraph=False
        )
        return AppendBatchAndDefer(
            [
                AppendNodeTag(node, 'figure'),
                AppendText(
                    make_tag(
                        'img',
                        id_=node.label,
                        classes=[],
                        src=node.path,
                        alt=node.caption,
                    )
                ),
                figcaption,
                AppendExternalTree(title),
                AppendText(str(node.caption)),
                figcaption.close_command(),
            ]
        )


class HandrailsTranslator(Translator):
    @staticmethod
    def _make_option_tag(opt):
        return AppendOpenCloseTag(
            'span',
            opt,
            classes=['option', f'option__{opt}'],
            newline_inner=False,
        )

    def _replace_items_with_handrails(self, index, items, cls, include_content=False):
        classes = ['handrail', 'handrail--offset']
        if include_content:
            handrail = AppendOpenTag(classes=classes)
        else:
            handrail = AppendOpenTagManualClose(classes=classes)
        btn_cont = AppendOpenTagManualClose(classes=['handrail__btn-container'])
        btn_menu = AppendOpenTagManualClose(
            classes=["handrail__btn", "handrail__btn-menu", "handrail__btn--relative"],
            newline_inner=False,
        )
        btn_togg = AppendOpenTagManualClose(
            classes=["handrail__btn", "handrail__btn-toggle"], newline_inner=False
        )
        opt_tag = AppendOpenTagManualClose(
            classes=["options", "hide"], newline_inner=True, newline_outer=True
        )
        options = [self._make_option_tag(opt) for opt in ['link', 'tree', 'source']]
        newitems = [
            handrail,
            btn_cont,
            btn_menu,
            AppendOpenCloseTag('span', '⋮', newline_inner=False, newline_outer=False),
            opt_tag,
            *options,
            opt_tag.close_command(),
            btn_menu.close_command(),
            btn_togg,
            AppendOpenCloseTag('span', '〉', newline_inner=False, newline_outer=False),
            btn_togg.close_command(),
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
        batch = super().visit_theorem(node)
        batch.items[1].classes.append('handrail__collapsible')
        batch = self._replace_batch_with_handrails(1, batch, include_content=True)
        batch.items[1].classes += [
            f'stars-{node.stars}',
            f'clocks-{node.clocks}',
        ]
        batch.items[-1].root.types.append("do-not-hide")
        return batch

    def visit_proof(self, node: nodes.Proof) -> EditCommand:
        batch = super().visit_proof(node)
        batch.items[2].classes.append('handrail__collapsible')

        # the last element is the proof title, we pop it as it will be inserted into the
        # proof header div
        tree = batch.items[1]
        batch.items = [batch.items[0], batch.items[2]]
        tree.root.types.append('do-not-hide')

        if any(type(c) is nodes.Sketch for c in node.children):
            self._add_proof_header_with_sketch(batch, tree, node)
            for c in node.children:
                if type(c) is not nodes.Sketch:
                    c.types.append('hide')
        else:
            self._add_proof_header_no_sketch(batch, tree, node)
        return self._replace_batch_with_handrails(1, batch, include_content=True)

    def _add_proof_header_with_sketch(
        self, batch: EditCommandBatch, tree: nodes.Node, node: nodes.Proof
    ) -> None:
        header = AppendOpenTagManualClose(classes=['proof__header'])
        tabs = AppendOpenTagManualClose(classes=['proof__tabs'])
        batch.items[1:1] = [
            header,
            tree,
            tabs,
            AppendOpenCloseTag(
                'button',
                content="sketch",
                classes=["sketch", "active"],
                newline_inner=False,
            ),
            AppendOpenCloseTag(
                'button', content="full", classes=['full'], newline_inner=False
            ),
            tabs.close_command(),
            header.close_command(),
        ]

    def _add_proof_header_no_sketch(
        self, batch: EditCommandBatch, tree: nodes.Node, node: nodes.Proof
    ) -> None:
        header = AppendOpenTagManualClose(classes=['proof__header'])
        batch.items[1:1] = [header, tree, header.close_command()]

    def visit_subproof(self, node: nodes.Subproof) -> EditCommand:
        batch = super().visit_subproof(node)
        batch.items[1].classes += ['handrail', 'handrail--hug', 'handrail__collapsible']
        return batch

    def visit_step(self, node: nodes.Step) -> EditCommand:
        cmd = super().visit_step(node)
        batch = self._replace_cmd_with_handrails(cmd, include_content=True)
        batch.items.insert(
            -1,
            AppendOpenCloseTag(
                classes=['step__number'],
                content=f'({node.full_number})',
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
        batch.items.insert(1, AppendHalmos(classes=['hide']))
        batch = AppendBatch(batch.items)
        return batch

    def visit_mathblock(self, node: nodes.MathBlock) -> EditCommand:
        # the strings '$$' and '$$' are MathJax's delimiters for inline math
        return AppendBatchAndDefer(
            [
                AppendNodeTag(node, 'div'),
                AppendOpenCloseTag(
                    content=f'({node.full_number})',
                    classes=['mathblock__number mathblock__number--phantom'],
                    newline_inner=False,
                ),
                AppendTextAndDefer('$$\n', '$$'),
            ]
        )
