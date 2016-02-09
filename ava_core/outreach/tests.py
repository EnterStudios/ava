# Rest Imports
from rest_framework import status
from rest_framework.reverse import reverse
# Local Imports
from ava_core.abstract.test import AvaCoreTest
from ava_core.outreach.test_data import SuspiciousTestData, QuestionTestData, ReportResponseTestData


class SuspiciousTest(AvaCoreTest):
    # step 2: replace outreach and Suspicious
    model_name = 'outreach.Suspicious'

    has_owner = False

    # step 3: populate this section to define what you expect the API permissions will be
    api_permissions = {
        'create': {'unauthenticated': False, 'standard': False, 'admin': True, 'owner': False},
        'retrieve': {'unauthenticated': False, 'standard': True, 'admin': True, 'owner': False},
        'update': {'unauthenticated': False, 'standard': False, 'admin': True, 'owner': False},
        'delete': {'unauthenticated': False, 'standard': False, 'admin': True, 'owner': False},
    }

    # step 4: update with the model name for apiviewset urls (for apiviews and custom api's this won't work
    api_urls = {
        'create': 'suspicious-list',
        'retrieve': 'suspicious-detail',
        'retrieve_all': 'suspicious-list',
        'update': 'suspicious-detail',
        'delete': 'suspicious-detail',
    }

    def setUp(self):
        # step 5: Update with Model Names
        super(SuspiciousTest, self).setUp()
        self.data = SuspiciousTestData()

    def create_object_via_api(self, data):
        # step 6: you will need to write this method.... this template only works with single models
        # with no relationships
        url = reverse(self.api_urls['create'])

        # must be admin to create
        self.login_user(user='admin')

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['admin'])

        self.logout_user()

        # return the id of the model you are testing
        if 'id' in response.data:
            return response.data['id']

    # step 7: replace suspicious globally with your model name in lowercase
    def test_suspicious_create_as_user(self):
        url = reverse(self.api_urls['create'])
        data = self.data.standard

        self.login_user(user='standard')

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['standard'])

    def test_suspicious_create_as_admin(self):
        url = reverse(self.api_urls['create'])
        data = self.data.standard

        self.login_user(user='admin')

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['admin'])

    def test_suspicious_create_as_unauthenticated(self):
        url = reverse(self.api_urls['create'])
        data = self.data.standard

        self.logout_user()

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['unauthenticated'])

    def test_suspicious_retrieve_single_as_user(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user='standard')

        url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['standard'])

    def test_suspicious_retrieve_all_as_user(self):
        self.create_object_via_api(data=self.data.standard)

        self.login_user(user='standard')

        url = reverse(self.api_urls['retrieve_all'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['standard'])

    def test_suspicious_retrieve_single_as_admin(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user='admin')

        url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['admin'])

    def test_suspicious_retrieve_all_as_admin(self):
        self.create_object_via_api(data=self.data.standard)

        self.login_user(user='admin')

        url = reverse(self.api_urls['retrieve_all'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['admin'])

    def test_suspicious_retrieve_single_as_unauthenticated(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['unauthenticated'])

    def test_suspicious_retrieve_all_as_unauthenticated(self):
        self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['retrieve_all'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['unauthenticated'])

    def test_suspicious_update_exists_as_user(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="standard")

        url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_suspicious_update_does_not_exist_as_user(self):
        self.login_user(user="standard")

        url = reverse(self.api_urls['update'], kwargs={'pk': 1})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_suspicious_update_exists_as_admin(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="admin")

        url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['admin'])

    def test_suspicious_update_does_not_exist_as_admin(self):
        self.login_user(user="admin")

        url = reverse(self.api_urls['update'], kwargs={'pk': 1})
        response = self.client.put(url, self.data.unique, format='json')

        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_suspicious_update_exists_as_unauthenticated(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_suspicious_update_does_not_exist_as_unauthenticated(self):
        self.logout_user()

        url = reverse(self.api_urls['update'], kwargs={'pk': 1})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_suspicious_delete_does_not_exist_as_user(self):
        self.login_user(user="standard")

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['standard'])

    def test_suspicious_delete_exists_as_user(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="standard")

        url = reverse(self.api_urls['delete'], kwargs={'pk': object_id})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['standard'])

    def test_suspicious_delete_exists_as_admin(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="admin")

        url = reverse(self.api_urls['delete'], kwargs={'pk': object_id})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['admin'])

    def test_suspicious_delete_does_not_exist_as_admin(self):
        self.login_user(user="admin")

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_suspicious_delete_exists_as_unauthenticated(self):
        self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['unauthenticated'])

    def test_suspicious_delete_does_not_exist_as_unauthenticated(self):
        self.logout_user()

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['unauthenticated'])


