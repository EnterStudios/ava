# Rest Imports
from rest_framework import status
from rest_framework.reverse import reverse
# Local Imports
from ava_core.abstract.test import AvaCoreTest
from ava_core.organize.test_data import GroupIdentifierAttributeTestData, PersonIdentifierAttributeTestData, \
    GroupReportTestData, PersonIdentifierReportTestData, PersonTestData, PersonAttributeTestData, GroupTestData, \
    GroupIdentifierTestData, PersonIdentifierTestData


class GroupIdentifierAttributeTest(AvaCoreTest):
    # step 2: replace organize and GroupIdentifierAttribute
    model_name = 'organize.GroupIdentifierAttribute'

    has_owner = False

    # step 3: populate this section to define what you expect the API permissions will be
    api_permissions = {
        'create': {'unauthenticated': False, 'standard': False, 'admin': False, 'owner': False},
        'retrieve': {'unauthenticated': False, 'standard': False, 'admin': False, 'owner': False},
        'update': {'unauthenticated': False, 'standard': False, 'admin': False, 'owner': False},
        'delete': {'unauthenticated': False, 'standard': False, 'admin': False, 'owner': False},
    }

    # step 4: update with the model name for apiviewset urls (for apiviews and custom api's this won't work
    api_urls = {
        'create': 'groupidentifierattribute-list',
        'retrieve': 'groupidentifierattribute-detail',
        'retrieve_all': 'groupidentifierattribute-list',
        'update': 'groupidentifierattribute-detail',
        'delete': 'groupidentifierattribute-detail',
    }

    def setUp(self):
        # step 5: Update with Model Names
        super(GroupIdentifierAttributeTest, self).setUp()
        self.data = GroupIdentifierAttributeTestData()

    def create_object_via_api(self, data, user='admin'):
        # step 6: you will need to write this method.... this template only works with single models
        # with no relationships
        url = reverse(self.api_urls['create'])

        # Check that a user has been passed.
        # True - Log in as user.
        # False - Ensure unauthenticated access.
        if user:
            self.login_user(user=user)
        else:
            self.logout_user()
            user = 'unauthenticated'

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create'][user])

        self.logout_user()

        # return the id of the model you are testing
        if 'id' in response.data:
            return response.data['id']

    # step 7: replace groupidentifierattribute globally with your model name in lowercase
    def test_groupidentifierattribute_create_as_user(self):
        url = reverse(self.api_urls['create'])
        data = self.data.standard

        self.login_user(user='standard')

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['standard'])

    def test_groupidentifierattribute_create_as_admin(self):
        url = reverse(self.api_urls['create'])
        data = self.data.standard

        self.login_user(user='admin')

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['admin'])

    def test_groupidentifierattribute_create_as_unauthenticated(self):
        url = reverse(self.api_urls['create'])
        data = self.data.standard

        self.logout_user()

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['unauthenticated'])

    def test_groupidentifierattribute_retrieve_single_as_user(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user='standard')

        url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['standard'])

    def test_groupidentifierattribute_retrieve_all_as_user(self):
        self.create_object_via_api(data=self.data.standard)

        self.login_user(user='standard')

        url = reverse(self.api_urls['retrieve_all'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['standard'])

    def test_groupidentifierattribute_retrieve_single_as_admin(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user='admin')

        url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['admin'])

    def test_groupidentifierattribute_retrieve_all_as_admin(self):
        self.create_object_via_api(data=self.data.standard)

        self.login_user(user='admin')

        url = reverse(self.api_urls['retrieve_all'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['admin'])

    def test_groupidentifierattribute_retrieve_single_as_unauthenticated(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['unauthenticated'])

    def test_groupidentifierattribute_retrieve_all_as_unauthenticated(self):
        self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['retrieve_all'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['unauthenticated'])

    def test_groupidentifierattribute_update_exists_as_user(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="standard")

        url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_groupidentifierattribute_update_does_not_exist_as_user(self):
        self.login_user(user="standard")

        url = reverse(self.api_urls['update'], kwargs={'pk': 1})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_groupidentifierattribute_update_exists_as_admin(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="admin")

        url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['admin'])

    def test_groupidentifierattribute_update_does_not_exist_as_admin(self):
        self.login_user(user="admin")

        url = reverse(self.api_urls['update'], kwargs={'pk': 1})
        response = self.client.put(url, self.data.unique, format='json')

        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_groupidentifierattribute_update_exists_as_unauthenticated(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_groupidentifierattribute_update_does_not_exist_as_unauthenticated(self):
        self.logout_user()

        url = reverse(self.api_urls['update'], kwargs={'pk': 1})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_groupidentifierattribute_delete_does_not_exist_as_user(self):
        self.login_user(user="standard")

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['standard'])

    def test_groupidentifierattribute_delete_exists_as_user(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="standard")

        url = reverse(self.api_urls['delete'], kwargs={'pk': object_id})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['standard'])

    def test_groupidentifierattribute_delete_exists_as_admin(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="admin")

        url = reverse(self.api_urls['delete'], kwargs={'pk': object_id})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['admin'])

    def test_groupidentifierattribute_delete_does_not_exist_as_admin(self):
        self.login_user(user="admin")

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_groupidentifierattribute_delete_exists_as_unauthenticated(self):
        self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['unauthenticated'])

    def test_groupidentifierattribute_delete_does_not_exist_as_unauthenticated(self):
        self.logout_user()

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['unauthenticated'])


