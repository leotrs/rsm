"""
tspaser.py
----------

Parse the concrete syntax tree output by tree-sitter into an abstract syntax tree.

"""
import tree_sitter
from rsm import nodes, translator, transformer
from itertools import groupby
from icecream import ic
from typing import cast, Callable
import string
import re

from .parser import RSMParserError
from .util import EscapedString
import logging

logger = logging.getLogger('RSM').getChild('parse')

DELIMS = ':%$`*{#'

TAGS_WITH_META = [
    "algorithm",
    'block',
    'caption',
    'codeblock',
    'mathblock',
    'code',
    'math',
    'inline',
    'item',
    'paragraph',
    'section',
    'specialblock',
    'specialinline',
    'source_file',
    'subsection',
    'subsubsection',
    'table',
]

# Nodes of these types are purely syntactical; their content is usually processed when
# processing their parent node.
DONT_PUSH_THESE_TYPES = {
    'algorithm',
    'asis_text',
    'blockmeta',
    'blocktag',
    'cite',
    'claimshort',
    'code',
    'codeblock',
    'inlinemeta',
    'inlinetag',
    'manuscript',  # the root node is of type source_file, not manuscript
    'mathblock',
    'math',
    'prev',
    'prev2',
    'previous',
    'ref',
    'section',
    'spanstrong',
    'spanemphas',
    'subsection',
    'subsubsection',
    'url',
}


class TSParser:
    def __init__(self):
        # !!!IMPORTANT!!!
        #
        # The Language class will look for its first argument (the .so file) inside the path
        # defined by $LD_LIBRARY_PATH.  This means that when installing RSM, we need to move the
        # language library there.  For now, for local dev, need to execute
        #
        # $ export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:./
        #
        # from the console BEFORE running this file.
        #
        tree_sitter.Language.build_library(
            'languages.so', ['/home/leo/code/tree-sitter-rsm']
        )
        self._lang = tree_sitter.Language('languages.so', 'RSM')
        self._parser = tree_sitter.Parser()
        self._parser.set_language(self._lang)
        self.cst = None
        self.ast = None

    def parse(self, src: str, abstractify: bool = True):
        logger.info('Parsing...')
        self.cst = self._parser.parse(bytes(str(src), 'utf-8'))

        # allow traverse() to print to stdout rather than use logger because it will
        # look better this way
        if logger.getEffectiveLevel() <= logging.DEBUG:
            traverse(self.cst)

        if not abstractify:
            return self.cst

        logger.info('Abstractifying...')
        self.ast = make_ast(self.cst)
        return self.ast


def traverse(tree, named_only=True):
    # children_att = 'named_children' if named_only else 'children'
    children_att = 'children'
    stack = [(0, tree.root_node)]
    while stack:
        indent, node = stack.pop()
        if node is None:
            print(')', end='')
            continue
        if indent:
            print()
        print(
            f'{" "*indent}({node.type} {node.start_point} - {node.end_point}',
            end='',
        )
        if node.type == 'text':
            print(f' "{node.text.decode("utf-8")}"', end='')
        stack.append((None, None))
        stack += reversed([(indent + 2, n) for n in getattr(node, children_att)])
    print()


CST_TYPE_TO_AST_TYPE: dict[str, Callable] = {
    'abstract': nodes.Abstract,
    'algorithm': nodes.Algorithm,
    'author': nodes.Author,
    'enumerate': nodes.Enumerate,
    'claim': nodes.Claim,
    'claimshort': nodes.Claim,
    'cite': nodes.PendingCite,
    'code': nodes.Code,
    'codeblock': nodes.CodeBlock,
    'definition': nodes.Definition,
    'draft': nodes.Draft,
    'item': nodes.Item,
    'itemize': nodes.Itemize,
    'caption': nodes.Caption,
    'figure': nodes.Figure,
    'lemma': nodes.Lemma,
    'math': nodes.Math,
    'mathblock': nodes.MathBlock,
    'note': nodes.Note,
    'paragraph': nodes.Paragraph,
    'prev': nodes.PendingPrev,
    'prev2': nodes.PendingPrev,
    'previous': nodes.PendingPrev,
    'proof': nodes.Proof,
    'proposition': nodes.Proposition,
    'ref': nodes.PendingReference,
    'remark': nodes.Remark,
    'section': nodes.Section,
    'sketch': nodes.Sketch,
    'source_file': nodes.Manuscript,
    'spanemphas': lambda: nodes.Span(emphas=True),
    'spanstrong': lambda: nodes.Span(strong=True),
    'step': nodes.Step,
    'subproof': nodes.Subproof,
    'subsection': nodes.Subsection,
    'subsubsection': nodes.Subsubsection,
    'span': nodes.Span,
    'table': nodes.Table,
    'tbody': nodes.TableBody,
    'text': nodes.Text,
    'thead': nodes.TableHead,
    'theorem': nodes.Theorem,
    'td': nodes.TableDatum,
    'tdcontent': nodes.TableDatum,
    'tr': nodes.TableRow,
    'trshort': nodes.TableRow,
    'url': nodes.URL,
}


