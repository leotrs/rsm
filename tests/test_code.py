from conftest import compare_have_want


def test_codeblock():
    compare_have_want(
        have="""\
        :manuscript:

        :codeblock:
          :label: some-code
          :types: python

          comp = [abs(x) for x in range(10)]

        ::

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div id="manuscript" class="manuscript">

        <section class="level-1">

        <h1></h1>

        <div id="some-code" class="codeblock python">
        comp = [abs(x) for x in range(10)]


        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )
