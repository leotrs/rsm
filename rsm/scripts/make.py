"""
make.py
-------

RSM command line utility to build a manuscript.

"""

import sys
from pathlib import Path
from argparse import ArgumentParser

import livereload
import rsm


def make(file):
    return rsm.Application(srcpath=file).run()


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('file', help='RSM source to parse')
    parser.add_argument('--serve', help='serve and autoreload', action='store_true')
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
        return make(args.file)


if __name__ == '__main__':
    main()
