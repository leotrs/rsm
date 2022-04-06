from distutils.core import setup

setup(
    name='RSM',
    version='0.1',
    description='reStructuredManuscript',
    author='leotrs',
    author_email='leo@leotrs.com',
    url='https://rsm-suite.org/',
    entry_points={
        'console_scripts': [
            'rsm-make=rsm.scripts.make:main',
            'rsm-render=rsm.scripts.render:main',
        ],
    },
)
