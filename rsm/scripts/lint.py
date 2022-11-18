"""
lint.py
-------

RSM command line utility to run the linter.

"""

from .app import LinterApplication
from .. import nodes
from argparse import ArgumentParser, Namespace


def lint(source: str) -> nodes.Manuscript:
    return LinterApplication(plain=source).run()


def parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument('src', help='RSM string to render')
    parser.add_argument(
        '-f',
        '--file',
        help='read source from file',
        action='store_true',
        default=False,
    )
    args = parser.parse_args()
    return args


def main() -> int:
    args = parse_args()
    if args.file:
        with open(args.src) as file:
            src = file.read()
    else:
        src = args.src
    lint(src)
    return 0


if __name__ == '__main__':
    main()
