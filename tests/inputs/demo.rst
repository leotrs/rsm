###################
A demo RSM document
###################

RSM is a suite of tools that aims to change the format of scientific publications using
modern web technology.  Currently, most scientific publications are made with LaTeX and
published in PDF format.  While the capabilities of LaTeX and related software are
undeniable, there are many pitfalls.  RSM aims to cover this gap.

RSM stands for (R)e(S)tructured (M)ath.  It is based on a modified version of the
(R)s(S)tructured (T)ext markup language.  Essentially, RSM works in the following way:
an author writes a manuscript in a plain text file with format :code:`.rsm` (which is an
alias of :code:`.rst`).  This file is transformed into a webpage by the command line
utility :code:`rsm-make`.  This website is completely standalone and can be viewed by
any web browser on any device.

The current document was written and processed with RSM.  It serves to illustrate some
of its features and functionality.  **WARNING**: Many of the features of RSM are
currently a work in progress.


********************
:no-num:The handrail
********************

One of the advantages of publishing manuscripts using web technology is interactivity.
This means embedability of images, video, and other media, but also more subtle design
elements that allow the user (i.e. the reader of the manuscript) to interact with the
document.  One of the main purposes of RSM is to make full use of such technology by
enhancing the UI/UX of reading scientific manuscripts in order to make reading papers a
satisfying experience.

One such design element is called the *handrail*.  This is the vertical gray bar that is
shown to the left of the title of this manuscript or to the left of this section's
title.  As a UI element, it serves to clearly demarcate where different sections start
and end.  As a UX element, it serves to signal opportunities for interaction.

For example, if you hover over the handrail to the left of this section's title, you
will see two buttons show up on the handrail.  First, the arrow button is the content
folding button: you can press it to hide the entire contents of the webpage.  Second,
the menu button with the three dots displays a context menu.  In the case of the
manuscript title, this menu allows the user to obtain a permanent link to the
manuscript, or to show a citation text.  (**NOTE**: currently these two buttons are
mock-ups and do not actually work.)


********
Tooltips
********

One of the main features of RSM is that anything can be labeled and referenced.  For
example,

.. theorem::
   :label: some-thm

   :label:`some-lbl` All `X` are `Y`.

The statement of the theorem has been labeled and can now be referred to :ref:`like this
<some-lbl>`.  Currently not all references will show the tooltips correctly, but the
reference in the previous line should work.  (**NOTE:** sometimes the math in the
tooltip is displayed incorrectly.  If the tooltip does not show, refresh the page a few
times first.)

Note the Theorem block also has a handrail and will eventually support a more
fully-featured context menu.


*****************
Structured Proofs
*****************

One major source of inspiration for the RSM project is what Leslie Lamport calls
'structured proofs'.  A good introduction to this topic is `this paper
<https://lamport.azurewebsites.net/pubs/proof.pdf>`_ or `this talk
<https://www.youtube.com/watch?v=uBiJpip9NVc&ab_channel=HeidelbergLaureateForum>`_.
Essentially, a structured proof is a mathematical proof written in a minimal markup
language that exposes its structure.  RSM implements some design and semantic elements
that support the idea of structured proofs.


A simple example
================

Perhaps the best way to discuss structured proofs is to illustrate with an example.
Consider the following theorem and its proof.

.. theorem::

   Socrates is mortal.

.. proof::

   :step: All men are mortal, and Socrates is mortal.  Therefore, Socrates is mortal.

This is the usual way in which mathematical proofs are presented in a manuscript: first
the statement, followed by chunk of text, followed by the filled square symbol
(a.k.a. *tombstone*).

**NOTE:** if you click the arrow button on the proof block's handrail, it should
show/hide the contents of the proof -- note this works on the proof block's handrail NOT
on the theorem block's handrail.  Note that when the contents of the proof are hidden,
the tombstone changes to a 'tombstone with ellipsis' symbol, which means that the proof
has contents (tombstone) that are hidden (ellipsis).

**NOTE:** Another design element in the proof block is that if you hover over the text
of the proof, you will see its own context menu as well as a gray number one in
parenthesis appear to the left of the handrail.  In RSM, each proof step has its own
context menu that allows for interaction.  The gray number is the step number within the
proof.  The following examples will make better use of these two new design elements,
but RSM includes them automatically, without requiring any additional work from the
manuscript's author, even in this simple theorem/proof.


:no-num:Adding some syntax
==========================

One of the problems with writing mathematics this way is that the logical structure is
lost in the text, especially when the text is long and involves displayed math, multiple
symbols, calls to previous results, intuitive explanations or 'proof sketches' along
with more rigorous derivations, etc.

The idea of 'structured proofs' as proposed by Lamport is to markup the text of a proof
with some keywords and indentation levels that expose its structure.  For example, we
can write the same proof as above in the following way.

.. theorem::

   |- Socrates is mortal.

.. proof::

   :step: All men are mortal.

   :step: Socrates is a man.


There are two main differences now.  First, the use of the '|-' symbol preceding each
claim.  Strictly speaking, a claim is a sentence that requires proof.  For example, the
statement of the theorem is a claim, as demarcated by the symbol '|-'.

The second main difference is that RSM recognizes that this proof has two steps.  It
does so by separating them in different paragraphs, each of which has its own context
menu and step number appearing in the handrail when you hover over them.  Finally, each
step has a tombstone that shows up only when you hover over the text.  This becomes more
useful in clearly separating the logic involved in different steps in a long proof.


Even more syntax
================

