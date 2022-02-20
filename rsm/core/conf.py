# Default Sphinx configuration used by RSM


# -- Path setup --------------------------------------------------------------

import os
import sys
sys.path.append(os.path.abspath("."))
sys.path.append(os.path.abspath("./ext"))


# -- Project information -----------------------------------------------------

project = 'RSM'
copyright = '2021, leotrs'
author = 'leotrs'


# -- Extensions --------------------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    'sphinxcontrib.bibtex',
    'proof_env',
    'thm_env',
    'misc',
    'labels',
    'contents',
    'writer',
]


# -- Bibliography ------------------------------------------------------------

bibtex_bibfiles = ['references.bib']
bibtex_bibliography_header = ''
bibtex_footbibliography_header = ''


# -- Auto number figures -----------------------------------------------------

numfig = True


# -- HTML theme --------------------------------------------------------------

html_theme = 'rsm_theme'
html_permalinks = False


# -- Math options ------------------------------------------------------------

default_role = 'math'
math_number_all = True
mathjax_options = {'onload': 'loadTooltips()'}


# -- User config -------------------------------------------------------------

# Here we should read a user-provided conf.py file from the directory where the
# manuscript is.  The user can override any of the options above, with the caveat that
# if they want to extend, for example, the list of extensions, they should use extension
# syntax (extensions += [ext1, ...]) or they will lose the rsm core extensions.
