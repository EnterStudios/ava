# Rest Imports
# Local Imports
from ava_core.abstract.test import AvaCoreTest
from ava_core.gather.gather_office365.test_data import Office365GatherHistoryTestData


# Implementation
class Office365GatherTest(AvaCoreTest):

    def setUp(self):
        pass
        # # Make call to super.
        # super(Office365GatherHistoryTest, self).setUp()
        #
        # # Set the data type.
        # self.data = Office365GatherHistoryTestData()

    def test_office365_gather_import(self):
        self.assertEqual(1,"Test not written")


# Implementation
class Office365GatherHistoryTest(AvaCoreTest):
    """
    Office365GatherHistory Test
    """

    def setUp(self):
        # Make call to super.
        super(Office365GatherHistoryTest, self).setUp()

        # Set the data type.
        self.data = Office365GatherHistoryTestData()

    def test_office365_gather_history_create_as_user(self):
        self.assertEqual(1,"Test not written")

    def test_office365_gather_history_create_as_admin(self):
        self.assertEqual(1,"Test not written")

    def test_office365_gather_history_create_as_unauthenticated(self):
        self.assertEqual(1,"Test not written")

    def test_office365_gather_history_retrieve_single_as_user(self):
        self.assertEqual(1,"Test not written")

    def test_office365_gather_history_retrieve_all_as_user(self):
        self.assertEqual(1,"Test not written")

    def test_office365_gather_history_retrieve_single_as_admin(self):
        self.assertEqual(1,"Test not written")

    def test_office365_gather_history_retrieve_all_as_admin(self):
        self.assertEqual(1,"Test not written")

    def test_office365_gather_history_retrieve_single_as_unauthorized(self):
        self.assertEqual(1,"Test not written")

    def test_office365_gather_history_retrieve_all_as_unauthorized(self):
        self.assertEqual(1,"Test not written")

    def test_office365_gather_history_update_exists_as_user(self):
        self.assertEqual(1,"Test not written")

    def test_office365_gather_history_update_does_not_exist_as_user(self):
        self.assertEqual(1,"Test not written")

    def test_office365_gather_history_update_exists_as_admin(self):
        self.assertEqual(1,"Test not written")

    def test_office365_gather_history_update_does_not_exist_as_admin(self):
        self.assertEqual(1,"Test not written")

    def test_office365_gather_history_update_exists_as_unauthorized(self):
        self.assertEqual(1,"Test not written")

    def test_office365_gather_history_update_does_not_exist_as_unauthorized(self):
        self.assertEqual(1,"Test not written")

    def test_office365_gather_history_delete_exists_as_user(self):
        self.assertEqual(1,"Test not written")

    def test_office365_gather_history_delete_does_not_exist_as_user(self):
        self.assertEqual(1,"Test not written")

    def test_office365_gather_history_delete_exists_as_admin(self):
        self.assertEqual(1,"Test not written")

    def test_office365_gather_history_delete_does_not_exist_as_admin(self):
        self.assertEqual(1,"Test not written")

    def test_office365_gather_history_delete_exists_as_unauthorized(self):
        self.assertEqual(1,"Test not written")

    def test_office365_gather_history_delete_does_not_exist_as_unauthorized(self):
        self.assertEqual(1,"Test not written")
