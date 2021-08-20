"""
main.py
-------

Main RSM command line utility.

"""

import sys
from argparse import ArgumentParser
import subprocess


CMDS = {
    False: (
        'sphinx-build '         # rsm-make is a wrapper for sphinx-build
        '-b html '              # build in html forat
        '-c ../rsm/rsm/core/ '  # use the config that ships with RSM
        '-D master_doc={root} ' # the root file
        '. '                    # SOURCEDIR
        'build '                # OUTPUTDIR
    ),
    True: (
        'sphinx-autobuild '     # this handles serving and autoreload
        '-a '                   # build all files, not only the outdated ones
        '. '                    # SOURCEDIR
        'build '                # OUTPUTDIR
        '--watch=*.rst '        # watch all source files
        ' -c ../rsm/rsm/core/ ' # use the config that ships with RSM
        '-D master_doc={root}'  # the root file
    )
}


def make_cmd(args):
    raw = CMDS[args.serve]
    return raw.format(file=args.file, root=args.root)


def main():
    parser = ArgumentParser()
    parser.add_argument('file', help='document to parse')
    parser.add_argument('--serve', help='serve and autoreload', action='store_true')
    parser.add_argument('--root', help='root file, if different from file',
                        default=None)
    args = parser.parse_args()

    if args.root is None:
        args.root = args.file
    if args.root.endswith('.rst'):
        args.root = args.root[:-4]

    cmd = make_cmd(args)
    return subprocess.run(cmd, check=True, shell=True)



if __name__ == '__main__':
    main()
