# Rest Imports
# Local Imports
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from ava_core.abstract.test import AvaCoreTest
from ava_core.game.models import Achievement
from ava_core.game.test_data import AchievementTestData


# Implementation
class AchievementTest(AvaCoreTest):
    def setUp(self):
        # Make call to super.
        super(AchievementTest, self).setUp()

        # self.client = APIClient(enforce_csrf_checks=self.enforce_csrf)
        # response = client.post(self.login_url, self.users['user'], format='json')
        # token = response.data['token']
        # print("Token :: " + token)
        # client.credentials(HTTP_AUTHORIZATION='JWT ' + token)

        # Set the data type.
        self.data = AchievementTestData()

    def test_achievement_create_as_user(self):
        url = reverse('achievement-list')
        data = self.data.standard

        self.login_user(user='normal')

        response = self.client.post(url, data, format='json')
        self.assertIn(response.status_code, self.status_forbidden)
        self.assertEqual(Achievement.objects.count(), 0)

    def test_achievement_create_as_admin(self):
        url = reverse('achievement-list')
        data = self.data.standard

        self.login_user(user='admin')

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Achievement.objects.count(), 1)
        self.assertEqual(Achievement.objects.get().name, data['name'])

    def test_achievement_create_as_unauthenticated(self):
        url = reverse('achievement-list')
        data = self.data.standard

        self.logout_user()

        response = self.client.post(url, data, format='json')

        self.assertIn(response.status_code, self.status_forbidden)
        self.assertEqual(Achievement.objects.count(), 0)

    def test_achievement_retrieve_single_as_user(self):
        self.assertEqual(1,"Test not written")

    def test_achievement_retrieve_all_as_user(self):
        self.assertEqual(1,"Test not written")

    def test_achievement_retrieve_single_as_admin(self):
        self.assertEqual(1,"Test not written")

    def test_achievement_retrieve_all_as_admin(self):
        self.assertEqual(1,"Test not written")

    def test_achievement_retrieve_single_as_unauthorized(self):
        self.assertEqual(1,"Test not written")

    def test_achievement_retrieve_all_as_unauthorized(self):
        self.assertEqual(1,"Test not written")

    def test_achievement_update_exists_as_user(self):
        self.assertEqual(1,"Test not written")

    def test_achievement_update_does_not_exist_as_user(self):
        self.assertEqual(1,"Test not written")

    def test_achievement_update_exists_as_admin(self):
        self.assertEqual(1,"Test not written")

    def test_achievement_update_does_not_exist_as_admin(self):
        self.assertEqual(1,"Test not written")

    def test_achievement_update_exists_as_unauthorized(self):
        self.assertEqual(1,"Test not written")

    def test_achievement_update_does_not_exist_as_unauthorized(self):
        self.assertEqual(1,"Test not written")

    def test_achievement_delete_does_not_exist_as_user(self):
        self.assertEqual(1,"Test not written")

    def test_achievement_delete_exists_as_admin(self):
        self.assertEqual(1,"Test not written")

    def test_achievement_delete_does_not_exist_as_admin(self):
        self.assertEqual(1,"Test not written")

    def test_achievement_delete_exists_as_unauthorized(self):
        self.assertEqual(1,"Test not written")

    def test_achievement_delete_does_not_exist_as_unauthorized(self):
        self.assertEqual(1,"Test not written")