class ReportResponseTest(AvaCoreTest):
    # step 2: replace outreach and ReportResponse
    model_name = 'outreach.ReportResponse'

    has_owner = False

    # step 3: populate this section to define what you expect the API permissions will be
    api_permissions = {
        'create': {'unauthenticated': False, 'standard': False, 'admin': True, 'owner': False},
        'retrieve': {'unauthenticated': False, 'standard': True, 'admin': True, 'owner': False},
        'update': {'unauthenticated': False, 'standard': False, 'admin': True, 'owner': False},
        'delete': {'unauthenticated': False, 'standard': False, 'admin': True, 'owner': False},
    }

    # step 4: update with the model name for apiviewset urls (for apiviews and custom api's this won't work
    api_urls = {
        'create': 'reportresponse-list',
        'retrieve': 'reportresponse-detail',
        'retrieve_all': 'reportresponse-list',
        'update': 'reportresponse-detail',
        'delete': 'reportresponse-detail',
    }

    def setUp(self):
        # step 5: Update with Model Names
        super(ReportResponseTest, self).setUp()
        self.data = ReportResponseTestData()

    def create_object_via_api(self, data):
        # step 6: you will need to write this method.... this template only works with single models
        # with no relationships
        url = reverse(self.api_urls['create'])

        # must be admin to create
        self.login_user(user='admin')

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['admin'])

        self.logout_user()

        # return the id of the model you are testing
        if 'id' in response.data:
            return response.data['id']

    # step 7: replace reportresponse globally with your model name in lowercase
    def test_reportresponse_create_as_user(self):
        url = reverse(self.api_urls['create'])
        data = self.data.standard

        self.login_user(user='standard')

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['standard'])

    def test_reportresponse_create_as_admin(self):
        url = reverse(self.api_urls['create'])
        data = self.data.standard

        self.login_user(user='admin')

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['admin'])

    def test_reportresponse_create_as_unauthenticated(self):
        url = reverse(self.api_urls['create'])
        data = self.data.standard

        self.logout_user()

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['unauthenticated'])

    def test_reportresponse_retrieve_single_as_user(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user='standard')

        url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['standard'])

    def test_reportresponse_retrieve_all_as_user(self):
        self.create_object_via_api(data=self.data.standard)

        self.login_user(user='standard')

        url = reverse(self.api_urls['retrieve_all'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['standard'])

    def test_reportresponse_retrieve_single_as_admin(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user='admin')

        url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['admin'])

    def test_reportresponse_retrieve_all_as_admin(self):
        self.create_object_via_api(data=self.data.standard)

        self.login_user(user='admin')

        url = reverse(self.api_urls['retrieve_all'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['admin'])

    def test_reportresponse_retrieve_single_as_unauthenticated(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['unauthenticated'])

    def test_reportresponse_retrieve_all_as_unauthenticated(self):
        self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['retrieve_all'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['unauthenticated'])

    def test_reportresponse_update_exists_as_user(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="standard")

        url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_reportresponse_update_does_not_exist_as_user(self):
        self.login_user(user="standard")

        url = reverse(self.api_urls['update'], kwargs={'pk': 1})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_reportresponse_update_exists_as_admin(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="admin")

        url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['admin'])

    def test_reportresponse_update_does_not_exist_as_admin(self):
        self.login_user(user="admin")

        url = reverse(self.api_urls['update'], kwargs={'pk': 1})
        response = self.client.put(url, self.data.unique, format='json')

        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_reportresponse_update_exists_as_unauthenticated(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_reportresponse_update_does_not_exist_as_unauthenticated(self):
        self.logout_user()

        url = reverse(self.api_urls['update'], kwargs={'pk': 1})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_reportresponse_delete_does_not_exist_as_user(self):
        self.login_user(user="standard")

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['standard'])

    def test_reportresponse_delete_exists_as_user(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="standard")

        url = reverse(self.api_urls['delete'], kwargs={'pk': object_id})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['standard'])

    def test_reportresponse_delete_exists_as_admin(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="admin")

        url = reverse(self.api_urls['delete'], kwargs={'pk': object_id})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['admin'])

    def test_reportresponse_delete_does_not_exist_as_admin(self):
        self.login_user(user="admin")

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_reportresponse_delete_exists_as_unauthenticated(self):
        self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['unauthenticated'])

    def test_reportresponse_delete_does_not_exist_as_unauthenticated(self):
        self.logout_user()

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['unauthenticated'])


