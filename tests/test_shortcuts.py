from conftest import compare_have_want


def test_one_strong():
    compare_have_want(
        have="""\
        :manuscript:
          :title: My Title

        This paragraph has a *shortcut* for strong span.

        ::
        """,
        want="""
        <body>
        <div id="manuscript" class="manuscript">
        <section class="level-1">
        <h1>My Title</h1>
        <p class="paragraph">This paragraph has a
        <span class="span">
        <strong>shortcut</strong>
        </span>
        for strong span.</p>
        </section>
        </div>
        </body>
        """
    )


def test_two_strong():
    compare_have_want(
        have="""\
        :manuscript:
          :title: My Title

        This paragraph has two *shortcuts* for strong *spans*.

        ::
        """,
        want="""
        <body>
        <div id="manuscript" class="manuscript">
        <section class="level-1">
        <h1>My Title</h1>
        <p class="paragraph">This paragraph has two
        <span class="span">
        <strong>shortcuts</strong>
        </span>
        for strong
        <span class="span">
        <strong>spans</strong>
        </span>
        .</p>
        </section>
        </div>
        </body>
        """
    )
