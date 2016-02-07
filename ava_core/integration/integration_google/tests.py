# Rest Imports
# Local Imports
from ava_core.abstract.test import AvaCoreTest
from ava_core.integration.integration_google.test_data import GoogleAuthorizationStoreTestData, \
    GoogleIntegrationAdapterTestData


# Implementation
class GoogleAuthorizationStoreTest(AvaCoreTest):
    """
    GoogleAuthorizationStore Test
    """

    def setUp(self):
        # Make call to super.
        super(GoogleAuthorizationStoreTest, self).setUp()

        # Set the data type.
        self.data = GoogleAuthorizationStoreTestData()

    def test_google_authorization_store_create_as_user(self):
        self.assertEqual(1,"Test not written")


class GoogleIntegrationAdapterTest(AvaCoreTest):
    """
    GoogleIntegrationAdapter Test
    """

    def setUp(self):
        # Make call to super.
        super(GoogleIntegrationAdapterTest, self).setUp()

        # Set the data type.
        self.data = GoogleIntegrationAdapterTestData()

    def test_google_integration_create_as_user(self):
        self.assertEqual(1,"Test not written")

    def test_google_integration_create_as_admin(self):
        self.assertEqual(1,"Test not written")

    def test_google_integration_create_as_unauthenticated(self):
        self.assertEqual(1,"Test not written")

    def test_google_integration_retrieve_single_as_user(self):
        self.assertEqual(1,"Test not written")

    def test_google_integration_retrieve_all_as_user(self):
        self.assertEqual(1,"Test not written")

    def test_google_integration_retrieve_single_as_admin(self):
        self.assertEqual(1,"Test not written")

    def test_google_integration_retrieve_all_as_admin(self):
        self.assertEqual(1,"Test not written")

    def test_google_integration_retrieve_single_as_unauthorized(self):
        self.assertEqual(1,"Test not written")

    def test_google_integration_retrieve_all_as_unauthorized(self):
        self.assertEqual(1,"Test not written")

    def test_google_integration_update_exists_as_user(self):
        self.assertEqual(1,"Test not written")

    def test_google_integration_update_does_not_exist_as_user(self):
        self.assertEqual(1,"Test not written")

    def test_google_integration_update_exists_as_admin(self):
        self.assertEqual(1,"Test not written")

    def test_google_integration_update_does_not_exist_as_admin(self):
        self.assertEqual(1,"Test not written")

    def test_google_integration_update_exists_as_unauthorized(self):
        self.assertEqual(1,"Test not written")

    def test_google_integration_update_does_not_exist_as_unauthorized(self):
        self.assertEqual(1,"Test not written")

    def test_google_integration_delete_exists_as_user(self):
        self.assertEqual(1,"Test not written")

    def test_google_integration_delete_does_not_exist_as_user(self):
        self.assertEqual(1,"Test not written")

    def test_google_integration_delete_exists_as_admin(self):
        self.assertEqual(1,"Test not written")

    def test_google_integration_delete_does_not_exist_as_admin(self):
        self.assertEqual(1,"Test not written")

    def test_google_integration_delete_exists_as_unauthorized(self):
        self.assertEqual(1,"Test not written")

    def test_google_integration_delete_does_not_exist_as_unauthorized(self):
        self.assertEqual(1,"Test not written")