def parse_metatag_list(cst_key, cst_val):
    key = cst_key.named_children[0].type
    if cst_val.named_children:
        val = [c.text.decode('utf-8').strip() for c in cst_val.named_children]
    else:
        val = [c.text.decode('utf-8').strip() for c in cst_val.named_children]
    return key, val


def parse_metatag_text(cst_key, cst_val):
    key = cst_key.named_children[0].type
    val = cst_val.text.decode('utf-8').strip()
    return key, val


def parse_metatag_any(cst_key, cst_val):
    return parse_metatag_text(cst_key, cst_val)


def parse_metatag_bool(cst_key, _):
    key = cst_key.named_children[0].type
    return key, True


def parse_meta_into_dict(node):
    pairs = {}
    for pair in [c for c in node.named_children if c.type.endswith('metapair')]:
        if len(pair.named_children) == 1:  # bool meta key
            cst_key, cst_val = pair.named_children[0], None
        else:
            cst_key, cst_val = pair.named_children
        key, val = globals()[f'parse_{cst_key.type}'](cst_key, cst_val)
        pairs[key] = val
    return pairs


def normalize_text(root):
    for node in root.traverse():
        # Merge consecutive text nodes (each text node ends at a newline, so consecutive
        # text nodes are just adjacent lines of text and can always be merged).  Also,
        # pad all text with spaces.  Spurious spaces added here are removed later.
        for run_is_text, run in groupby(
            node.children, key=lambda c: isinstance(c, nodes.Text)
        ):
            if not run_is_text:
                continue
            run = list(run)

            if len(run) == 2:
                first, last = run
                first.text = first.text.rstrip() + ' ' + last.text.lstrip()
                last.remove_self()

            elif len(run) > 2:
                # Watch the use of rstrip, strip, and lstrip here.
                first, rest = run[0], run[1:]
                first.text = (
                    first.text.rstrip()
                    + ' '
                    + ' '.join([t.text.strip() for t in run[1:-1]])
                    + ' '
                    + run[-1].text.lstrip()
                )
                for t in rest:
                    t.remove_self()

        if not isinstance(node, nodes.Paragraph) and node.children:
            if isinstance((first := node.children[0]), nodes.Text):
                first.text = first.text.lstrip()
            if isinstance((last := node.children[-1]), nodes.Text):
                last.text = last.text.rstrip()

        # Strip both ends of a paragraph's text content.
        if isinstance(node, nodes.Paragraph):
            if (first := node.first_of_type(nodes.Text)) and not first.prev_sibling(
                object
            ):
                first.text = first.text.lstrip()
            if (last := node.last_of_type(nodes.Text)) and not last.next_sibling(
                object
            ):
                last.text = last.text.rstrip()

        # At this point, the whitespace within non-paragraphs (e.g. Span, Claim) has
        # been dealt with, as has the leading and trailing whitespace of Paragraphs.
        # Since the text nodes have been merged, now every Paragraph's children look
        # like [..., Span, Text, Claim, Text, Span, ...].  We need to deal with the
        # whitespace at the boundaries between the Text and non-Text nodes in this list.
        # Since the inner whitespace of non-Texts has been dealt with, all we need to
        # care about is the outer whitespace of Text children.  Suppose we have a Text
        # node followed by a Span.  We want to give the user two options: either no
        # whitespace between them, or exactly one space.
        for idx, child in enumerate(node.children):
            if not isinstance(child, nodes.Text):
                continue
            child.text = re.sub(r'(.*?)\s+$', r'\1 ', child.text)
            child.text = re.sub(r'^\s+(.*?)', r' \1', child.text)

        # Manage escaped characters.
        if isinstance(node, nodes.Text) and not node.asis:
            node.text = EscapedString(node.text, DELIMS).escape()
        if isinstance(node, nodes.Section):
            node.title = EscapedString(node.title, DELIMS).escape()


