# Rest Imports
# Local Imports
from ava_core.abstract.test import AvaCoreTest
from ava_core.integration.integration_office365.test_data import Office365AuthorizationStoreTestData, \
    Office365IntegrationAdapterTestData


# Implementation
class Office365AuthorizationStoreTest(AvaCoreTest):
    """
    Office365AuthorizationStore Test
    """

    def setUp(self):
        # Make call to super.
        super(Office365AuthorizationStoreTest, self).setUp()

        # Set the data type.
        self.data = Office365AuthorizationStoreTestData()

    def test_office365_authorization_create_as_user(self):
        self.assertEqual(1,"Test not written")


class Office365IntegrationAdapterTest(AvaCoreTest):
    """
    Office365IntegrationAdapter Test
    """

    def setUp(self):
        # Make call to super.
        super(Office365IntegrationAdapterTest, self).setUp()

        # Set the data type.
        self.data = Office365IntegrationAdapterTestData()

    def test_office365_integration_create_as_user(self):
        self.assertEqual(1,"Test not written")

    def test_office365_integration_create_as_admin(self):
        self.assertEqual(1,"Test not written")

    def test_office365_integration_create_as_unauthenticated(self):
        self.assertEqual(1,"Test not written")

    def test_office365_integration_retrieve_single_as_user(self):
        self.assertEqual(1,"Test not written")

    def test_office365_integration_retrieve_all_as_user(self):
        self.assertEqual(1,"Test not written")

    def test_office365_integration_retrieve_single_as_admin(self):
        self.assertEqual(1,"Test not written")

    def test_office365_integration_retrieve_all_as_admin(self):
        self.assertEqual(1,"Test not written")

    def test_office365_integration_retrieve_single_as_unauthorized(self):
        self.assertEqual(1,"Test not written")

    def test_office365_integration_retrieve_all_as_unauthorized(self):
        self.assertEqual(1,"Test not written")

    def test_office365_integration_update_exists_as_user(self):
        self.assertEqual(1,"Test not written")

    def test_office365_integration_update_does_not_exist_as_user(self):
        self.assertEqual(1,"Test not written")

    def test_office365_integration_update_exists_as_admin(self):
        self.assertEqual(1,"Test not written")

    def test_office365_integration_update_does_not_exist_as_admin(self):
        self.assertEqual(1,"Test not written")

    def test_office365_integration_update_exists_as_unauthorized(self):
        self.assertEqual(1,"Test not written")

    def test_office365_integration_update_does_not_exist_as_unauthorized(self):
        self.assertEqual(1,"Test not written")

    def test_office365_integration_delete_exists_as_user(self):
        self.assertEqual(1,"Test not written")

    def test_office365_integration_delete_does_not_exist_as_user(self):
        self.assertEqual(1,"Test not written")

    def test_office365_integration_delete_exists_as_admin(self):
        self.assertEqual(1,"Test not written")

    def test_office365_integration_delete_does_not_exist_as_admin(self):
        self.assertEqual(1,"Test not written")

    def test_office365_integration_delete_exists_as_unauthorized(self):
        self.assertEqual(1,"Test not written")

    def test_office365_integration_delete_does_not_exist_as_unauthorized(self):
        self.assertEqual(1,"Test not written")
