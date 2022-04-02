"""
parser.py
---------

RSM Parser: take a partial source string and output a single node.

"""

from datetime import datetime
from typing import Any, Type
from collections.abc import Iterable
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from string import whitespace as whitespace_chars

from . import nodes

from icecream import ic

class RSMParserError(Exception):
    pass


class Tag(str):
    delim: str = ':'

    def __new__(cls, name):
        if isinstance(name, cls):
            return name
        return str.__new__(cls, f'{cls.delim}{name}{cls.delim}')

    @property
    def name(self):
        return f'{self[1:-1]}'


Tombstone = Tag('')
NotATag = Tag('__NOT_A_TAG__')
NoHint = Tag('__NO_HINT__')


@dataclass(frozen=True)
class ParsingResult:
    success: bool
    result: Any = None
    hint: Tag = NoHint
    consumed: int = 0


class Parser(ABC):
    def __init__(self, parent: 'Parser' = None, frompos: int = 0, src: str = None):
        self.parent: Parser | None = None
        self.src: str | None = src
        self.frompos: int = 0
        self.pos: int = 0
        if parent:
            self.parent, self.src, self.pos = parent, parent.src, parent.pos
            self.frompos = frompos if frompos else parent.frompos
            if self.frompos < parent.frompos:
                raise RSMParserError(
                    f'Starting position {frompos} cannot be '
                    'less than parent\'s {parent.frompos}'
                )
        else:
            self.frompos = frompos

    @abstractmethod
    def process(self) -> ParsingResult:
        pass

    def _pre_process(self) -> None:
        pass

    def _post_process(self) -> None:
        pass

    def parse(self) -> ParsingResult:
        self._pre_process()
        result = self.process()
        self._post_process()
        return result

    def consume_whitespace(self) -> int:
        """Skip any whitespace characters and return the number of characters skipped."""
        oldpos = self.pos
        self.pos += len(self.src[self.pos:]) - len(self.src[self.pos:].lstrip())
        return self.pos - oldpos

    def consume_tombstone(self) -> int:
        oldpos = self.pos
        self.pos += len(Tombstone)
        return self.pos - oldpos

    def get_tag_at_pos(self, consume) -> Tag:
        """Return the first tag starting at self.pos. If skip is True, skip it and update self.pos."""
        if self.src[self.pos] != Tag.delim:
            raise RSMParserError(f'No tag at position {self.pos}')

        src = self.src[self.pos:]
        index = src[1:].index(Tag.delim)
        tag = Tag(src[1:index + 1])
        if consume:
            self.pos += len(tag)

        return tag


class ParagraphParser(Parser):

    def __init__(self, parent: Parser, frompos: int = 0):
        super().__init__(parent=parent, frompos=frompos)
        self.node: nodes.Paragraph = None

    def _pre_process(self) -> None:
        super()._pre_process()
        idx = self.frompos - 1
        while self.src[idx] in whitespace_chars:
            idx -= 1
        if self.src[idx + 1] != '\n':
            raise RSMParserError(f'Paragraph must start after a newline')

    def process(self) -> ParsingResult:
        s = f'{self.__class__.__name__}.process start'
        ic(s, self.pos)
        self.pos = self.frompos
        self.node = nodes.Paragraph()

        try:
            tag = self.get_tag_at_pos(consume=False)
        except RSMParserError:
            tag = None

        if tag:
            if tag != Tag('paragraph'):
                raise RSMParserError(f'Was expecting pargraph tag, found {tag}')
            self.pos += len(Tag('paragraph'))
            self.consume_whitespace()
            parser = MetaParser(parent=self, nodeclass=nodes.Paragraph, frompos=self.pos)
            result = parser.parse()
            if not result.success:
                raise RSMParserError(f'Problem reading meta for paragraph block at position {self.pos}')
            for key, value in result.result.items():
                setattr(self.node, key, value)
            self.pos += result.consumed
            self.consume_whitespace()

        text = ''
        while True:
            idx = self.src.find('\n', self.pos)
            line = self.src[self.pos:idx + 1]
            text += line.lstrip()
            self.pos = idx + 1
            if line == '\n':
                break
        self.consume_whitespace()

        self.node.add(nodes.Text(text=text))

        s = f'{self.__class__.__name__}.process end'
        ic(s, self.pos)
        return ParsingResult(
            success=True,
            result=self.node,
            hint=NoHint,
            consumed=self.pos - self.frompos
        )


class StartEndParser(Parser):

    def __init__(self, start: str, end: str, parent: Parser | None, src: str, frompos: int = 0):
        super().__init__(parent=parent, src=src, frompos=frompos)
        self.start = start
        self.end = end

    def _pre_process(self):
        super()._pre_process()
        if not self.src[self.frompos:].startswith(self.start):
            raise RSMParserError(
                f'Did not find starting string "{self.start}" '
                f'in source at position {self.frompos}'
            )

    def _post_process(self):
        src = self.src[:self.pos]
        if not src.endswith(self.end):
            name = self.__class__.__name__
            raise RSMParserError(f'{name} did not find ending string "{self.end}"')
        super()._post_process()


