"""
parser.py
---------

RSM Parser: take a partial source string and output a single node.

"""

from datetime import datetime
from typing import Any, Type, Optional, Callable, cast
from dataclasses import dataclass
from abc import ABC, abstractmethod
from collections import namedtuple
from pathlib import Path
import re

from . import nodes
from . import tags
from .tags import TagName, Tag, Halmos
from .manuscript import PlainTextManuscript
from .nodes import Manuscript

from icecream import ic

import logging

logger = logging.getLogger('RSM').getChild('parse')


class RSMParserError(Exception):
    def __init__(self, pos: int, msg: str | None = None) -> None:
        self.pos = pos
        self.msg = f'Parser error at position {self.pos}' if msg is None else msg
        super().__init__(self.msg)


@dataclass(frozen=True)
class BaseParsingResult:
    success: bool
    result: Any = None
    hint: TagName | None = None
    consumed: int = 0

    @staticmethod
    def from_result(
        prev: 'BaseParsingResult',
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


@dataclass(frozen=True)
class ParsingResult(BaseParsingResult):
    result: nodes.Node | None = None


class Parser(ABC):
    """All parsers work on regions."""

    src: PlainTextManuscript | str

    def __init__(self, parent: Optional['Parser'], frompos: int):
        self.parent: Parser | None = parent
        self.frompos: int = frompos
        if parent:
            self.parent, self.src = parent, parent.src
            self.frompos = frompos if frompos else parent.frompos
            if self.frompos < parent.frompos:
                raise RSMParserError(
                    frompos,
                    f'Starting position {frompos} cannot be '
                    'less than parent\'s {parent.frompos}',
                )
        else:
            self.src: str = ''
        self.pos = self.frompos

    @abstractmethod
    def process(self) -> BaseParsingResult:
        pass

    def _pre_process(self) -> None:
        pass

    def _post_process(self) -> None:
        pass

    def parse(self) -> BaseParsingResult:
        _s = f'{self.__class__.__name__}'
        if hasattr(self, 'tag'):
            _s += f'({self.tag})'
        self._pre_process()
        s = _s + ' start' + f', {self.pos}'
        logger.debug(s)
        result = self.process()
        s = _s + ' end' + f', {self.pos}'
        logger.debug(s)
        self._post_process()
        return result

    def consume_whitespace(self) -> int:
        """Skip any whitespace characters and return the number of characters skipped."""
        oldpos = self.pos
        self.pos += len(self.src[self.pos :]) - len(self.src[self.pos :].lstrip())
        return self.pos - oldpos

    def consume_halmos(self) -> int:
        num = len(Halmos)
        self.pos += num
        return num

    def get_tagname_at_pos(self, consume: bool = False) -> TagName | None:
        """Return the first tag starting at self.pos. If skip is True, skip it and update self.pos."""
        if self.src[self.pos] != TagName.delim:
            return None
        if self.src[self.pos - 1] == '\\':  # ignore escaped delimiters!
            return None
        index = self.src.index(TagName.delim, self.pos + 1)
        tag = TagName(str(self.src[self.pos + 1 : index]))
        if consume:
            self.pos += len(tag)
        return tag

    def get_lines_until(
        self, condition: Callable, consume: bool = False
    ) -> tuple[str, int]:
        content = ''
        pos = self.pos
        while True:
            idx = self.src.find('\n', pos)
            line = self.src[pos : idx + 1]
            content += line
            pos = idx + 1
            if condition(line):
                break
        if consume:
            self.pos = pos
        return content, pos

    def get_subparser(self, tag: Tag) -> 'Parser':
        if tag == Halmos or not tag.name:
            raise RSMParserError(self.pos, 'Requesting parser for Halmos')
        try:
            parserclass = _parsers[tag.name]
        except KeyError as e:
            raise RSMParserError(self.pos, f'No parser for tag {tag}') from e
        return parserclass(self, self.pos, tags.get(tag.name))


class ParagraphParser(Parser):
    """Paraser for regions that are paragraphs. Whether the tag is optional is read from the
    tag object itself."""

    def __init__(
        self,
        parent: Parser,
        frompos: int,
        tag: Tag = tags.get('paragraph'),
    ):
        super().__init__(parent=parent, frompos=frompos)
        self.tag = tag
        self.node = cast(nodes.Paragraph, tag.makenode())
        if not isinstance(self.node, nodes.BaseParagraph):
            raise TypeError(
                'ParagraphParser called with a tag that created a non-Paragraph '
                f'node ({type(self.node)})'
            )

    def _pre_process(self) -> None:
        cease = self.src[: self.frompos].rfind('\n')
        start = self.src[:cease].rfind('\n')
        preceeding_line = self.src[start:cease]
        if preceeding_line.strip() != '':
            raise RSMParserError(
                self.pos, 'Paragraphs must be preceeded by blank lines'
            )

    def process(self) -> ParsingResult:
        self.pos = self.frompos

        tag = self.get_tagname_at_pos()
        if not self.tag.tag_optional:
            if not tag:
                raise RSMParserError(
                    self.pos, f'Was expecting {self.tag}, found nothing'
                )
            if tag != self.tag:
                raise RSMParserError(
                    self.pos, f'Was expecting {self.tag} tag, found {tag}'
                )

        if tag and tag.name == self.tag.name:
            self.parse_meta()

        result = self.parse_content()
        self.consume_whitespace()
        if self.pos == self.frompos:
            return ParsingResult(success=False, result=None, hint=None, consumed=0)

        self.node.append(result.result)

        return ParsingResult(
            success=True,
            result=self.node,
            hint=None,
            consumed=self.pos - self.frompos,
        )

    def parse_meta(self) -> None:
        self.pos += len(self.tag)
        self.consume_whitespace()
        metaparser = MetaParser(self, self.pos, self.tag.meta_inline_only)
        result = metaparser.parse_into_node(self.node)
        if not result.success:
            raise RSMParserError(
                self.pos,
                f'Problem reading meta for paragraph block at position {self.pos}',
            )
        self.pos += result.consumed
        self.consume_whitespace()

    def parse_content(self) -> BaseParsingResult:
        oldpos = self.pos
        # every paragraph must end with a blank line
        _, end_of_content = self.get_lines_until(lambda l: l == '\n')

        children = []
        end_at_halmos = False
        end_at_block = False
        hint = None
        while self.pos < end_of_content:
            tagname = self.get_tagname_at_pos()
            if tagname:
                if tagname == Halmos:
                    end_at_halmos = True
                    hint = Halmos
                    break

                nexttag = tags.get(tagname)
                if isinstance(nexttag, tags.BlockTag):
                    # Paragraph regions cannot contain blocks, so if we find a block,
                    # just end the paragraph here.
                    end_at_block = True
                    hint = tagname
                    break
                parser = self.get_subparser(tagname)
                result = parser.parse()
                child, consumed = result.result, result.consumed
                children.append(child)
            else:
                index = self.src.find(Tag.delim, self.pos, end_of_content)
                if index < 0:
                    index = end_of_content
                text = self.src[self.pos : index]
                consumed = len(text)
                if text.strip():
                    child = nodes.Text(text=text.escape())
                    children.append(child)

            self.pos += consumed

        if not end_at_halmos and not end_at_block:
            # Every paragraph ends with (at least) two new lines.  The first one is the end
            # of line of the last line in the paragraph.  The second one is the obligatory
            # blank line after the paragraph.  Both are unnecessary in the final output.
            if children and isinstance(children[-1], nodes.Text):
                children[-1].text = children[-1].text[:-2]

        return BaseParsingResult(
            success=True, result=children, hint=hint, consumed=self.pos - oldpos
        )


class InlineContentParser(Parser):
    def process(self) -> BaseParsingResult:
        oldpos = self.pos
        children = []

        left = self.pos
        while not self.src[self.pos :].startswith(Halmos):
            tagname = self.get_tagname_at_pos()
            if tagname is None:
                self.pos += 1
                continue
            tag = tags.get(tagname)
            if not isinstance(tag, tags.InlineTag):
                raise RSMParserError(self.pos, f'Tag {tag} cannot be inline')
            if self.pos > left:
                children.append(nodes.Text(text=self.src[left : self.pos].escape()))
            parser = self.get_subparser(tag)
            result = parser.parse()
            children.append(result.result)
            self.pos += result.consumed
            left = self.pos

        if self.pos > left:
            children.append(nodes.Text(text=self.src[left : self.pos].escape()))

        return BaseParsingResult(
            success=True, result=children, hint=None, consumed=self.pos - oldpos
        )


class AsIsContentParser(Parser):
    def process(self) -> ParsingResult:
        oldpos = self.pos
        index = self.src.index(Halmos, self.pos)
        content = self.src[self.pos : index]
        node = nodes.Text(text=content.escape())
        self.pos = index
        return ParsingResult(
            success=True, result=node, hint=Halmos, consumed=self.pos - oldpos
        )


class DelimitedRegionParser(Parser):
    """Parser for regions with a set starting string and ending string."""

    def __init__(self, parent: Parser | None, frompos: int, start: str, end: str):
        super().__init__(parent=parent, frompos=frompos)
        if not start.strip():
            raise RSMParserError(self.pos, 'Block starting string cannot be whitespace')
        self.start = start
        if not end.strip():
            raise RSMParserError(self.pos, 'Block ending string cannot be whitespace')
        self.end = end

    def _pre_process(self) -> None:
        super()._pre_process()
        if not self.src[self.frompos :].startswith(self.start):
            raise RSMParserError(
                self.pos,
                f'Did not find starting string "{self.start}" '
                f'in source at position {self.frompos}',
            )

    def _post_process(self) -> None:
        src = self.src[: self.pos]
        if not src.rstrip().endswith(self.end):
            name = self.__class__.__name__
            raise RSMParserError(
                self.pos, f'{name} did not find ending string "{self.end}"'
            )
        super()._post_process()


class TagRegionParser(DelimitedRegionParser):
    """Parser for regions that start at a tag and end with a Halmos.

    This includes all blocks and all inlines.

    Only for nodes whose content will be parsed into children and added to self.node.

    """

    contentparsers = {
        tags.BLOCK: ParagraphParser,
        tags.INLINE: InlineContentParser,
        tags.ASIS: AsIsContentParser,
    }

    def __init__(self, parent: Parser | None, frompos: int, tag: Tag):
        super().__init__(parent=parent, frompos=frompos, start=tag, end=Halmos)
        self.tag: Tag = tag
        self.node: nodes.NodeWithChildren = tag.makenode()
        if self.tag.has_content and tag.content_mode is not None:
            self.contentparser: Type[Parser] = self.contentparsers[tag.content_mode]

    def process(self) -> ParsingResult:
        oldpos = self.pos
        self.consume_starttag()
        self.consume_whitespace()
        metaparser = MetaParser(self, self.pos, self.tag.meta_inline_only)
        result = metaparser.parse_into_node(self.node)
        self.pos += result.consumed

        if not result.success:
            raise RSMParserError(
                self.pos, '{self.__class__.__name__} could not parse meta block'
            )

        if result.hint == Halmos:
            self.consume_halmos()
            return ParsingResult(
                success=True,
                result=self.node,
                hint=None,
                consumed=self.pos - oldpos,
            )
        self.consume_whitespace()

        if not self.tag.has_content:
            return ParsingResult.from_result(
                result, result=self.node, consumed=self.pos - oldpos
            )

        tag = result.hint if result.hint is not None else self.get_tagname_at_pos()
        result = self.parse_content(tag)

        return ParsingResult.from_result(result, consumed=self.pos - oldpos)

    def parse_content(self, starting_tag: TagName | None) -> ParsingResult:
        s = f'{self.__class__.__name__}.parse_content start'
        oldpos = self.pos

        hint = starting_tag
        while hint != Halmos:
            if hint is None:
                parser = self.contentparser(self, self.pos)
            else:
                nexttag = tags.get(hint)
                if self.tag.content_mode == tags.BLOCK:
                    if isinstance(nexttag, tags.InlineTag):
                        # We have found an inline tag at the start of a block that we
                        # expected to be a paragraph.  Since all our children must be
                        # paragraphs, create a paragraph parser instead of the
                        # appropriate inline parser, and let the paragraph parser take
                        # care of the inline tag we have just found.
                        nexttag = tags.get('paragraph')
                elif self.tag.content_mode == tags.INLINE:
                    if isinstance(nexttag, tags.BlockTag):
                        # Inline regions cannot contain blocks!
                        raise RSMParserError(
                            self.pos, f'Found block {nexttag} inside inline {self.tag}'
                        )
                parser = self.get_subparser(nexttag)

            result = parser.parse()
            if not result.success:
                raise RSMParserError(self.pos, 'Something went wrong')

            self.node.append(result.result)
            self.pos += result.consumed

            self.consume_whitespace()
            hint = self.get_tagname_at_pos()

        self.consume_halmos()

        return ParsingResult(
            success=True,
            result=self.node,
            hint=hint,
            consumed=self.pos - oldpos,
        )

    def consume_starttag(self) -> int:
        if self.pos != self.frompos:
            raise ValueError(
                'consume_starttag can only be called when self.pos == self.frompos'
            )
        numchars = len(self.tag)
        self.pos += numchars
        return numchars


class SpecialTagRegionParser(DelimitedRegionParser):
    """For regions delimited by tags and Halmoss but whose content is 'special' i.e. it
    won't be parsed recursively.

    """

    def __init__(self, parent: Parser, frompos: int, tag: Tag):
        super().__init__(
            parent=parent,
            frompos=frompos,
            start=tag,
            end=Halmos,
        )
        self.tag = tag
        self.node = None

    def process(self) -> ParsingResult:
        oldpos = self.pos
        self.pos += len(self.tag)
        self.consume_whitespace()

        # Tag delimiters (i.e. ':') are allowed within the content of a special tag.  So
        # we keep searching until we find a Halmos.
        right = self.src.find(Tag.delim, self.pos)
        while not self.src[right:].startswith(Halmos):
            right = self.src.find(Tag.delim, right + 1)
        content = self.src[self.pos : right]

        self.node = self.parse_content(content)

        self.pos = right
        self.consume_halmos()
        return ParsingResult(
            success=True,
            result=self.node,
            hint=None,
            consumed=self.pos - oldpos,
        )

    def parse_content(self, content: str) -> nodes.Node:
        raise NotImplementedError


class LabelCommaTextParser(SpecialTagRegionParser):
    def parse_content(self, content: str, cls: Type[nodes.Node]) -> Type[nodes.Node]:
        split = content.split(',')
        if len(split) > 1:
            if len(split) > 2:
                raise RSMParserError(
                    self.pos,
                    'Use either ":ref:<label>::" or ":ref:<label>, <reftext>::"',
                )
            label, reftext = split[0].strip(), split[1]
        else:
            label, reftext = content.strip(), None
        return cls(target=label, overwrite_reftext=reftext)


class RefParser(LabelCommaTextParser):
    def parse_content(self, content: str) -> nodes.PendingReference:
        return super().parse_content(content, nodes.PendingReference)


class URLParser(LabelCommaTextParser):
    def parse_content(self, content: str) -> nodes.URL:
        return super().parse_content(content, nodes.URL)


class PrevParser(LabelCommaTextParser):
    def parse_content(self, content: str) -> nodes.PendingReference:
        return super().parse_content(content, nodes.PendingPrev)


class CiteParser(SpecialTagRegionParser):
    def parse_content(self, content: str) -> nodes.PendingCite:
        targets = [s.strip() for s in content.split(',')]
        return nodes.PendingCite(targetlabels=targets)


class ShouldHaveHeadingParser(TagRegionParser):
    def _pre_process(self) -> None:
        super()._pre_process()
        if not isinstance(self.node, nodes.Heading):
            raise RSMParserError(
                self.pos,
                f'Processing node of type {type(self.node)} as if it was a subclass of nodes.Heading.'
                f'Instead of using {type(self)}, use {self.__class__.__bases__[0]} instead',
            )

    def _post_process(self) -> None:
        self.node: nodes.Heading
        if not self.node.title:
            nodeclass = self.node.__class__.__name__
            logger.warning(f'{nodeclass} with empty title')
        super()._post_process()


class MetaParser(Parser):
    """Parser for regions that contain the meta pairs of some other region."""

    inline_meta_open_delim = '{'
    inline_meta_close_delim = '}'

    def __init__(
        self,
        parent: Parser,
        frompos: int = 0,
        inline_only: bool = False,
    ):
        super().__init__(parent=parent, frompos=frompos)
        self.inline_only: bool = inline_only
        self.inline_mode: bool | None = True if inline_only else None
        self.validkeys: set = set()

    def parse_into_node(self, node: nodes.Node) -> ParsingResult:
        self.validkeys = node.metakeys()
        result = self.parse()
        if result.success:
            node.ingest_dict_as_meta(result.result)
            return ParsingResult.from_result(result, result=node)
        else:
            return ParsingResult.from_result(result, result=None, hint=None)

    def process(self) -> BaseParsingResult:
        oldpos = self.pos

        if self.inline_mode is None:
            if self.src[self.frompos] == self.inline_meta_open_delim:
                self.inline_mode = True
            elif self.src[self.frompos :].startswith(Tag.delim):
                self.inline_mode = False
            else:
                return BaseParsingResult(True, {}, None, 0)

        if self.inline_mode:
            if self.src[self.frompos] != self.inline_meta_open_delim:
                return BaseParsingResult(True, {}, None, 0)
            else:
                self.pos += len(self.inline_meta_open_delim)

        pairparser = MetaPairParser(parent=self, validkeys=self.validkeys)
        meta = {}
        numchars = 0
        found = False
        while True:
            result = pairparser.parse()
            if result.success:
                found = True
                key, value = result.result
                meta[str(key)] = value
                self.pos += result.consumed
                numchars += result.consumed
                numchars += self.consume_whitespace()
                if result.hint == Halmos:
                    result = BaseParsingResult(
                        success=True,
                        result=meta,
                        hint=Halmos,
                        consumed=numchars,
                    )
                    break
                if result.hint == pairparser.delim:
                    self.pos += len(pairparser.delim)
                    self.consume_whitespace()
                pairparser.frompos, pairparser.pos = self.pos, self.pos

            else:
                result = BaseParsingResult(
                    success=True,
                    result=meta,
                    hint=result.hint,
                    consumed=numchars,
                )
                break

        if self.inline_mode and found:
            self.consume_whitespace()
            if self.src[self.pos] != self.inline_meta_close_delim:
                raise RSMParserError(
                    self.pos,
                    f'Expected {self.inline_meta_close_delim} after inline meta, found {self.src[self.pos]}',
                )
            self.pos += len(self.inline_meta_close_delim)
            self.consume_whitespace()
            result = BaseParsingResult(
                success=True,
                result=meta,
                hint=None,
                consumed=self.pos - oldpos,
            )

        self.pos += result.consumed
        return result


class MetaPairParser(Parser):
    """Parser for a region that contains a single meta pair."""

    parent: MetaParser

    parse_value_methods = {
        # Node
        'label': 'parse_upto_delim_value',
        'types': 'parse_list_value',
        'reftext': 'parse_upto_delim_value',
        # Heading
        'title': 'parse_upto_delim_value',
        # Author
        'date': 'parse_datetime_value',
        'name': 'parse_upto_delim_value',
        'affiliation': 'parse_upto_delim_value',
        'email': 'parse_upto_delim_value',
        # Abstract
        'keywords': 'parse_list_value',
        'MSC': 'parse_list_value',
        # Span
        'strong': 'parse_bool_value',
        'emphas': 'parse_bool_value',
        'little': 'parse_bool_value',
        'insert': 'parse_bool_value',
        'delete': 'parse_bool_value',
        'number': 'parse_bool_value',
        'nonum': 'parse_bool_value',
        # Theorem
        'goals': 'parse_list_value',
        'stars': 'parse_int_value',
        'clocks': 'parse_int_value',
        # Figure
        'path': 'parse_path_value',
        'caption': 'parse_paragraph_value',
    }

    block_delim = '\n'
    inline_delim = ','

    def __init__(self, parent: MetaParser, validkeys: set):
        super().__init__(parent=parent, frompos=parent.pos)
        self.validkeys = validkeys

    def process(self) -> BaseParsingResult:
        oldpos = self.pos

        # find the key
        key = self.get_tagname_at_pos()
        if not key:
            return ParsingResult(
                success=False,
                result=None,
                hint=None,
                consumed=self.pos - oldpos,
            )

        # check if key is valid
        if key.name not in self.validkeys:
            return ParsingResult(
                success=False,
                result=None,
                hint=key,
                consumed=self.pos - oldpos,
            )

        # advance and find the value
        self.pos += len(key)
        self.consume_whitespace()
        try:
            method_name = self.parse_value_methods[key.name]
        except KeyError as e:
            raise RSMParserError(
                self.pos,
                f'A parsing method for {key} has not been registered '
                'in MetaPairParser.parse_value_methods',
            ) from e
        value, numchars = getattr(self, method_name)(key.name)
        self.pos += numchars
        self.consume_whitespace()

        # setup hint
        if self.src[self.pos :].startswith(self.delim):
            hint = self.delim
        elif self.src[self.pos :].startswith(Halmos):
            hint = Halmos
        else:
            hint = None

        return BaseParsingResult(
            success=True,
            result=(key.name, value),
            hint=hint,
            consumed=self.pos - oldpos,
        )

    @property
    def delim(self) -> str:
        return self.inline_delim if self.parent.inline_mode else self.block_delim

    @property
    def inline_mode(self) -> bool:
        return bool(self.parent.inline_mode)

    def parse_upto_delim_value(self, key: str) -> tuple[str, int]:
        left = self.pos

        if self.inline_mode:
            right1 = self.src.find(self.parent.inline_meta_close_delim, left)
        else:
            right1 = float('inf')

        if (right2 := self.src.find(self.delim, left)) == -1:
            right2 = right1 + 1
        right = min(right1, right2)
        value = self.src[left:right]
        return value.strip(), len(value)

    def parse_paragraph_value(self, key: str) -> tuple[str, int]:
        left = self.pos
        right = self.src.index(Halmos, left)
        value = self.src[left:right]
        return value.strip(), len(value) + len(Halmos)

    def parse_int_value(self, key: str) -> tuple[int, int]:
        value, numchars = self.parse_upto_delim_value(key)
        return int(str(value)), numchars

    def parse_datetime_value(self, key: str) -> tuple[datetime, int]:
        value, numchars = self.parse_upto_delim_value(key)
        return datetime.fromisoformat(str(value)), numchars

    def parse_path_value(self, key: str) -> tuple[Path, int]:
        value, numchars = self.parse_upto_delim_value(key)
        return Path(str(value)), numchars

    def parse_bool_value(self, key: str) -> tuple[bool, int]:
        return True, 0

    def parse_list_value(self, key: str) -> tuple[list, int]:
        src = self.src[self.pos :]
        if src[0] != '{':
            # if no brace, there can only be one element in the list
            value, numchars = self.parse_upto_delim_value(key)
            if ',' in value:
                raise RSMParserError(
                    self.pos,
                    f'Key "{key}"' + ' expects a list surrounded by curlybraces; '
                    'if there is only one element, it cannot contain a comma ","',
                )
            return [value], numchars

        try:
            brace = src.index('}')
        except ValueError:
            raise RSMParserError(
                self.pos, f'Key "{key}"' + ' expects a list, could not find "}"'
            )
        try:
            colon = src.index(':')
        except RSMParserError:
            colon = brace + 1
        if colon <= brace:
            raise RSMParserError(
                self.pos, f'Key "{key}"' + ' expects a list, but found ":" before "}"'
            )

        after = src[brace + 1 :]
        inline_delim = self.parent.inline_meta_close_delim
        if not after.startswith(self.delim) and not after.startswith(inline_delim):
            raise RSMParserError(
                self.pos,
                f'Expected a "{self.delim}" or a "{inline_delim}" after value of key "{key}"',
            )

        value = src[1:brace]
        numchars = len(value) + 2
        return [x.strip() for x in value.split(',')], numchars


class BibTexParser(DelimitedRegionParser):
    def __init__(self, src) -> None:
        self.tag = tags.get('bibtex')
        super().__init__(parent=None, frompos=0, start=self.tag, end=Halmos)
        self.src = src

    def process(self) -> ParsingResult:
        oldpos = self.pos
        self.pos += len(self.tag)
        self.consume_whitespace()
        endpos = self.src.find(Halmos, self.pos)
        if endpos < -1:
            raise RSMParserError(
                self.pos, 'Could not find closing Halmos for tag {self.tag}'
            )
        all_content = self.src[self.pos : endpos]

        items = [stripped for it in all_content.split('@') if (stripped := it.strip())]
        children = []
        for item in items:
            pairs = {}
            match = re.match(r'(\w+)\s*{([^,]*),\s*(.*)\s*}', item, re.DOTALL)
            if match is None:
                raise RSMParserError(self.pos, f'Could not parse bibtex item "{item}"')
            pairs['kind'] = match.group(1)
            pairs['label'] = match.group(2)
            content = match.group(3).strip()

            spans = []
            # RSM only accepts fields surrounded by curly braces, NOT quotes.
            patterns = [
                r'([^=]*)=\s*{([^}]*)}\s*,?',
                # r'([^=]*)=\s*\"([^\"]*)\"',
                # r'([^=]*)=\s*([^,]*),',
            ]
            for pat in patterns:
                for match in re.finditer(pat, content, re.DOTALL):
                    spans.append(match.span())
                    key, val = [
                        stripped
                        for g in match.groups('')
                        if (stripped := g.strip().strip(',{}\"').strip())
                    ]
                    pairs[key.lower()] = val
            spans.sort()
            if spans[0][0] != 0:
                txt = content[slice(*spans[0])].strip()
                logger.warning(f'The key "{txt}" has not been parsed')
            if spans[-1][1] != len(content):
                txt = content[slice(*spans[-1])].strip()
                logger.warning(f'The key "{txt}" has not been parsed')
            prev = 0
            for start, cease in spans:
                if prev != start:
                    txt = content[start:cease].strip()
                    logger.warning(f'The key "{txt}" has not been parsed')
                prev = cease

            child = nodes.Bibitem()
            child.ingest_dict_as_meta(pairs)
            child.label = pairs['label']
            children.append(child)

        self.pos = endpos
        self.consume_halmos()
        return ParsingResult(
            success=True, result=children, hint=None, consumed=self.pos - oldpos
        )


class ManuscriptParser(ShouldHaveHeadingParser):
    keywords = ['LET', 'ASSUME', 'SUFFICES', 'DEFINE', 'PROVE', 'QED']
    Shortcut = namedtuple('Shortcut', 'pattern repl flags', defaults=(re.DOTALL,))

    # order matters!
    shortcuts = [
        # Having an escaped colon '\:' right behind a non-esaped colon is a BAD IDEA, so
        # before applying any other regex, we separate them.
        Shortcut(r'\\::', r'\\: :'),
        Shortcut(r'%(.*)$', r'', re.MULTILINE),
        Shortcut(r'\*\*(.*?)\*\*', r':span: {:strong:} \1::'),
        Shortcut(r'\*(.*?)\*', r':span: {:emphas:} \1::'),
        Shortcut(r'^###(.*)$', r':subsubsection:\n  :title: \1\n', re.MULTILINE),
        Shortcut(r'^##(.*)$', r':subsection:\n  :title: \1\n', re.MULTILINE),
        Shortcut(r'^#(.*)$', r':section:\n  :title: \1\n', re.MULTILINE),
        Shortcut(r'\$\$(.*?)\$\$', r':mathblock:\n  \1\n::'),
        Shortcut(r'\$(.*?)\$', r':math:\1::'),
        Shortcut(r'```(.*?)```', r':codeblock:\n  \1\n::'),
        Shortcut(r'`(.*?)`', r':code:\1::'),
        Shortcut(r'\|-(.*?)\.', r':claim:\1::.'),
        Shortcut(r'⊢(.*?)\.', r':claim:\1::.'),
        Shortcut(r':prev:(?=\W)', r':previous:1::'),
        Shortcut(r':prev2:(?=\W)', r':previous:2::'),
        Shortcut(r':prev3:(?=\W)', r':previous:3::'),
        # After applying all the regexes, we may have accidentally left an escaped colon
        # behind a non-escaped colon, so deal with those again.
        Shortcut(r'\\::', r'\\: :'),
    ]

    def __init__(self, src: PlainTextManuscript):
        self.tag = tags.ManuscriptTag('manuscript')
        self.tag.set_source(src)
        super().__init__(parent=None, frompos=0, tag=self.tag)

    def parse(self) -> BaseParsingResult:
        self.node: nodes.Manuscript
        self.src = self.apply_shortcuts(self.node.src)
        return super().parse()

    def apply_shortcuts(self, src: PlainTextManuscript) -> PlainTextManuscript:
        logger.debug('applying shortcuts')

        src = str(src)
        for keyword in self.keywords:
            src = src.replace(keyword, f':keyword:{keyword} ::')

        for pattern, replacement, flags in self.shortcuts:
            src = re.sub(pattern, replacement, src, flags=flags)

        return PlainTextManuscript(src)


class MainParser:
    def __init__(self) -> None:
        self.src: PlainTextManuscript | None = None
        self.tree: nodes.Manuscript | None = None

    def parse(self, src: str) -> nodes.Manuscript:
        logger.info('Parsing...')

        self.src = src.strip()
        parser = ManuscriptParser(self.src)
        self.tree = parser.parse().result
        parser.consume_whitespace()

        # note here we must compare against len(parser.src) and NOT against
        # len(self.src) because the parser will most likely have changed the source by
        # applying shortcuts
        if parser.pos >= len(parser.src):
            return self.tree
        # likewise, we must take the input to BibTexParser from parser.src, NOT from
        # self.src
        bibsrc = parser.src[parser.pos :].strip()

        parser = BibTexParser(bibsrc)
        result = parser.parse()
        bib_nodes = list(self.tree.traverse(nodeclass=nodes.Bibliography))
        if len(bib_nodes) > 1:
            raise RSMParserError(parser.pos, 'Found more than one bibtex node')
        if bib_nodes:
            bib_nodes[0].append(result.result)
            if len(bib_nodes) > 1:
                logger.warning(
                    'Found more than one bibliography tag, using first one',
                )
        else:
            logger.warning(
                'Did not find a bibliography node to add the bib items to',
            )
        return self.tree


_parsers: dict[str, Type[Parser]] = {}
for t in tags.all():
    if isinstance(t, tags.ParagraphTag):
        _parsers[t.name] = ParagraphParser
    elif isinstance(t, tags.BlockTag):
        _parsers[t.name] = TagRegionParser
    elif isinstance(t, tags.InlineTag):
        _parsers[t.name] = TagRegionParser
    elif isinstance(t, tags.Tag):
        if t is Halmos:
            continue
        raise RSMParserError(None, f"I don't know what to do with tag {t}")
_parsers['bibtex'] = BibTexParser
_parsers['ref'] = RefParser
_parsers['url'] = URLParser
_parsers['previous'] = PrevParser
_parsers['cite'] = CiteParser
_parsers['manuscript'] = ManuscriptParser
