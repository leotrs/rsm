"""
parser.py
---------

RSM Parser: take a partial source string and output a single node.

"""

from datetime import datetime
from typing import Any, Type
from dataclasses import dataclass
from abc import ABC, abstractmethod

from . import nodes

from icecream import ic
import logging
logger = logging.getLogger('RSM').getChild('Parser')

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

    @staticmethod
    def from_result(
            prev: 'ParsingResult',
            *,
            success: bool = None,
            result: Any = None,
            hint: Tag = None,
            consumed: int = None,
    ) -> 'ParsingResult':
        return ParsingResult(
            success=success if success else prev.success,
            result=result if result else prev.result,
            hint=hint if hint else prev.hint,
            consumed=consumed if consumed else prev.consumed,
        )


class Parser(ABC):
    def __init__(self, parent: 'Parser' = None, frompos: int = 0, src: str = None):
        self.parent: Parser | None = None
        self.src: str | None = src
        self.frompos: int = 0
        self.pos: int = 0
        if parent:
            self.parent, self.src = parent, parent.src
            self.frompos = frompos if frompos else parent.frompos
            if self.frompos < parent.frompos:
                raise RSMParserError(
                    f'Starting position {frompos} cannot be '
                    'less than parent\'s {parent.frompos}'
                )
        else:
            self.frompos = frompos
        self.pos = self.frompos

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
        num = len(Tombstone)
        self.pos += num
        return num

    def get_tag_at_pos(self, consume) -> Tag:
        """Return the first tag starting at self.pos. If skip is True, skip it and update self.pos."""
        if self.src[self.pos] != Tag.delim:
            return None

        src = self.src[self.pos:]
        index = src[1:].index(Tag.delim)
        tag = Tag(src[1:index + 1])
        if consume:
            self.pos += len(tag)

        return tag


