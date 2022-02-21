from distutils.core import setup

setup(
    name='rsm_test_theme',
    version='0.0.1',
    description='reStructuredManuscript test theme',
    author='leotrs',
    author_email='leo@leotrs.com',
    url='https://rsm-suite.org/',
    entry_points={
        'sphinx.html_themes': [
            'rsm_test_theme = rsm_test_theme',
        ]
    },
)
