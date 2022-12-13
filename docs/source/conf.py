"""
conf.py
-------

Sphinx configuration.

"""

project = "rsm"
copyright = "2022, leotrs"
author = "leotrs"

# Extensions
extensions = [
    "sphinx_design",  # for cards and tabs; https://sphinx-design.readthedocs.io/en/latest/get_started.html
    "sphinx.ext.doctest",  # test snippets in docs
]

# options for HTML output
html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_logo = "_static/rsm-tag.png"

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

# required for "Edit this page button"; see also "use_edit_page_button"
html_context = {
    "github_user": "<your-github-org>",
    "github_repo": "<your-github-repo>",
    "github_version": "<your-branch>",
    "doc_path": "<path-from-root-to-your-docs>",
}

# Templates
templates_path = ["_templates"]
exclude_patterns = []
