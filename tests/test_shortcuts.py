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
        <p class="paragraph">This paragraph has a<span class="span"><strong>shortcut</strong></span>for strong span.</p>
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
        <p class="paragraph">This paragraph has two<span class="span"><strong>shortcuts</strong></span>for strong<span class="span"><strong>spans</strong></span>.</p>
        </section>
        </div>
        </body>
        """
    )


def test_one_math():
    compare_have_want(
        have="""\
        :manuscript:
          :title: My Title

        This paragraph has some $2+2=4$ awesome math.

        ::
        """,
        want="""
        <body>
        <div id="manuscript" class="manuscript">
        <section class="level-1">
        <h1>My Title</h1>
        <p class="paragraph">This paragraph has some<span class="math">
        2+2=4
        </span>awesome math.</p>
        </section>
        </div>
        </body>
        """
    )


def test_two_math():
    compare_have_want(
        have="""\
        :manuscript:
          :title: My Title

        This paragraph has some $2+2=4$ awesome math and also some math that $2 + 2 + 2
        + 2 + 2 = 10$ is broken down.

        ::
        """,
        want="""
        <body>
        <div id="manuscript" class="manuscript">
        <section class="level-1">
        <h1>My Title</h1>
        <p class="paragraph">This paragraph has some<span class="math">
        2+2=4
        </span>awesome math and also some math that<span class="math">
        2 + 2 + 2
        + 2 + 2 = 10
        </span>is broken down.</p>
        </section>
        </div>
        </body>
        """
    )
