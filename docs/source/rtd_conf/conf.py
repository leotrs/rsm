"""
rtd_conf/conf.py
----------------

Production-ready sphinx configuration.

"""

import sys

sys.path.append("..")

from conf import *

html_static_path = ["../_static"]
html_logo = "../_static/logo.svg"
rsm_build_prod = True
