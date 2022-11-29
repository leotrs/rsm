"""
make.py
-------

RSM command line utility to build a manuscript.

"""

from .app import FullBuildApplication
from argparse import ArgumentParser, Namespace
from pathlib import Path
import sys
import livereload


def make(
    file: str, lint: bool = True, treesitter: bool = False, verbose: int = 0
) -> str:
    app = FullBuildApplication(
        srcpath=Path(file), run_linter=lint, verbosity=verbose, treesitter=treesitter
    )
    return app.run()


def parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument('file', help='RSM source to parse')
    parser.add_argument('--serve', help='serve and autoreload', action='store_true')
    parser.add_argument('--lint', help='activate the linter', action='store_true')
    parser.add_argument('-v', '--verbose', help='verbosity', action='count', default=0)
    parser.add_argument(
        '-t',
        '--treesitter',
        help='use the tree-sitter parser',
        action='store_true',
    )
    args = parser.parse_args()
    return args


def main() -> int:
    args = parse_args()
    if args.serve:
        other_args = [a for a in sys.argv if a != '--serve']
        cmd = ' '.join(other_args)
        server = livereload.Server()
        server.watch(args.file, livereload.shell(cmd))
        server.serve(root='.')
    else:
        make(args.file, args.lint, args.treesitter, args.verbose)
    return 0


if __name__ == '__main__':
    main()
