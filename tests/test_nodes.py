import rsm


def test_equality():
    s1, s2 = rsm.core.nodes.Step(), rsm.core.nodes.Step()
    assert s1 is not s2
    assert s1 == s2


def test_equality_different_number_ofchildren():
    s1, s2 = rsm.core.nodes.Step(), rsm.core.nodes.Step()
    s1.append(rsm.core.nodes.Paragraph())
    assert s1 is not s2
    assert s1 != s2


def test_equality_different_children():
    s1, s2 = rsm.core.nodes.Step(), rsm.core.nodes.Step()
    s1.append(rsm.core.nodes.Paragraph())
    s2.append(rsm.core.nodes.Subproof())
    assert s1 is not s2
    assert s1 != s2

    s2.prepend(rsm.core.nodes.Paragraph())
    assert s1 is not s2
    assert s1 != s2


def test_equality_different_parent():
    p = rsm.core.nodes.Proof()
    s1, s2 = rsm.core.nodes.Step(), rsm.core.nodes.Step()
    p.append(s1)
    assert s1 is not s2
    assert s1 != s2
