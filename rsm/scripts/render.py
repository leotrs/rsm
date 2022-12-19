"""
render.py
---------

RSM command line utility to convert RSM markup to HTML.

"""

from . import cli
from .app import render


def main() -> int:
    parser = cli.init_parser()
    # ...add/tweak parser options here...
    return cli.main(parser, render)


if __name__ == "__main__":
    main()