class PersonIdentifierAttributeTest(AvaCoreTest):
    # step 2: replace organize and PersonIdentifierAttribute
    model_name = 'organize.PersonIdentifierAttribute'

    has_owner = False

    # step 3: populate this section to define what you expect the API permissions will be
    api_permissions = {
        'create': {'unauthenticated': False, 'standard': False, 'admin': False, 'owner': False},
        'retrieve': {'unauthenticated': False, 'standard': False, 'admin': False, 'owner': False},
        'update': {'unauthenticated': False, 'standard': False, 'admin': False, 'owner': False},
        'delete': {'unauthenticated': False, 'standard': False, 'admin': False, 'owner': False},
    }

    # step 4: update with the model name for apiviewset urls (for apiviews and custom api's this won't work
    api_urls = {
        'create': 'personidentifierattribute-list',
        'retrieve': 'personidentifierattribute-detail',
        'retrieve_all': 'personidentifierattribute-list',
        'update': 'personidentifierattribute-detail',
        'delete': 'personidentifierattribute-detail',
    }

    def setUp(self):
        # step 5: Update with Model Names
        super(PersonIdentifierAttributeTest, self).setUp()
        self.data = PersonIdentifierAttributeTestData()

    def create_object_via_api(self, data, user='admin'):
        # step 6: you will need to write this method.... this template only works with single models
        # with no relationships
        url = reverse(self.api_urls['create'])

        # Check that a user has been passed.
        # True - Log in as user.
        # False - Ensure unauthenticated access.
        if user:
            self.login_user(user=user)
        else:
            self.logout_user()
            user = 'unauthenticated'

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create'][user])

        self.logout_user()

        # return the id of the model you are testing
        if 'id' in response.data:
            return response.data['id']

    # step 7: replace personidentifierattribute globally with your model name in lowercase
    def test_personidentifierattribute_create_as_user(self):
        url = reverse(self.api_urls['create'])
        data = self.data.standard

        self.login_user(user='standard')

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['standard'])

    def test_personidentifierattribute_create_as_admin(self):
        url = reverse(self.api_urls['create'])
        data = self.data.standard

        self.login_user(user='admin')

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['admin'])

    def test_personidentifierattribute_create_as_unauthenticated(self):
        url = reverse(self.api_urls['create'])
        data = self.data.standard

        self.logout_user()

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['unauthenticated'])

    def test_personidentifierattribute_retrieve_single_as_user(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user='standard')

        url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['standard'])

    def test_personidentifierattribute_retrieve_all_as_user(self):
        self.create_object_via_api(data=self.data.standard)

        self.login_user(user='standard')

        url = reverse(self.api_urls['retrieve_all'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['standard'])

    def test_personidentifierattribute_retrieve_single_as_admin(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user='admin')

        url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['admin'])

    def test_personidentifierattribute_retrieve_all_as_admin(self):
        self.create_object_via_api(data=self.data.standard)

        self.login_user(user='admin')

        url = reverse(self.api_urls['retrieve_all'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['admin'])

    def test_personidentifierattribute_retrieve_single_as_unauthenticated(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['unauthenticated'])

    def test_personidentifierattribute_retrieve_all_as_unauthenticated(self):
        self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['retrieve_all'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['unauthenticated'])

    def test_personidentifierattribute_update_exists_as_user(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="standard")

        url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_personidentifierattribute_update_does_not_exist_as_user(self):
        self.login_user(user="standard")

        url = reverse(self.api_urls['update'], kwargs={'pk': 1})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_personidentifierattribute_update_exists_as_admin(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="admin")

        url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['admin'])

    def test_personidentifierattribute_update_does_not_exist_as_admin(self):
        self.login_user(user="admin")

        url = reverse(self.api_urls['update'], kwargs={'pk': 1})
        response = self.client.put(url, self.data.unique, format='json')

        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_personidentifierattribute_update_exists_as_unauthenticated(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_personidentifierattribute_update_does_not_exist_as_unauthenticated(self):
        self.logout_user()

        url = reverse(self.api_urls['update'], kwargs={'pk': 1})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_personidentifierattribute_delete_does_not_exist_as_user(self):
        self.login_user(user="standard")

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['standard'])

    def test_personidentifierattribute_delete_exists_as_user(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="standard")

        url = reverse(self.api_urls['delete'], kwargs={'pk': object_id})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['standard'])

    def test_personidentifierattribute_delete_exists_as_admin(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="admin")

        url = reverse(self.api_urls['delete'], kwargs={'pk': object_id})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['admin'])

    def test_personidentifierattribute_delete_does_not_exist_as_admin(self):
        self.login_user(user="admin")

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_personidentifierattribute_delete_exists_as_unauthenticated(self):
        self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['unauthenticated'])

    def test_personidentifierattribute_delete_does_not_exist_as_unauthenticated(self):
        self.logout_user()

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['unauthenticated'])


