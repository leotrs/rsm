"""
conftest.py
-----------

pytest configuration.

"""

import shutil
import rsm


CMD = (
    'sphinx-build '         # rsm-make is a wrapper for sphinx-build
    '-b rsm_test '          # build in html forat
    '-c . '                 # folder containing conf.py
    'inputs/ '              # SOURCEDIR
    'outputs/ '             # OUTPUTDIR
)


def pytest_configure(config):
    print('Cleaning up output files...')
    try:
        shutil.rmtree('outputs/', )
    except FileNotFoundError:
        print('outputs/ directory not found, continuing...')
    print('Generating new output files...')
    print(rsm.make(cmd=CMD))
