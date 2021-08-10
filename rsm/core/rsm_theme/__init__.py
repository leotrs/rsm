from os import listdir, path
from sphinx.util.fileutil import copy_asset_file


def setup(app):
    app.add_html_theme('rsm_theme', path.abspath(path.dirname(__file__)))
    app.add_js_file('hoverstepnumber.js')