The next step is to realize that each step of a proof can also contain a claim.  In
fact, it is not necessarily obvious why each step in the previous theorem should be
accepted as true.  This means we need to write a mini sub-proof for each of the steps
that needs one.  RSM naturally supports this nested structure.  How many steps and
sub-steps a proof needs can only be determined by the author.  As Lamport puts it,
'write as many levels as you need, and then go one level deeper'.

In our case, we could explain each step like so:

.. theorem::

   |- Socrates is mortal.

.. proof::

   :step: |- All men are mortal.

      :p: Axiom.

   :step: |- Socrates is a man.

      :p: Axiom.

   :step: QED

      :p: By the previous two steps.

A few things to note: each sub-step can be folded using the arrow buttons appearing on
the handrail.  Each time you fold a step, a 'tombstone with ellipsis' symbol will appear
signaling that there is part of the proof (tombstone) that is hidden (ellipsis).
Another new element is the word QED.  Lamport suggests its use as a single step in a
proof when the previous steps of the proof are sufficient to establish what is claimed
but some additional text may be necessary to clarify that.

**NOTE:** The current example allows us to illustrate another function of the context
menu.  If you hover over the Proof title (i.e. the bold text that literally reads
**Proof** and NOT any of the contained steps), the context menu now shows a 'STEPS'
button.  If you press it, it should be obvious what it does: it automatically folds the
content of each step contained in the proof.  In this case, the proof now looks very
similar to the proof in the previous section, but the 'tombstone with ellipsis' symbols
signal that there is more content hidden.  If you press the 'STEPS' button again, each
step will show its contents again.  Of course, each step can be individually shown or
hidden by using its own context menu.


Keywords
========

Lamport also suggests the use of keywords that better expose the logical function of
each statement or claim in a proof.  For example, consider the following.

.. theorem::

   |- Socrates is mortal.

.. proof::

   :step: |- SUFFICES Socrates is a man.

      :p: It suffices to show that Socrates is a man because this fact plus Lemma X together imply the Theorem.

   :step: |- Socrates is a man.

      :p: Axiom.

The first step uses the SUFFICES keyword.  Note the claim in the first step includes
this keyword.  A statement involving the SUFFICES keyword has an important impact in the
proof: it changes what is being proved.  In this case, it changes the objective of the
proof from showing that 'Socrates is mortal' to showing that 'Socrates is a man'.
Highlighting the SUFFICES keyword allows the reader to keep track of the current
objective of the proof.  This is why the proof can now end after 'Socrates is a man' has
been shown, when in the previous case we needed one more step to guarantee that the
theorem had been established.

A much lengthier and better explanation of the SUFFICES keyword and others can be found
`here <https://lamport.azurewebsites.net/pubs/proof.pdf>`_ For now let us remark that
RSM is designed to support these keywords both syntactically and semantically.


**************
A longer proof
**************

The following example shows some of these features in a more realistic setting.  It also
shows one more feature: if you hover over the statement of the theorem, you will see
some stars and clocks icons appear to the left of the handrail.  These are meant to
signal to the reader how important (stars) and time-consuming (clocks) it is to read and
understand this particular theorem.  Accordingly, since this is an important theorem (it
has three stars), the handrail is thicker and colored.  Other keywords proposed by
Lamport are also used; their full explanation can be found in the cited paper.  Another
thing to note is that if you hover over a sub-proof, the gray numbers on the left will
show the appropriate sub-step number as well as the number of all parent steps.
Finally, note that the hyperlinked text will show the appropriate tooltips (**NOTE:** if
tooltips don't work, try reloading the page a few times and waiting a bit.)

.. theorem::
   :label: thm-some-name
   :stars: 3
   :clocks: 2

   ASSUME `f'(x) > 0` for all `x` in an interval `I`.  PROVE |- `f` is increasing on `I`.

.. proof::

   :step:`asm` |- SUFFICES to ASSUME that

          1. :label:`asm-1` `a` and `b` are points in `I`, and
          2. :label:`asm-2` `a < b`

          and PROVE |- `f(b) > f(a)`.

      :p: By definition of increasing function.

   :step: |- There is some `x` in `(a, b)` with `f(x)' = \frac{f(b) - f(a)}{b - a}`.

      :step: |- `f` is differentiable on `[a, b]`.  The following equation has nothing to do with the proof but illustrates the feature of displayed math within a sub-step.

             .. math::

                c^2 = b^2 + a^2

         :p: By :ref:`assumption 1 <asm-1>`, since `f` is differentiable on `I` by hypothesis.

      :step: |- `f` is continuous on `[a, b]`.

         :p: By :prev: and some other theorem.

      :step: QED

         :p: By :prev:, :prev2:, and the mean value theorem.

   :step: |- `f'(x) > 0` for all `x` in `(a, b)`.

      :p: By the hypothesis and :ref:`assumption 1<asm-1>`.

   :step:`star` |- `\frac{f(b) - f(a)}{b - a} > 0`.

      :p: By :prev:`the prev. step` and :prev2:`the one before`, also :prev2: which is the same, and :prev3:.

   :step: QED

      :p: :ref:`Assumption 2 <asm-2>` implies `b - a > 0`, so :ref:`star` implies `f(b) - f(a) > 0`, which implies `f(b) > f(a)`. By :ref:`asm`, this proves the original statement of the corollary.


*******
Wrap up
*******

RSM is very much still a work in progress but it aims to put together ideas from
Lamport's structured proofs, components from UI/UX, and standard web technologies to
change the way scientists write, read, and publish their work.  Note that the features
relating to Lamport's structured proofs are completely optional and other features (such
as the handrail and context menus, tooltips, design elements, etc) work independently of
whether or not the author choose to use structured proofs.
