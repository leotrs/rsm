"""The conversion pipeline: a LaTeX file to a rendered HTML page.

Uses rsm-lang's importer and builder. build produces the full self-contained
HTML document (standalone inlines the JS and pulls the RSM CSS from the jsDelivr
CDN). lint is off because the crude import often produces RSM the linter would
reject. The importer only handles a subset of LaTeX today, so output is rough
until the rsm-ddx importer beads land.
"""

from __future__ import annotations

from rsm.app import build, pandoc_import


def convert(tex_path: str) -> str:
    rsm_source = pandoc_import(path=tex_path, from_format="latex")
    return build(source=rsm_source, handrails=True, standalone=True, lint=False)
