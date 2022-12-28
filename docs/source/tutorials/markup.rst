.. _markup:

RSM markup
==========

At the core of ReStructured Manuscripts is the RSM markup language. Inspired by popular
languages such as Markdown, ReST, and LaTeX, RSM strives for simplicity, flexibility,
and functionality.

Every RSM manuscript starts with the string ``:manuscript:`` and ends with a double
colon ``::``.  The entire contents of the manuscript are placed within these delimiters.

.. rsm::

   :manuscript:

   Hello, RSM!

   ::

Strings such as ``:manuscript:`` are called *tags*.  Tags are used to annotate regions
of text, for example to delimit sections and other parts of a manuscript.  The tag
functions as open delimiter, and the empty tag ``::``, a.k.a. *Halmos*, is the closing
delimiter.

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

Some tags are used to add meta-data to the annotated regions.  For example, the
``:section:`` tag in the previous example introduces a new region of the manuscript,
while the ``:title:`` tag directly below it modifies the parent ``:section:`` tag by
specifying its title.

Tags such as ``:manuscript:``, ``:abstract:``, and ``:section:`` introduce parts of the
manuscript that are clearly separated from other parts.  In contrast, the ``:span:`` tag
introduces a region of text that lies within some other, enclosing, parent part.

.. rsm::

   :manuscript:

   Span tags do not introduce new parts, but
   :span: {:strong:} live within:: their
   parents.

   ::

In this example, we have used the ``:strong:`` tag to modify the enclosing ``:span:``
tag, which is in turn part of the surrounding paragraph of text.  Note the use of braces
to introduce the ``:strong:`` tag and the use of the Halmos ``::`` as closing delimiter
of ``:span:``.

The notation ``:span: {:strong:} text ::`` to introduce bold text allows an alternative
*shorthand* notation using asterisks (``*``).  Similarly, the hashtag (``#``) symbol can
be used as shorthand to introduce a section with a title.

.. rsm::

   :manuscript:

   # Awesome section

   Span tags do not introduce new parts, but
   *live within* their parents.

   ::

   ::

Here is a complete example using all the basic features of RSM markup.

.. rsm::

   :manuscript:
     :title: RSM Markup

   :author:
     :name: Melvin J. Blanc
     :affiliation: ACME University
     :email: mel@acme.edu
   ::

   :abstract:

     Web-first scientific manuscripts.

   ::

   # Awesome Section

   Simple markup for :span:{:strong:, :emphas:}
   web native:: scientific publications.

   ::

   ::

The features on this page cover 90% of what can be done with RSM.

.. admonition:: Summary

   The base language is comprised of *tags*, which delimit or modify text.  Some tags
   introduce new parts of the manuscript, while others simply annotate their content.
   All tags are introduced by using their name surrounded by colons ``:tag-name:`` and
   end at a Halmos, or empty tag, ``::``.  Some tags allow for shorthand notation, such
   as using asterisks ``*`` to introduce bold text.  Tags can be nested within the
   contents of other tags.

.. tip::

   Whitespace is ignored essentially everywhere in RSM.  It is recommended to leave
   generous whitespace where desired to improve readability.
