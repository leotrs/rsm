# RSM configuration used only when testing


# -- Import default config ---------------------------------------------------
import sys
from pathlib import Path
import rsm
root_dir = Path(rsm.__file__).parents[0] / 'core/'
sys.path.append(root_dir.as_posix())
from conf import *


# -- Override deafult config -------------------------------------------------

project = 'RSM test suite'
html_use_index = False          # do not generate index files
html_theme = 'rsm_test_theme'

sys.path.append('.')
extensions = extensions + ['rsm_test_builder']