def make_ast(cst):
    ast_root_node = None
    bibliography_node = None
    stack = [(None, cst.root_node)]
    while stack:
        parent, cst_node = stack.pop()
        dont_push_these_ids = set()
        if cst_node.type == 'comment':
            continue

        # Handle bibliography-related nodes first and continue
        if (
            cst_node.type == 'specialblock'
            and cst_node.children
            and cst_node.children[0].type == 'bibliography'
        ):
            bibliography_node = nodes.Bibliography()
            ast_root_node.append(bibliography_node)
            continue

        if cst_node.type == 'bibtex':
            if bibliography_node is None:
                logger.warning(msg='Found bibtex but no bibliography node')
                continue

            stack += reversed(
                [
                    (bibliography_node, c)
                    for c in cst_node.named_children
                    if c.type == 'bibitem'
                ]
            )

            for c in [c for c in cst_node.named_children if c.type == 'ERROR']:
                logger.warning(msg=f'Bibitem at {(c.start_point)} has an error')

            continue

        if cst_node.type == 'bibitem':
            ast_node = nodes.Bibitem()
            ast_node.kind = cst_node.child_by_field_name('kind').text.decode('utf-8')
            ast_node.label = cst_node.child_by_field_name('label').text.decode('utf-8')
            for pair in [c for c in cst_node.named_children if c.type == 'bibitempair']:
                key, value = pair.named_children
                key, value = key.text.decode('utf-8'), value.text.decode('utf-8')
                setattr(ast_node, key, value)

            parent.append(ast_node)
            continue

        # After this if statement, cst_node is the node that actually contains the
        # interesting stuff, and ast_node_type is a string with the type of syntax node
        # that we are currently analyzing.  NOTE: It may be the case that cst_node is
        # redirected to point to one of its children; ast_node_type may or may not be
        # equal to cst_node.type, or neither, or both!  For this reason ,from now on, DO
        # NOT use cst_node.tpye, always use ast_node_type instead.
        ast_node_type = ""
        if cst_node.type in ['specialblock', 'specialinline']:
            ast_node_type = cst_node.named_children[0].type

            # Tables are special because the entire contents are in the first children,
            # so we might as well add that with the current parent and ignore the
            # current node
            if ast_node_type == 'table':
                stack.append((parent, cst_node.named_children[0]))
                continue

        if cst_node.type == 'td':
            # td tags are special because the entire contents are in the first children,
            # so we might as well add that with the current parent and ignore the
            # current node
            stack.append((parent, cst_node.named_children[0]))
            continue

        elif cst_node.type == 'paragraph':
            first = cst_node.named_children[0]
            if first.type in ['item', 'caption']:
                cst_node = first
        if not ast_node_type:
            ast_node_type = cst_node.type

        # make the correct type of AST node
        if ast_node_type in CST_TYPE_TO_AST_TYPE:
            ast_node = CST_TYPE_TO_AST_TYPE[ast_node_type]()
            if isinstance(ast_node, nodes.Manuscript):
                ast_root_node = ast_node
            elif isinstance(ast_node, nodes.Text):
                ast_node.text = cst_node.text.decode('utf-8')
        elif ast_node_type in ['inline', 'block']:
            ast_node = CST_TYPE_TO_AST_TYPE[cst_node.children[0].children[0].type]()
        elif ast_node_type == 'ERROR':
            raise RSMParserError(msg='The CST contains errors.')
        else:
            print(f'not found {ast_node_type}')
            exit(1)

        # process meta
        if ast_node_type in TAGS_WITH_META:
            meta = cst_node.child_by_field_name('meta')
            if meta:
                ast_node.ingest_dict_as_meta(parse_meta_into_dict(meta))

        # process some special tags
        if ast_node_type in ['math', 'code', 'mathblock', 'codeblock', 'algorithm']:
            # "asis_text" is not pushed to the stack for further processing so must
            # handle it here
            asis = cst_node.named_children[-1]
            assert asis.type == 'asis_text'
            text = asis.text.decode('utf-8').strip()
            ast_node.append(nodes.Text(text, asis=True))

        if ast_node_type.endswith('section') and cst_node.type == 'specialblock':
            # Sections with a hastag shurtcut ("# Section Title") have the title as a
            # text child node, so must extract that here.  Sections with a tag
            # (":section:") have the title as a meta key, so that is handled elsewhere.
            # Sections of the former kind have cst_node type of 'specialblock' while the
            # latter have type 'block'.
            text_node = cst_node.named_children[1]
            ast_node.title = text_node.text.decode('utf-8')
            dont_push_these_ids.add(id(text_node))

        if ast_node_type in ['ref', 'previous', 'url']:
            target_node = cst_node.named_children[1]
            ast_node.target = target_node.text.decode('utf-8')
            dont_push_these_ids.add(id(target_node))

            if len(cst_node.named_children) > 2:
                reftext_node = cst_node.named_children[2]
                ast_node.overwrite_reftext = reftext_node.text.decode('utf-8')
                dont_push_these_ids.add(id(reftext_node))

        if ast_node_type.startswith('prev') and ast_node_type != 'previous':
            if ast_node_type == 'prev':
                target = 1
            else:
                target = int(ast_node_type[4:])
            ast_node.target = target

        if ast_node_type == 'cite':
            target_node = cst_node.named_children[1]
            labels = target_node.text.decode('utf-8').split(',')
            ast_node.targetlabels = [l.strip() for l in labels]
            dont_push_these_ids.add(id(target_node))

        # add the AST node to the correct place
        if parent and not isinstance(parent, nodes.Text):
            parent.append(ast_node)

        # push the children that need to be processed
        stack += reversed(
            [
                (ast_node, c)
                for c in cst_node.named_children
                if c.type not in DONT_PUSH_THESE_TYPES
                and id(c) not in dont_push_these_ids
            ]
        )

    normalize_text(ast_root_node)
    return ast_root_node