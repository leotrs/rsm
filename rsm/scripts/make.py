"""
make.py
-------

RSM command line utility to build a manuscript.

"""

import sys

import livereload

from . import cli
from .app import make


def main() -> int:
    parser = cli.init_parser()
    parser.add_argument("--serve", help="serve and autoreload", action="store_true")
    args = parser.parse_args()

    if args.serve:
        other_args = [a for a in sys.argv if a != "--serve"]
        cmd = " ".join(other_args)
        server = livereload.Server()
        server.watch(args.path, livereload.shell(cmd))
        server.serve(root=".")
    else:
        cli.main(parser, make, args)
    return 0


if __name__ == "__main__":
    main()
