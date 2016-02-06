# Rest Imports
# Local Imports
from ava_core.abstract.test import AvaCoreTest
from ava_core.gather.gather_abstract.test_data import GatherHistoryTestData


# Implementation
class GatherHistoryTest(AvaCoreTest):
    """
    GatherHistory Test
    """

    def setUp(self):
        # Make call to super.
        super(GatherHistoryTest, self).setUp()

        # Set the data type.
        self.data = GatherHistoryTestData()

    def test_gather_history_create_as_user(self):
        pass

    def test_gather_history_create_as_admin(self):
        pass

    def test_gather_history_create_as_unauthenticated(self):
        pass

    def test_gather_history_retrieve_single_as_user(self):
        pass

    def test_gather_history_retrieve_all_as_user(self):
        pass

    def test_gather_history_retrieve_single_as_admin(self):
        pass

    def test_gather_history_retrieve_all_as_admin(self):
        pass

    def test_gather_history_retrieve_single_as_unauthorized(self):
        pass

    def test_gather_history_retrieve_all_as_unauthorized(self):
        pass

    def test_gather_history_update_exists_as_user(self):
        pass

    def test_gather_history_update_does_not_exist_as_user(self):
        pass

    def test_gather_history_update_exists_as_admin(self):
        pass

    def test_gather_history_update_does_not_exist_as_admin(self):
        pass

    def test_gather_history_update_exists_as_unauthorized(self):
        pass

    def test_gather_history_update_does_not_exist_as_unauthorized(self):
        pass

    def test_gather_history_delete_does_not_exist_as_user(self):
        pass

    def test_gather_history_delete_exists_as_admin(self):
        pass

    def test_gather_history_delete_does_not_exist_as_admin(self):
        pass

    def test_gather_history_delete_exists_as_unauthorized(self):
        pass

    def test_gather_history_delete_does_not_exist_as_unauthorized(self):
        pass
