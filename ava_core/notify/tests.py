# Rest Imports
from rest_framework import status
# Local Imports
from ava_core.abstract.test import AvaCoreTest
from ava_core.notify.test_data import NotificationEmailTestData


# Implementation
class NotificationEmailTest(AvaCoreTest):
    """
    NotificationEmail Test
    """

    def setUp(self):
        # Make call to super.
        super(NotificationEmailTest, self).setUp()

        # Set the data type.
        self.data = NotificationEmailTestData()

    def test_notification_email_create_as_user(self):
        # Log in as user.
        self.login_user(self.user_user)

        # Take count.
        count = self.data.model.objects.count()

        # Store data to use.
        data = self.data.get_data('standard')

        # Make post request and ensure created response.
        response = self.client.post(self.format_url(self.data.url), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.data.model.objects.count(), count + 1)
        self.assertTrue(self.does_contain_data(response.data, data))

    def test_notification_email_create_as_admin(self):
        # Log in as admin.
        self.login_user(self.user_admin)

        # Take count.
        count = self.data.model.objects.count()

        # Store data to use.
        data = self.data.get_data('standard')

        # Make post request and ensure created response.
        response = self.client.post(self.format_url(self.data.url), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.data.model.objects.count(), count + 1)
        self.assertTrue(self.does_contain_data(response.data, data))

    def test_notification_email_create_as_unauthenticated(self):
        # Take count.
        count = self.data.model.objects.count()

        # Store data to use.
        data = self.data.get_data('standard')

        # Make post request and ensure unauthorized response.
        response = self.client.post(self.format_url(self.data.url), data, format='json')
        self.assertIn(response.status_code, self.status_forbidden)
        self.assertEqual(self.data.model.objects.count(), count)

    def test_notification_email_retrieve_single_as_user(self):
        # Create new NotificationEmail models, storing URL.
        url = self.create_model_logout(self.data, data_name='standard', owner=self.user_user)

        # Log in as user.
        self.login_user(self.user_user)

        # Make get request and ensure OK response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data(response.data, self.data.standard))

    def test_notification_email_retrieve_all_as_user(self):
        # Create new NotificationEmail models.
        self.create_model_logout(self.data, data_name='standard', owner=self.user_user)
        self.create_model_logout(self.data, data_name='modified', owner=self.user_user)

        # Log in as user.
        self.login_user(self.user_user)

        # Make get request and ensure OK response
        response = self.client.get(self.format_url(self.data.url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_list(response.data['results'], [self.data.standard, self.data.unique]))

    def test_notification_email_retrieve_single_as_admin(self):
        # Create new NotificationEmail models, storing URL.
        url = self.create_model_logout(self.data, data_name='standard', owner=self.user_admin)

        # Log in as admin.
        self.login_user(self.user_admin)

        # Make get request and ensure OK response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data(response.data, self.data.standard))

    def test_notification_email_retrieve_all_as_admin(self):
        # Create new NotificationEmail models.
        self.create_model_logout(self.data, data_name='standard', owner=self.user_admin)
        self.create_model_logout(self.data, data_name='modified', owner=self.user_admin)

        # Log in as admin.
        self.login_user(self.user_admin)

        # Make get request and ensure OK response
        response = self.client.get(self.format_url(self.data.url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_list(response.data['results'], [self.data.standard, self.data.unique]))

    def test_notification_email_retrieve_single_as_unauthorized(self):
        # Create new NotificationEmail models, storing URL.
        url = self.create_model_logout(self.data, data_name='standard', owner=self.user_admin)

        # Make get request and ensure unauthorized response
        response = self.client.get(url)
        self.assertIn(response.status_code, self.status_forbidden)

    def test_notification_email_retrieve_all_as_unauthorized(self):
        # Create new NotificationEmail models.
        self.create_model_logout(self.data, data_name='standard', owner=self.user_admin)
        self.create_model_logout(self.data, data_name='modified', owner=self.user_admin)

        # Make get request and ensure unauthorized response
        response = self.client.get(self.format_url(self.data.url))
        self.assertIn(response.status_code, self.status_forbidden)

    # TODO:    Write retrieve owner tests    def test_notification_email_update_exists_as_user(self):
        # Create new NotificationEmail models, storing URL.
        url = self.create_model_logout(self.data, data_name='standard', owner=self.user_user)
        # Log in as user.
        self.login_user(self.user_user)

        # Make put request and ensure OK response.
        response = self.client.put(url, self.data.get_data('unique'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_url(url, self.data.unique))

    def test_notification_email_update_does_not_exist_as_user(self):
        # Log in as user.
        self.login_user(self.user_user)

        # Make put request and ensure not found response.
        response = self.client.put(self.format_url(self.data.url + '9999'), self.data.get_data('unique'))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_notification_email_update_exists_as_admin(self):
        # Create new NotificationEmail models, storing URL.
        url = self.create_model_logout(self.data, data_name='standard', owner=self.user_admin)
        # Log in as admin.
        self.login_user(self.user_admin)

        # Make put request and ensure OK response.
        response = self.client.put(url, self.data.get_data('unique'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_url(url, self.data.unique))

    def test_notification_email_update_does_not_exist_as_admin(self):
        # Log in as admin.
        self.login_user(self.user_admin)

        # Make put request and ensure not found response.
        response = self.client.put(self.format_url(self.data.url + '9999'), self.data.get_data('unique'))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_notification_email_update_exists_as_unauthorized(self):
        # Create new NotificationEmail models, storing URL.
        url = self.create_model_logout(self.data, data_name='standard', owner=self.user_admin)
        # Make put request and ensure unauthorized response.
        response = self.client.put(url, self.data.get_data('unique'))
        self.assertIn(response.status_code, self.status_forbidden)
        self.assertTrue(self.does_contain_data_url(url, self.data.standard))

    def test_notification_email_update_does_not_exist_as_unauthorized(self):
        # Make put request and ensure unauthorized response.
        response = self.client.put(self.format_url(self.data.url + '9999'), self.data.get_data('unique'))
        self.assertIn(response.status_code, self.status_forbidden)

    # TODO:    Write update owner tests    def test_notification_email_delete_exists_as_user(self):
        # Create new NotificationEmail models, storing URL.
        url = self.create_model_logout(self.data, data_name='standard', owner=self.user_user)
        # Log in as user.
        self.login_user(self.user_user)

        # Make delete request and ensure no content response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(self.data.model.objects.count(), 0)

    def test_notification_email_delete_does_not_exist_as_user(self):
        # Log in as user.
        self.login_user(self.user_user)

        # Make delete request and ensure not found response
        response = self.client.get(self.format_url(self.data.url + '9999'))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_notification_email_delete_exists_as_admin(self):
        # Create new NotificationEmail models, storing URL.
        url = self.create_model_logout(self.data, data_name='standard', owner=self.user_admin)
        # Log in as admin.
        self.login_user(self.user_admin)

        # Make delete request and ensure no content response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(self.data.model.objects.count(), 0)

    def test_notification_email_delete_does_not_exist_as_admin(self):
        # Log in as admin.
        self.login_user(self.user_admin)

        # Make delete request and ensure not found response
        response = self.client.get(self.format_url(self.data.url + '9999'))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_notification_email_delete_exists_as_unauthorized(self):
        # Create new NotificationEmail models, storing URL.
        url = self.create_model_logout(self.data, data_name='standard', owner=self.user_admin)
        # Make delete request and ensure unauthorized response
        response = self.client.get(url)
        self.assertIn(response.status_code, self.status_forbidden)
        self.assertEqual(self.data.model.objects.count(), 1)

    def test_notification_email_delete_does_not_exist_as_unauthorized(self):
        # Make delete request and ensure unauthorized response
        response = self.client.get(self.format_url(self.data.url + '9999'))
        self.assertIn(response.status_code, self.status_forbidden)

    # TODO:    Write delete owner tests

