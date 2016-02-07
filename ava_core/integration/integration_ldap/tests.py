# Rest Imports
# Local Imports
from ava_core.abstract.test import AvaCoreTest
from ava_core.integration.integration_ldap.test_data import LDAPIntegrationAdapterTestData


# Implementation
class LDAPIntegrationAdapterTest(AvaCoreTest):
    """
    LDAPIntegrationAdapter Test
    """

    def setUp(self):
        # Make call to super.
        super(LDAPIntegrationAdapterTest, self).setUp()

        # Set the data type.
        self.data = LDAPIntegrationAdapterTestData()

    def test_ldap_integration_create_as_user(self):
        self.assertEqual(1,"Test not written")

    def test_ldap_integration_create_as_admin(self):
        self.assertEqual(1,"Test not written")

    def test_ldap_integration_create_as_unauthenticated(self):
        self.assertEqual(1,"Test not written")

    def test_ldap_integration_retrieve_single_as_user(self):
        self.assertEqual(1,"Test not written")

    def test_ldap_integration_retrieve_all_as_user(self):
        self.assertEqual(1,"Test not written")

    def test_ldap_integration_retrieve_single_as_admin(self):
        self.assertEqual(1,"Test not written")

    def test_ldap_integration_retrieve_all_as_admin(self):
        self.assertEqual(1,"Test not written")

    def test_ldap_integration_retrieve_single_as_unauthorized(self):
        self.assertEqual(1,"Test not written")

    def test_ldap_integration_retrieve_all_as_unauthorized(self):
        self.assertEqual(1,"Test not written")

    def test_ldap_integration_update_exists_as_user(self):
        self.assertEqual(1,"Test not written")

    def test_ldap_integration_update_does_not_exist_as_user(self):
        self.assertEqual(1,"Test not written")

    def test_ldap_integration_update_exists_as_admin(self):
        self.assertEqual(1,"Test not written")

    def test_ldap_integration_update_does_not_exist_as_admin(self):
        self.assertEqual(1,"Test not written")

    def test_ldap_integration_update_exists_as_unauthorized(self):
        self.assertEqual(1,"Test not written")

    def test_ldap_integration_update_does_not_exist_as_unauthorized(self):
        self.assertEqual(1,"Test not written")

    def test_ldap_integration_delete_exists_as_user(self):
        self.assertEqual(1,"Test not written")

    def test_ldap_integration_delete_does_not_exist_as_user(self):
        self.assertEqual(1,"Test not written")

    def test_ldap_integration_delete_exists_as_admin(self):
        self.assertEqual(1,"Test not written")

    def test_ldap_integration_delete_does_not_exist_as_admin(self):
        self.assertEqual(1,"Test not written")

    def test_ldap_integration_delete_exists_as_unauthorized(self):
        self.assertEqual(1,"Test not written")

    def test_ldap_integration_delete_does_not_exist_as_unauthorized(self):
        self.assertEqual(1,"Test not written")
