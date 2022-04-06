"""
render.py
---------

RSM command line utility to convert RSM markup to HTML.

"""

from argparse import ArgumentParser
import rsm


def render(source):
    return rsm.RSMProcessorApplication(plain=source).run()


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('src', help='RSM string to render')
    args = parser.parse_args()
    return args


def main():
    from icecream import ic
    ic.disable()
    args = parse_args()
    body = render(args.src)
    print(body)
    return 0


if __name__ == '__main__':
    main()