class GroupReportTest(AvaCoreTest):
    # step 2: replace organize and GroupReport
    model_name = 'organize.GroupReport'

    has_owner = False

    # step 3: populate this section to define what you expect the API permissions will be
    api_permissions = {
        'create': {'unauthenticated': False, 'standard': True, 'admin': False, 'owner': False},
        'retrieve': {'unauthenticated': False, 'standard': True, 'admin': True, 'owner': True},
        'update': {'unauthenticated': False, 'standard': False, 'admin': False, 'owner': False},
        'delete': {'unauthenticated': False, 'standard': False, 'admin': True, 'owner': False},
    }

    # step 4: update with the model name for apiviewset urls (for apiviews and custom api's this won't work
    api_urls = {
        'create': 'groupreport-list',
        'retrieve': 'groupreport-detail',
        'retrieve_all': 'groupreport-list',
        'update': 'groupreport-detail',
        'delete': 'groupreport-detail',
    }

    def setUp(self):
        # step 5: Update with Model Names
        super(GroupReportTest, self).setUp()
        self.data = GroupReportTestData()

    def create_object_via_api(self, data, user='admin'):
        # step 6: you will need to write this method.... this template only works with single models
        # with no relationships
        url = reverse(self.api_urls['create'])

        # Check that a user has been passed.
        # True - Log in as user.
        # False - Ensure unauthenticated access.
        if user:
            self.login_user(user=user)
        else:
            self.logout_user()
            user = 'unauthenticated'

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create'][user])

        self.logout_user()

        # return the id of the model you are testing
        if 'id' in response.data:
            return response.data['id']

    # step 7: replace groupreport globally with your model name in lowercase
    def test_groupreport_create_as_user(self):
        url = reverse(self.api_urls['create'])
        data = self.data.standard

        self.login_user(user='standard')

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['standard'])

    def test_groupreport_create_as_admin(self):
        url = reverse(self.api_urls['create'])
        data = self.data.standard

        self.login_user(user='admin')

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['admin'])

    def test_groupreport_create_as_unauthenticated(self):
        url = reverse(self.api_urls['create'])
        data = self.data.standard

        self.logout_user()

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['unauthenticated'])

    def test_groupreport_retrieve_single_as_user(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user='standard')

        url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['standard'])

    def test_groupreport_retrieve_all_as_user(self):
        self.create_object_via_api(data=self.data.standard)

        self.login_user(user='standard')

        url = reverse(self.api_urls['retrieve_all'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['standard'])

    def test_groupreport_retrieve_single_as_admin(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user='admin')

        url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['admin'])

    def test_groupreport_retrieve_all_as_admin(self):
        self.create_object_via_api(data=self.data.standard)

        self.login_user(user='admin')

        url = reverse(self.api_urls['retrieve_all'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['admin'])

    def test_groupreport_retrieve_single_as_unauthenticated(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['unauthenticated'])

    def test_groupreport_retrieve_all_as_unauthenticated(self):
        self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['retrieve_all'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['unauthenticated'])

    def test_groupreport_update_exists_as_user(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="standard")

        url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_groupreport_update_does_not_exist_as_user(self):
        self.login_user(user="standard")

        url = reverse(self.api_urls['update'], kwargs={'pk': 1})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_groupreport_update_exists_as_admin(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="admin")

        url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['admin'])

    def test_groupreport_update_does_not_exist_as_admin(self):
        self.login_user(user="admin")

        url = reverse(self.api_urls['update'], kwargs={'pk': 1})
        response = self.client.put(url, self.data.unique, format='json')

        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_groupreport_update_exists_as_unauthenticated(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_groupreport_update_does_not_exist_as_unauthenticated(self):
        self.logout_user()

        url = reverse(self.api_urls['update'], kwargs={'pk': 1})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_groupreport_delete_does_not_exist_as_user(self):
        self.login_user(user="standard")

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['standard'])

    def test_groupreport_delete_exists_as_user(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="standard")

        url = reverse(self.api_urls['delete'], kwargs={'pk': object_id})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['standard'])

    def test_groupreport_delete_exists_as_admin(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="admin")

        url = reverse(self.api_urls['delete'], kwargs={'pk': object_id})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['admin'])

    def test_groupreport_delete_does_not_exist_as_admin(self):
        self.login_user(user="admin")

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_groupreport_delete_exists_as_unauthenticated(self):
        self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['unauthenticated'])

    def test_groupreport_delete_does_not_exist_as_unauthenticated(self):
        self.logout_user()

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['unauthenticated'])


