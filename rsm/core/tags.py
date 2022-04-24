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


Tombstone = Tag('')
_tags = {}
_tags['paragraph'] = BlockTag.newtag(nodes.Paragraph)
_tags['author'] = BlockOnlyTag.newtag(nodes.Author, has_content=False)
_tags['abstract'] = BlockOnlyTag.newtag(nodes.Abstract)
_tags['enumerate'] = BlockTag.newtag(nodes.Enumerate)
_tags['itemize'] = BlockTag.newtag(nodes.Itemize)
_tags['item'] = BlockTag.newtag(nodes.Item)
_tags['comment'] = BlockTag.newtag(nodes.Comment)
_tags['theorem'] = BlockOnlyTag.newtag(nodes.Theorem)
_tags['lemma'] = BlockOnlyTag.newtag(nodes.Lemma)
_tags['displaymath'] = BlockOnlyTag.newtag(nodes.DisplayMath, content_mode=ASIS)
_tags['section'] = BlockOnlyTag.newtag(nodes.Section)
_tags['subsection'] = BlockOnlyTag.newtag(nodes.Subsection)
_tags['subsubsection'] = BlockOnlyTag.newtag(nodes.Subsubsection)
_tags['keyword'] = BlockTag.newtag(nodes.Keyword, content_mode=ASIS)
_tags['claim'] = InlineTag.newtag(nodes.Claim)
_tags['span'] = InlineTag.newtag(nodes.Span)
_tags['math'] = InlineTag.newtag(nodes.Math, content_mode=ASIS)
_tags['ref'] = SpecialInlineTag.newtag(nodes.PendingReference, name='ref')
_tags['cite'] = SpecialInlineTag.newtag(nodes.Cite)
_tags['manuscript'] = ManuscriptTag.newtag(nodes.Manuscript)
_tags[''] = Tombstone


def get(name: str):
    if isinstance(name, TagName):
        name = name.name
    try:
        return _tags[name]
    except KeyError as e:
        raise KeyError(f'Unrecognized tag name {name}') from e
