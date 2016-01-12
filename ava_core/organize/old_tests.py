# Rest Imports
from rest_framework import status
# Local Imports
from ava_core.organize.test_data_attributes import PersonTestDataAttributes, GroupTestDataAttributes
from .test_data import data
from ava_core.abstract.tests import AVATestCase

# Implementation
"""
Test harnesses for Person Model
"""


class PersonTests(AVATestCase):
    def setUp(self):
        super(PersonTests, self).setUp()
        self.data = data['person']
        self.data_attributes = PersonTestDataAttributes

    """
     Create tests
     """

    def test_create_person_as_user(self):
        # Log in as standard
        self.login_user(user=self.user_standard)

        # Make post and ensure unauthorized response
        response = self.client.post(self.data_attributes.url, self.data['standard'], format='json')
        self.assertIn(response.status_code, self.status_forbidden)
        self.assertEqual(self.data_attributes.query_set.count(), 0)

    def test_create_person_as_admin(self):
        # Log in as admin
        self.login_user(user=self.user_admin)

        # Make post and ensure created response
        response = self.client.post(self.data_attributes.url, self.data['standard'], format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.data_attributes.query_set.count(), 1)
        self.assertTrue(self.does_contain_data(data_target=response.data, data_source=self.data['standard']))

    def test_create_person_unauthenticated(self):
        # Make post and ensure unauthorized response
        response = self.client.post(self.data_attributes.url, self.data['standard'], format='json')
        self.assertIn(response.status_code, self.status_forbidden)
        self.assertEqual(self.data_attributes.query_set.count(), 0)

    def test_create_person_multiple(self):
        # Log in as admin
        self.login_user(user=self.user_admin)

        # Make first post and ensure created response
        response = self.client.post(self.data_attributes.url, self.data['standard'], format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.data_attributes.query_set.count(), 1)
        self.assertTrue(self.does_contain_data(data_target=response.data, data_source=self.data['standard']))

        # Make second post and ensure created response
        response = self.client.post(self.data_attributes.url, self.data['modified'], format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.data_attributes.query_set.count(), 2)
        self.assertTrue(self.does_contain_data(data_target=response.data, data_source=self.data['modified']))

    def test_create_person_duplicate(self):
        # Log in as admin
        self.login_user(user=self.user_admin)

        # Make first post and ensure created response
        response = self.client.post(self.data_attributes.url, self.data['standard'], format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.data_attributes.query_set.count(), 1)
        self.assertTrue(self.does_contain_data(data_target=response.data, data_source=self.data['standard']))

        # Make second post and ensure added ok response
        response = self.client.post(self.data_attributes.url, self.data['standard'], format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.data_attributes.query_set.count(), 2)

    def test_create_person_duplicate_altered_case(self):
        # Log in as admin
        self.login_user(user=self.user_admin)

        # Make first post and ensure created response
        response = self.client.post(self.data_attributes.url, self.data['standard'], format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.data_attributes.query_set.count(), 1)
        self.assertTrue(self.does_contain_data(data_target=response.data, data_source=self.data['standard']))

        # Make second post and ensure bad request response
        response = self.client.post(self.data_attributes.url, self.data.altered_case, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.data_attributes.query_set.count(), 2)

    """
    Retrieve tests
    """

    def test_retrieve_person_as_user_single(self):
        # Add new version, storing URL
        url = self.create_data_logout(user=self.user_admin, test_data_attributes=self.data_attributes,
                                      request_data=self.data['standard'])

        # Log in as standard
        self.login_user(user=self.user_standard)

        # Make get request for single and ensure OK response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data(data_target=response.data, data_source=self.data['standard']))

    def test_retrieve_person_as_user_all(self):
        # Add new version, storing URL
        self.create_data_logout(user=self.user_admin, test_data_attributes=self.data_attributes,
                                request_data=self.data['standard'])
        self.create_data_logout(user=self.user_admin, test_data_attributes=self.data_attributes,
                                request_data=self.data['modified'])

        # Log in as standard
        self.login_user(user=self.user_standard)

        # Make get request for all and ensure OK response
        response = self.client.get(self.data_attributes.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_list(data_list_target=response.data,
                                                    data_list_source=[self.data['standard'], self.data['modified']]))

    def test_retrieve_person_as_admin_single(self):
        # Add new version, storing URL
        url = self.create_data_logout(user=self.user_admin, test_data_attributes=self.data_attributes,
                                      request_data=self.data['standard'])

        # Log in as standard
        self.login_user(user=self.user_admin)

        # Make get request for single and ensure OK response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data(data_target=response.data, data_source=self.data['standard']))

    def test_retrieve_person_as_admin_all(self):
        # Add new versions
        self.create_data_logout(user=self.user_admin, test_data_attributes=self.data_attributes,
                                request_data=self.data['modified'])
        self.create_data_logout(user=self.user_admin, test_data_attributes=self.data_attributes,
                                request_data=self.data['standard'])

        # Log in as standard
        self.login_user(user=self.user_standard)

        # Make get request for all and ensure OK response
        response = self.client.get(self.data_attributes.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_list(data_list_target=response.data, data_list_source=
        [self.data['standard'], self.data['modified']]))

    def test_retrieve_person_unauthenticated_single(self):
        # Add new version, storing URL
        url = self.create_data_logout(user=self.user_admin, test_data_attributes=self.data_attributes,
                                      request_data=self.data['standard'])

        # Make get request for single and ensure unauthorised response
        response = self.client.get(url)
        self.assertIn(response.status_code, self.status_forbidden)

    def test_retrieve_person_unauthenticated_all(self):
        # Add new versions
        self.create_data_logout(user=self.user_admin, test_data_attributes=self.data_attributes,
                                request_data=self.data['standard'])
        self.create_data_logout(user=self.user_admin, test_data_attributes=self.data_attributes,
                                request_data=self.data['modified'])

        # Make get request for all and ensure unauthorised response
        response = self.client.get(self.data_attributes.url)
        self.assertIn(response.status_code, self.status_forbidden)

    def test_retrieve_person_does_not_exist(self):
        # Log in as admin
        self.login_user(user=self.user_admin)

        # Make get request for single and ensure moved permanently response
        response = self.client.get(self.data_attributes.url_does_not_exist)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    """
    Update tests
    """

    def test_update_person_as_user(self):
        # Add new version, storing URL
        url = self.create_data_logout(user=self.user_admin, test_data_attributes=self.data_attributes,
                                      request_data=self.data['standard'])

        # Log in as standard
        self.login_user(user=self.user_standard)

        # Make put request and ensure unauthorised response
        response = self.client.put(url, self.data['modified'])
        self.assertIn(response.status_code, self.status_forbidden)
        self.assertTrue(self.does_contain_data_url(url, self.data['standard']))

    def test_update_person_as_admin(self):
        # Add new version, storing URL
        url = self.create_data_logout(user=self.user_admin, test_data_attributes=self.data_attributes,
                                      request_data=self.data['standard'])

        # Log in as admin
        self.login_user(user=self.user_admin)

        # Make put request and ensure OK response
        response = self.client.put(url, self.data['modified'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_url(url, self.data['modified']))

    def test_update_person_unauthenticated(self):
        # Add new version, storing URL
        url = self.create_data_logout(user=self.user_admin, test_data_attributes=self.data_attributes,
                                      request_data=self.data['standard'])

        # Make put request and ensure unauthorised response
        response = self.client.put(url, self.data['modified'])
        self.assertIn(response.status_code, self.status_forbidden)
        self.assertTrue(self.does_contain_data_url(url, self.data['standard']))

    def test_update_person_does_not_exist(self):
        # Log in as admin
        self.login_user(user=self.user_admin)

        # Make put request and ensure moved permanently response
        response = self.client.put(self.data_attributes.url_does_not_exist)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_person_duplicate(self):
        # Add new versions, storing URL to be updated
        self.create_data_logout(user=self.user_admin, test_data_attributes=self.data_attributes,
                                request_data=self.data['modified'])
        url = self.create_data_logout(user=self.user_admin, test_data_attributes=self.data_attributes,
                                      request_data=self.data['standard'])

        # Log in as admin
        self.login_user(user=self.user_admin)

        # Make duplicating put and ensure bad request response
        response = self.client.put(url, self.data['modified'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_person_duplicate_altered_case(self):
        # Add new versions, storing URL to be updated
        self.create_data_logout(user=self.user_admin, test_data_attributes=self.data_attributes,
                                request_data=self.data['standard'])
        url = self.create_data_logout(user=self.user_admin, test_data_attributes=self.data_attributes,
                                      request_data=self.data['modified'])

        # Log in as admin
        self.login_user(user=self.user_admin)

        # Make duplicating put and ensure bad request response
        response = self.client.put(url, self.data.altered_case)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    """
    Delete tests
    """

    def test_delete_person_as_user(self):
        # Add new version, storing URL
        url = self.create_data_logout(user=self.user_admin, test_data_attributes=self.data_attributes,
                                      request_data=self.data['standard'])

        # Log in as standard
        self.login_user(user=self.user_standard)

        # Make delete and ensure unauthorised response
        response = self.client.delete(url)
        self.assertIn(response.status_code, self.status_forbidden)
        self.assertEqual(self.data_attributes.query_set.count(), 1)

    def test_delete_person_as_admin(self):
        # Add new version, storing URL
        url = self.create_data_logout(user=self.user_admin, test_data_attributes=self.data_attributes,
                                      request_data=self.data['standard'])

        # Log in as admin
        self.login_user(user=self.user_admin)

        # Make delete and ensure no content response
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(self.data_attributes.query_set.count(), 0)

    def test_delete_person_unauthenticated(self):
        # Add new version, storing URL
        url = self.create_data_logout(user=self.user_admin, test_data_attributes=self.data_attributes,
                                      request_data=self.data['standard'])

        # Make delete and ensure unauthorised response
        response = self.client.delete(url)
        self.assertIn(response.status_code, self.status_forbidden)
        self.assertEqual(self.data_attributes.query_set.count(), 1)

    def test_delete_person_does_not_exist(self):
        # Log in as admin
        self.login_user(user=self.user_admin)

        # Make delete and ensure not found response
        response = self.client.delete(self.data_attributes.url_does_not_exist)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class GroupTests(AVATestCase):
    def setUp(self):
        super(GroupTests, self).setUp()
        self.data = data['group']
        self.data_attributes = GroupTestDataAttributes

    """
     Create tests
     """

    def test_create_group_as_user(self):
        # Log in as standard
        self.login_user(user=self.user_standard)

        # Make post and ensure unauthorized response
        response = self.client.post(self.data_attributes.url, self.data['standard'], format='json')
        self.assertIn(response.status_code, self.status_forbidden)
        self.assertEqual(self.data_attributes.query_set.count(), 0)

    def test_create_group_as_admin(self):
        # Log in as admin
        self.login_user(user=self.user_admin)

        # Make post and ensure created response
        response = self.client.post(self.data_attributes.url, self.data['standard'], format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.data_attributes.query_set.count(), 1)
        self.assertTrue(self.does_contain_data(data_target=response.data, data_source=self.data['standard']))

    def test_create_group_unauthenticated(self):
        # Make post and ensure unauthorized response
        response = self.client.post(self.data_attributes.url, self.data['standard'], format='json')
        self.assertIn(response.status_code, self.status_forbidden)
        self.assertEqual(self.data_attributes.query_set.count(), 0)

    def test_create_group_multiple(self):
        # Log in as admin
        self.login_user(user=self.user_admin)

        # Make first post and ensure created response
        response = self.client.post(self.data_attributes.url, self.data['standard'], format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.data_attributes.query_set.count(), 1)
        self.assertTrue(self.does_contain_data(data_target=response.data, data_source=self.data['standard']))

        # Make second post and ensure created response
        response = self.client.post(self.data_attributes.url, self.data['modified'], format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.data_attributes.query_set.count(), 2)
        self.assertTrue(self.does_contain_data(data_target=response.data, data_source=self.data['modified']))

    def test_create_group_duplicate(self):
        # Log in as admin
        self.login_user(user=self.user_admin)

        # Make first post and ensure created response
        response = self.client.post(self.data_attributes.url, self.data['standard'], format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.data_attributes.query_set.count(), 1)
        self.assertTrue(self.does_contain_data(data_target=response.data, data_source=self.data['standard']))

        # Make second post and ensure bad request response
        response = self.client.post(self.data_attributes.url, self.data['standard'], format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(self.data_attributes.query_set.count(), 1)

    def test_create_group_duplicate_altered_case(self):
        # Log in as admin
        self.login_user(user=self.user_admin)

        # Make first post and ensure created response
        response = self.client.post(self.data_attributes.url, self.data['standard'], format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.data_attributes.query_set.count(), 1)
        self.assertTrue(self.does_contain_data(data_target=response.data, data_source=self.data['standard']))

        # Make second post and ensure bad request response
        response = self.client.post(self.data_attributes.url, self.data.altered_case, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(self.data_attributes.query_set.count(), 1)

    """
    Retrieve tests
    """

    def test_retrieve_group_as_user_single(self):
        # Add new version, storing URL
        url = self.create_data_logout(user=self.user_admin, test_data_attributes=self.data_attributes,
                                      request_data=self.data['standard'])

        # Log in as standard
        self.login_user(user=self.user_standard)

        # Make get request for single and ensure OK response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data(data_target=response.data, data_source=self.data['standard']))

    def test_retrieve_group_as_user_all(self):
        # Add new version, storing URL
        self.create_data_logout(user=self.user_admin, test_data_attributes=self.data_attributes,
                                request_data=self.data['standard'])
        self.create_data_logout(user=self.user_admin, test_data_attributes=self.data_attributes,
                                request_data=self.data['modified'])

        # Log in as standard
        self.login_user(user=self.user_standard)

        # Make get request for all and ensure OK response
        response = self.client.get(self.data_attributes.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_list(data_list_target=response.data, data_list_source=
        [self.data['standard'], self.data['modified']]))

    def test_retrieve_group_as_admin_single(self):
        # Add new version, storing URL
        url = self.create_data_logout(user=self.user_admin, test_data_attributes=self.data_attributes,
                                      request_data=self.data['standard'])

        # Log in as standard
        self.login_user(user=self.user_admin)

        # Make get request for single and ensure OK response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data(data_target=response.data, data_source=self.data['standard']))

    def test_retrieve_group_as_admin_all(self):
        # Add new versions
        self.create_data_logout(user=self.user_admin, test_data_attributes=self.data_attributes,
                                request_data=self.data['modified'])
        self.create_data_logout(user=self.user_admin, test_data_attributes=self.data_attributes,
                                request_data=self.data['standard'])

        # Log in as standard
        self.login_user(user=self.user_standard)

        # Make get request for all and ensure OK response
        response = self.client.get(self.data_attributes.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_list(data_list_target=response.data, data_list_source=
        [self.data['standard'], self.data['modified']]))

    def test_retrieve_group_unauthenticated_single(self):
        # Add new version, storing URL
        url = self.create_data_logout(user=self.user_admin, test_data_attributes=self.data_attributes,
                                      request_data=self.data['standard'])

        # Make get request for single and ensure unauthorised response
        response = self.client.get(url)
        self.assertIn(response.status_code, self.status_forbidden)

    def test_retrieve_group_unauthenticated_all(self):
        # Add new versions
        self.create_data_logout(user=self.user_admin, test_data_attributes=self.data_attributes,
                                request_data=self.data['standard'])
        self.create_data_logout(user=self.user_admin, test_data_attributes=self.data_attributes,
                                request_data=self.data['modified'])

        # Make get request for all and ensure unauthorised response
        response = self.client.get(self.data_attributes.url)
        self.assertIn(response.status_code, self.status_forbidden)

    def test_retrieve_group_does_not_exist(self):
        # Log in as admin
        self.login_user(user=self.user_admin)

        # Make get request for single and ensure moved permanently response
        response = self.client.get(self.data_attributes.url_does_not_exist)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    """
    Update tests
    """

    def test_update_group_as_user(self):
        # Add new version, storing URL
        url = self.create_data_logout(user=self.user_admin, test_data_attributes=self.data_attributes,
                                      request_data=self.data['standard'])

        # Log in as standard
        self.login_user(user=self.user_standard)

        # Make put request and ensure unauthorised response
        response = self.client.put(url, self.data['modified'])
        self.assertIn(response.status_code, self.status_forbidden)
        self.assertTrue(self.does_contain_data_url(url, self.data['standard']))

    def test_update_group_as_admin(self):
        # Add new version, storing URL
        url = self.create_data_logout(user=self.user_admin, test_data_attributes=self.data_attributes,
                                      request_data=self.data['standard'])

        # Log in as admin
        self.login_user(user=self.user_admin)

        # Make put request and ensure OK response
        response = self.client.put(url, self.data['modified'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_url(url, self.data['modified']))

    def test_update_group_unauthenticated(self):
        # Add new version, storing URL
        url = self.create_data_logout(user=self.user_admin, test_data_attributes=self.data_attributes,
                                      request_data=self.data['standard'])

        # Make put request and ensure unauthorised response
        response = self.client.put(url, self.data['modified'])
        self.assertIn(response.status_code, self.status_forbidden)
        self.assertTrue(self.does_contain_data_url(url, self.data['standard']))

    def test_update_group_does_not_exist(self):
        # Log in as admin
        self.login_user(user=self.user_admin)

        # Make put request and ensure moved permanently response
        response = self.client.put(self.data_attributes.url_does_not_exist)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_group_duplicate(self):
        # Add new versions, storing URL to be updated
        self.create_data_logout(user=self.user_admin, test_data_attributes=self.data_attributes,
                                request_data=self.data['modified'])
        url = self.create_data_logout(user=self.user_admin, test_data_attributes=self.data_attributes,
                                      request_data=self.data['standard'])

        # Log in as admin
        self.login_user(user=self.user_admin)

        # Make duplicating put and ensure bad request response
        response = self.client.put(url, self.data['modified'])
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue(self.does_contain_data_url(url, self.data['standard']))

    def test_update_group_duplicate_altered_case(self):
        # Add new versions, storing URL to be updated
        self.create_data_logout(user=self.user_admin, test_data_attributes=self.data_attributes,
                                request_data=self.data['standard'])
        url = self.create_data_logout(user=self.user_admin, test_data_attributes=self.data_attributes,
                                      request_data=self.data['modified'])

        # Log in as admin
        self.login_user(user=self.user_admin)

        # Make duplicating put and ensure bad request response
        response = self.client.put(url, self.data.altered_case)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue(self.does_contain_data_url(url, self.data['modified']))

    """
    Delete tests
    """

    def test_delete_group_as_user(self):
        # Add new version, storing URL
        url = self.create_data_logout(user=self.user_admin, test_data_attributes=self.data_attributes,
                                      request_data=self.data['standard'])

        # Log in as standard
        self.login_user(user=self.user_standard)

        # Make delete and ensure unauthorised response
        response = self.client.delete(url)
        self.assertIn(response.status_code, self.status_forbidden)
        self.assertEqual(self.data_attributes.query_set.count(), 1)

    def test_delete_group_as_admin(self):
        # Add new version, storing URL
        url = self.create_data_logout(user=self.user_admin, test_data_attributes=self.data_attributes,
                                      request_data=self.data['standard'])

        # Log in as admin
        self.login_user(user=self.user_admin)

        # Make delete and ensure no content response
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(self.data_attributes.query_set.count(), 0)

    def test_delete_group_unauthenticated(self):
        # Add new version, storing URL
        url = self.create_data_logout(user=self.user_admin, test_data_attributes=self.data_attributes,
                                      request_data=self.data['standard'])

        # Make delete and ensure unauthorised response
        response = self.client.delete(url)
        self.assertIn(response.status_code, self.status_forbidden)
        self.assertEqual(self.data_attributes.query_set.count(), 1)

    def test_delete_group_does_not_exist(self):
        # Log in as admin
        self.login_user(user=self.user_admin)

        # Make delete and ensure not found response
        response = self.client.delete(self.data_attributes.url_does_not_exist)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
