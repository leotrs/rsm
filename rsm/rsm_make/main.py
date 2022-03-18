"""
main.py
-------

Main RSM command line utility.

"""

import sys
from argparse import ArgumentParser
import subprocess
from pathlib import Path


RAN_FROM_PYTEST = False
DEFAULT_CONFIG = Path(__file__).parents[1] / 'core'
OUTPUT_DIR = 'build'
CMD = (
    'sphinx-build '         # rsm-make is a wrapper for sphinx-build
    '-b html '              # build in html forat
    '-c {config} '          # folder containing conf.py
    '-D master_doc={root} ' # the root file
    '. '                    # SOURCEDIR
    '{output_dir} '         # OUTPUTDIR
)
SERVE = (
    'sphinx-autobuild '     # this handles serving and autoreload
    '-a '                   # build all files, not only the outdated ones
    '. '                    # SOURCEDIR
    '{output_dir} '         # OUTPUTDIR
    '--watch=*.rst '        # watch all source files
    '-c {config} '          # folder containing conf.py
    '-D master_doc={root}'  # the root file
    )


def make_cmd(args):
    if args.serve:
        raw = SERVE
    else:
        raw = CMD

    return raw.format(
        file=args.file,
        root=args.root,
        config=args.config,
        output_dir=OUTPUT_DIR,
    )


def make(file=None, cmd=None, return_output=False):
    if file is not None:
        args = None
        cmd = CMD.format(file=file, root=file, config=DEFAULT_CONFIG, output_dir=OUTPUT_DIR)

    elif cmd is None:
        parser = ArgumentParser()

        parser.add_argument('file', help='document to parse')
        parser.add_argument('--serve', help='serve and autoreload', action='store_true')
        parser.add_argument('--root', help='root file, if different from file',
                            default=None)
        parser.add_argument('--config', help='config file, if different from default',
                            default=DEFAULT_CONFIG)
        args = parser.parse_args()

        if args.root is None:
            args.root = args.file
        if args.root.endswith('.rst'):
            args.root = args.root[:-4]
        cmd = make_cmd(args)

    print(cmd)
    result = subprocess.run(cmd, check=True, shell=True)

    if not return_output:
        return result

    output_file = args.root if args is not None else file
    with open(f'{OUTPUT_DIR}/{output_file}.html') as outfile:
        output = outfile.read()

    return result, output


if __name__ == '__main__':
    make()
