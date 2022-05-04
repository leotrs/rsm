"""
lint.py
-------

RSM command line utility to run the linter.

"""

from .app import LinterApplication
from ..core.manuscript import AbstractTreeManuscript
from argparse import ArgumentParser, Namespace


def lint(source: str) -> AbstractTreeManuscript:
    return LinterApplication(plain=source).run()


def parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument('src', help='RSM string to render')
    args = parser.parse_args()
    return args


def main() -> int:
    args = parse_args()
    result = lint(args.src)
    print(result)
    return 0


if __name__ == '__main__':
    main()
