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
        <p class="paragraph">This paragraph has a <span class="span"><strong>shortcut</strong></span> for strong span.</p>
        </section>
        </div>
        </body>
        """,
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
        <p class="paragraph">This paragraph has two <span class="span"><strong>shortcuts</strong></span> for strong <span class="span"><strong>spans</strong></span>.</p>
        </section>
        </div>
        </body>
        """,
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
        <p class="paragraph">This paragraph has some <span class="math">
        \(2+2=4\)
        </span> awesome math.</p>
        </section>
        </div>
        </body>
        """,
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
        <p class="paragraph">This paragraph has some <span class="math">
        \(2+2=4\)
        </span> awesome math and also some math that <span class="math">
        \(2 + 2 + 2
        + 2 + 2 = 10\)
        </span> is broken down.</p>
        </section>
        </div>
        </body>
        """,
    )


def test_displaymath():
    compare_have_want(
        have="""\
        :manuscript:

        This paragraph contains display math
        $:2 + 2 = 4.:$

        ::
        """,
        want="""
        <body>
        <div id="manuscript" class="manuscript">
        <section class="level-1">
        <h1></h1>
        <p class="paragraph">This paragraph contains display math
        <div class="displaymath">
        $$
        2 + 2 = 4.
        $$
        </div></p>
        </section>
        </div>
        </body>
        """,
    )


def test_section_shortcut():
    compare_have_want(
        have="""\
        :manuscript:

        # My Section
          :label: my-sec

        This section contains a shortcut

        ::

        ::
        """,
        want="""
        <body>
        <div id="manuscript" class="manuscript">
        <section class="level-1">
        <h1></h1>
        <section id="my-sec" class="section level-2">
        <h2>1. My Section</h2>
        <p class="paragraph">This section contains a shortcut</p>
        </section>
        </section>
        </div>
        </body>
        """,
    )


def test_claim_shortcut():
    compare_have_want(
        have="""\
        :manuscript:

        This paragraph contains a |- claim with a turnstile. And also another one ⊢ but it takes
        multiple lines.

        ::
        """,
        want="""
        <body>
        <div id="manuscript" class="manuscript">
        <section class="level-1">
        <h1></h1>
        <p class="paragraph">This paragraph contains a <span class="claim">claim with a turnstile</span>. And also another one <span class="claim">but it takes
        multiple lines</span>.</p>
        </section>
        </div>
        </body>
        """,
    )
