"""The conversion pipeline: an arXiv e-print to a rendered HTML page.

rsmify fetches the e-print and hands the payload to rsm-lang. Everything else,
unpacking it, finding the main file, flattening includes, extracting and
structuring the bibliography, converting, and building the page, is rsm-lang's
importer and builder, so nothing here duplicates the importer. lint is off
because the crude import often produces RSM the linter would reject.
"""

from __future__ import annotations

from rsm.app import build, import_project


def convert(eprint_path: str) -> str:
    rsm_source = import_project(eprint_path, from_format="latex")
    return build(source=rsm_source, handrails=True, standalone=True, lint=False)
