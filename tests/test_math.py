from conftest import compare_have_want


def test_display_alone():
    compare_have_want(
        have="""\
        :manuscript:

        :displaymath:
          :label: eqn-plus
          :types: {smallequation}
          :number:

          2 + 2 = 4

        ::

        ::
        """,
        want="""\
        <body>
        <div id="manuscript" class="manuscript">
        <section class="level-1">
        <h1></h1>
        <div id="eqn-plus" class="math smallequation">
        2 + 2 = 4
        </div>
        </section>
        </div>
        </body>
        """
    )



def test_inline_no_meta():
    compare_have_want(
        have="""\
        :manuscript:

        This paragraph contains inline math :math: :label: bar, :types: {smallequation} :: 2 + 2
        = 4 ::.

        ::
        """,
        want="""\
        <body>
        <div id="manuscript" class="manuscript">
        <section class="level-1">
        <h1></h1>
        <p class="paragraph">This paragraph contains inline math<span id="bar" class="math smallequation">
        2 + 2
        = 4
        </span>.</p>
        </section>
        </div>
        </body>
        """
    )


def test_display_in_paragraph_no_meta():
    compare_have_want(
        have="""\
        :manuscript:

        This paragraph contains display math
        :displaymath:
        2 + 2 = 4.
        ::

        ::
        """,
        want="""\
        <body>
        <div id="manuscript" class="manuscript">
        <section class="level-1">
        <h1></h1>
        <p class="paragraph">This paragraph contains display math<div class="math">
        2 + 2 = 4.
        </div></p>
        </section>
        </div>
        </body>
        """
    )


def test_display_in_paragraph_no_meta():
    compare_have_want(
        have="""\
        :manuscript:

        This paragraph contains display math
        :displaymath:
          :label: foo
          2 + 2 = 4.
        ::

        ::
        """,
        want="""\
        <body>
        <div id="manuscript" class="manuscript">
        <section class="level-1">
        <h1></h1>
        <p class="paragraph">This paragraph contains display math<div id="foo" class="math">
        2 + 2 = 4.
        </div></p>
        </section>
        </div>
        </body>
        """
    )


def test_inline_with_meta():
    compare_have_want(
        have="""\
        :manuscript:

        This paragraph contains inline math :math: :label: bar, :types: {smallequation} :: 2 + 2
        = 4 ::.

        ::
        """,
        want="""\
        <body>
        <div id="manuscript" class="manuscript">
        <section class="level-1">
        <h1></h1>
        <p class="paragraph">This paragraph contains inline math<span id="bar" class="math smallequation">
        2 + 2
        = 4
        </span>.</p>
        </section>
        </div>
        </body>
        """
    )
