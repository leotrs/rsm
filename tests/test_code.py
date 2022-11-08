from conftest import compare_have_want


def test_display_alone():
    compare_have_want(
        have="""\
        :manuscript:

        :displaycode:
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

        <div id="some-code" class="displaycode python">
        comp = [abs(x) for x in range(10)]


        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_display_alone():
    compare_have_want(
        have="""\
        :manuscript:

        :displaycode:
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

        <div id="some-code" class="displaycode python">
        comp = [abs(x) for x in range(10)]


        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )
