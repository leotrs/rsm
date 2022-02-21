"""
conftest.py
-----------

pytest configuration.

"""

from rsm.rsm_make import main


def pytest_configure(config):
    main.RAN_FROM_PYTEST = True
    print(main.main(['demo.rst', '--config', '.']))
