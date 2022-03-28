from pathlib import Path

import sass
from sphinx.util.fileutil import copy_asset_file
from sphinx.util import logging
from sphinx.builders.html import JavaScript

from icecream import ic

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


def register_static_files(app, config):
    need_local = config.rsm_theme_local_static
    domain = 'https://leotrs.com/rsm/_static'
    fn = lambda s: s if need_local else f'{domain}/{s}'

    app.add_css_file(fn('tooltipster.bundle.css'))

    # There is a bug where calling app.add_js_file will add the file twice to the <head>
    # of the HTML output: see https://github.com/sphinx-doc/sphinx/issues/9267
    # As a workaround, we call app.registry.add_js_file instead
    app.registry.add_js_file('https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js')
    app.registry.add_js_file('https://cdn.jsdelivr.net/npm/@svgdotjs/svg.js@latest/dist/svg.min.js')
    app.registry.add_js_file('https://d3js.org/d3.v7.min.js')
    app.registry.add_js_file(
        'https://kit.fontawesome.com/0e1aa62e6e.js',
        crossorigin="anonymous",
    )

    app.registry.add_js_file(fn('classes.js'))
    app.registry.add_js_file(fn('tooltips.js'))
    app.registry.add_js_file(fn('tooltipster.bundle.js'))
    # app.registry.add_js_file(fn('tree.js'))


def modify_static_files(app):
    need_local = app.config.rsm_theme_local_static
    domain = 'https://leotrs.com/rsm/_static'
    fn = lambda s: s if need_local else f'{domain}/{s}'

    if not need_local:
        files = app.builder.script_files[:]
        app.builder.script_files = []

        for file in files:
            if '://' in file.filename:
                app.builder.script_files.append(file)
            else:
                newfilename = f'{domain}/{file.filename[8:]}'
                newjs = JavaScript(newfilename, priority=file.priority, **file.attributes)
                app.builder.script_files.append(newjs)

        files = app.builder.css_files[:]
        app.builder.css_files = []

        for file in files:
            if '://' in file.filename:
                app.builder.css_files.append(file)
            else:
                newfilename = f'{domain}/{file.filename[8:]}'
                newjs = JavaScript(newfilename, priority=file.priority, **file.attributes)
                app.builder.css_files.append(newjs)


def setup(app):
    app.add_html_theme('rsm_theme', THIS_DIR)
    app.add_config_value('rsm_theme_local_static', True, 'html', bool)

    app.connect('config-inited', register_static_files)
    app.connect('builder-inited', modify_static_files)
    app.connect('builder-inited', process_sass)
    app.connect('build-finished', remove_css)
