import subprocess
import unittest
import os

from django.test import TestCase


## This is a django.test.Testcase, not a unittest.TestCase.
## That way even though the *test* does nothing, the DB is
## still bootstrapped.
class SimpleTests(TestCase):
    def test_pass(self):
        """This test will always pass, unless the boostrapping is broken."""
        self.assertTrue(True)


class SimpleCodeTests(unittest.TestCase):

    def test_flake8_compliance(self):
        """Run the flake8 style compliance tool over the Python files.

        This test executes the flake8 script in the ava/bin directory.

        You can use that script to run the code analysis without having
        to wait for the test suite to do it.
        """
        flake8_script = os.path.join(os.path.dirname(__file__), '../bin/flake8-checks.sh')
        results = subprocess.Popen(
            [flake8_script],
            shell=False,
            stdout=subprocess.PIPE,
        ).communicate()[0].decode('ascii')
        if results.strip():
            self.fail("\n" + results)

    def test_imports(self):
        """Test that some module will even import -- for code coverage"""
        MODULES = [
            'ava.core_auth.views',
            'ava.core.views',
        ]
        for module in MODULES:
            __import__(module)
        pass
