"""
lint.py
-------

RSM command line utility to run the linter.

"""

from . import cli
from .app import lint


def main() -> int:
    parser = cli.init_parser()
    # ...add/tweak parser options here...
    return cli.main(parser, lint)


if __name__ == "__main__":
    main()