class TagBlockParser(StartEndParser):

    def __init__(
            self,
            parent: Parser | None,
            tag: Tag,
            nodeclass: Type[nodes.Node],
            src: str = None,
            frompos: int = 0
    ):
        super().__init__(start=tag, end=Tombstone, parent=parent, src=src, frompos=frompos)
        self.tag: Tag = tag
        self.nodeclass: Type[nodes.Node] = nodeclass
        self.node: nodes.Node | None = None

    def process(self) -> ParsingResult:
        s = f'{self.__class__.__name__}.process start'
        ic(s, self.pos)

        if self.nodeclass is nodes.Manuscript:
            self.node = self.nodeclass(src=self.src)
        else:
            self.node = self.nodeclass()

        oldpos = self.pos
        self.consume_starttag()
        self.consume_whitespace()
        result = self.parse_meta()

        if not result.success:
            raise RSMParserError('{self.__class__.__name__} could not parse meta block')

        if result.hint == Tombstone:
            self.consume_tombstone()
            s = f'{self.__class__.__name__}.process end (found Tombstone)'
            ic(s, self.pos)
            result = ParsingResult(
                success=True,
                result=self.node,
                hint=NoHint,
                consumed=self.pos - oldpos,
            )
        elif result.hint == NoHint:
            self.consume_whitespace()
            try:
                tag = self.get_tag_at_pos(consume=False)
            except RSMParserError:
                tag = None
            result = self.parse_content(tag)
        elif result.hint == NotATag:
            self.consume_whitespace()
            result = self.parse_content(None)
        elif isinstance(result.hint, Tag):
            self.consume_whitespace()
            result = self.parse_content(result.hint)

        s = f'{self.__class__.__name__}.process end'
        ic(s, self.pos)
        return ParsingResult(
            success=result.success,
            result=result.result,
            hint=result.hint,
            consumed=self.pos - oldpos,
        )

    def parse_meta(self) -> ParsingResult:
        s = f'{self.__class__.__name__}.parse_meta start'
        ic(s, self.pos)
        oldpos = self.pos
        parser = MetaParser(parent=self, nodeclass=self.nodeclass, frompos=self.pos)
        result = parser.parse()
        if result.success:
            for key, value in result.result.items():
                setattr(self.node, key, value)
            self.pos += result.consumed
            s = f'{self.__class__.__name__}.parse_meta end'
            ic(s, self.pos)
            return ParsingResult(
                success=True,
                result=self.node,
                hint=result.hint,
                consumed=self.pos - oldpos
            )
        else:
            return ParsingResult(
                success=False,
                result=None,
                hint=NoHint,
                consumed=self.pos - oldpos
            )

    def parse_content(self, starting_tag: Tag | None) -> ParsingResult:
        s = f'{self.__class__.__name__}.parse_content start'
        ic(s, self.pos)
        oldpos = self.pos

        hint = starting_tag
        while hint != Tombstone:
            if hint in {None, NotATag, NoHint}:
                parser = ParagraphParser(self, frompos=self.pos)
            else:
                parser = _get_tagparser(self, hint)
            result = parser.parse()
            if not result.success:
                raise RSMParserError('Something went wrong')

            s = f'subparser {parser.__class__.__name__} done'
            ic(s, result.consumed)
            if isinstance(result.result, nodes.Node):
                self.node.add(result.result)
            self.pos += result.consumed

            self.consume_whitespace()
            try:
                hint = self.get_tag_at_pos(consume=False)
            except RSMParserError:
                hint = None
            ic(hint)

        self.consume_tombstone()

        s = f'{self.__class__.__name__}.parse_content end'
        ic(s, self.pos)
        return ParsingResult(
            success=True,
            result=self.node,
            hint=hint,
            consumed=self.pos - oldpos,
        )

    def consume_starttag(self) -> int:
        if self.pos != self.frompos:
            raise RSMParserError('consume_starttag can only when self.pos == self.frompos')
        numchars = len(self.tag)
        self.pos += numchars
        return numchars


class ManuscriptParser(TagBlockParser):
    def __init__(self):
        super().__init__(
            parent=None,
            tag=Tag('manuscript'),
            nodeclass=nodes.Manuscript,
        )

    def parse(self, src: str) -> nodes.Manuscript:
        self.src = src
        result = super().parse()
        assert isinstance(result.result, nodes.Manuscript)
        return  result.result


class AuthorParser(TagBlockParser):
    def __init__(self, parent: Parser, frompos: int = 0):
        super().__init__(
            parent=parent,
            tag=Tag('author'),
            nodeclass=nodes.Author,
            frompos=frompos
        )


class AbstractParser(TagBlockParser):
    def __init__(self, parent: Parser, frompos: int = 0):
        super().__init__(
            parent=parent,
            tag=Tag('abstract'),
            nodeclass=nodes.Abstract,
            frompos=frompos
        )


class SectionParser(TagBlockParser):
    def __init__(self, parent: Parser, frompos: int = 0):
        super().__init__(
            parent=parent,
            tag=Tag('section'),
            nodeclass=nodes.Section,
            frompos=frompos
        )


