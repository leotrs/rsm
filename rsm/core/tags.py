"""
tags.py
-------

Tag objects contain information about how a :tag: should be interpreted.

"""

from typing import Type
from enum import Enum, auto

from . import nodes


class TagName(str):
    delim: str = ':'
    has_content: bool = False
    inline_only: bool = True
    content_mode: ContentMode | None = None
    nodeclass: Type[nodes.Node] | None = None
    meta_inline_only: bool = False

    def __new__(cls, name):
        if isinstance(name, cls):
            return name
        return super().__new__(cls, f'{cls.delim}{name}{cls.delim}')

    def __init__(self, name):
        super().__init__()
        self.name = name

    def makenode(self) -> nodes.Node:
        if self.nodeclass is None:
            raise ValueError(f'Tag with name {self.name} cannot create nodes')
        return self.nodeclass()


Tombstone = Tag('')
NotATag = Tag('__NOT_A_TAG__')
NoHint = Tag('__NO_HINT__')
Placeholder = Tag('__PLACEHOLDER__')


class BlockTag(Tag):
    has_content: bool = True
    inline_only: bool = False
    content_mode: ContentMode = ContentMode.PARAGRAPH
    nodeclass: None = None
    meta_inline_only: bool = False


class ParagraphTag(BlockTag):
    nodeclass: Type[nodes.Node] = nodes.Paragraph


class AuthorTag(BlockTag):
    has_content: bool = False
    nodeclass: Type[nodes.Node] = nodes.Author


class AbstractTag(BlockTag):
    nodeclass: Type[nodes.Node] = nodes.Abstract


class EnumerateTag(BlockTag):
    nodeclass: Type[nodes.Node] = nodes.Enumerate


class ItemizeTag(BlockTag):
    nodeclass: Type[nodes.Node] = nodes.Itemize


class ItemTag(BlockTag):
    nodeclass: Type[nodes.Node] = nodes.Item


class CommentTag(BlockTag):
    nodeclass: Type[nodes.Node] = nodes.Comment


class TheoremTag(BlockTag):
    nodeclass: Type[nodes.Node] = nodes.Theorem


class LemmaTag(BlockTag):
    nodeclass: Type[nodes.Node] = nodes.Lemma


class DisplaymathTag(BlockTag):
    nodeclass: Type[nodes.Node] = nodes.DisplayMath
    content_mode: ContentMode = ContentMode.ASIS


class KeywordTag(BlockTag):
    nodeclass: Type[nodes.Node] = nodes.Keyword
    content_mode: ContentMode = ContentMode.ASIS


class SectionTag(BlockTag):
    nodeclass: Type[nodes.Node] = nodes.Section


class SubsectionTag(BlockTag):
    nodeclass: Type[nodes.Node] = nodes.Subsection


class SubsubsectionTag(BlockTag):
    nodeclass: Type[nodes.Node] = nodes.Subsubsection


class ManuscriptTag(BlockTag):
    nodeclass: Type[nodes.Node] = nodes.Manuscript

    def set_source(self, src):
        self.src = src

    def makenode(self) -> nodes.Node:
        return nodes.Manuscript(src=self.src)


class InlineTag(Tag):
    has_content: bool = True
    inline_only: bool = True
    content_mode: ContentMode = ContentMode.INLINE
    nodeclass: None = None
    meta_inline_only: bool = True


class ClaimTag(InlineTag):
    nodeclass: Type[nodes.Node] = nodes.Claim


class SpanTag(InlineTag):
    nodeclass: Type[nodes.Node] = nodes.Span


class MathTag(InlineTag):
    nodeclass: Type[nodes.Node] = nodes.Math
    content_mode: ContentMode = ContentMode.ASIS


class SpecialInlineTag(Tag):
    has_content: bool = False
    inline_only: bool = True
    content_mode: None = None
    nodeclass: None = None
    meta_inline_only: bool = True


class RefTag(SpecialInlineTag):
    nodeclass: Type[nodes.Node] = nodes.PendingReference


class CiteTag(SpecialInlineTag):
    nodeclass: Type[nodes.Node] = nodes.Cite


def gettag(name):
    classname = f'{name.capitalize()}Tag'
    return globals().get(classname, Tag)(name)
