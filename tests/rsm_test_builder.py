"""
rsm_test_builder.py
-------------------

Custom Sphinx builder to use during testing.

"""

from sphinx.builders.html import StandaloneHTMLBuilder
from rsm.core.ext.writer import RSMTranslator


class RSMTestBuilder(StandaloneHTMLBuilder):
    name = 'rsm_test'
    search = False              # do not generate search files
    copysource = False          # do not generate _sources directory


def setup(app):
    print('setting up rsm test buiilder')
    app.add_builder(RSMTestBuilder)
    app.registry.add_translator('rsm_test', RSMTranslator)
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
