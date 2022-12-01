from conftest import compare_have_want


def test_simple():
    compare_have_want(
        have="""
        :manuscript:

        # Foo
        ::

        :appendix:

        # Bar
        ::

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <section class="section level-2">

        <h2>1. Foo</h2>

        </section>

        <section class="section level-2">

        <h2>A. Bar</h2>

        </section>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_subsection():
    compare_have_want(
        have="""
        :manuscript:

        # Foo
        ## Sub Foo
        ::
        ::

        :appendix:

        # Bar
        ## Sub Bar
        ::
        ::

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <section class="section level-2">

        <h2>1. Foo</h2>

        <section class="subsection level-3">

        <h3>1.1. Sub Foo</h3>

        </section>

        </section>

        <section class="section level-2">

        <h2>A. Bar</h2>

        <section class="subsection level-3">

        <h3>A.1. Sub Bar</h3>

        </section>

        </section>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_theorem():
    compare_have_want(
        have="""
        :manuscript:

        # Foo
        ## Sub Foo

        :theorem: ::

        ::
        ::

        :appendix:

        # Bar
        ## Sub Bar

        :theorem: ::
        ::
        ::

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <section class="section level-2">

        <h2>1. Foo</h2>

        <section class="subsection level-3">

        <h3>1.1. Sub Foo</h3>

        <div class="theorem">

        <div class="theorem-contents">

        <p class="paragraph theorem__title"><span class="span"><strong>Theorem 1.1.</strong></span></p>

        </div>

        </div>

        </section>

        </section>

        <section class="section level-2">

        <h2>A. Bar</h2>

        <section class="subsection level-3">

        <h3>A.1. Sub Bar</h3>

        <div class="theorem">

        <div class="theorem-contents">

        <p class="paragraph theorem__title"><span class="span"><strong>Theorem A.1.</strong></span></p>

        </div>

        </div>

        </section>

        </section>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_section_reftext():
    compare_have_want(
        have="""
        :manuscript:

        :ref:app::

        :appendix:

        # Foo bar
        :label: app
        ::

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <p class="paragraph"><a class="reference" href="#app">Appendix A</a></p>

        <section id="app" class="section level-2">

        <h2>A. Foo bar</h2>

        </section>

        </section>

        </div>

        </div>

        </body>
        """,
    )
