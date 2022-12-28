.. _special:

Special tags
============

All tags are introduced using the ``:tag-name: <contents> ::`` notation.  However, some
tags deviate from this standard.


Shorthand
*********

Some tags allow for *shorthand* notation.  For example, the following are two different
ways for introducing bold text.

.. rsm::

   :manuscript:
   This text is :span: {:strong:} bold ::, as
   is *this one*.
   ::

.. tip::

   The standard notation using colons and Halmos as delimiters is easy to parse by
   automated tools.  The shorthand notation is easy to read by humans.

Other tags that allow shorthand notation are math and code blocks.  These in turn may be
inline or block.

.. grid:: 1 2 2 2

   .. grid-item-card:: Inline math

     .. rsm::

	:manuscript:

	Either :math:2 + 2 = 4::
	or $2 + 2 = 4$.

	::

   .. grid-item-card:: Block math

     .. rsm::

	:manuscript:

	Either

	:mathblock:
	2 + 2 = 4
	::

	or

	$$
	2 + 2 = 4.
	$$

	::

   .. grid-item-card:: Inline code

     .. rsm::

	:manuscript:

	Either :code:
	var = "value"::
	or `2 + 2 = 4`.

	::

   .. grid-item-card:: Block code

     .. rsm::

	:manuscript:

	Either

	:codeblock:
	var = "value"
	::

	or

	```
	2 + 2 = 4.
	```

	::

.. tip::

   Either standard or shorthand notation allow meta tags.  For example, to assign a
   label to an inline math region, you may use either ``:math:{:label:some-lbl} 2+2=4
   ::`` or ``${:label:some-lbl} 2+2=4 $``.


Stamps
******

Some tags deviate from the standard ``:tag-name: <contents> ::`` syntax in that they do
not allow contents nor need a closing Halmos.  These are called *stamp* tags.  One
example is the ``:appendix:`` tag, whose role is to mark the place in the manuscript
where the Appendix starts.

.. rsm::

   :manuscript:

   # First section
   ::

   # Second section
   ::

   :appendix:

   # First appendix
   ::

   ::

Among other things, the ``:appendix:`` stamp restarts the numbering of the following
sections and changes it from arabic to roman numerals.
