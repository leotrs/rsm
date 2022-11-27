"""
tspaser.py
----------

Parse the concrete syntax tree output by tree-sitter into an abstract syntax tree.

"""
import tree_sitter
from rsm import nodes, translator, transformer
from itertools import groupby
from icecream import ic

from .parser import RSMParserError


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
            self.ast = None
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


CST_TYPE_TO_AST_TYPE = {
    'source_file': nodes.Manuscript,
    'paragraph': nodes.Paragraph,
    # 'text': nodes.Text,
    'span': nodes.Span,
    'math': nodes.Math,
    'mathblock': nodes.MathBlock,
    'code': nodes.Code,
    'codeblock': nodes.CodeBlock,
    'author': nodes.Author,
    'abstract': nodes.Abstract,
    'section': nodes.Section,
    'subsection': nodes.Subsection,
    'subsubsection': nodes.Subsubsection,
    'theorem': nodes.Theorem,
    'lemma': nodes.Lemma,
    'claim': nodes.Claim,
    'proof': nodes.Proof,
    'step': nodes.Step,
    'sketch': nodes.Sketch,
    'enumerate': nodes.Enumerate,
}


def parse_metatag_list(cst_key, cst_val):
    key = cst_key.named_children[0].type
    val = [c.text.decode('utf-8') for c in cst_val.named_children]
    return key, val


def parse_metatag_text(cst_key, cst_val):
    key = cst_key.named_children[0].type
    val = cst_val.text.decode('utf-8')
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


def make_ast(cst):
    stack = [(None, cst.root_node)]
    while stack:
        parent, cst_node = stack.pop()

        # get node that actually contains the contents
        if cst_node.type in ['specialblock', 'specialinline']:
            cst_node = cst_node.named_children[0]

        # make the correct type of AST node
        if cst_node.type in CST_TYPE_TO_AST_TYPE:
            ast_node = CST_TYPE_TO_AST_TYPE[cst_node.type]()
            if isinstance(ast_node, nodes.Manuscript):
                ast_root = ast_node
            # elif isinstance(ast_node, nodes.Text):
            #     ast_node.text = cst_node.text.decode('utf-8') + '\n'
            if cst_node.type in ['math', 'code']:
                text = cst_node.text.decode('utf-8')
                text = text[1:-1]  # get rid of $ and `
                ast_node.append(nodes.Text(text))

        elif cst_node.type in ['inline', 'block']:
            ast_node = CST_TYPE_TO_AST_TYPE[cst_node.children[0].children[0].type]()

        elif cst_node.type == 'ERROR':
            raise RSMParserError(msg='The CST contains errors.')

        else:
            print(f'not found {cst_node.type}')
            exit(1)

        # process meta
        if cst_node.type in [
            'specialinline',
            'specialblock',
            'inline',
            'block',
            'manuscript',
            'source_file',
            'paragraph',
        ]:
            meta = cst_node.child_by_field_name('meta')
            if meta:
                ast_node.ingest_dict_as_meta(parse_meta_into_dict(meta))

        # merge text children
        for run_is_text, run in groupby(
            cst_node.children, key=lambda c: c.type == 'text'
        ):
            if run_is_text:
                ast_text = nodes.Text()
                ast_text.text = '\n'.join([t.text.decode('utf-8').strip() for t in run])
                ast_node.append(ast_text)

        # add the AST node to the correct place
        if parent and not isinstance(parent, nodes.Text):
            parent.append(ast_node)

        # push the children that need to be processed
        stack += reversed(
            [
                (ast_node, c)
                for c in cst_node.named_children
                if c.type
                not in {
                    'inlinetag',
                    'blocktag',
                    'inlinemeta',
                    'blockmeta',
                    'manuscript',  # the manuscript node is of type source_file
                    'text',  # text nodes are handled when their parents are visited
                }
            ]
        )

    return ast_root