class MetaParser(Parser):
    def __init__(
            self,
            parent: Parser,
            nodeclass: Type[nodes.Node],
            frompos: int = 0
    ):
        super().__init__(parent=parent, frompos=frompos)
        self.nodeclass: Type[nodes.Node] = nodeclass
        self.inline_mode: bool = False

    def process(self) -> ParsingResult:
        s = f'{self.__class__.__name__}.process start'
        ic(s, self.pos)

        if not self.src[self.frompos].startswith(':'): # there is no meta
            return ParsingResult(True, {}, NoHint, 0)

        left = self.frompos
        right = left + self.src[left:].index('\n')
        if Tombstone in self.src[left:right]:
            self.inline_mode = True

        pairparser = MetaPairParser(parent=self)
        meta = {}
        numchars = 0
        while True:
            result = pairparser.parse()
            if result.success:
                key, value = result.result
                meta[key] = value
                self.pos += result.consumed
                numchars += result.consumed
                numchars += self.consume_whitespace()
                pairparser.frompos, pairparser.pos = self.pos, self.pos

            else:
                result = ParsingResult(
                    success=True,
                    result=meta,
                    hint=result.hint,
                    consumed=numchars,
                )
                break

        s = f'{self.__class__.__name__}.process end ({result.hint})'
        ic(s, self.pos)
        return result


class MetaPairParser(Parser):

    parse_value_methods = {
        'label': 'parse_end_of_line_value',
        'title': 'parse_end_of_line_value',
        'date': 'parse_datetime_value',
        'name': 'parse_end_of_line_value',
        'affiliation': 'parse_end_of_line_value',
        'email': 'parse_end_of_line_value',
        'keywords': 'parse_list_value',
        'MSC': 'parse_list_value',
        'types': 'parse_list_value',
    }

    block_delim = '\n'
    inline_delim = ','

    def __init__(self, parent: Type[Parser]):
        super().__init__(parent=parent)
        self.nodeclass: Type[nodes.Node] = parent.nodeclass

    def process(self) -> ParsingResult:
        oldpos = self.pos

        # find the key
        try:
            key = self.get_tag_at_pos(consume=True)
            key = key.name
        except RSMParserError:
            return ParsingResult(
                success=False,
                result=None,
                hint=NoHint,
                consumed=self.pos - oldpos,
            )

        # check if key is valid
        if key not in self.nodeclass.metakeys() | {'label', 'types'}:
            return ParsingResult(
                success=False,
                result=None,
                hint=Tag(key),
                consumed=self.pos - oldpos,
            )

        # find the value
        self.consume_whitespace()
        value, numchars = getattr(self, self.parse_value_methods[key])(key)
        self.pos += numchars
        self.consume_whitespace()

        return ParsingResult(
            success=True,
            result=(key, value),
            hint=NoHint,
            consumed=self.pos - oldpos,
        )

    @property
    def delim(self) -> str:
        return self.inline_delim if self.parent.inline_mode else self.block_delim

    def parse_end_of_line_value(self, key: str) -> tuple[str, int]:
        left = self.pos
        right1 = left + self.src[left:].index(Tombstone)
        try:
            right2 = left + self.src[left:].index(self.delim)
        except ValueError:
            right2 = right1 + 1
        right, delim = min((right1, Tombstone), (right2, self.delim))
        value = self.src[left:right]
        return value.strip(), len(value) + len(delim)

    def parse_datetime_value(self, key: str) -> tuple[datetime, int]:
        value, numchars = self.parse_end_of_line_value(key)
        return datetime.fromisoformat(value), numchars

    def parse_list_value(self, key: str) -> tuple[list, int]:
        ic(self.pos)
        src = self.src[self.pos:]
        if src[0] != '{':
            raise ValueError(f'Key "{key}"' + ' expects a list, must start with "{"')

        try:
            brace = src.index('}')
        except ValueError:
            raise ValueError(f'Key "{key}"' + ' expects a list, could not find "}"')
        try:
            colon = src.index(':')
        except ValueError:
            colon = brace+1
        if colon <= brace:
            raise ValueError(f'Key "{key}"' + ' expects a list, but found ":" before "}"')

        after = src[brace+1:]
        if not after.startswith(self.delim) and not after.startswith(' ' + Tombstone):
            raise ValueError(f'Expected a "{self.delim}" or a "{Tombstone}" after value of key "{key}"')

        value = src[1:brace]
        ic(value)
        oldpos = self.pos
        numchars = len(value) + 2
        ic(self.pos, numchars)
        if self.src[self.pos+numchars:].startswith(self.delim):
            numchars += len(self.delim)
        else:
            assert self.parent.inline_mode and self.src[self.pos+numchars:].startswith(' ' + Tombstone)
            numchars += len(' ' + Tombstone)
        return [x.strip() for x in value.split(',')], numchars


def _get_tagparser(parent, tag):
    parserclass = globals()[f'{tag.name.capitalize()}Parser']
    return parserclass(parent=parent, frompos=parent.pos)
