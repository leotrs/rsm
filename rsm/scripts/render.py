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
    parser.add_argument('-f', '--file', help='read source from file', action='store_true', default=False)
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    if args.file:
        with open(args.src) as file:
            src = file.read()
    else:
        src = args.src
    body = render(src)
    print(body)
    return 0


if __name__ == '__main__':
    main()
