"""
render.py
---------

RSM command line utility to convert RSM markup to HTML.

"""

from .app import RSMProcessorApplication
from argparse import ArgumentParser


def render(source):
    return RSMProcessorApplication(plain=source).run()


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('src', help='RSM string to render')
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    body = render(args.src)
    print(body)
    return 0


if __name__ == '__main__':
    main()
