# conftest.py
#
# Global pytest configuration and fixtures.
#
# NOTE: the definitions here are only visible to tests within this directory and its
# children dirs.  In particular, for pytest to run unit tests (or other tests) in the
# tests directory (../tests/), there needs to be a different conftest.py file in that
# directory.

import sys

import pytest

import rsm

sys.path.append("docs/source/")
import doctest_setup


@pytest.fixture(autouse=True)
def add_rsm_to_doctest_namespace(doctest_namespace):
    """Ensure doctests have access to rsm."""
    # without this, each doctest would have to import rsm
    doctest_namespace["rsm"] = rsm
    doctest_namespace["nodes"] = rsm.nodes
