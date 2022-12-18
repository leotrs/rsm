.. _markup:

RSM markup
==========

At the core of ReStructured Manuscripts is the RSM markup language. Inspired by popular
languages such as Markdown, ReST, and LaTeX, RSM strives for simplicity and power.


Base language
*************

Every RSM manuscript starts with the string ``:manuscript:`` and ends with a double
colon ``::``.  The entire contents of the manuscript are placed within these delimiters.

.. code-block:: text

   :manuscript:
   Hello, RSM!
   ::

The string ``:manuscript:`` is called a *tag*.  Tags are used in RSM to annotate their
contents.  For example, here we use two new tags ``:abstract:`` and ``:section:`` to
mark where the corresponding parts of the manuscript start and end.

.. code-block:: text

   :manuscript:

   :abstract:
     This is the manuscript's abstract.
   ::

   :section:
     And this is the contents of a section.
   ::

   ::

Every one of these tags ends with a double colon ``::``.  The double colon is referred
to as `Halmos <https://en.wikipedia.org/wiki/Tombstone_(typography)>`_.

Tags may contain other tags:



.. info::
   The base language is comprised of
   1. One special character, the colon, used to delimit tags and Halmos
   2. Tags which semantically annotate content.
   3.


Tags
----

One of the main goals of RSM is to separate your manuscript's content from the look and
feel.  Accordingly, RSM provides *semantic tags* that annotate the contents of your
manuscript.  A tag has the form ``:tag-name: <contents> ::``.  As mentioned above, every
RSM manuscript starts with the ``:manuscript:`` tag and ends with the Halmos ``::``.
The entire contents of your manuscript are the contents of the ``:manuscript:`` tag.

Tags being semantic means that a tag determines what its contents *are*, not what they
should look like.  Two parts of your manuscript may be annotated with the same tag but
end up looking differently in the final output.  Later on we will see examples of this.

You can think of the Halmos ``::`` as the *empty* tag.  With few exceptions, every
region of text annotated with a tag always ends with a Halmos.


Types of tags
-------------

There are three different types of tags in RSM: block, inline, and meta.  If you are
familiar with HTML, blocks and inlines work in RSM much the same way as block and inline
elements in HTML, whereas meta tags are similar in some respects to HTML attributes.

Block and inline tags are meant to carry content.  The content may be text or other
tags.  Meta tags are special in that they associate metadata to the immediately
enclosing tag.  Consider this example

.. code-block:: text

   :manuscript:
      :title: Three types of tags.

   Hello, RSM!

   ::

Here the role of the ``:title:`` tag is to associate the title ``Three types of tags``
to the enclosing ``:manuscript:`` tag.  This tells RSM that the given title is a
property of the contents of the ``:manuscript:`` tag, i.e. a property of the entire
manuscript.  We say the ``:title:`` is a *meta key* for the enclosing ``:manuscript:``
tag, while the title ``Three types of tags`` is the *meta value* of said key.  Meta tags
always come in key-values pairs.

In the previous example, the ``:title:`` meta tag had a visible effect on the output
manuscript, namely it made the main title appear in the output.  Some meta tags do not
have a visible output.  For example,

.. code-block:: text

   :manuscript:
      :title: Three types of tags.

   :section:
     :title: First section
     :label: first-sec

   This section has a label.

   ::

   ::

We have added a section within the manuscript, using the block tag ``:section:``.  This
tag has two meta tags: ``:title:``, which works in much the same way as the manuscript's
title, and a new meta tag ``:label:``, whose value is ``first-sec``.  This tag has no
visible effect on the output, but it has huge importance to the internal structure of
the manuscript.  In particular, the label of a tag is a unique identifier that allows
you to refer to it later on.  For example,

.. code-block:: text

   :manuscript:
      :title: Three types of tags.

   :section:
     :title: First section
     :label: first-sec

   This section has a label.

   ::

   We can now refer back to the :ref:first-sec::.

   ::


Syntax rules
------------

Foo bar
