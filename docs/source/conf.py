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

# extensions
extensions = [
    "sphinx_design",  # for cards and tabs; https://sphinx-design.readthedocs.io/en/latest/get_started.html
    "sphinx.ext.doctest",  # test snippets in docs
    "sphinx.ext.autosummary",  # generate nice tables and stub files
    "sphinx.ext.autodoc",  # autogenerate pages from docstrings
]

# autosummary
autosummary_generate = True

# PyData sphinx theme configuration
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
html_context = {
    # required for "Edit this page button"; see also "use_edit_page_button"
    "github_user": "<your-github-org>",
    "github_repo": "<your-github-repo>",
    "github_version": "<your-branch>",
    "doc_path": "<path-from-root-to-your-docs>",
}
