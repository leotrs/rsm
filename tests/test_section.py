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

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <section class="section level-2" data-nodeid="1">

        <h2>1. Section</h2>

        <p class="paragraph" data-nodeid="2">Lorem ipsum.</p>

        </section>

        </section>

        </div>

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

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <section class="section level-2" data-nodeid="1">

        <h2>1. Section</h2>

        <p class="paragraph" data-nodeid="2">Lorem ipsum.</p>

        <section class="subsection level-3" data-nodeid="4">

        <h3>1.1. Sub section</h3>

        <p class="paragraph" data-nodeid="5">Foo</p>

        <section class="subsubsection level-4" data-nodeid="7">

        <h4>1.1.1. Sub sub section</h4>

        <p class="paragraph" data-nodeid="8">Bar</p>

        </section>

        </section>

        </section>

        </section>

        </div>

        </div>

        </body>
        """,
    )
