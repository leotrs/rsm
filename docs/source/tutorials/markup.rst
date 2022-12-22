.. _markup:

RSM markup
==========

At the core of ReStructured Manuscripts is the RSM markup language. Inspired by popular
languages such as Markdown, ReST, and LaTeX, RSM strives for simplicity and power.


Base language
*************

Every RSM manuscript starts with the string ``:manuscript:`` and ends with a double
colon ``::``.  The entire contents of the manuscript are placed within these delimiters.

.. rsm::

   :manuscript:
   Hello, RSM!
   ::

The string ``:manuscript:`` is called a *tag*.  The double colon is called a `Halmos
<https://en.wikipedia.org/wiki/Tombstone_(typography)>`_ and acts as closing delimiter
for the corresponding tag.  Everything in between the tag and the Halmos is the tag's
*content*.

Tags may be embedded within the content of other tags.

.. rsm::

   :manuscript:

   :abstract:
     This is the manuscript's abstract.
   ::

   :section:
     :title: First Section
     And this is the contents of a section.
   ::

   ::

Some tags are *blocks*, meant to delimit a new section, part, or any other single
cohesive unit of content, while other tags are *inline*, meant to be embedded within
other tags.

.. rsm::

   :manuscript:

   :section:
     :title: Sections are blocks

   And notes are inline.:note:yay tooltips!::

   ::

   ::

The third type of tag is *meta* tags.  Meta tags modify their parent tag.  The
``:title:`` tag we used in the previous example is a meta tag that modifies the parent
``:section:`` tag.


Meta tags for blocks appear directly underneath the block tag, before the content, one
per line.  Meta tags for inlines appear within braces, separated by commas.

.. rsm::

   :manuscript:

   :section:
     :title: Fun with meta
     :nonum:

   Spans tags are fun because they can be
   be :span: {:strong:} bold and heavy ::
   or :span: {:emphas:} slanted and classy ::
   or :span: {:strong:, :emphas:} even both!::

   ::

   ::

In this example, the ``:section:`` tag has two meta tags: ``:title:`` and ``:nonum:``.
The second one of these determines that this section should not be numbered.  The
ensuing paragraph contains three ``:span:`` tags.  The ``:span:`` tag is a general
purpose inline tag that annotates its contents with special attributes, specified as
meta tags.  In this case, we show how to make some text bold, italic, or both.

And that's it!  What we have illustrated up to now covers 90% of the RSM markup
language.

.. admonition:: Summary

   The base language is comprised of

   1. A special character, the colon ``:``, used to delimit tags and Halmos.
   2. Tags which semantically annotate content.
   3. Tags may be blocks, inlines, or meta.
   4. Blocks are standalone units, inlines are embedded within the content of other
      tags, and meta modify or annotate other tags.
   5. Two other special characters, the braces ``{``, ``}``, used to enclose meta tags
      for inlines.





The base RSM language is comprised of tags, which may be blocks,
inlines, or meta.


Similarly to HTML, tags in RSM are used to indicate the type of their contents.  For
example, here we use two new tags ``:abstract:`` and ``:section:`` to mark where the
corresponding parts of the manuscript start and end.  Note each of these tags also ends
with a Halmos.



Tags may contain other tags.

.. rsm::

   :manuscript:

   :section:
     :title: First Section

   :enumerate:

     :item: First.

     :item: Second.

     :item: Third.

   ::
   ::

   ::


Shorthand
---------

In the previous section we illustrated how to generate bold and italic text in base RSM.

.. rsm::

   :manuscript:
   This text is :span: {:strong:} black ::
   and :span: {:emphas:} classy ::.
   ::

That's a lot of characters for something this simple.  RSM supports shorthand notation
for some common formulas.  In particular, the previous manuscript is identical to the
following.

.. rsm::

   :manuscript:
   This text is *black* and /classy/.
   ::

Other tags that support shorthand notation are the tags that introduce mathematical
content (using LaTeX notation).

.. rsm::

   :manuscript:

   Some math is about to happen, :math: 2+2 = 4::.
   And even more now, but centered,

   :mathblock:
   3+3 = 6
   ::

   ::

The following is the shorthand version.

.. rsm::

   :manuscript:

   Some math is about to happen, $2+2 = 4$.
   And even more now, but centered,

   $$
   3+3 = 6
   $$

   ::




Syntax rules
------------

Foo bar





Some tags are special in that they do not have content and therefore don't need a
Halmos.  A special example of tags of this kind are *meta* tags which are used to
annotate an enclosing tag.  For example, sections are usually numbered automatically:

.. rsm::

   :manuscript:

   :section:
     :title: First
   ::

   :section:
     :title: Second
   ::

   :section:
     :title: Third
   ::

   ::

However, the meta tag ``:nonum:`` may be used to prevent a section from being numbered:

.. rsm::

   :manuscript:

   :section:
     :title: First
   ::

   :section:
     :title: Second
     :nonum:
   ::

   :section:
     :title: Third (with number 2!)
   ::

   ::


Escaping
--------

Since