class PersonIdentifierReportTest(AvaCoreTest):
    # step 2: replace organize and PersonIdentifierReport
    model_name = 'organize.PersonIdentifierReport'

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
        'create': 'personidentifierreport-list',
        'retrieve': 'personidentifierreport-detail',
        'retrieve_all': 'personidentifierreport-list',
        'update': 'personidentifierreport-detail',
        'delete': 'personidentifierreport-detail',
    }

    def setUp(self):
        # step 5: Update with Model Names
        super(PersonIdentifierReportTest, self).setUp()
        self.data = PersonIdentifierReportTestData()

    def create_object_via_api(self, data, user='admin'):
        # step 6: you will need to write this method.... this template only works with single models
        # with no relationships
        url = reverse(self.api_urls['create'])

        # Check that a user has been passed.
        # True - Log in as user.
        # False - Ensure unauthenticated access.
        if user:
            self.login_user(user=user)
        else:
            self.logout_user()
            user = 'unauthenticated'

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create'][user])

        self.logout_user()

        # return the id of the model you are testing
        if 'id' in response.data:
            return response.data['id']

    # step 7: replace personidentifierreport globally with your model name in lowercase
    def test_personidentifierreport_create_as_user(self):
        url = reverse(self.api_urls['create'])
        data = self.data.standard

        self.login_user(user='standard')

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['standard'])

    def test_personidentifierreport_create_as_admin(self):
        url = reverse(self.api_urls['create'])
        data = self.data.standard

        self.login_user(user='admin')

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['admin'])

    def test_personidentifierreport_create_as_unauthenticated(self):
        url = reverse(self.api_urls['create'])
        data = self.data.standard

        self.logout_user()

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['unauthenticated'])

    def test_personidentifierreport_retrieve_single_as_user(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user='standard')

        url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['standard'])

    def test_personidentifierreport_retrieve_all_as_user(self):
        self.create_object_via_api(data=self.data.standard)

        self.login_user(user='standard')

        url = reverse(self.api_urls['retrieve_all'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['standard'])

    def test_personidentifierreport_retrieve_single_as_admin(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user='admin')

        url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['admin'])

    def test_personidentifierreport_retrieve_all_as_admin(self):
        self.create_object_via_api(data=self.data.standard)

        self.login_user(user='admin')

        url = reverse(self.api_urls['retrieve_all'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['admin'])

    def test_personidentifierreport_retrieve_single_as_unauthenticated(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['unauthenticated'])

    def test_personidentifierreport_retrieve_all_as_unauthenticated(self):
        self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['retrieve_all'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['unauthenticated'])

    def test_personidentifierreport_update_exists_as_user(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="standard")

        url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_personidentifierreport_update_does_not_exist_as_user(self):
        self.login_user(user="standard")

        url = reverse(self.api_urls['update'], kwargs={'pk': 1})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_personidentifierreport_update_exists_as_admin(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="admin")

        url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['admin'])

    def test_personidentifierreport_update_does_not_exist_as_admin(self):
        self.login_user(user="admin")

        url = reverse(self.api_urls['update'], kwargs={'pk': 1})
        response = self.client.put(url, self.data.unique, format='json')

        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_personidentifierreport_update_exists_as_unauthenticated(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_personidentifierreport_update_does_not_exist_as_unauthenticated(self):
        self.logout_user()

        url = reverse(self.api_urls['update'], kwargs={'pk': 1})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_personidentifierreport_delete_does_not_exist_as_user(self):
        self.login_user(user="standard")

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['standard'])

    def test_personidentifierreport_delete_exists_as_user(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="standard")

        url = reverse(self.api_urls['delete'], kwargs={'pk': object_id})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['standard'])

    def test_personidentifierreport_delete_exists_as_admin(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="admin")

        url = reverse(self.api_urls['delete'], kwargs={'pk': object_id})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['admin'])

    def test_personidentifierreport_delete_does_not_exist_as_admin(self):
        self.login_user(user="admin")

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_personidentifierreport_delete_exists_as_unauthenticated(self):
        self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['unauthenticated'])

    def test_personidentifierreport_delete_does_not_exist_as_unauthenticated(self):
        self.logout_user()

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['unauthenticated'])


