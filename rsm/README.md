# File list

## Core Modules

The following are modules that implement the basic functionality of RSM document
processing.

+ builder.py
+ linter.py
+ manuscript.py
+ nodes.py
+ reader.py
+ rsmlogger.py
+ transformer.py
+ translator.py
+ tsparser.py
+ util.py
+ writer.py


## App modules

The following are modules that implement applications, i.e., scripts that use the core
modules above to actually process a file.

+ app.py
+ cli.py


## Other files

+ static contains static files to be served alongside the HTML output
+ rsm.so contains the tree-sitter parser for RSM, generated during build
+ conftest.py contains pytest setup code used when running doctests from docstrings
