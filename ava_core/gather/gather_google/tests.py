# Rest Imports
from rest_framework import status
# Local Imports
from ava_core.abstract.test import AvaCoreTest
from ava_core.gather.gather_google.test_data import GoogleGatherHistoryTestData


# Implementation
class GoogleGatherTest(AvaCoreTest):

    def setUp(self):
        pass
        # # Make call to super.
        # super(GoogleGatherTest, self).setUp()
        #
        # # Set the data type.
        # self.data = GoogleGatherTestData()

    def test_google_gather_import(self):
        pass

# Implementation
class GoogleGatherHistoryTest(AvaCoreTest):
    """
    GoogleGatherHistory Test
    """

    def setUp(self):
        # Make call to super.
        super(GoogleGatherHistoryTest, self).setUp()

        # Set the data type.
        self.data = GoogleGatherHistoryTestData()

    def test_google_gather_history_create_as_user(self):
        pass

    def test_google_gather_history_create_as_admin(self):
        pass

    def test_google_gather_history_create_as_unauthenticated(self):
        pass

    def test_google_gather_history_retrieve_single_as_user(self):
        pass

    def test_google_gather_history_retrieve_all_as_user(self):
        pass
    
    def test_google_gather_history_retrieve_single_as_admin(self):
        pass

    def test_google_gather_history_retrieve_all_as_admin(self):
        pass

    def test_google_gather_history_retrieve_single_as_unauthorized(self):
        pass

    def test_google_gather_history_retrieve_all_as_unauthorized(self):
        pass

    def test_google_gather_history_update_exists_as_user(self):
        pass
 
    def test_google_gather_history_update_does_not_exist_as_user(self):
        pass

    def test_google_gather_history_update_exists_as_admin(self):
        pass

    def test_google_gather_history_update_does_not_exist_as_admin(self):
        pass

    def test_google_gather_history_update_exists_as_unauthorized(self):
        pass

    def test_google_gather_history_update_does_not_exist_as_unauthorized(self):
        pass
       
    def test_google_gather_history_delete_exists_as_user(self):
        pass

    def test_google_gather_history_delete_does_not_exist_as_user(self):
        pass

    def test_google_gather_history_delete_exists_as_admin(self):
        pass
       
    def test_google_gather_history_delete_does_not_exist_as_admin(self):
        pass

    def test_google_gather_history_delete_exists_as_unauthorized(self):
        pass

    def test_google_gather_history_delete_does_not_exist_as_unauthorized(self):
        pass

