# tests/

RSM is tested in the following manner:

1. The files inputs/*.rsm files are processed via rsm-make and the output is placed in
   outputs/*.
2. This particular instance of rsm-make is called programmatically from conftest.py
3. The conftest.py file sets up the entire testing environment - it is executed before
   any tests are ran
4. Note that the rsm-make is called with a test-specific builer ('rsm_test' instead of
   'html')
5. The rsm_test builder is defined in tests/rsm_test_builder.py
5. The conf.py file is a custom rsm config file (which in turn is just a sphinx
   configuration file) that is specific to the needs of testing.  In particular, it sets
   the theme to `rsm_test_theme` which has a dummy template that only outputs the
   contents, not the header/footer/etc.
6. Once the inputs have been converted into outputs, the tests are actually ran
