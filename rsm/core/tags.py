"""
tags.py
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

A typical region is comprised of the following parts: a tag, an optional meta region,
the content, and the tombstone.  As mentioned before, if the region is a paragraph, the
tag is optional and the ending delimiter is a blank line instead of a Tombstone.

The content of a tag can be either itself or 'as is'.  More concretely, a block tag may
declare its 'content mode' to be 'block' or 'as is', while the content mode of an inline
tag may be 'inline' or 'as is'.  If the content mode of a (block or inline) tag is 'as
is', its contents will not be parsed at all and will be gathered into a single Text node
and added to the manuscrip tree without change.

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
    BLOCK = auto()
    INLINE = auto()
    ASIS = auto()


BLOCK = ContentMode.BLOCK
INLINE = ContentMode.INLINE
ASIS = ContentMode.ASIS


class Tag(TagName):
    delim: str = TagName.delim
    nodeclass: Type[nodes.Node] | None = None
    has_content: bool = False
    content_mode: ContentMode | None = None
    meta_inline_only: bool = False
    tag_optional: bool = False

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
        tag_optional=None,
    ):
        name = name or nodeclass.__name__.lower()
        tag = cls(name)
        tag.nodeclass = nodeclass
        tag.has_content = has_content or cls.has_content
        tag.content_mode = content_mode or cls.content_mode
        tag.meta_inline_only = meta_inline_only or cls.meta_inline_only
        tag.tag_optional = tag_optional or cls.tag_optional
        return tag


class ParagraphTag(Tag):
    nodeclass: Type[nodes.Paragraph] = nodes.Paragraph
    has_content: bool = True
    content_mode: ContentMode = INLINE
    meta_inline_only: bool = False
    tag_optional: bool = False


class BlockTag(Tag):
    nodeclass: Type[nodes.Node] | None = None
    has_content: bool = True
    content_mode: ContentMode = BLOCK
    meta_inline_only: bool = False
    tag_optional: bool = False


class InlineTag(Tag):
    nodeclass: Type[nodes.Node] | None = None
    has_content: bool = True
    content_mode: ContentMode = INLINE
    meta_inline_only: bool = True
    tag_optional: bool = False


class ManuscriptTag(BlockTag):
    nodeclass: Type[nodes.Node] = nodes.Manuscript

    def set_source(self, src):
        self.src = src

    def makenode(self) -> nodes.Node:
        return nodes.Manuscript(src=self.src)


Tombstone = Tag('')
_tags = {}
_tags['paragraph'] = ParagraphTag.newtag(nodes.Paragraph, tag_optional=True)
_tags['item'] = ParagraphTag.newtag(nodes.Item)
_tags['comment'] = ParagraphTag.newtag(nodes.Comment)
_tags['author'] = BlockTag.newtag(nodes.Author, has_content=False)
_tags['abstract'] = BlockTag.newtag(nodes.Abstract)
_tags['enumerate'] = BlockTag.newtag(nodes.Enumerate)
_tags['itemize'] = BlockTag.newtag(nodes.Itemize)
_tags['theorem'] = BlockTag.newtag(nodes.Theorem)
_tags['lemma'] = BlockTag.newtag(nodes.Lemma)
_tags['section'] = BlockTag.newtag(nodes.Section)
_tags['subsection'] = BlockTag.newtag(nodes.Subsection)
_tags['subsubsection'] = BlockTag.newtag(nodes.Subsubsection)
_tags['displaymath'] = BlockTag.newtag(nodes.DisplayMath, content_mode=ASIS)
_tags['claim'] = InlineTag.newtag(nodes.Claim)
_tags['span'] = InlineTag.newtag(nodes.Span)
_tags['keyword'] = InlineTag.newtag(nodes.Keyword, content_mode=ASIS)
_tags['math'] = InlineTag.newtag(nodes.Math, content_mode=ASIS)
_tags['ref'] = InlineTag.newtag(nodes.PendingReference, name='ref', content_mode=ASIS)
_tags['cite'] = InlineTag.newtag(nodes.Cite, content_mode=ASIS)
_tags['manuscript'] = ManuscriptTag.newtag(nodes.Manuscript)
_tags[''] = Tombstone


def get(name: str):
    if isinstance(name, TagName):
        name = name.name
    try:
        return _tags[name]
    except KeyError as e:
        raise KeyError(f'Unrecognized tag name {name}') from e


def all():
    return list(_tags.values())
