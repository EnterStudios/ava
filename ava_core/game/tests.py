# Rest Imports
# Local Imports
from rest_framework.reverse import reverse, reverse_lazy
from ava_core.abstract.test import AvaCoreTest
from ava_core.game.test_data import AchievementTestData


# Implementation
class AchievementTest(AvaCoreTest):
    model_name = 'game.Achievement'

    has_owner = False

    # populate this section to define what you expect the API permissions will be
    api_permissions = {
        'create': {'unauthenticated': False, 'standard': False, 'admin': True, 'owner': False},
        'retrieve': {'unauthenticated': False, 'standard': True, 'admin': True, 'owner': False},
        'update': {'unauthenticated': False, 'standard': False, 'admin': True, 'owner': False},
        'delete': {'unauthenticated': False, 'standard': False, 'admin': True, 'owner': False},
    }

    pk = 1

    api_urls = {
        'create': reverse('achievement-list'),
        'retrieve': reverse('achievement-detail', args=[pk]),
        'retrieve_all': reverse('achievement-list'),
        'update': reverse_lazy('achievement-detail', args=[pk]),
        'delete': reverse_lazy('achievement-detail', args=[pk]),
    }

    def setUp(self):
        super(AchievementTest, self).setUp()
        self.data = AchievementTestData()

    def test_achievement_create_as_user(self):
        url = self.api_urls['create']
        data = self.data.standard

        self.login_user(user='standard')

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['standard'])

    def test_achievement_create_as_admin(self):
        url = self.api_urls['create']
        data = self.data.standard

        self.login_user(user='admin')

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['admin'])

    def test_achievement_create_as_unauthenticated(self):
        url = self.api_urls['create']
        data = self.data.standard

        self.logout_user()

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['unauthenticated'])

    def test_achievement_retrieve_single_as_user(self):
        url = self.api_urls['create']
        data = self.data.standard

        # must be admin to create
        self.login_user(user='admin')

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['admin'])

        self.login_user(user='standard')

        url = self.api_urls['retrieve'].format(response.data['id'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['standard'])

    def test_achievement_retrieve_all_as_user(self):
        url = self.api_urls['create']
        data = self.data.standard

        # must be admin to create
        self.login_user(user='admin')

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['admin'])

        self.login_user(user='standard')

        url = self.api_urls['retrieve']
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['standard'])

    def test_achievement_retrieve_single_as_admin(self):
        url = self.api_urls['create']
        data = self.data.standard

        # must be admin to create
        self.login_user(user='admin')

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['admin'])

        self.login_user(user='admin')

        url = self.api_urls['retrieve'].format(response.data['id'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['admin'])

    def test_achievement_retrieve_all_as_admin(self):
        url = self.api_urls['create']
        data = self.data.standard

        # must be admin to create
        self.login_user(user='admin')

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['admin'])

        self.login_user(user='admin')

        url = self.api_urls['retrieve']
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['admin'])

    def test_achievement_retrieve_single_as_unauthorized(self):
        url = self.api_urls['create']
        data = self.data.standard

        # must be admin to create
        self.login_user(user='admin')

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['admin'])

        self.logout_user()

        url = self.api_urls['retrieve'].format(response.data['id'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['unauthenticated'])

    def test_achievement_retrieve_all_as_unauthorized(self):
        url = self.api_urls['create']
        data = self.data.standard

        # must be admin to create
        self.login_user(user='admin')

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['admin'])

        self.logout_user()

        url = self.api_urls['retrieve']
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['unauthenticated'])

    def test_achievement_update_exists_as_user(self):
        self.assertEqual(1, "Test not written")

    def test_achievement_update_does_not_exist_as_user(self):
        self.assertEqual(1, "Test not written")

    def test_achievement_update_exists_as_admin(self):
        self.assertEqual(1, "Test not written")

    def test_achievement_update_does_not_exist_as_admin(self):
        self.assertEqual(1, "Test not written")

    def test_achievement_update_exists_as_unauthorized(self):
        self.assertEqual(1, "Test not written")

    def test_achievement_update_does_not_exist_as_unauthorized(self):
        self.assertEqual(1, "Test not written")

    def test_achievement_delete_does_not_exist_as_user(self):
        self.assertEqual(1, "Test not written")

    def test_achievement_delete_exists_as_admin(self):
        self.assertEqual(1, "Test not written")

    def test_achievement_delete_does_not_exist_as_admin(self):
        self.assertEqual(1, "Test not written")

    def test_achievement_delete_exists_as_unauthorized(self):
        self.assertEqual(1, "Test not written")

    def test_achievement_delete_does_not_exist_as_unauthorized(self):
        self.assertEqual(1, "Test not written")
