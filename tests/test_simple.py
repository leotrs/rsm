from conftest import compare_have_want


def test_simple():
    compare_have_want(
        have="""\
        :manuscript:

        Lorem ipsum.

        ::
        """,
        want="""\
        <body>
        <div id="manuscript" class="manuscript">
        <section class="level-1">
        <h1></h1>
        <p class="paragraph">Lorem ipsum.</p>
        </section>
        </div>
        </body>
        """
    )

    compare_have_want(
        have="""\
        :manuscript:
          :title: My Title

        Lorem ipsum.

        ::
        """,
        want="""\
        <body>
        <div id="manuscript" class="manuscript">
        <section class="level-1">
        <h1>My Title</h1>
        <p class="paragraph">Lorem ipsum.</p>
        </section>
        </div>
        </body>
        """
    )

    compare_have_want(
        have="""\
        :manuscript:
          :label: mylbl
          :title: My Title
          :date: 2022-03-29
        ::
        """,
        want="""\
        <body>
        <div id="mylbl" class="manuscript">
        <section class="level-1">
        <h1>My Title</h1>
        </section>
        </div>
        </body>
        """
    )
