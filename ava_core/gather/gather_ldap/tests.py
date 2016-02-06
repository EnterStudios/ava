# Rest Imports
# Local Imports
from ava_core.abstract.test import AvaCoreTest
from ava_core.gather.gather_ldap.test_data import LDAPGatherHistoryTestData


# Implementation
class LDAPGatherTest(AvaCoreTest):

    def setUp(self):
        # Make call to super.
        super(GoogleGatherHistoryTest, self).setUp()

        # Set the data type.
        self.data = GoogleGatherHistoryTestData()

    def test_ldap_gather_import(self):
        pass

# Implementation
class LDAPGatherHistoryTest(AvaCoreTest):
    """
    LDAPGatherHistory Test
    """

    def setUp(self):
        # Make call to super.
        super(LDAPGatherHistoryTest, self).setUp()

        # Set the data type.
        self.data = LDAPGatherHistoryTestData()

    def test_ldap_gather_history_create_as_user(self):
        pass

    def test_ldap_gather_history_create_as_admin(self):
        pass

    def test_ldap_gather_history_create_as_unauthenticated(self):
        pass

    def test_ldap_gather_history_retrieve_single_as_user(self):
        pass

    def test_ldap_gather_history_retrieve_all_as_user(self):
        pass

    def test_ldap_gather_history_retrieve_single_as_admin(self):
        pass

    def test_ldap_gather_history_retrieve_all_as_admin(self):
        pass

    def test_ldap_gather_history_retrieve_single_as_unauthorized(self):
        pass

    def test_ldap_gather_history_retrieve_all_as_unauthorized(self):
        pass

    def test_ldap_gather_history_update_exists_as_user(self):
        pass

    def test_ldap_gather_history_update_does_not_exist_as_user(self):
        pass

    def test_ldap_gather_history_update_exists_as_admin(self):
        pass

    def test_ldap_gather_history_update_does_not_exist_as_admin(self):
        pass

    def test_ldap_gather_history_update_exists_as_unauthorized(self):
        pass

    def test_ldap_gather_history_update_does_not_exist_as_unauthorized(self):
        pass

    def test_ldap_gather_history_delete_exists_as_user(self):
        pass

    def test_ldap_gather_history_delete_does_not_exist_as_user(self):
        pass

    def test_ldap_gather_history_delete_exists_as_admin(self):
        pass

    def test_ldap_gather_history_delete_does_not_exist_as_admin(self):
        pass

    def test_ldap_gather_history_delete_exists_as_unauthorized(self):
        pass

    def test_ldap_gather_history_delete_does_not_exist_as_unauthorized(self):
        pass
