from conftest import compare_have_want




def test_simple():
    compare_have_want(
        have="""\
        :manuscript:

        :section:
          :title: Section

        This pargraph contains a claim :claim: :label: clm-lbl :: all $X$ are $Y$ ::.

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
        <p class="paragraph">This pargraph contains a claim <span id="clm-lbl" class="claim">all <span class="math">
        \(X\)
        </span> are <span class="math">
        \(Y\)
        </span> </span>.</p>
        </section>
        </section>
        </div>
        </body>
        """
    )
