.. _tutorials:

Getting started
===============

The easiest way to try out RSM and all its features is to use the online live editor.

If you are ready to use RSM for your manuscript, the following instructions will guide
you through the necessary steps to install and use RSM locally on your machine.



.. _installation:

Installation
************

The package name is :code:`rsm-markup` and is available via pypi,

.. code-block:: bash

   $ pip install rsm-markup


Or, if you are using poetry and you already have a :code:`pyproject.toml` file in the
current directory:

.. code-block:: bash

   $ poetry add rsm-markup



.. _checking-your-install:

Checking your install
---------------------

.. tip::
   :class: sidebar

   The command

   .. code-block:: bash

      $ rsm-render manuscript.rsm

   is essentially equivalent to the following code

   .. code-block:: python

      import rsm
      with open("manuscript.rsm") as f:
          src = f.read()
      print(rsm.render(src))

.. grid:: 1 1 1 1

   .. grid-item::

      To test whether the installation was successful you may execute

      .. code-block:: bash

         $ rsm-render --version

      Finally, if you are interested in using RSM from a python script, you may import the library with

      .. code-block:: python

         import rsm



.. _first-manuscript:

Your first manuscript
*********************

Create a new file called :code:`manuscript.rsm` and add the following contents

.. code-block:: plain

   :manuscript:

   Web-first scientific publishing.

   ::

In the command line, :code:`cd` to the directory where the :code:`manuscript.rsm` file
is stored and execute

.. code-block:: bash

   $ rsm-make manuscript.rsm

This will create a new file called :code:`index.html` in the same directory.  Open this
file with your web browser to see the web manuscript created by RSM.

When running the last command, you probably saw the following message (or something similar):

.. code-block:: bash

   RSM.tlate WRN | Manuscript with no title

Here, RSM is telling us that our manuscript is missing a title.  We can rectify that by
editing :code:`manuscript.rsm` as follows

.. code-block:: plain

   :manuscript:
     :title: ReStructured Manuscripts

   Web-first scientific publishing.

   ::

Run again the same command,

.. code-block:: bash

   $ rsm-make manuscript.rsm

And the message should have disappeared.  You can refresh your browser to see now the
title of your manuscript displayed.



Next steps
**********

tutorial 1 (put this one in the TOC!)


.. toctree::
   :maxdepth: 3
   :hidden:
