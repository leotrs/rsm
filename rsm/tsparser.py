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

from .parser import RSMParserError
from .util import EscapedString


DELIMS = ':%$`*{'

TAGS_WITH_META = [
    'block',
    'caption',
    'codeblock',
    'mathblock',
    'code',
    'math',
    'inline',
    'item',
    'paragraph',
    'specialblock',
    'specialinline',
    'source_file',
]

# Nodes of these types are purely syntactical; their content is usually processed when
# processing their parent node.
DO_NOT_PROCESS = {
    'asis_text',
    'blockmeta',
    'blocktag',
    'codeblock',
    'mathblock',
    'math',
    'code',
    'inlinemeta',
    'inlinetag',
    'spanstrong',
    'spanemphas',
    'manuscript',  # the root node is of type source_file, not manuscript
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
        self.cst = self._parser.parse(bytes(str(src), 'utf-8'))
        traverse(self.cst)
        if not abstractify:
            return self.cst
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
    'author': nodes.Author,
    'enumerate': nodes.Enumerate,
    'claim': nodes.Claim,
    'code': nodes.Code,
    'codeblock': nodes.CodeBlock,
    'item': nodes.Item,
    'lemma': nodes.Lemma,
    'math': nodes.Math,
    'mathblock': nodes.MathBlock,
    'paragraph': nodes.Paragraph,
    'proof': nodes.Proof,
    'section': nodes.Section,
    'sketch': nodes.Sketch,
    'source_file': nodes.Manuscript,
    'step': nodes.Step,
    'spanstrong': lambda: nodes.Span(strong=True),
    'subsection': nodes.Subsection,
    'subsubsection': nodes.Subsubsection,
    'span': nodes.Span,
    'text': nodes.Text,
    'theorem': nodes.Theorem,
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
        # Merge consecutive text nodes.
        for run_is_text, run in groupby(
            node.children, key=lambda c: isinstance(c, nodes.Text)
        ):
            if not run_is_text:
                continue
            run = list(run)
            if len(run) < 2:
                continue
            first, rest = run[0], run[1:]
            first.text = '\n'.join([t.text.strip() for t in run])
            for t in rest:
                t.remove_self()

        # Strip both ends of a paragraph's text content.
        if isinstance(node, nodes.Paragraph):
            first, last = node.first_of_type(nodes.Text), node.last_of_type(nodes.Text)
            if first:
                first.text = first.text.lstrip()
            if last:
                last.text = last.text.rstrip()

        # Manage escaped characters
        if isinstance(node, nodes.Text):
            node.text = EscapedString(node.text, DELIMS).escape()


def make_ast(cst):
    stack = [(None, cst.root_node)]
    while stack:
        parent, cst_node = stack.pop()

        # After this if statement, cst_node is the node that actually contains the
        # interesting stuff, and ast_node_type is a string with the type of syntax node
        # that we are currently analyzing.  NOTE: It may be the case that cst_node is
        # redirected to point to one of its children; ast_node_type may or may not be
        # equal to cst_node.type, or neither, or both!  For this reason ,from now on, DO
        # NOT use cst_node.tpye, always use ast_node_type instead.
        ast_node_type = ""
        if cst_node.type in ['specialblock', 'specialinline']:
            ast_node_type = cst_node.named_children[0].type
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
                ast_root = ast_node
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
        if ast_node_type in ['math', 'code', 'mathblock', 'codeblock']:
            asis = cst_node.named_children[-1]
            assert asis.type == 'asis_text'
            text = asis.text.strip()
            ast_node.append(nodes.Text(text.decode('utf-8')))

        # add the AST node to the correct place
        if parent and not isinstance(parent, nodes.Text):
            parent.append(ast_node)

        # push the children that need to be processed
        stack += reversed(
            [
                (ast_node, c)
                for c in cst_node.named_children
                if c.type not in DO_NOT_PROCESS
            ]
        )

    normalize_text(ast_root)
    return ast_root