class ParseMetaMixIn:

    def parse_meta(self) -> ParsingResult:
        oldpos = self.pos
        parser = MetaParser(
            parent=self,
            nodeclass=self.nodeclass,
            frompos=self.pos,
            inline_mode=self.meta_inline_mode,
        )
        result = parser.parse()
        if result.success:
            for key, value in result.result.items():
                setattr(self.node, key, value)
            self.pos += result.consumed
            return ParsingResult(
                success=True,
                result=result.result,
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


class BaseParagraphParser(Parser, ParseMetaMixIn):

    def __init__(
            self,
            parent: Parser,
            nodeclass: Type[nodes.Node],
            tag: Tag,
            frompos: int = 0,
            tag_optional: bool = True,
            *,
            meta_inline_mode: bool | None = None,
    ):
        super().__init__(parent=parent, frompos=frompos)
        self.nodeclass: Type[nodes.Node] = nodeclass
        self.node: nodes.Paragraph = None
        self.tag: Tag = tag
        self.tag_optional: bool = tag_optional
        self.meta_inline_mode: bool | None = meta_inline_mode

    def _pre_process(self) -> None:
        cease = self.src[:self.frompos].rfind('\n')
        start = self.src[:cease].rfind('\n')
        preceeding_line = self.src[start:cease]
        if preceeding_line.strip() != '':
            raise RSMParserError('Paragraphs must be preceeded by blank lines')

    def process(self) -> ParsingResult:
        s = f'{self.__class__.__name__}.process start'
        ic(s, self.pos)
        self.pos = self.frompos
        self.node = self.nodeclass()

        tag = self.get_tag_at_pos(consume=False)
        if not self.tag_optional:
            if not tag:
                raise RSMParserError(f'Was expecting {self.tag}, found nothing')
            if tag != self.tag:
                raise RSMParserError(f'Was expecting {self.tag} tag, found {tag}')

        if tag:
            self.pos += len(self.tag)
            self.consume_whitespace()
            result = self.parse_meta()
            if not result.success:
                raise RSMParserError(f'Problem reading meta for paragraph block at position {self.pos}')
            self.consume_whitespace()

        result = self.parse_content()
        self.consume_whitespace()
        if self.pos == self.frompos:
            s = f'{self.__class__.__name__}.process end - did not find ANY characters'
            ic(s, self.pos)
            return ParsingResult(
                success=False,
                result=None,
                hint=NoHint,
                consumed=0
            )

        self.node.add(result.result)

        s = f'{self.__class__.__name__}.process end'
        ic(s, self.pos)
        return ParsingResult(
            success=True,
            result=self.node,
            hint=NoHint,
            consumed=self.pos - self.frompos
        )

    def parse_content(self) -> ParsingResult:
        oldpos = self.pos
        content = ''
        pos = self.pos
        while True:
            idx = self.src.find('\n', pos)
            line = self.src[pos:idx + 1]
            content += line
            pos = idx + 1
            if line == '\n':
                break
        end_of_content = pos

        pos = 0
        children = []
        while pos < len(content):
            index = content.find(':', pos)
            if index < 0:
                break
            text = content[pos:index]
            if text.strip():
                ic(text)
                children.append(nodes.Text(text=text))

            pos = index
            parser = SpanParser(self, self.pos + pos)
            ic(self.pos+pos, self.pos, self.frompos, parser.pos, parser.frompos)
            result = parser.parse()
            children.append(result.result)
            pos += result.consumed
            ic(self.pos + pos)

        if pos < len(content):
            text = content[pos:]
            if text.strip():
                ic(text)
                children.append(nodes.Text(text=text))
            pos = len(content)

        self.pos = end_of_content

        ic([type(c) for c in children])
        ic(children)
        return ParsingResult(
                success=True,
                result=children,
                hint=NoHint,
                consumed=self.pos - oldpos
            )


class ParagraphParser(BaseParagraphParser):
    def __init__(self, parent: Parser, frompos: int = 0):
        super().__init__(parent, nodes.Paragraph, Tag('paragraph'), frompos, True)


class InlineParser(Parser):

    inline_tags = {Tag('span')}

    def __init__(self, parent: Parser, frompos: int = 0):
        super().__init__(parent, frompos)

    def process(self) -> ParsingResult:
        s = f'{self.__class__.__name__}.process start'
        ic(s, self.pos)
        oldpos = self.pos
        children = []

        left = self.pos
        pos = self.pos
        while not self.src[pos:].startswith(Tombstone):
            tag = self.get_tag_at_pos(consume=False)
            if tag and tag not in self.inline_tags:
                raise RSMParserError(f'Tag {tag} cannot be inline')
            if tag:
                if pos > left:
                    children.append(nodes.Text(text=self.src[left:pos]))
                    ic(children[-1].text)
                    self.pos = pos
                parser = _get_tagparser(self, tag)
                result = parser.parse()
                children.append(result.result)
                self.pos += result.consumed
                left, pos = self.pos, self.pos
            else:
                pos += 1

        if pos > left:
            ic(pos, left, self.src[left:pos])
            children.append(nodes.Text(text=self.src[left:pos]))
            ic(children[-1].text)
            self.pos = pos

        s = f'{self.__class__.__name__}.process end'
        ic(s, self.pos)
        return ParsingResult(
            success=True,
            result=children,
            hint=NoHint,
            consumed=self.pos - oldpos
        )


class StartEndParser(Parser):

    def __init__(self, start: str, end: str, parent: Parser | None, src: str, frompos: int = 0):
        super().__init__(parent=parent, src=src, frompos=frompos)
        if not start.strip():
            raise RSMParserError('Block starting string cannot be whitespace')
        self.start = start
        if not end.strip():
            raise RSMParserError('Block ending string cannot be whitespace')
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
        if not src.rstrip().endswith(self.end):
            name = self.__class__.__name__
            raise RSMParserError(f'{name} did not find ending string "{self.end}"')
        super()._post_process()


class TagBlockParser(StartEndParser, ParseMetaMixIn):

    def __init__(
            self,
            parent: Parser | None,
            tag: Tag,
            nodeclass: Type[nodes.Node],
            frompos: int = 0,
            src: str = None,
            *,
            meta_inline_mode: bool | None = None,
            has_content: bool = True,
            contentparser: Type[Parser] = ParagraphParser,
    ):
        super().__init__(start=tag, end=Tombstone, parent=parent, src=src, frompos=frompos)
        self.tag: Tag = tag
        self.nodeclass: Type[nodes.Node] = nodeclass
        self.node: nodes.Node | None = None
        self.meta_inline_mode: bool | None = meta_inline_mode
        self.has_content: bool = has_content
        self.contentparser: Type[Parser] = contentparser

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
            return ParsingResult(
                success=True,
                result=self.node,
                hint=NoHint,
                consumed=self.pos - oldpos,
            )
        self.consume_whitespace()

        if not self.has_content:
            s = f'{self.__class__.__name__}.process end'
            ic(s, self.pos)
            return ParsingResult.from_result(
                result,
                result=self.node,
                consumed=self.pos - oldpos
            )

        if result.hint == NoHint:
            tag = self.get_tag_at_pos(consume=False)
            result = self.parse_content(tag)
        elif result.hint == NotATag:
            result = self.parse_content(None)
        elif isinstance(result.hint, Tag):
            result = self.parse_content(result.hint)

        s = f'{self.__class__.__name__}.process end'
        ic(s, self.pos)
        return ParsingResult(
            success=result.success,
            result=result.result,
            hint=result.hint,
            consumed=self.pos - oldpos,
        )

    def parse_content(self, starting_tag: Tag | None) -> ParsingResult:
        s = f'{self.__class__.__name__}.parse_content start'
        ic(s, self.pos)
        oldpos = self.pos

        hint = starting_tag
        while hint != Tombstone:
            if hint in {None, NotATag, NoHint}:
                parser = self.contentparser(self, frompos=self.pos)
            else:
                parser = _get_tagparser(self, hint)
            result = parser.parse()
            if not result.success:
                raise RSMParserError('Something went wrong')

            s = f'subparser {parser.__class__.__name__} done'
            ic(s, result.consumed)
            self.node.add(result.result)
            self.pos += result.consumed

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
            ic(self.pos, self.frompos)
            raise RSMParserError('consume_starttag can only be called when self.pos == self.frompos')
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
        logger.info('ManuscriptParser.parse()')
        self.src = src
        result = super().parse()
        assert isinstance(result.result, nodes.Manuscript)
        return result.result


class AuthorParser(TagBlockParser):
    def __init__(self, parent: Parser, frompos: int = 0):
        super().__init__(parent, Tag('author'), nodes.Author, frompos, has_content=False)


class AbstractParser(TagBlockParser):
    def __init__(self, parent: Parser, frompos: int = 0):
        super().__init__(parent, Tag('abstract'), nodes.Abstract, frompos)


class SectionParser(TagBlockParser):
    def __init__(self, parent: Parser, frompos: int = 0):
        super().__init__(parent, Tag('section'), nodes.Section, frompos)


class ItemParser(BaseParagraphParser):
    def __init__(self, parent: Parser, frompos: int = 0):
        super().__init__(parent, nodes.Item, Tag('item'), frompos, tag_optional=False)
        if type(parent) not in [EnumerateParser, ItemizeParser]:
            ic(type(parent))
            raise RSMParserError('Found an :item: ouside of :enumerate: or :itemize:')


class EnumerateParser(TagBlockParser):
    def __init__(self, parent: Parser, frompos: int = 0):
        super().__init__(parent, Tag('enumerate'), nodes.Enumerate, frompos)


class ItemizeParser(TagBlockParser):
    def __init__(self, parent: Parser, frompos: int = 0):
        super().__init__(parent, Tag('itemize'), nodes.Section, frompos)


class SpanParser(TagBlockParser):
    def __init__(self, parent: Parser, frompos: int = 0):
        super().__init__(
            parent=parent,
            tag=Tag('span'),
            nodeclass=nodes.Span,
            frompos=frompos,
            meta_inline_mode=True,
            contentparser=InlineParser,
        )


class MetaParser(Parser):
    def __init__(
            self,
            parent: Parser,
            nodeclass: Type[nodes.Node],
            frompos: int = 0,
            inline_mode: bool | None = None,
    ):
        super().__init__(parent=parent, frompos=frompos)
        self.nodeclass: Type[nodes.Node] = nodeclass
        self.inline_mode: bool | None = inline_mode

    def process(self) -> ParsingResult:
        oldpos = self.pos
        s = f'{self.__class__.__name__}.process start'
        ic(s, self.pos)

        if not self.src[self.frompos].startswith(':'): # there is no meta
            return ParsingResult(True, {}, NoHint, 0)

        left = self.frompos
        right = left + self.src[left:].index('\n')

        if self.inline_mode is None and Tombstone in self.src[left:right]:
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
                if result.hint == Tombstone:
                    result = ParsingResult(
                        success=True,
                        result=meta,
                        hint=Tombstone,
                        consumed=numchars,
                    )
                    break
                if result.hint == pairparser.delim:
                    self.pos += len(pairparser.delim)
                    self.consume_whitespace()
                pairparser.frompos, pairparser.pos = self.pos, self.pos

            else:
                result = ParsingResult(
                    success=True,
                    result=meta,
                    hint=result.hint,
                    consumed=numchars,
                )
                break

        if self.inline_mode:
            ic(self.pos)
            self.consume_whitespace()
            if not self.src[self.pos:].startswith(Tombstone):
                raise RSMParserError('Expected {Tombstone} after inline meta')
            self.consume_tombstone()
            self.consume_whitespace()
            result = ParsingResult(
                success=True,
                result=meta,
                hint=NoHint,
                consumed=self.pos - oldpos,
            )

        s = f'{self.__class__.__name__}.process end ({result.hint})'
        ic(s, self.pos)
        return result


class MetaPairParser(Parser):

    parse_value_methods = {
        'label': 'parse_upto_delim_value',
        'title': 'parse_upto_delim_value',
        'date': 'parse_datetime_value',
        'name': 'parse_upto_delim_value',
        'affiliation': 'parse_upto_delim_value',
        'email': 'parse_upto_delim_value',
        'keywords': 'parse_list_value',
        'MSC': 'parse_list_value',
        'types': 'parse_list_value',
        'strong': 'parse_bool_value',
        'emphas': 'parse_bool_value',
        'little': 'parse_bool_value',
        'insert': 'parse_bool_value',
        'delete': 'parse_bool_value',
    }

    block_delim = '\n'
    inline_delim = ','

    def __init__(self, parent: Type[Parser]):
        super().__init__(parent=parent)
        self.nodeclass: Type[nodes.Node] = parent.nodeclass

    def process(self) -> ParsingResult:
        s = f'{self.__class__.__name__}.process start'
        ic(s, self.pos)
        oldpos = self.pos

        # find the key
        key = self.get_tag_at_pos(consume=True)
        if not key:
            return ParsingResult(
                success=False,
                result=None,
                hint=NoHint,
                consumed=self.pos - oldpos,
            )
        key = key.name

        # check if key is valid
        if key not in self.nodeclass.metakeys() | nodes.Node.globalmetakeys:
            return ParsingResult(
                success=False,
                result=None,
                hint=Tag(key),
                consumed=self.pos - oldpos,
            )

        # find the value
        self.consume_whitespace()
        try:
            method_name = self.parse_value_methods[key]
        except KeyError as e:
            raise RSMParserError(
                f'A parsing method for {Tag(key)} has not been registered '
                'in MetaPairParser.parse_value_methods') from e
        value, numchars = getattr(self, method_name)(key)
        self.pos += numchars
        self.consume_whitespace()

        # setup hint
        if self.src[self.pos:].startswith(self.delim):
            hint = self.delim
        elif self.src[self.pos:].startswith(Tombstone):
            hint = Tombstone
        else:
            hint = NoHint

        s = f'{self.__class__.__name__}.process end'
        ic(s, self.pos, key, value)
        return ParsingResult(
            success=True,
            result=(key, value),
            hint=hint,
            consumed=self.pos - oldpos,
        )

    @property
    def delim(self) -> str:
        return self.inline_delim if self.parent.inline_mode else self.block_delim

    def parse_upto_delim_value(self, key: str) -> tuple[str, int]:
        left = self.pos
        right1 = self.src.index(Tombstone, left)
        try:
            right2 = self.src.index(self.delim, left)
        except ValueError:
            right2 = right1 + 1
        right = min(right1, right2)
        value = self.src[left:right]
        return value.strip(), len(value)

    def parse_datetime_value(self, key: str) -> tuple[datetime, int]:
        value, numchars = self.parse_upto_delim_value(key)
        return datetime.fromisoformat(value), numchars

    def parse_bool_value(self, key: str) -> tuple[bool, int]:
        return True, 0

    def parse_list_value(self, key: str) -> tuple[list, int]:
        src = self.src[self.pos:]
        if src[0] != '{':
            raise RSMParserError(f'Key "{key}"' + ' expects a list, must start with "{"')

        try:
            brace = src.index('}')
        except ValueError:
            raise RSMParserError(f'Key "{key}"' + ' expects a list, could not find "}"')
        try:
            colon = src.index(':')
        except RSMParserError:
            colon = brace+1
        if colon <= brace:
            raise RSMParserError(f'Key "{key}"' + ' expects a list, but found ":" before "}"')

        after = src[brace+1:]
        if not after.startswith(self.delim) and not after.startswith(' ' + Tombstone):
            raise RSMParserError(f'Expected a "{self.delim}" or a "{Tombstone}" after value of key "{key}"')

        value = src[1:brace]
        numchars = len(value) + 2
        return [x.strip() for x in value.split(',')], numchars


def _get_tagparser(parent, tag):
    try:
        parserclass = globals()[f'{tag.name.capitalize()}Parser']
    except KeyError as e:
        raise RSMParserError(f'Unknown tag {tag}') from e
    return parserclass(parent=parent, frompos=parent.pos)
