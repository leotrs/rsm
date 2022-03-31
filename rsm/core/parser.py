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

        text = ''
        while True:
            idx = self.src.find('\n', self.pos)
            line = self.src[self.pos:idx + 1]
            text += line
            self.pos = idx + 1
            if line == '\n':
                break
        self.consume_whitespace()

        self.node = nodes.Paragraph()
        ic(self.node)
        ic('adding to paragraph', len(text))
        self.node.add(nodes.Text(text=text))
        ic(self.node)

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
            tag = None
            try:
                tag = self.get_tag_at_pos(consume=False)
            except RSMParserError:
                result = self.parse_content(None)
            if tag:
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
            ic(self.pos)
            self.pos += result.consumed
            ic(self.pos)

            self.consume_whitespace()
            hint = self.get_tag_at_pos(consume=False)
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
    def __init__(self, src: str):
        super().__init__(
            parent=None,
            tag=Tag('manuscript'),
            nodeclass=nodes.Manuscript,
            src=src
        )

    def parse(self) -> nodes.Manuscript:
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

    def process(self) -> ParsingResult:
        s = f'{self.__class__.__name__}.process start'
        ic(s, self.pos)

        if not self.src[self.frompos].startswith(':'): # there is no meta
            return {}, 0

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

    def __init__(self, parent: Type[Parser]):
        super().__init__(parent=parent)
        self.nodeclass = parent.nodeclass

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
        ic('found key', key)
        if key not in self.nodeclass.metakeys() | {'label', 'types'}:
            ic('invalid key for', self.nodeclass, self.nodeclass.metakeys())
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

        return ParsingResult(
            success=True,
            result=(key, value),
            hint=NoHint,
            consumed=self.pos - oldpos,
        )

    def parse_end_of_line_value(self, key: str) -> tuple[str, int]:
        left = self.pos
        right = left + self.src[left:].index('\n')
        value = self.src[left:right+1].strip()
        return value, len(value) + 1

    def parse_datetime_value(self, key: str) -> tuple[datetime, int]:
        value, numchars = self.parse_end_of_line_value(key)
        return datetime.fromisoformat(value), numchars

    def parse_list_value(self, key: str) -> tuple[list, int]:
        value, numchars = self.parse_end_of_line_value(key)
        if not value.startswith('{'):
            raise ValueError(f'Key {key}' + ' expects a list, must start with "{"')
        if not value.endswith('}'):
            raise ValueError(f'Key {key}' + ' expects a list, must end with "}"')
        return [x.strip() for x in value[1:-1].split(',')], numchars


def _get_tagparser(parent, tag):
    parserclass = globals()[f'{tag.name.capitalize()}Parser']
    return parserclass(parent=parent, frompos=parent.pos)
