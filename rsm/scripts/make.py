"""
make.py
-------

RSM command line utility to build a manuscript.

"""

from .app import FullBuildApplication
from argparse import ArgumentParser
import livereload


def make(file, lint, verbose):
    app = FullBuildApplication(srcpath=file, run_linter=lint, verbosity=verbose)
    return app.run()


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('file', help='RSM source to parse')
    parser.add_argument('--serve', help='serve and autoreload', action='store_true')
    parser.add_argument('--lint', help='activate the linter', action='store_true')
    parser.add_argument('-v', '--verbose', help='verbosity', action='count', default=0)
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    if args.serve:
        cmd = f'rsm-make {args.file}'
        server = livereload.Server()
        server.watch(args.file, livereload.shell(cmd))
        server.serve(root='.')
    else:
        make(args.file, args.lint, args.verbose)
        return 0


if __name__ == '__main__':
    main()