class PersonAttributeTest(AvaCoreTest):
    # step 2: replace organize and PersonAttribute
    model_name = 'organize.PersonAttribute'

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
        'create': 'personattribute-list',
        'retrieve': 'personattribute-detail',
        'retrieve_all': 'personattribute-list',
        'update': 'personattribute-detail',
        'delete': 'personattribute-detail',
    }

    def setUp(self):
        # step 5: Update with Model Names
        super(PersonAttributeTest, self).setUp()
        self.data = PersonAttributeTestData()

    def create_object_via_api(self, data, user='admin'):
        # step 6: you will need to write this method.... this template only works with single models
        # with no relationships
        url = reverse(self.api_urls['create'])

        # Check that a user has been passed.
        # True - Log in as user.
        # False - Ensure unauthenticated access.
        if user:
            self.login_user(user=user)
        else:
            self.logout_user()
            user = 'unauthenticated'

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create'][user])

        self.logout_user()

        # return the id of the model you are testing
        if 'id' in response.data:
            return response.data['id']

    # step 7: replace personattribute globally with your model name in lowercase
    def test_personattribute_create_as_user(self):
        url = reverse(self.api_urls['create'])
        data = self.data.standard

        self.login_user(user='standard')

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['standard'])

    def test_personattribute_create_as_admin(self):
        url = reverse(self.api_urls['create'])
        data = self.data.standard

        self.login_user(user='admin')

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['admin'])

    def test_personattribute_create_as_unauthenticated(self):
        url = reverse(self.api_urls['create'])
        data = self.data.standard

        self.logout_user()

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['unauthenticated'])

    def test_personattribute_retrieve_single_as_user(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user='standard')

        url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['standard'])

    def test_personattribute_retrieve_all_as_user(self):
        self.create_object_via_api(data=self.data.standard)

        self.login_user(user='standard')

        url = reverse(self.api_urls['retrieve_all'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['standard'])

    def test_personattribute_retrieve_single_as_admin(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user='admin')

        url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['admin'])

    def test_personattribute_retrieve_all_as_admin(self):
        self.create_object_via_api(data=self.data.standard)

        self.login_user(user='admin')

        url = reverse(self.api_urls['retrieve_all'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['admin'])

    def test_personattribute_retrieve_single_as_unauthenticated(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['unauthenticated'])

    def test_personattribute_retrieve_all_as_unauthenticated(self):
        self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['retrieve_all'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['unauthenticated'])

    def test_personattribute_update_exists_as_user(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="standard")

        url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_personattribute_update_does_not_exist_as_user(self):
        self.login_user(user="standard")

        url = reverse(self.api_urls['update'], kwargs={'pk': 1})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_personattribute_update_exists_as_admin(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="admin")

        url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['admin'])

    def test_personattribute_update_does_not_exist_as_admin(self):
        self.login_user(user="admin")

        url = reverse(self.api_urls['update'], kwargs={'pk': 1})
        response = self.client.put(url, self.data.unique, format='json')

        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_personattribute_update_exists_as_unauthenticated(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_personattribute_update_does_not_exist_as_unauthenticated(self):
        self.logout_user()

        url = reverse(self.api_urls['update'], kwargs={'pk': 1})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_personattribute_delete_does_not_exist_as_user(self):
        self.login_user(user="standard")

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['standard'])

    def test_personattribute_delete_exists_as_user(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="standard")

        url = reverse(self.api_urls['delete'], kwargs={'pk': object_id})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['standard'])

    def test_personattribute_delete_exists_as_admin(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="admin")

        url = reverse(self.api_urls['delete'], kwargs={'pk': object_id})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['admin'])

    def test_personattribute_delete_does_not_exist_as_admin(self):
        self.login_user(user="admin")

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_personattribute_delete_exists_as_unauthenticated(self):
        self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['unauthenticated'])

    def test_personattribute_delete_does_not_exist_as_unauthenticated(self):
        self.logout_user()

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['unauthenticated'])


class GroupTest(AvaCoreTest):
    # step 2: replace organize and Group
    model_name = 'organize.Group'

    has_owner = False

    # step 3: populate this section to define what you expect the API permissions will be
    api_permissions = {
        'create': {'unauthenticated': False, 'standard': False, 'admin': False, 'owner': False},
        'retrieve': {'unauthenticated': False, 'standard': True, 'admin': True, 'owner': True},
        'update': {'unauthenticated': False, 'standard': False, 'admin': True, 'owner': False},
        'delete': {'unauthenticated': False, 'standard': False, 'admin': False, 'owner': False},
    }

    # step 4: update with the model name for apiviewset urls (for apiviews and custom api's this won't work
    api_urls = {
        'create': 'group-list',
        'retrieve': 'group-detail',
        'retrieve_all': 'group-list',
        'update': 'group-detail',
        'delete': 'group-detail',
    }

    def setUp(self):
        # step 5: Update with Model Names
        super(GroupTest, self).setUp()
        self.data = GroupTestData()

    def create_object_via_api(self, data, user='admin'):
        # step 6: you will need to write this method.... this template only works with single models
        # with no relationships
        url = reverse(self.api_urls['create'])

        # Check that a user has been passed.
        # True - Log in as user.
        # False - Ensure unauthenticated access.
        if user:
            self.login_user(user=user)
        else:
            self.logout_user()
            user = 'unauthenticated'

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create'][user])

        self.logout_user()

        # return the id of the model you are testing
        if 'id' in response.data:
            return response.data['id']

    # step 7: replace group globally with your model name in lowercase
    def test_group_create_as_user(self):
        url = reverse(self.api_urls['create'])
        data = self.data.standard

        self.login_user(user='standard')

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['standard'])

    def test_group_create_as_admin(self):
        url = reverse(self.api_urls['create'])
        data = self.data.standard

        self.login_user(user='admin')

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['admin'])

    def test_group_create_as_unauthenticated(self):
        url = reverse(self.api_urls['create'])
        data = self.data.standard

        self.logout_user()

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['unauthenticated'])

    def test_group_retrieve_single_as_user(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user='standard')

        url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['standard'])

    def test_group_retrieve_all_as_user(self):
        self.create_object_via_api(data=self.data.standard)

        self.login_user(user='standard')

        url = reverse(self.api_urls['retrieve_all'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['standard'])

    def test_group_retrieve_single_as_admin(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user='admin')

        url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['admin'])

    def test_group_retrieve_all_as_admin(self):
        self.create_object_via_api(data=self.data.standard)

        self.login_user(user='admin')

        url = reverse(self.api_urls['retrieve_all'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['admin'])

    def test_group_retrieve_single_as_unauthenticated(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['unauthenticated'])

    def test_group_retrieve_all_as_unauthenticated(self):
        self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['retrieve_all'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['unauthenticated'])

    def test_group_update_exists_as_user(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="standard")

        url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_group_update_does_not_exist_as_user(self):
        self.login_user(user="standard")

        url = reverse(self.api_urls['update'], kwargs={'pk': 1})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_group_update_exists_as_admin(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="admin")

        url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['admin'])

    def test_group_update_does_not_exist_as_admin(self):
        self.login_user(user="admin")

        url = reverse(self.api_urls['update'], kwargs={'pk': 1})
        response = self.client.put(url, self.data.unique, format='json')

        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_group_update_exists_as_unauthenticated(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_group_update_does_not_exist_as_unauthenticated(self):
        self.logout_user()

        url = reverse(self.api_urls['update'], kwargs={'pk': 1})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_group_delete_does_not_exist_as_user(self):
        self.login_user(user="standard")

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['standard'])

    def test_group_delete_exists_as_user(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="standard")

        url = reverse(self.api_urls['delete'], kwargs={'pk': object_id})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['standard'])

    def test_group_delete_exists_as_admin(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="admin")

        url = reverse(self.api_urls['delete'], kwargs={'pk': object_id})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['admin'])

    def test_group_delete_does_not_exist_as_admin(self):
        self.login_user(user="admin")

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_group_delete_exists_as_unauthenticated(self):
        self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['unauthenticated'])

    def test_group_delete_does_not_exist_as_unauthenticated(self):
        self.logout_user()

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['unauthenticated'])


