from django.test import TestCase

from ava_core.models import *

class TargetMethodTests(TestCase):

    def test_was_created_at_with_future_item(self):
        #future_item = TargetPerson(created_at=timezone.now() + datetime.timedelta(days=30))
        self.assertEqual(False, False)
