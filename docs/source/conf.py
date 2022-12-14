"""
conf.py
-------

Sphinx configuration.

"""

#################
# General options
#################

# project definition
project = "rsm"
copyright = "2022, leotrs"
author = "leotrs"

# options for HTML output
html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_logo = "_static/rsm-tag.png"

# templates
templates_path = ["_templates"]
exclude_patterns = []


#######################
# Per-extension options
#######################

#
# extensions
#
extensions = [
    "sphinx_design",  # for cards and tabs; https://sphinx-design.readthedocs.io/en/latest/get_started.html
    "sphinx.ext.doctest",  # test snippets in docs
    "sphinx.ext.autosummary",  # generate nice tables and stub files
    "sphinx.ext.napoleon",  # support for numpy style docstrings
    "sphinx.ext.autodoc",  # autogenerate pages from docstrings
    "sphinx.ext.linkcode",  # 'source' links for each class and method
    "sphinx_copybutton",  # copy button on code blocks
]


#
# doctest
#
doctest_global_setup = """
import rsm
from rsm import nodes
"""

# Add a new IGNORE_RESULT flag to skip checking a single line within a doctest.
# Taken from https://stackoverflow.com/a/69780437.
import doctest

IGNORE_RESULT = doctest.register_optionflag("IGNORE_RESULT")
OutputChecker = doctest.OutputChecker


class CustomOutputChecker(OutputChecker):
    def check_output(self, want, got, optionflags):
        if IGNORE_RESULT & optionflags:
            return True
        return OutputChecker.check_output(self, want, got, optionflags)


doctest.OutputChecker = CustomOutputChecker


#
# autodoc
#

# add typehints in description, not signature
autodoc_typehints = "description"

# only show typehints for parameters that are documented in the docstring
autodoc_typehints_description_target = "documented"


#
# napoleon
#
napoleon_numpy_docstring = True
napoleon_use_rtype = False


#
# autosummary
#
autosummary_generate = True


#
# PyData sphinx theme configuration
#
html_theme_options = {
    # navbar options
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["navbar-icon-links"],
    "navbar_persistent": ["search-button"],
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/<your-org>/<your-repo>",
            "icon": "fa-brands fa-square-github",
            "type": "fontawesome",
        },
        {
            "name": "Home",
            "url": "https://github.com/<your-org>/<your-repo>",
            "icon": "fa-solid fa-house",
            "type": "fontawesome",
        },
    ],
    # page options
    "use_edit_page_button": True,
}

# required for "Edit this page button"; see also "use_edit_page_button"
html_context = {
    "github_user": "<your-github-org>",
    "github_repo": "<your-github-repo>",
    "github_version": "<your-branch>",
    "doc_path": "<path-from-root-to-your-docs>",
}


#
# linkcode needs a function that tells it where to link to
#
def linkcode_resolve(domain, info):
    if domain != "py":
        return None
    if not info["module"]:
        return None
    filename = info["module"].replace(".", "/")
    return f"https://github.com/leotrs/rsm/tree/main/{filename}.py"