class PersonIdentifierTest(AvaCoreTest):
    # step 2: replace organize and PersonIdentifier
    model_name = 'organize.PersonIdentifier'

    has_owner = False

    # step 3: populate this section to define what you expect the API permissions will be
    api_permissions = {
        'create': {'unauthenticated': False, 'standard': False, 'admin': False, 'owner': False},
        'retrieve': {'unauthenticated': False, 'standard': False, 'admin': False, 'owner': False},
        'update': {'unauthenticated': False, 'standard': False, 'admin': False, 'owner': False},
        'delete': {'unauthenticated': False, 'standard': False, 'admin': False, 'owner': False},
    }

    # step 4: update with the model name for apiviewset urls (for apiviews and custom api's this won't work
    api_urls = {
        'create': 'personidentifier-list',
        'retrieve': 'personidentifier-detail',
        'retrieve_all': 'personidentifier-list',
        'update': 'personidentifier-detail',
        'delete': 'personidentifier-detail',
    }

    def setUp(self):
        # step 5: Update with Model Names
        super(PersonIdentifierTest, self).setUp()
        self.data = PersonIdentifierTestData()

    def create_object_via_api(self, data, user='admin'):
        # step 6: you will need to write this method.... this template only works with single models
        # with no relationships
        url = reverse(self.api_urls['create'])

        # Check that a user has been passed.
        # True - Log in as user.
        # False - Ensure unauthenticated access.
        if user:
            self.login_user(user=user)
        else:
            self.logout_user()
            user = 'unauthenticated'

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create'][user])

        self.logout_user()

        # return the id of the model you are testing
        if 'id' in response.data:
            return response.data['id']

    # step 7: replace personidentifier globally with your model name in lowercase
    def test_personidentifier_create_as_user(self):
        url = reverse(self.api_urls['create'])
        data = self.data.standard

        self.login_user(user='standard')

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['standard'])

    def test_personidentifier_create_as_admin(self):
        url = reverse(self.api_urls['create'])
        data = self.data.standard

        self.login_user(user='admin')

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['admin'])

    def test_personidentifier_create_as_unauthenticated(self):
        url = reverse(self.api_urls['create'])
        data = self.data.standard

        self.logout_user()

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['unauthenticated'])

    def test_personidentifier_retrieve_single_as_user(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user='standard')

        url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['standard'])

    def test_personidentifier_retrieve_all_as_user(self):
        self.create_object_via_api(data=self.data.standard)

        self.login_user(user='standard')

        url = reverse(self.api_urls['retrieve_all'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['standard'])

    def test_personidentifier_retrieve_single_as_admin(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user='admin')

        url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['admin'])

    def test_personidentifier_retrieve_all_as_admin(self):
        self.create_object_via_api(data=self.data.standard)

        self.login_user(user='admin')

        url = reverse(self.api_urls['retrieve_all'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['admin'])

    def test_personidentifier_retrieve_single_as_unauthenticated(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['unauthenticated'])

    def test_personidentifier_retrieve_all_as_unauthenticated(self):
        self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['retrieve_all'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['unauthenticated'])

    def test_personidentifier_update_exists_as_user(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="standard")

        url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_personidentifier_update_does_not_exist_as_user(self):
        self.login_user(user="standard")

        url = reverse(self.api_urls['update'], kwargs={'pk': 1})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_personidentifier_update_exists_as_admin(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="admin")

        url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['admin'])

    def test_personidentifier_update_does_not_exist_as_admin(self):
        self.login_user(user="admin")

        url = reverse(self.api_urls['update'], kwargs={'pk': 1})
        response = self.client.put(url, self.data.unique, format='json')

        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_personidentifier_update_exists_as_unauthenticated(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_personidentifier_update_does_not_exist_as_unauthenticated(self):
        self.logout_user()

        url = reverse(self.api_urls['update'], kwargs={'pk': 1})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_personidentifier_delete_does_not_exist_as_user(self):
        self.login_user(user="standard")

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['standard'])

    def test_personidentifier_delete_exists_as_user(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="standard")

        url = reverse(self.api_urls['delete'], kwargs={'pk': object_id})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['standard'])

    def test_personidentifier_delete_exists_as_admin(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="admin")

        url = reverse(self.api_urls['delete'], kwargs={'pk': object_id})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['admin'])

    def test_personidentifier_delete_does_not_exist_as_admin(self):
        self.login_user(user="admin")

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_personidentifier_delete_exists_as_unauthenticated(self):
        self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['unauthenticated'])

    def test_personidentifier_delete_does_not_exist_as_unauthenticated(self):
        self.logout_user()

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['unauthenticated'])


