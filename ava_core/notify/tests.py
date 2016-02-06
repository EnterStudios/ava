# Rest Imports
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
        pass

    def test_notification_email_create_as_admin(self):
        pass

    def test_notification_email_create_as_unauthenticated(self):
        pass

    def test_notification_email_retrieve_single_as_user(self):
        pass

    def test_notification_email_retrieve_all_as_user(self):
        pass

    def test_notification_email_retrieve_single_as_admin(self):
        pass

    def test_notification_email_retrieve_all_as_admin(self):
        pass

    def test_notification_email_retrieve_single_as_unauthorized(self):
        pass

    def test_notification_email_retrieve_all_as_unauthorized(self):
        pass

    def test_notification_email_update_exists_as_user(self):
        pass

    def test_notification_email_update_does_not_exist_as_user(self):
        pass

    def test_notification_email_update_exists_as_admin(self):
        pass

    def test_notification_email_update_does_not_exist_as_admin(self):
        pass

    def test_notification_email_update_exists_as_unauthorized(self):
        pass

    def test_notification_email_update_does_not_exist_as_unauthorized(self):
        pass

    def test_notification_email_delete_exists_as_user(self):
        pass

    def test_notification_email_delete_does_not_exist_as_user(self):
        pass

    def test_notification_email_delete_exists_as_admin(self):
        pass

    def test_notification_email_delete_does_not_exist_as_admin(self):
        pass

    def test_notification_email_delete_exists_as_unauthorized(self):
        pass

    def test_notification_email_delete_does_not_exist_as_unauthorized(self):
        pass

        # TODO:    Write delete owner tests
