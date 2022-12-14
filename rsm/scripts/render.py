"""
render.py
---------

RSM command line utility to convert RSM markup to HTML.

"""

from argparse import ArgumentParser, Namespace
from importlib.metadata import version

from .app import RSMProcessorApplication
from ..tsparser import RSMParserError


def render(source: str, handrails: bool = False, verbosity: int = 0) -> str:
    return RSMProcessorApplication(
        plain=source, handrails=handrails, verbosity=verbosity
    ).run()


def parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("src", help="RSM string to render")
    parser.add_argument(
        "-f",
        "--file",
        help="read source from file",
        action="store_true",
        default=False,
    )
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
        help="do not show the resulting HTML, show the logs only",
        action="store_true",
        default=False,
    )
    parser.add_argument("-v", "--verbose", help="verbosity", action="count", default=0)
    parser.add_argument(
        "-V",
        "--version",
        help="rsm-markup version",
        action="version",
        version=f'rsm-markup v{version("rsm-markup")}',
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
    try:
        body = render(src, args.handrails, args.verbose)
    except RSMParserError as exc:
        if exc.pos == 0:
            raise ValueError(
                "The source does not contain valid RSM.  Did you forget to use the -f flag?"
            )
        else:
            raise exc
    if not args.supress_output:
        print(body)
    return 0


if __name__ == "__main__":
    main()
