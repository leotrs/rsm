"""tags.py
-------

Tag objects contain information about how a :tag: should be interpreted.

A region in a RSM document is a sequence of consecutive characters.  Ther is no other
restriction to what constitutes a region.  For example, a region may span several lines,
start and end in the middle of a sentence, or otherwise carry no real (semantic or
structural) meaning.  Tags are the way that the RSM markup language denotes which
regions are meaningful.  If a region starts with a :tag: and ends with a tombstone '::',
then it is considered a structurally meaningful region that indicates something about
the structure of the document.  There are a few exceptions to this rule (see below).

There are three different types of meaningful regions: blocks, paragraphs, and inlines.
A paragraph is a region that contains a sequence of complete sentences.  A block is a
region that can contain one or more paragraphs, as well as other block regions.  An
inline is a region that can only be contained within a paragraph or another inline.

At the time of writing, all blocks and inlines must start with a tag and end with a
tombstone.  On the other hand, paragraphs have neither restriction.

"""

from typing import Type
from enum import Enum, auto

from . import nodes


class TagName(str):
    delim: str = ':'

    def __new__(cls, name):
        if isinstance(name, cls):
            return name
        return super().__new__(cls, f'{cls.delim}{name}{cls.delim}')

    def __init__(self, name):
        super().__init__()
        self.name = name


class ContentMode(Enum):
    PARAGRAPH = auto()
    INLINE = auto()
    ASIS = auto()


PARAGRAPH = ContentMode.PARAGRAPH
INLINE = ContentMode.INLINE
ASIS = ContentMode.ASIS


class Tag(TagName):
    delim: str = TagName.delim
    has_content: bool = False
    content_mode: ContentMode | None = None
    nodeclass: Type[nodes.Node] | None = None
    meta_inline_only: bool = False
    may_be_block: bool = True
    may_be_inline: bool = True

    def makenode(self) -> nodes.Node:
        if self.nodeclass is None:
            raise ValueError(f'Tag with name {self.name} cannot create nodes')
        return self.nodeclass()

    @classmethod
    def newtag(
        cls,
        nodeclass,
        *,
        name=None,
        has_content=None,
        content_mode=None,
        meta_inline_only=None,
        may_be_block=None,
        may_be_inline=None,
    ):
        name = name or nodeclass.__name__.lower()
        tag = cls(name)
        tag.nodeclass = nodeclass
        tag.has_content = has_content or cls.has_content
        tag.content_mode = content_mode or cls.content_mode
        tag.meta_inline_only = meta_inline_only or cls.meta_inline_only
        tag.may_be_block = may_be_block or cls.may_be_block
        tag.may_be_inline = may_be_inline or cls.may_be_inline
        return tag


class InlineTag(Tag):
    has_content: bool = True
    content_mode: ContentMode = INLINE
    nodeclass: Type[nodes.Node] | None = None
    meta_inline_only: bool = True
    may_be_block: bool = False
    may_be_inline: bool = True


class SpecialInlineTag(Tag):
    has_content: bool = False
    content_mode: None = None
    nodeclass: Type[nodes.Node] | None = None
    meta_inline_only: bool = True
    may_be_block: bool = False
    may_be_inline: bool = True


class BlockTag(Tag):
    has_content: bool = True
    content_mode: ContentMode = PARAGRAPH
    nodeclass: Type[nodes.Node] | None = None
    meta_inline_only: bool = False
    may_be_block: bool = True
    may_be_inline: bool = True


class BlockOnlyTag(BlockTag):
    may_be_block: bool = True
    may_be_inline: bool = False


class ManuscriptTag(BlockOnlyTag):
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
