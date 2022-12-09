from conftest import compare_have_want


def test_empty_table():
    compare_have_want(
        have="""\
        :manuscript:

        :table:

        ::

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <table class="table">

        </table>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_one_row_no_header():
    compare_have_want(
        have="""
        :manuscript:

        :table:

        :tbody:

        :tr: :td:foo:: :td:bar:: ::

        ::

        ::

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <table class="table">

        <tbody class="tablebody">

        <tr class="tablerow">

        <td class="tabledatum">foo</td>

        <td class="tabledatum">bar</td>

        </tr>

        </tbody>

        </table>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_two_rows_no_header():
    compare_have_want(
        have="""
        :manuscript:

        :table:

        :tbody:

        :tr: :td:one:: :td:two:: ::

        :tr: :td:three:: :td:four:: ::

        ::

        ::

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <table class="table">

        <tbody class="tablebody">

        <tr class="tablerow">

        <td class="tabledatum">one</td>

        <td class="tabledatum">two</td>

        </tr>

        <tr class="tablerow">

        <td class="tabledatum">three</td>

        <td class="tabledatum">four</td>

        </tr>

        </tbody>

        </table>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_with_header():
    compare_have_want(
        have="""
        :manuscript:

        :table:

        :thead:

        :tr: :td: head1 :: :td: head2 :: ::

        ::

        :tbody:

        :tr: :td:one:: :td:two:: ::

        :tr: :td:three:: :td:four:: ::

        ::

        ::

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <table class="table">

        <thead class="tablehead">

        <tr class="tablerow">

        <td class="tabledatum">head1</td>

        <td class="tabledatum">head2</td>

        </tr>

        </thead>

        <tbody class="tablebody">

        <tr class="tablerow">

        <td class="tabledatum">one</td>

        <td class="tabledatum">two</td>

        </tr>

        <tr class="tablerow">

        <td class="tabledatum">three</td>

        <td class="tabledatum">four</td>

        </tr>

        </tbody>

        </table>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_math_in_header():
    compare_have_want(
        have=r"""        :manuscript:

        :table:

        :thead:

        :tr: :td: $H^{\eta}$ :: :td: $H^{*}$ :: :td: $H^{c}$ :: ::

        ::

        ::

        ::
        """,
        want=r"""        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <table class="table">

        <thead class="tablehead">

        <tr class="tablerow">

        <td class="tabledatum"><span class="math">\(H^{\eta}\)</span></td>

        <td class="tabledatum"><span class="math">\(H^{*}\)</span></td>

        <td class="tabledatum"><span class="math">\(H^{c}\)</span></td>

        </tr>

        </thead>

        </table>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_shortcuts_in_header():
    compare_have_want(
        have="""
        :manuscript:

        :table:

        :tbody:

        :tr: :td: /foo/ :: :td: *bar* :: ::

        ::

        ::

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <table class="table">

        <tbody class="tablebody">

        <tr class="tablerow">

        <td class="tabledatum"><span class="span"><em>foo</em></span></td>

        <td class="tabledatum"><span class="span"><strong>bar</strong></span></td>

        </tr>

        </tbody>

        </table>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_simple_caption():
    compare_have_want(
        have="""
        :manuscript:

        :table:

        :tbody:

        :tr: :td:foo:: :td:bar:: ::

        ::

        :caption:
        This is a caption.

        ::

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <table class="table">

        <tbody class="tablebody">

        <tr class="tablerow">

        <td class="tabledatum">foo</td>

        <td class="tabledatum">bar</td>

        </tr>

        </tbody>

        <caption>
        <span class="span"><strong>Table 1. </strong></span>This is a caption.
        </caption>

        </table>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_simple_caption_with_shortcuts():
    compare_have_want(
        have="""
        :manuscript:

        :table:

        :tbody:

        :tr: :td:foo:: :td:bar:: ::

        ::

        :caption:
        This is a /caption/ with shortcuts $2+2$.

        ::

        ::
        """,
        want=r"""        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <table class="table">

        <tbody class="tablebody">

        <tr class="tablerow">

        <td class="tabledatum">foo</td>

        <td class="tabledatum">bar</td>

        </tr>

        </tbody>

        <caption>
        <span class="span"><strong>Table 1. </strong></span>This is a <span class="span"><em>caption</em></span> with shortcuts <span class="math">\(2+2\)</span>.
        </caption>

        </table>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_reference_to_table():
    compare_have_want(
        have="""
        :manuscript:

        :table:
        :label: lbl

        :tbody:

        :tr: :td:foo:: :td:bar:: ::

        ::

        ::

        This :ref:lbl:: refers to the table.

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <table id="lbl" class="table">

        <tbody class="tablebody">

        <tr class="tablerow">

        <td class="tabledatum">foo</td>

        <td class="tabledatum">bar</td>

        </tr>

        </tbody>

        </table>

        <p class="paragraph">This <a class="reference" href="#lbl">Table 1</a> refers to the table.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_reference_to_table_with_reftext():
    compare_have_want(
        have="""
        :manuscript:

        :table:
        :label: lbl

        :tbody:

        :tr: :td:foo:: :td:bar:: ::

        ::

        ::

        This :ref:lbl,refers:: to the table.

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <table id="lbl" class="table">

        <tbody class="tablebody">

        <tr class="tablerow">

        <td class="tabledatum">foo</td>

        <td class="tabledatum">bar</td>

        </tr>

        </tbody>

        </table>

        <p class="paragraph">This <a class="reference" href="#lbl">refers</a> to the table.</p>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_extra_space_within_tr():
    compare_have_want(
        have="""
        :manuscript:

        :table:

        :tbody:

        :tr:
          :td:foo::
          :td:bar::
        ::

        ::

        ::

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <table class="table">

        <tbody class="tablebody">

        <tr class="tablerow">

        <td class="tabledatum">foo</td>

        <td class="tabledatum">bar</td>

        </tr>

        </tbody>

        </table>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_real_life_example():
    compare_have_want(
        have=r"""        :manuscript:

        :table:
          :label: lbl

          :thead:
            :tr: :td: $H^{\tau}$ :: :td: $H^{*}$ :: :td: $H^{c}$ :: ::
          ::
          :tbody:
            :tr: :td: $0.0001$ :: :td: $0.0146$ :: :td: $0.0549$ :: ::
            :tr: :td: $0.1222$ :: :td: $0.0139$ :: :td: $0.0106$ :: ::

          ::

          :caption:
          Values of $\epsilon$ and $\delta$ for select subgraphs of Gr-Qc.

        ::

        ::
        """,
        want=r"""        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <table id="lbl" class="table">

        <thead class="tablehead">

        <tr class="tablerow">

        <td class="tabledatum"><span class="math">\(H^{\tau}\)</span></td>

        <td class="tabledatum"><span class="math">\(H^{*}\)</span></td>

        <td class="tabledatum"><span class="math">\(H^{c}\)</span></td>

        </tr>

        </thead>

        <tbody class="tablebody">

        <tr class="tablerow">

        <td class="tabledatum"><span class="math">\(0.0001\)</span></td>

        <td class="tabledatum"><span class="math">\(0.0146\)</span></td>

        <td class="tabledatum"><span class="math">\(0.0549\)</span></td>

        </tr>

        <tr class="tablerow">

        <td class="tabledatum"><span class="math">\(0.1222\)</span></td>

        <td class="tabledatum"><span class="math">\(0.0139\)</span></td>

        <td class="tabledatum"><span class="math">\(0.0106\)</span></td>

        </tr>

        </tbody>

        <caption>
        <span class="span"><strong>Table 1. </strong></span>Values of <span class="math">\(\epsilon\)</span> and <span class="math">\(\delta\)</span> for select subgraphs of Gr-Qc.
        </caption>

        </table>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_real_life_example_different_spacing():
    compare_have_want(
        have=r"""         :manuscript:

        :table:
          :label: lbl

          :thead:
          :tr:
            :td: $H^{\tau}$ ::
            :td: $H^{*}$ ::
            :td: $H^{c}$ :: ::
          ::
          :tbody:
          :tr:
            :td: $0.0001$ ::
            :td: $0.0146$ ::
            :td: $0.0549$ :: ::
          :tr:
            :td: $0.1222$ ::
            :td: $0.0139$ ::
            :td: $0.0106$ ::
          ::
          ::

          :caption:
          Values of $\epsilon$ and $\delta$ for select subgraphs of Gr-Qc.

        ::

        ::
        """,
        want=r"""        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <table id="lbl" class="table">

        <thead class="tablehead">

        <tr class="tablerow">

        <td class="tabledatum"><span class="math">\(H^{\tau}\)</span></td>

        <td class="tabledatum"><span class="math">\(H^{*}\)</span></td>

        <td class="tabledatum"><span class="math">\(H^{c}\)</span></td>

        </tr>

        </thead>

        <tbody class="tablebody">

        <tr class="tablerow">

        <td class="tabledatum"><span class="math">\(0.0001\)</span></td>

        <td class="tabledatum"><span class="math">\(0.0146\)</span></td>

        <td class="tabledatum"><span class="math">\(0.0549\)</span></td>

        </tr>

        <tr class="tablerow">

        <td class="tabledatum"><span class="math">\(0.1222\)</span></td>

        <td class="tabledatum"><span class="math">\(0.0139\)</span></td>

        <td class="tabledatum"><span class="math">\(0.0106\)</span></td>

        </tr>

        </tbody>

        <caption>
        <span class="span"><strong>Table 1. </strong></span>Values of <span class="math">\(\epsilon\)</span> and <span class="math">\(\delta\)</span> for select subgraphs of Gr-Qc.
        </caption>

        </table>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_tr_shortcut():
    compare_have_want(
        have="""
        :manuscript:

        :table:

        :thead:
        :tr: foo : bar : baz ::
        ::
        :tbody:
        :tr: a1 : a2 : a3 ::
        :tr: b1 : b2 : b3 ::
        ::

        ::

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <table class="table">

        <thead class="tablehead">

        <tr class="tablerow">

        <td class="tabledatum">foo</td>

        <td class="tabledatum">bar</td>

        <td class="tabledatum">baz</td>

        </tr>

        </thead>

        <tbody class="tablebody">

        <tr class="tablerow">

        <td class="tabledatum">a1</td>

        <td class="tabledatum">a2</td>

        <td class="tabledatum">a3</td>

        </tr>

        <tr class="tablerow">

        <td class="tabledatum">b1</td>

        <td class="tabledatum">b2</td>

        <td class="tabledatum">b3</td>

        </tr>

        </tbody>

        </table>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_tr_shortcut_with_math():
    compare_have_want(
        have=r"""        :manuscript:

        :table:

        :thead:
        :tr: $H^{\tau}$ : $H^{\top}$ : $H^{c}$ ::
        ::
        :tbody:
        :tr: $0.0001$ : $0.0146$ : $0.0549$ ::
        :tr: $0.1222$ : $0.0139$ : $0.0106$ ::
        ::

        ::

        ::
        """,
        want=r"""        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <table class="table">

        <thead class="tablehead">

        <tr class="tablerow">

        <td class="tabledatum"><span class="math">\(H^{\tau}\)</span></td>

        <td class="tabledatum"><span class="math">\(H^{\top}\)</span></td>

        <td class="tabledatum"><span class="math">\(H^{c}\)</span></td>

        </tr>

        </thead>

        <tbody class="tablebody">

        <tr class="tablerow">

        <td class="tabledatum"><span class="math">\(0.0001\)</span></td>

        <td class="tabledatum"><span class="math">\(0.0146\)</span></td>

        <td class="tabledatum"><span class="math">\(0.0549\)</span></td>

        </tr>

        <tr class="tablerow">

        <td class="tabledatum"><span class="math">\(0.1222\)</span></td>

        <td class="tabledatum"><span class="math">\(0.0139\)</span></td>

        <td class="tabledatum"><span class="math">\(0.0106\)</span></td>

        </tr>

        </tbody>

        </table>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_tr_shortcut_with_newlines():
    compare_have_want(
        have="""
        :manuscript:

        :table:

        :thead:
        :tr:
        foo : bar : baz
        ::
        ::
        :tbody:
        :tr:
        a1 : a2 : a3
        ::
        :tr:
        b1 : b2 : b3
        ::
        ::

        ::

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <table class="table">

        <thead class="tablehead">

        <tr class="tablerow">

        <td class="tabledatum">foo</td>

        <td class="tabledatum">bar</td>

        <td class="tabledatum">baz</td>

        </tr>

        </thead>

        <tbody class="tablebody">

        <tr class="tablerow">

        <td class="tabledatum">a1</td>

        <td class="tabledatum">a2</td>

        <td class="tabledatum">a3</td>

        </tr>

        <tr class="tablerow">

        <td class="tabledatum">b1</td>

        <td class="tabledatum">b2</td>

        <td class="tabledatum">b3</td>

        </tr>

        </tbody>

        </table>

        </section>

        </div>

        </div>

        </body>
        """,
    )


def test_tr_shortcut_with_escaped_colon():
    compare_have_want(
        have=r"""        :manuscript:

        :table:

        :thead:
        :tr: foo : bar : baz ::
        ::
        :tbody:
        :tr: a\: : a2 : a3 ::
        :tr: b1  : b2 : b3 ::
        ::

        ::

        ::
        """,
        want="""
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript">

        <section class="level-1">

        <table class="table">

        <thead class="tablehead">

        <tr class="tablerow">

        <td class="tabledatum">foo</td>

        <td class="tabledatum">bar</td>

        <td class="tabledatum">baz</td>

        </tr>

        </thead>

        <tbody class="tablebody">

        <tr class="tablerow">

        <td class="tabledatum">a:</td>

        <td class="tabledatum">a2</td>

        <td class="tabledatum">a3</td>

        </tr>

        <tr class="tablerow">

        <td class="tabledatum">b1</td>

        <td class="tabledatum">b2</td>

        <td class="tabledatum">b3</td>

        </tr>

        </tbody>

        </table>

        </section>

        </div>

        </div>

        </body>
        """,
    )
