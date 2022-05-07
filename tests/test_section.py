from conftest import compare_have_want


def test_simple():
    compare_have_want(
        have="""\
        :manuscript:

        :section:
          :title: Section

        Lorem ipsum.

        ::

        ::
        """,
        want="""\
        <body>
        <div id="manuscript" class="manuscript">
        <section class="level-1">
        <h1></h1>
        <section class="section level-2">
        <h2>1. Section</h2>
        <p class="paragraph">Lorem ipsum.</p>
        </section>
        </section>
        </div>
        </body>
        """,
    )


def test_subsections():
    compare_have_want(
        have="""\
        :manuscript:

        :section:
          :title: Section

        Lorem ipsum.

        :subsection:
          :title: Sub section

        Foo

        :subsubsection:
          :title: Sub sub section

        Bar

        ::

        ::

        ::

        ::
        """,
        want="""\
        <body>
        <div id="manuscript" class="manuscript">
        <section class="level-1">
        <h1></h1>
        <section class="section level-2">
        <h2>1. Section</h2>
        <p class="paragraph">Lorem ipsum.</p><section class="subsection level-3">
        <h3>1.1. Sub section</h3>
        <p class="paragraph">Foo</p><section class="subsubsection level-4">
        <h4>1.1.1. Sub sub section</h4>
        <p class="paragraph">Bar</p>
        </section>
        </section>
        </section>
        </section>
        </div>
        </body>
        """,
    )


def test_shortcut():
    compare_have_want(
        have="""\
        :manuscript:

        # Section

        Lorem ipsum.

        ## Sub section

        Foo

        ### Sub sub section

        Bar

        ::

        ::

        ::

        ::
        """,
        want="""\
        <body>
        <div id="manuscript" class="manuscript">
        <section class="level-1">
        <h1></h1>
        <section class="section level-2">
        <h2>1. Section</h2>
        <p class="paragraph">Lorem ipsum.</p><section class="subsection level-3">
        <h3>1.1. Sub section</h3>
        <p class="paragraph">Foo</p><section class="subsubsection level-4">
        <h4>1.1.1. Sub sub section</h4>
        <p class="paragraph">Bar</p>
        </section>
        </section>
        </section>
        </section>
        </div>
        </body>
        """,
    )
