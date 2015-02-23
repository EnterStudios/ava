from django.test import TestCase

from ava_core_identity.models import Person


class PersonModelTests(TestCase):

    
    def setUp(self):
        self.person1 = Person.objects.create(firstname="Betty", surname="Paige")
        self.person2 = Person.objects.create(firstname="Clark", surname="Gable")

    
    def test_was_created_at_with_future_item(self):
        #future_item = TargetPerson(created=timezone.now() + datetime.timedelta(days=30))
        self.assertEqual(False, False)


