# tests/

RSM is tested in the following manner:

1. The files inputs/*.rsm files are processed via rsm-make and the output is placed in
   outputs/*.
2. This particular instance of rsm-make is called programmatically from conftest.py
3. The conftest.py file sets up the entire testing environment - it is executed before
   any tests are ran
4. Note that the rsm-make is already aware of when it is being called from pytest (see
   rsm.rsm-make.main.RAN_FROM_PYTEST and conftest.py) and it will use the correct
   builder in that case ('rsm_test' instead of 'html')
5. The rsm_test builder is defined in tests/rsm_test_builder.py
5. The conf.py file is a custom rsm config file (which in turn is just a sphinx
   configuration file) that is specific to the needs of testing
