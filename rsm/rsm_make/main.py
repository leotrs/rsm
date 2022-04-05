"""
main.py
-------

Main RSM command line utility.

"""

from argparse import ArgumentParser

import rsm


def make(file=None):
    if file is None:
        parser = ArgumentParser()
        parser.add_argument('file', help='file to parse')
        args = parser.parse_args()
        file = args.file
    return rsm.Application(srcpath=file).run()


if __name__ == '__main__':
    make()
