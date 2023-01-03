.. _reference:

Reference manual
================

For users
*********

.. toctree::
   :maxdepth: 1

   reference/tags
   reference/steps


For developers
**************

.. currentmodule:: rsm

The :code:`rsm` package contains core modules, implementing each of the steps in the
file processing pipeline:

.. autosummary::
   :toctree: reference
   :caption: Core Modules

   nodes
   reader
   tsparser
   transformer
   translator
   builder
   writer

And user-facing modules, which use the modules above to actually process a file:

.. autosummary::
   :toctree: reference
   :caption: User-facing modules

   app
   cli
   rsmlogger
