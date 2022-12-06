"""
tags.py
-------

Tag objects contain information about how a :tag: should be interpreted.

A region in a RSM document is a sequence of consecutive characters.  There is no other
restriction to what constitutes a region.  For example, a region may span several lines,
start and end in the middle of a sentence, or otherwise carry no real (semantic or
structural) meaning.  Tags are the way that the RSM markup language denotes which
regions are meaningful.  If a region starts with a :tag: and ends with a halmos '::',
then it is considered a structurally meaningful region that indicates something about
the structure of the document.  There are a few exceptions to this rule (see below).

There are three different types of meaningful regions: blocks, paragraphs, and inlines.
A paragraph is a region that contains a sequence of complete sentences.  A block is a
region that can contain one or more paragraphs, as well as other block regions.  An
inline is a region that can only be contained within a paragraph or another inline.  A
paragraph can only contain inlines.

At the time of writing, all blocks and inlines must start with a tag and end with a
halmos.  On the other hand, paragraphs have neither restriction.

A typical region is comprised of the following parts: a tag, an optional meta region,
the content, and the halmos.  As mentioned before, if the region is a paragraph, the
tag is optional and the ending delimiter is a blank line instead of a Halmos.

The content of a tag can be either itself or 'as is'.  More concretely, a block tag may
declare its 'content mode' to be 'block' or 'as is', while the content mode of an inline
tag may be 'inline' or 'as is'.  If the content mode of a (block or inline) tag is 'as
is', its contents will not be parsed as RSM syntax and will be gathered into a single
Text node and added to the manuscript tree without change.  The contents of a paragraph
are always parsed as RSM syntax.

"""

from typing import Type
from enum import Enum, auto

from . import nodes


class TagName(str):
    delim: str = ':'

    def __new__(cls, name: str) -> 'TagName':
        if isinstance(name, cls):
            return name
        return super().__new__(cls, f'{cls.delim}{name}{cls.delim}')

    def __init__(self, name: str) -> None:
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
            raise ValueError(f'Tag with name "{self.name}" cannot create nodes')
        return self.nodeclass()

    @classmethod
    def newtag(
        cls: Type['Tag'],
        nodeclass: Type[nodes.Node] | None,
        *,
        name: str | None = None,
        has_content: bool | None = None,
        content_mode: ContentMode | None = None,
        meta_inline_only: bool | None = None,
        tag_optional: bool | None = None,
    ) -> 'Tag':
        if name:
            name = name
        else:
            if nodeclass:
                name = nodeclass.__name__.lower()
            else:
                raise ValueError('Must supply name or nodeclass')
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

    def set_source(self, src: str) -> None:
        self.src = src

    def makenode(self) -> nodes.Node:
        return nodes.Manuscript(src=self.src)


Halmos = Tag('')
_tags = {}
_tags['paragraph'] = ParagraphTag.newtag(nodes.Paragraph, tag_optional=True)
_tags['item'] = ParagraphTag.newtag(nodes.Item)
_tags['note'] = InlineTag.newtag(nodes.Note)
_tags['author'] = BlockTag.newtag(nodes.Author, has_content=False)
_tags['abstract'] = BlockTag.newtag(nodes.Abstract)
_tags['enumerate'] = BlockTag.newtag(nodes.Enumerate)
_tags['itemize'] = BlockTag.newtag(nodes.Itemize)
_tags['theorem'] = BlockTag.newtag(nodes.Theorem)
_tags['lemma'] = BlockTag.newtag(nodes.Lemma)
_tags['proposition'] = BlockTag.newtag(nodes.Proposition)
_tags['definition'] = BlockTag.newtag(nodes.Definition)
_tags['remark'] = BlockTag.newtag(nodes.Remark)
_tags['section'] = BlockTag.newtag(nodes.Section)
_tags['subsection'] = BlockTag.newtag(nodes.Subsection)
_tags['subsubsection'] = BlockTag.newtag(nodes.Subsubsection)
_tags['bibliography'] = BlockTag.newtag(nodes.Bibliography, has_content=False)
_tags['bibtex'] = BlockTag.newtag(None, name='bibtex')
_tags['proof'] = BlockTag.newtag(nodes.Proof)
_tags['p'] = BlockTag.newtag(nodes.Subproof, name='p')
_tags['sketch'] = BlockTag.newtag(nodes.Sketch)
_tags['step'] = BlockTag.newtag(nodes.Step)
_tags['mathblock'] = BlockTag.newtag(nodes.MathBlock, content_mode=ASIS)
_tags['codeblock'] = BlockTag.newtag(nodes.CodeBlock, content_mode=ASIS)
_tags['claim'] = InlineTag.newtag(nodes.Claim)
_tags['span'] = InlineTag.newtag(nodes.Span)
_tags['keyword'] = InlineTag.newtag(nodes.Keyword, content_mode=ASIS)
_tags['math'] = InlineTag.newtag(nodes.Math, content_mode=ASIS)
_tags['code'] = InlineTag.newtag(nodes.Code, content_mode=ASIS)
_tags['ref'] = InlineTag.newtag(nodes.PendingReference, name='ref', content_mode=ASIS)
_tags['url'] = InlineTag.newtag(nodes.URL, content_mode=ASIS)
_tags['previous'] = InlineTag.newtag(
    nodes.PendingPrev, name='previous', content_mode=ASIS
)
_tags['cite'] = InlineTag.newtag(nodes.PendingCite, name='cite', content_mode=ASIS)
_tags['figure'] = BlockTag.newtag(nodes.Figure, has_content=False)
_tags['caption'] = ParagraphTag.newtag(nodes.Caption)
_tags['draft'] = InlineTag.newtag(nodes.Draft)
_tags['table'] = BlockTag.newtag(nodes.Table)
_tags['thead'] = BlockTag.newtag(nodes.TableHead, name='thead', content_mode=INLINE)
_tags['tbody'] = BlockTag.newtag(nodes.TableBody, name='tbody', content_mode=INLINE)
_tags['tr'] = InlineTag.newtag(nodes.TableRow, name='tr')
_tags['td'] = InlineTag.newtag(nodes.TableDatum, name='td')
_tags['manuscript'] = ManuscriptTag.newtag(nodes.Manuscript)
_tags[''] = Halmos


def get(name: str) -> Tag:
    if isinstance(name, TagName):
        name = name.name
    try:
        return _tags[name]
    except KeyError as e:
        raise ValueError(
            f'Unrecognized tag name "{name}". Did you forget to escape a colon?'
        ) from e


def all() -> list[Tag]:
    return list(_tags.values())
