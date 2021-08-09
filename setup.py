from distutils.core import setup

setup(
    name='RSM',
    version='0.1',
    description='reStructuredManuscript',
    author='leotrs',
    author_email='leo@leotrs.com',
    url='https://rescript.science/',
    entry_points = {
        'console_scripts': ['rsm-make=rsm.rsm_make.main:main'],
    }
)
