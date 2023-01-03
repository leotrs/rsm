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
    parser.add_argument(
        "src",
        help="RSM source path",
    )
    parser.add_argument(
        "-c",
        "--string",
        help="interpret src as a source string, not a path",
        action="store_true",
    )
    parser.add_argument(
        "-r",
        "--handrails",
        help="output handrails",
        action="store_true",
    )
    parser.add_argument(
        "-s",
        "--suppress-output",
        help="do not show output, only the logs",
        action="store_true",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        help="verbosity",
        action="count",
        default=0,
    )
    parser.add_argument(
        "--log-format",
        help="format for logs",
        choices=["plain", "rsm", "json", "lint"],
        default="rsm",
    )
    parser.add_argument(
        "--log-exclude-time",
        dest="log_time",
        help="exclude timestamp in logs",
        action="store_false",
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
    kwargs = dict(
        handrails=args.handrails,
        loglevel=app.RSMApp.default_log_level - args.verbose * 10,
        log_format=args.log_format,
        log_time=args.log_time,
    )
    if args.string:
        kwargs["source"] = args.src
    else:
        kwargs["path"] = args.src
    output = func(**kwargs)
    if not args.suppress_output and output:
        print(output)
    return 0


def render() -> int:
    parser = init_parser()
    return main(parser, app.render)


def lint() -> int:
    parser = init_parser()
    parser.set_defaults(log_format="lint")
    parser.set_defaults(suppress_output=True)
    return main(parser, app.lint)


def make() -> int:
    parser = init_parser()
    parser.add_argument("--serve", help="serve and autoreload", action="store_true")
    parser.set_defaults(handrails=True)
    args = parser.parse_args()

    if args.serve:
        other_args = [a for a in sys.argv if a != "--serve"]
        cmd = " ".join(other_args)
        server = livereload.Server()
        server.watch(args.src, livereload.shell(cmd))
        server.serve(root=".")
    else:
        main(parser, app.make, args)
    return 0
