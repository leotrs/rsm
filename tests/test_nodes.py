import rsm
from rsm.core.nodes import (
    Paragraph,
    PendingReference,
    Reference,
    Text,
    Step,
    Proof,
    Subproof,
)


def test_equality():
    s1, s2 = Step(), Step()
    assert s1 is not s2
    assert s1 == s2


def test_equality_different_number_ofchildren():
    s1, s2 = Step(), Step()
    s1.append(Paragraph())
    assert s1 is not s2
    assert s1 != s2


def test_equality_different_children():
    s1, s2 = Step(), Step()
    s1.append(Paragraph())
    s2.append(Subproof())
    assert s1 is not s2
    assert s1 != s2

    s2.prepend(Paragraph())
    assert s1 is not s2
    assert s1 != s2


def test_equality_different_parent():
    p = Proof()
    s1, s2 = Step(), Step()
    p.append(s1)
    assert s1 is not s2
    assert s1 != s2


def test_equal_to_self():
    pending = PendingReference(target='lbl')
    assert pending == pending


def test_replace_self():
    target = Paragraph(label='lbl')
    para = Paragraph()
    pending = PendingReference(target='lbl')
    para.append(Text('foo'))
    para.append(pending)
    para.append(Text('bar'))
    assert pending is para.children[1]
    assert pending == para.children[1]
    assert pending != para.children[0]
    assert pending != para.children[2]

    ref = Reference(target=target)
    pending.replace_self(ref)
    assert pending.parent is None
    assert ref.parent is para
    assert pending not in para.children
    assert ref is para.children[1]
    assert ref == para.children[1]
