"""
cli.py
------

RSM command line utility.

"""

import sys
from argparse import ArgumentParser, Namespace
from importlib.metadata import version
from typing import Callable, Optional

import livereload

from rsm import app
from rsm.tsparser import RSMParserError


def init_parser() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument("path", help="source file")
    parser.add_argument(
        "-r",
        "--handrails",
        help="output handrails",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "-s",
        "--supress-output",
        help="do not show output, only the logs",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "-v",
        "--verbose",
        help="verbosity",
        action="count",
        default=0,
    )
    parser.add_argument(
        "-V",
        "--version",
        help="rsm-markup version",
        action="version",
        version=f'rsm-markup v{version("rsm-markup")}',
    )

    return parser


def main(
    parser: ArgumentParser, func: Callable, args: Optional[Namespace] = None
) -> int:
    if args is None:
        args = parser.parse_args()
    with open(args.path, encoding="utf-8") as file:
        src = file.read()
    output = func(src, args.handrails, args.verbose)
    if not args.supress_output and output:
        print(output)
    return 0


def render() -> int:
    parser = init_parser()
    return main(parser, app.render)


def lint() -> int:
    parser = init_parser()
    return main(parser, app.lint)


def make() -> int:
    parser = init_parser()
    parser.add_argument("--serve", help="serve and autoreload", action="store_true")
    args = parser.parse_args()

    if args.serve:
        other_args = [a for a in sys.argv if a != "--serve"]
        cmd = " ".join(other_args)
        server = livereload.Server()
        server.watch(args.path, livereload.shell(cmd))
        server.serve(root=".")
    else:
        main(parser, make, args)
    return 0
