"""The conversion pipeline: a LaTeX file to a rendered HTML page.

Uses rsm-lang's importer and renderer. render is used rather than build:
build segfaults on real papers (a crash in rsm-lang's warning logging during
the translate step, filed separately), while render is stable. render returns
only the <body>, so we attach the standalone document head (CDN CSS, inlined
JS, the RSM.onload wiring) from rsm's own StandaloneBuilder, mirroring how
build's make_main_file wraps the body. The importer still handles only a subset
of LaTeX, so output is rough until the rsm-ddx importer beads land.
"""

from __future__ import annotations

import logging
import re

from rsm.app import pandoc_import, render
from rsm.builder import StandaloneBuilder


def convert(tex_path: str) -> str:
    rsm_source = pandoc_import(path=tex_path, from_format="latex")
    body = render(
        source=rsm_source, handrails=True, standalone=True, loglevel=logging.ERROR
    ).strip()
    return _wrap_standalone(body)


def _wrap_standalone(body: str) -> str:
    # Reuse rsm's standalone <head> (CDN CSS, inlined JS, onload wiring) without
    # running build(), which segfaults. make_html_header reads only these four
    # attributes, so a bare instance is enough.
    builder = StandaloneBuilder.__new__(StandaloneBuilder)
    builder.body = body
    builder.custom_css = None
    builder.menu_position = "left"
    builder.theme_toggle = True
    header = builder.make_html_header()

    accent = re.search(r'<body[^>]*data-accent="([^"]*)"', body)
    accent_attr = f' data-accent="{accent.group(1)}"' if accent else ""
    lang = re.search(r'<body[^>]*data-lang="([^"]*)"', body)
    lang_value = lang.group(1) if lang else "en"
    return (
        f'<!DOCTYPE html>\n<html lang="{lang_value}"{accent_attr}>\n\n'
        + header
        + "\n"
        + body
        + "\n\n</html>\n"
    )
