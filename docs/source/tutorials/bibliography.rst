.. _bibliography:

Bibliography
============

RSM supports bibliography using BibTex notation.  Use the ``:bibliography:`` tag to note
where in the manuscript the list of references will appear.

.. rsm::

   :manuscript:

   # Some Section

   Some content here.

   ::

   :bibliography: ::

   ::

This creates an empty reference list because there aren't any citations in our
manuscript yet.

.. tip::

   Even though the ``:bibliography:`` tag does not accept content, it always needs a
   closing Halmos ``::``.  It may accept meta tags such as ``:label:``.

Use the ``:bibtex:`` tag to supply the necessary references in BibTex notation.

.. code-block:: text

   :bibtex:

   @book{knuth,
         title={Art of computer programming, volume 2, Seminumerical algorithms},
         author={Knuth, Donald E},
         year={2014},
         publisher={Addison-Wesley Professional},
         doi={10.1137/1012065},
        }

   ::

Within the manuscript contents, use ``:cite:`` to refer to a bibliography item.  Here is
a complete example of the bibliography system.

.. rsm::

   :manuscript:

   # Some section

   Some content here :cite:knuth::.

   ::

   :bibliography: ::

   ::

   :bibtex:

   @book{knuth,
         title={Art of Computer Programming},
         author={Knuth, Donald E},
         year={2014},
         publisher={Addison-Wesley},
         doi={10.1137/1012065},
        }

   ::

Much like references, citations always display with a tooltip.  Similarly, each
bibliography item in the generated reference list contains backlinks, also with
tooltips, to those places in the manuscript where the item has been cited.  Finally, RSM
will automatically add a link to the DOI of the referenced work, if available.

.. important::

   The ``:bibtex:`` tag is located outside, and immediately after, the closing Halmos of
   the ``:manuscript:`` tag.
