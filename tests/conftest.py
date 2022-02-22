"""
conftest.py
-----------

pytest configuration.

"""

import shutil
from rsm.rsm_make import main


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
        pass
    print('Generating new output files...')
    print(main.main(CMD))