class GroupIdentifierTest(AvaCoreTest):
    # step 2: replace organize and GroupIdentifier
    model_name = 'organize.GroupIdentifier'

    has_owner = False

    # step 3: populate this section to define what you expect the API permissions will be
    api_permissions = {
        'create': {'unauthenticated': False, 'standard': False, 'admin': False, 'owner': False},
        'retrieve': {'unauthenticated': False, 'standard': False, 'admin': False, 'owner': False},
        'update': {'unauthenticated': False, 'standard': False, 'admin': False, 'owner': False},
        'delete': {'unauthenticated': False, 'standard': False, 'admin': False, 'owner': False},
    }

    # step 4: update with the model name for apiviewset urls (for apiviews and custom api's this won't work
    api_urls = {
        'create': 'groupidentifier-list',
        'retrieve': 'groupidentifier-detail',
        'retrieve_all': 'groupidentifier-list',
        'update': 'groupidentifier-detail',
        'delete': 'groupidentifier-detail',
    }

    def setUp(self):
        # step 5: Update with Model Names
        super(GroupIdentifierTest, self).setUp()
        self.data = GroupIdentifierTestData()

    def create_object_via_api(self, data, user='admin'):
        # step 6: you will need to write this method.... this template only works with single models
        # with no relationships
        url = reverse(self.api_urls['create'])

        # Check that a user has been passed.
        # True - Log in as user.
        # False - Ensure unauthenticated access.
        if user:
            self.login_user(user=user)
        else:
            self.logout_user()
            user = 'unauthenticated'

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create'][user])

        self.logout_user()

        # return the id of the model you are testing
        if 'id' in response.data:
            return response.data['id']

    # step 7: replace groupidentifier globally with your model name in lowercase
    def test_groupidentifier_create_as_user(self):
        url = reverse(self.api_urls['create'])
        data = self.data.standard

        self.login_user(user='standard')

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['standard'])

    def test_groupidentifier_create_as_admin(self):
        url = reverse(self.api_urls['create'])
        data = self.data.standard

        self.login_user(user='admin')

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['admin'])

    def test_groupidentifier_create_as_unauthenticated(self):
        url = reverse(self.api_urls['create'])
        data = self.data.standard

        self.logout_user()

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['unauthenticated'])

    def test_groupidentifier_retrieve_single_as_user(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user='standard')

        url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['standard'])

    def test_groupidentifier_retrieve_all_as_user(self):
        self.create_object_via_api(data=self.data.standard)

        self.login_user(user='standard')

        url = reverse(self.api_urls['retrieve_all'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['standard'])

    def test_groupidentifier_retrieve_single_as_admin(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user='admin')

        url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['admin'])

    def test_groupidentifier_retrieve_all_as_admin(self):
        self.create_object_via_api(data=self.data.standard)

        self.login_user(user='admin')

        url = reverse(self.api_urls['retrieve_all'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['admin'])

    def test_groupidentifier_retrieve_single_as_unauthenticated(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['unauthenticated'])

    def test_groupidentifier_retrieve_all_as_unauthenticated(self):
        self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['retrieve_all'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['unauthenticated'])

    def test_groupidentifier_update_exists_as_user(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="standard")

        url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_groupidentifier_update_does_not_exist_as_user(self):
        self.login_user(user="standard")

        url = reverse(self.api_urls['update'], kwargs={'pk': 1})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_groupidentifier_update_exists_as_admin(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="admin")

        url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['admin'])

    def test_groupidentifier_update_does_not_exist_as_admin(self):
        self.login_user(user="admin")

        url = reverse(self.api_urls['update'], kwargs={'pk': 1})
        response = self.client.put(url, self.data.unique, format='json')

        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_groupidentifier_update_exists_as_unauthenticated(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_groupidentifier_update_does_not_exist_as_unauthenticated(self):
        self.logout_user()

        url = reverse(self.api_urls['update'], kwargs={'pk': 1})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_groupidentifier_delete_does_not_exist_as_user(self):
        self.login_user(user="standard")

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['standard'])

    def test_groupidentifier_delete_exists_as_user(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="standard")

        url = reverse(self.api_urls['delete'], kwargs={'pk': object_id})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['standard'])

    def test_groupidentifier_delete_exists_as_admin(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="admin")

        url = reverse(self.api_urls['delete'], kwargs={'pk': object_id})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['admin'])

    def test_groupidentifier_delete_does_not_exist_as_admin(self):
        self.login_user(user="admin")

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_groupidentifier_delete_exists_as_unauthenticated(self):
        self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['unauthenticated'])

    def test_groupidentifier_delete_does_not_exist_as_unauthenticated(self):
        self.logout_user()

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['unauthenticated'])