class QuestionTest(AvaCoreTest):
    # step 2: replace outreach and Question
    model_name = 'outreach.Question'

    has_owner = False

    # step 3: populate this section to define what you expect the API permissions will be
    api_permissions = {
        'create': {'unauthenticated': False, 'standard': False, 'admin': True, 'owner': False},
        'retrieve': {'unauthenticated': False, 'standard': True, 'admin': True, 'owner': False},
        'update': {'unauthenticated': False, 'standard': False, 'admin': True, 'owner': False},
        'delete': {'unauthenticated': False, 'standard': False, 'admin': True, 'owner': False},
    }

    # step 4: update with the model name for apiviewset urls (for apiviews and custom api's this won't work
    api_urls = {
        'create': 'question-list',
        'retrieve': 'question-detail',
        'retrieve_all': 'question-list',
        'update': 'question-detail',
        'delete': 'question-detail',
    }

    def setUp(self):
        # step 5: Update with Model Names
        super(QuestionTest, self).setUp()
        self.data = QuestionTestData()

    def create_object_via_api(self, data):
        # step 6: you will need to write this method.... this template only works with single models
        # with no relationships
        url = reverse(self.api_urls['create'])

        # must be admin to create
        self.login_user(user='admin')

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['admin'])

        self.logout_user()

        # return the id of the model you are testing
        if 'id' in response.data:
            return response.data['id']

    # step 7: replace question globally with your model name in lowercase
    def test_question_create_as_user(self):
        url = reverse(self.api_urls['create'])
        data = self.data.standard

        self.login_user(user='standard')

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['standard'])

    def test_question_create_as_admin(self):
        url = reverse(self.api_urls['create'])
        data = self.data.standard

        self.login_user(user='admin')

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['admin'])

    def test_question_create_as_unauthenticated(self):
        url = reverse(self.api_urls['create'])
        data = self.data.standard

        self.logout_user()

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['unauthenticated'])

    def test_question_retrieve_single_as_user(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user='standard')

        url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['standard'])

    def test_question_retrieve_all_as_user(self):
        self.create_object_via_api(data=self.data.standard)

        self.login_user(user='standard')

        url = reverse(self.api_urls['retrieve_all'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['standard'])

    def test_question_retrieve_single_as_admin(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user='admin')

        url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['admin'])

    def test_question_retrieve_all_as_admin(self):
        self.create_object_via_api(data=self.data.standard)

        self.login_user(user='admin')

        url = reverse(self.api_urls['retrieve_all'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['admin'])

    def test_question_retrieve_single_as_unauthenticated(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['unauthenticated'])

    def test_question_retrieve_all_as_unauthenticated(self):
        self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['retrieve_all'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['unauthenticated'])

    def test_question_update_exists_as_user(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="standard")

        url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_question_update_does_not_exist_as_user(self):
        self.login_user(user="standard")

        url = reverse(self.api_urls['update'], kwargs={'pk': 1})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_question_update_exists_as_admin(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="admin")

        url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['admin'])

    def test_question_update_does_not_exist_as_admin(self):
        self.login_user(user="admin")

        url = reverse(self.api_urls['update'], kwargs={'pk': 1})
        response = self.client.put(url, self.data.unique, format='json')

        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_question_update_exists_as_unauthenticated(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_question_update_does_not_exist_as_unauthenticated(self):
        self.logout_user()

        url = reverse(self.api_urls['update'], kwargs={'pk': 1})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_question_delete_does_not_exist_as_user(self):
        self.login_user(user="standard")

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['standard'])

    def test_question_delete_exists_as_user(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="standard")

        url = reverse(self.api_urls['delete'], kwargs={'pk': object_id})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['standard'])

    def test_question_delete_exists_as_admin(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="admin")

        url = reverse(self.api_urls['delete'], kwargs={'pk': object_id})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['admin'])

    def test_question_delete_does_not_exist_as_admin(self):
        self.login_user(user="admin")

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_question_delete_exists_as_unauthenticated(self):
        self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['unauthenticated'])

    def test_question_delete_does_not_exist_as_unauthenticated(self):
        self.logout_user()

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['unauthenticated'])
