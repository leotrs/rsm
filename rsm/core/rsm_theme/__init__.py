from pathlib import Path

import sass
from sphinx.util.fileutil import copy_asset_file
from sphinx.util import logging

logger = logging.getLogger(__name__)
THIS_DIR = Path(__file__).parent.absolute()
CSS_DIR = THIS_DIR / 'static'
FILES = {CSS_DIR / 'rsm.scss': CSS_DIR / 'rsm.css'}


def process_sass(app):
    logger.debug('Compiling SASS to CSS')
    for src, dst in FILES.items():
        content = src.read_text()
        css = sass.compile(
            string=content, output_style='nested', include_paths=[str(src.parent)]
        )
        Path(dst).write_text(css)


def remove_css(app, exc):
    logger.debug('Cleaning up CSS files')
    for fn in FILES.values():
        fn.unlink()


def setup(app):
    app.add_html_theme('rsm_theme', THIS_DIR)
    app.connect('builder-inited', process_sass)
    app.connect('build-finished', remove_css)

    # There is a bug where calling app.add_js_file will add the file twice to the <head>
    # of the HTML output: see https://github.com/sphinx-doc/sphinx/issues/9267
    # As a workaround, we call app.registry.add_js_file instead
    app.registry.add_js_file('hoverstepnumber.js')