"""Unit tests for the pandoc AST to RSM import translator (PandocImporter)."""

from rsm.pandoc import PandocImporter


def test_figure_with_caption_does_not_crash():
    # Regression: a pandoc Figure caption is a list [short-caption, [blocks]],
    # not a node with a "c" key. _block_figure called .get on it and crashed on
    # any captioned figure, which is most real papers.
    ast = {
        "blocks": [
            {
                "t": "Figure",
                "c": [
                    ["", [], []],
                    [
                        None,
                        [
                            {
                                "t": "Para",
                                "c": [
                                    {"t": "Str", "c": "A"},
                                    {"t": "Space"},
                                    {"t": "Str", "c": "caption"},
                                ],
                            }
                        ],
                    ],
                    [
                        {
                            "t": "Plain",
                            "c": [
                                {
                                    "t": "Image",
                                    "c": [["", [], []], [], ["fig.png", ""]],
                                }
                            ],
                        }
                    ],
                ],
            }
        ]
    }
    out = PandocImporter().from_json(ast)
    assert ":figure:" in out
    assert "fig.png" in out
    assert "A caption" in out