class PersonTest(AvaCoreTest):
    # step 2: replace organize and Person
    model_name = 'organize.Person'

    has_owner = False

    # step 3: populate this section to define what you expect the API permissions will be
    api_permissions = {
        'create': {'unauthenticated': False, 'standard': False, 'admin': False, 'owner': False},
        'retrieve': {'unauthenticated': False, 'standard': True, 'admin': True, 'owner': True},
        'update': {'unauthenticated': False, 'standard': False, 'admin': True, 'owner': False},
        'delete': {'unauthenticated': False, 'standard': False, 'admin': False, 'owner': False},
    }

    # step 4: update with the model name for apiviewset urls (for apiviews and custom api's this won't work
    api_urls = {
        'create': 'person-list',
        'retrieve': 'person-detail',
        'retrieve_all': 'person-list',
        'update': 'person-detail',
        'delete': 'person-detail',
    }

    def setUp(self):
        # step 5: Update with Model Names
        super(PersonTest, self).setUp()
        self.data = PersonTestData()

    def create_object_via_api(self, data, user='admin'):
        # step 6: you will need to write this method.... this template only works with single models
        # with no relationships
        url = reverse(self.api_urls['create'])

        # Check that a user has been passed.
        # True - Log in as user.
        # False - Ensure unauthenticated access.
        if user:
            self.login_user(user=user)
        else:
            self.logout_user()
            user = 'unauthenticated'

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create'][user])

        self.logout_user()

        # return the id of the model you are testing
        if 'id' in response.data:
            return response.data['id']

    # step 7: replace person globally with your model name in lowercase
    def test_person_create_as_user(self):
        url = reverse(self.api_urls['create'])
        data = self.data.standard

        self.login_user(user='standard')

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['standard'])

    def test_person_create_as_admin(self):
        url = reverse(self.api_urls['create'])
        data = self.data.standard

        self.login_user(user='admin')

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['admin'])

    def test_person_create_as_unauthenticated(self):
        url = reverse(self.api_urls['create'])
        data = self.data.standard

        self.logout_user()

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['unauthenticated'])

    def test_person_retrieve_single_as_user(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user='standard')

        url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['standard'])

    def test_person_retrieve_all_as_user(self):
        self.create_object_via_api(data=self.data.standard)

        self.login_user(user='standard')

        url = reverse(self.api_urls['retrieve_all'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['standard'])

    def test_person_retrieve_single_as_admin(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user='admin')

        url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['admin'])

    def test_person_retrieve_all_as_admin(self):
        self.create_object_via_api(data=self.data.standard)

        self.login_user(user='admin')

        url = reverse(self.api_urls['retrieve_all'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['admin'])

    def test_person_retrieve_single_as_unauthenticated(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['unauthenticated'])

    def test_person_retrieve_all_as_unauthenticated(self):
        self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['retrieve_all'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['unauthenticated'])

    def test_person_update_exists_as_user(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="standard")

        url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_person_update_does_not_exist_as_user(self):
        self.login_user(user="standard")

        url = reverse(self.api_urls['update'], kwargs={'pk': 1})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_person_update_exists_as_admin(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="admin")

        url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['admin'])

    def test_person_update_does_not_exist_as_admin(self):
        self.login_user(user="admin")

        url = reverse(self.api_urls['update'], kwargs={'pk': 1})
        response = self.client.put(url, self.data.unique, format='json')

        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_person_update_exists_as_unauthenticated(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_person_update_does_not_exist_as_unauthenticated(self):
        self.logout_user()

        url = reverse(self.api_urls['update'], kwargs={'pk': 1})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_person_delete_does_not_exist_as_user(self):
        self.login_user(user="standard")

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['standard'])

    def test_person_delete_exists_as_user(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="standard")

        url = reverse(self.api_urls['delete'], kwargs={'pk': object_id})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['standard'])

    def test_person_delete_exists_as_admin(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="admin")

        url = reverse(self.api_urls['delete'], kwargs={'pk': object_id})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['admin'])

    def test_person_delete_does_not_exist_as_admin(self):
        self.login_user(user="admin")

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_person_delete_exists_as_unauthenticated(self):
        self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['unauthenticated'])

    def test_person_delete_does_not_exist_as_unauthenticated(self):
        self.logout_user()

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['unauthenticated'])
