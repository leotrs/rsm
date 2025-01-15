from conftest import compare_have_want

import rsm


def test_mechanism():
    cls = rsm.nodes.Section
    node = cls()
    assert node.classreftext == cls.classreftext
    assert node.reftext_template == cls.classreftext
    assert node.reftext == "Section "

    node.reftext_template = "foobar"
    assert node.classreftext == cls.classreftext
    assert node.reftext_template == "foobar"
    assert node.reftext == "foobar"
    node.reftext_template = "{number}"
    assert node.reftext == ""
    node.number = 1
    assert node.reftext == "1"

    node = cls(reftext_template="foobar")
    assert node.classreftext == cls.classreftext
    assert node.reftext_template == "foobar"
    node.reftext_template = "{number}"
    assert node.reftext == ""
    node.number = 1
    assert node.reftext == "1"


def test_simple():
    compare_have_want(
        have="""\
        :manuscript:

        Some math
        :mathblock:
          :label: eqn
          :reftext: Important Equation
          2+2=4
        ::

        Here we refer to the :ref:eqn::.

        ::
        """,
        want="""\
        <body>

        <div class="manuscriptwrapper">

        <div class="manuscript" data-nodeid="0">

        <section class="level-1">

        <div class="paragraph" data-nodeid="1">

        <p>Some math </p>
        <div id="eqn" class="mathblock" data-nodeid="3">
        $$
        2+2=4
        $$
        </div>

        </div>

        <div class="paragraph" data-nodeid="5">

        <p>Here we refer to the <a class="reference" href="#eqn">Important Equation</a>.</p>

        </div>

        </section>

        </div>

        </div>

        </body>
        """,
    )
