# doctest_setup.py
#
# Setup the doctest module to be used by sphinx and pytest.

# Add a new IGNORE_RESULT flag to skip checking a single line within a doctest.
# Taken from https://stackoverflow.com/a/69780437.
import doctest

IGNORE_RESULT = doctest.register_optionflag("IGNORE_RESULT")
OutputChecker = doctest.OutputChecker


class CustomOutputChecker(OutputChecker):
    def check_output(self, want, got, optionflags):
        if IGNORE_RESULT & optionflags:
            return True
        return OutputChecker.check_output(self, want, got, optionflags)


doctest.OutputChecker = CustomOutputChecker
