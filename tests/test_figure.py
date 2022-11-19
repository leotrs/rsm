from conftest import compare_have_want


SIMPLE_WANT = """\
<body>

<div class="manuscriptwrapper">

<div id="manuscript" class="manuscript">

<section class="level-1">

<h1></h1>

<figure class="figure">
<img src="assets/example.png" alt="Figure 1.">
<figcaption>
<span class="span"><strong>Figure 1. </strong></span>This is the figure caption.
</figcaption>

</figure>

</section>

</div>

</div>

</body>
"""


def test_simple():
    compare_have_want(
        have="""\
        :manuscript:

        :figure:
          :path: assets/example.png

          :caption: This is the figure caption.

        ::

        ::
        """,
        want=SIMPLE_WANT,
    )


def test_simple_with_extra_whitespace():
    compare_have_want(
        have="""\
        :manuscript:

        :figure:
          :path: assets/example.png

          :caption:
            This is the figure caption.


        ::

        ::
        """,
        want=SIMPLE_WANT,
    )


def test_simple_with_multi_line_caption():
    compare_have_want(
        have="""\
        :manuscript:

        :figure:
          :path: assets/example.png

          :caption:
            This is the figure caption.
            And it spans multiple lines.

        ::

        ::
        """,
        want=SIMPLE_WANT.replace(
            'This is the figure caption.',
            'This is the figure caption.\n    And it spans multiple lines.',
        ),
    )


def test_caption_with_inline_tags():
    compare_have_want(
        have="""\
        :manuscript:

        :figure:
          :path: assets/example.png

          :caption: This is the **figure** caption.

        ::

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <figure class="figure">
        <img src="assets/example.png" alt="Figure 1.">
        <figcaption>
        <span class="span"><strong>Figure 1. </strong></span>This is the <span class="span"><strong>figure</strong></span> caption.
        </figcaption>

        </figure>

        </section>

        </div>

        </div>

        </body>
        """,
    )
