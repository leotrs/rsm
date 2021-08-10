from distutils.core import setup

setup(
    name='rsm_theme',
    version='0.0.1',
    description='reStructuredManuscript theme',
    author='leotrs',
    author_email='leo@leotrs.com',
    url='https://rsm-suite.org/',
    entry_points={
        'sphinx.html_themes': [
            'rsm_theme = rsm_theme',
        ]
    },
)
