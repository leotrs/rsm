# File list

## Core Modules

The following are modules that implement the basic functionality of RSM document
processing.

+ reader.py
+ tsparser.py
+ transformer.py
+ linter.py
+ translator.py
+ builder.py
+ writer.py


## Auxiliary modules

The following are modules that are required by the previous ones.

+ manuscript.py
+ nodes.py
+ rsmlogger.py
+ util.py


## App modules

The following are modules that implement applications, i.e., scripts that use the core
modules above to actually process a file.

+ `app.py`
+ `cli.py`


## Other files

+ `static/` contains static files to be served alongside the HTML output.
+ `rsm.so` contains the tree-sitter parser for RSM, generated during build.
+ `conftest.py` contains pytest setup code used when running doctests from docstrings.
+ `tags.py` contains information about each tag in the RSM markup language.  This module
  is provided for documentation purposes only and is not actually involved in processing
  an RSM file.
