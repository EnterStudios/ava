from django.test import SimpleTestCase

from ava_core_people.models import Person, Identifier


class PeopleViewsTestCase(SimpleTestCase):

    urls='axiom.urls'
    person_id=''
    identifier_id=''

    def setUp(self):
        testperson = Person(firstname='betty', surname='rebel')
        testperson.save()
        testidentifier = Identifier(identifier='test@example.com',identifiertype='EMAIL',person=testperson)
        testidentifier.save()
        people = Person.objects.all()
        self.person_id=testperson.id
        self.identifier_id=testidentifier.id

    def test_index(self):
        resp = self.client.get('/people/')
        self.assertEqual(resp.status_code, 200)
        #self.assertTrue('latest_poll_list' in resp.context)
        #self.assertEqual([poll.pk for poll in resp.context['latest_poll_list']], [1])

    def test_new(self):
        resp = self.client.get('/people/new/')
        self.assertEqual(resp.status_code, 200)
    
   #def test_search(self):
   #    resp = self.client.get('/people/search/')
   #    self.assertEqual(resp.status_code, 200)
    
    def test_view(self):
        resp = self.client.get('/people/'+str(self.person_id)+'/view/')
        self.assertEqual(resp.status_code, 200)
    
    #def test_update(self):
    #    resp = self.client.get('/people/'+str(self.person_id)+'/update')
    #    self.assertEqual(resp.status_code, 200)
    
    #def test_delete(self):
    #    resp = self.client.get('/people/'+str(self.person_id)+'/delete')
    #    self.assertEqual(resp.status_code, 200)

    #def test_id_update(self):
    #    resp = self.client.get('/people/'+str(self.identifier_id)+'/id/update')
    #    self.assertEqual(resp.status_code, 200)

    #def test_id_delete(self):
    #    resp = self.client.get('/people/'+str(self.identifier_id)+'/id/delete')
    #    self.assertEqual(resp.status_code, 200)




