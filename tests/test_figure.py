from conftest import compare_have_want


SIMPLE_WANT = """\
<body>

<div class="manuscriptwrapper">

<div id="manuscript" class="manuscript">

<section class="level-1">

<h1></h1>

<figure class="figure">
<img src="assets/example.png" alt="This is the figure caption.">
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
          :caption: This is the figure caption.::

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
            And it spans multiple lines.
          ::

        ::

        ::
        """,
        want=SIMPLE_WANT.replace(
            'This is the figure caption.',
            'This is the figure caption.\n    And it spans multiple lines.',
        ),
    )
