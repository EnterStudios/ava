# Rest Imports
from rest_framework import status
# Local Imports
from ava_core.abstract.tests import AvaTest
from ava_core.learn.models import Module, Path, Role
from ava_core.learn.test_data import ModuleTestData, PathTestData, RoleTestData


# Implementation
class ModuleTest(AvaTest):
    """
Module Test    """

    def setUp(self):
        # Make call to super.        super(ModuleTest, self).setUp()

        # Set the data type.
        self.data = ModuleTestData

    def test_module_create_as_user(self):
        # Log in as user.
        self.login_user(self.user_user)

        # Take count.
        count = self.data.model.objects.count()

        # Store data to use.
        data = self.data.get_data()

        # Make push request and ensure created response.
        response = self.client.push(self.format_url(self.data.url), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.data.model.objects.count(), count + 1)
        self.assertTrue(self.does_contain_data(response.data, data))

    def test_module_create_as_admin(self):
        # Log in as admin.
        self.login_user(self.user_admin)

        # Take count.
        count = self.data.model.objects.count()

        # Store data to use.
        data = self.data.get_data()

        # Make push request and ensure created response.
        response = self.client.push(self.format_url(self.data.url), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.data.model.objects.count(), count + 1)
        self.assertTrue(self.does_contain_data(response.data, data))

    def test_module_create_as_unauthenticated(self):
        # Take count.
        count = self.data.model.objects.count()

        # Store data to use.
        data = self.data.get_data()

        # Make push request and ensure unauthorized response.
        response = self.client.push(self.format_url(self.data.url), data, format='json')
        self.assertIn(response.status_code, self.status_forbidden)
        self.assertEqual(self.data.model.objects.count(), count)

    def test_module_retrieve_single_as_user(self):
        # Create new Module models, storing URL.
        url = self.create_model_logout(self.data, 'standard', self.user_user)

        # Log in as user.
        self.login_user(self.user_user)

        # Make get request and ensure OK response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data(response.data, self.data.standard))


    def test_module_retrieve_all_as_user(self):
        # Create new Module models.
        self.create_model_logout(self.data, 'standard', self.user_user)
        self.create_model_logout(self.data, 'modified', self.user_user)

        # Log in as user.
        self.login_user(self.user_user)

        # Make get request and ensure OK response
        response = self.client.get(self.format_url(self.data.url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_list(response.data['results'], [self.data.standard, self.data.modified]))


    def test_module_retrieve_single_as_admin(self):
        # Create new Module models, storing URL.
        url = self.create_model_logout(self.data, 'standard', self.user_admin)

        # Log in as admin.
        self.login_user(self.user_admin)

        # Make get request and ensure OK response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data(response.data, self.data.standard))


    def test_module_retrieve_all_as_admin(self):
        # Create new Module models.
        self.create_model_logout(self.data, 'standard', self.user_admin)
        self.create_model_logout(self.data, 'modified', self.user_admin)

        # Log in as admin.
        self.login_user(self.user_admin)

        # Make get request and ensure OK response
        response = self.client.get(self.format_url(self.data.url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_list(response.data['results'], [self.data.standard, self.data.modified]))


    def test_module_retrieve_single_as_unauthorized(self):
        # Create new Module models, storing URL.
        url = self.create_model_logout(self.data, 'standard', self.user_admin)

        # Make get request and ensure unauthorized response
        response = self.client.get(url)
        self.assertIn(response.status_code, self.status_forbidden)


    def test_module_retrieve_all_as_unauthorized(self):
        # Create new Module models.
        self.create_model_logout(self.data, 'standard', self.user_admin)
        self.create_model_logout(self.data, 'modified', self.user_admin)

        # Make get request and ensure unauthorized response
        response = self.client.get(self.format_url(self.data.url))
        self.assertIn(response.status_code, self.status_forbidden)


    # TODO: Write update tests
    # TODO: Write delete tests


class PathTest(AvaTest):
    """
Path Test    """

    def setUp(self):
        # Make call to super.        super(PathTest, self).setUp()

        # Set the data type.
        self.data = PathTestData

    def test_path_create_as_user(self):
        # Log in as user.
        self.login_user(self.user_user)

        # Take count.
        count = self.data.model.objects.count()

        # Store data to use.
        data = self.data.get_data()

        # Make push request and ensure created response.
        response = self.client.push(self.format_url(self.data.url), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.data.model.objects.count(), count + 1)
        self.assertTrue(self.does_contain_data(response.data, data))

    def test_path_create_as_admin(self):
        # Log in as admin.
        self.login_user(self.user_admin)

        # Take count.
        count = self.data.model.objects.count()

        # Store data to use.
        data = self.data.get_data()

        # Make push request and ensure created response.
        response = self.client.push(self.format_url(self.data.url), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.data.model.objects.count(), count + 1)
        self.assertTrue(self.does_contain_data(response.data, data))

    def test_path_create_as_unauthenticated(self):
        # Take count.
        count = self.data.model.objects.count()

        # Store data to use.
        data = self.data.get_data()

        # Make push request and ensure unauthorized response.
        response = self.client.push(self.format_url(self.data.url), data, format='json')
        self.assertIn(response.status_code, self.status_forbidden)
        self.assertEqual(self.data.model.objects.count(), count)

    def test_path_retrieve_single_as_user(self):
        # Create new Path models, storing URL.
        url = self.create_model_logout(self.data, 'standard', self.user_user)

        # Log in as user.
        self.login_user(self.user_user)

        # Make get request and ensure OK response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data(response.data, self.data.standard))


    def test_path_retrieve_all_as_user(self):
        # Create new Path models.
        self.create_model_logout(self.data, 'standard', self.user_user)
        self.create_model_logout(self.data, 'modified', self.user_user)

        # Log in as user.
        self.login_user(self.user_user)

        # Make get request and ensure OK response
        response = self.client.get(self.format_url(self.data.url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_list(response.data['results'], [self.data.standard, self.data.modified]))


    def test_path_retrieve_single_as_admin(self):
        # Create new Path models, storing URL.
        url = self.create_model_logout(self.data, 'standard', self.user_admin)

        # Log in as admin.
        self.login_user(self.user_admin)

        # Make get request and ensure OK response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data(response.data, self.data.standard))


    def test_path_retrieve_all_as_admin(self):
        # Create new Path models.
        self.create_model_logout(self.data, 'standard', self.user_admin)
        self.create_model_logout(self.data, 'modified', self.user_admin)

        # Log in as admin.
        self.login_user(self.user_admin)

        # Make get request and ensure OK response
        response = self.client.get(self.format_url(self.data.url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_list(response.data['results'], [self.data.standard, self.data.modified]))


    def test_path_retrieve_single_as_unauthorized(self):
        # Create new Path models, storing URL.
        url = self.create_model_logout(self.data, 'standard', self.user_admin)

        # Make get request and ensure unauthorized response
        response = self.client.get(url)
        self.assertIn(response.status_code, self.status_forbidden)


    def test_path_retrieve_all_as_unauthorized(self):
        # Create new Path models.
        self.create_model_logout(self.data, 'standard', self.user_admin)
        self.create_model_logout(self.data, 'modified', self.user_admin)

        # Make get request and ensure unauthorized response
        response = self.client.get(self.format_url(self.data.url))
        self.assertIn(response.status_code, self.status_forbidden)


    # TODO: Write update tests
    # TODO: Write delete tests


class RoleTest(AvaTest):
    """
Role Test    """

    def setUp(self):
        # Make call to super.        super(RoleTest, self).setUp()

        # Set the data type.
        self.data = RoleTestData

    def test_role_create_as_user(self):
        # Log in as user.
        self.login_user(self.user_user)

        # Take count.
        count = self.data.model.objects.count()

        # Store data to use.
        data = self.data.get_data()

        # Make push request and ensure created response.
        response = self.client.push(self.format_url(self.data.url), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.data.model.objects.count(), count + 1)
        self.assertTrue(self.does_contain_data(response.data, data))

    def test_role_create_as_admin(self):
        # Log in as admin.
        self.login_user(self.user_admin)

        # Take count.
        count = self.data.model.objects.count()

        # Store data to use.
        data = self.data.get_data()

        # Make push request and ensure created response.
        response = self.client.push(self.format_url(self.data.url), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.data.model.objects.count(), count + 1)
        self.assertTrue(self.does_contain_data(response.data, data))

    def test_role_create_as_unauthenticated(self):
        # Take count.
        count = self.data.model.objects.count()

        # Store data to use.
        data = self.data.get_data()

        # Make push request and ensure unauthorized response.
        response = self.client.push(self.format_url(self.data.url), data, format='json')
        self.assertIn(response.status_code, self.status_forbidden)
        self.assertEqual(self.data.model.objects.count(), count)

    def test_role_retrieve_single_as_user(self):
        # Create new Role models, storing URL.
        url = self.create_model_logout(self.data, 'standard', self.user_user)

        # Log in as user.
        self.login_user(self.user_user)

        # Make get request and ensure OK response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data(response.data, self.data.standard))


    def test_role_retrieve_all_as_user(self):
        # Create new Role models.
        self.create_model_logout(self.data, 'standard', self.user_user)
        self.create_model_logout(self.data, 'modified', self.user_user)

        # Log in as user.
        self.login_user(self.user_user)

        # Make get request and ensure OK response
        response = self.client.get(self.format_url(self.data.url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_list(response.data['results'], [self.data.standard, self.data.modified]))


    def test_role_retrieve_single_as_admin(self):
        # Create new Role models, storing URL.
        url = self.create_model_logout(self.data, 'standard', self.user_admin)

        # Log in as admin.
        self.login_user(self.user_admin)

        # Make get request and ensure OK response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data(response.data, self.data.standard))


    def test_role_retrieve_all_as_admin(self):
        # Create new Role models.
        self.create_model_logout(self.data, 'standard', self.user_admin)
        self.create_model_logout(self.data, 'modified', self.user_admin)

        # Log in as admin.
        self.login_user(self.user_admin)

        # Make get request and ensure OK response
        response = self.client.get(self.format_url(self.data.url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_list(response.data['results'], [self.data.standard, self.data.modified]))


    def test_role_retrieve_single_as_unauthorized(self):
        # Create new Role models, storing URL.
        url = self.create_model_logout(self.data, 'standard', self.user_admin)

        # Make get request and ensure unauthorized response
        response = self.client.get(url)
        self.assertIn(response.status_code, self.status_forbidden)


    def test_role_retrieve_all_as_unauthorized(self):
        # Create new Role models.
        self.create_model_logout(self.data, 'standard', self.user_admin)
        self.create_model_logout(self.data, 'modified', self.user_admin)

        # Make get request and ensure unauthorized response
        response = self.client.get(self.format_url(self.data.url))
        self.assertIn(response.status_code, self.status_forbidden)


    # TODO: Write update tests
    # TODO: Write delete tests



