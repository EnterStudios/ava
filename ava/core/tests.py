from django.test import TestCase

class SimpleTests(TestCase):
    def test_pass(self):
        """This test will always pass, unless the boostrapping is broken."""
        self.assertTrue(True)
