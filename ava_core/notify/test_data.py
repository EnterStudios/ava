# Rest Imports
from rest_framework import status
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.notify.models import NotificationEmail


# Implementation
class NotificationEmailTestData(AvaCoreTestData):
    """
    Test data for NotificationEmail
    """

    def __init__(self):
        # Store self information
        self.model = NotificationEmail
        self.url = '/example'

        # Create any necessary required models.
        self.init_requirements()

    def init_requirements(self):
        pass

    standard = {
        'notification_type': 0,
        'address_from': 'standard_char',
        'description': 'standard_text',
        'subject': 'standard_char',
        'name': 'standard_char',
        'body': 'standard_text',
    }

    unique = {
        'notification_type': 5,
        'address_from': 'unique_char',
        'description': 'unique_text',
        'subject': 'unique_char',
        'name': 'unique_char',
        'body': 'unique_text',
    }

    modified_notification_type = {
        'notification_type': 5,
        'address_from': 'standard_char',
        'description': 'standard_text',
        'subject': 'standard_char',
        'name': 'standard_char',
        'body': 'standard_text',
    }
    missing_notification_type = {
        'address_from': 'standard_char',
        'description': 'standard_text',
        'subject': 'standard_char',
        'name': 'standard_char',
        'body': 'standard_text',
    }

    missing_address_from = {
        'notification_type': 0,
        'description': 'standard_text',
        'subject': 'standard_char',
        'name': 'standard_char',
        'body': 'standard_text',
    }
    modified_address_from = {
        'notification_type': 0,
        'address_from': 'modified_char',
        'description': 'standard_text',
        'subject': 'standard_char',
        'name': 'standard_char',
        'body': 'standard_text',
    }

    missing_description = {
        'notification_type': 0,
        'address_from': 'standard_char',
        'subject': 'standard_char',
        'name': 'standard_char',
        'body': 'standard_text',
    }
    modified_description = {
        'notification_type': 0,
        'address_from': 'standard_char',
        'description': 'modified_text',
        'subject': 'standard_char',
        'name': 'standard_char',
        'body': 'standard_text',
    }

    modified_subject = {
        'notification_type': 0,
        'address_from': 'standard_char',
        'description': 'standard_text',
        'subject': 'modified_char',
        'name': 'standard_char',
        'body': 'standard_text',
    }
    missing_subject = {
        'notification_type': 0,
        'address_from': 'standard_char',
        'description': 'standard_text',
        'name': 'standard_char',
        'body': 'standard_text',
    }

    modified_name = {
        'notification_type': 0,
        'address_from': 'standard_char',
        'description': 'standard_text',
        'subject': 'standard_char',
        'name': 'modified_char',
        'body': 'standard_text',
    }
    missing_name = {
        'notification_type': 0,
        'address_from': 'standard_char',
        'description': 'standard_text',
        'subject': 'standard_char',
        'body': 'standard_text',
    }

    missing_body = {
        'notification_type': 0,
        'address_from': 'standard_char',
        'description': 'standard_text',
        'subject': 'standard_char',
        'name': 'standard_char',
    }
    modified_body = {
        'notification_type': 0,
        'address_from': 'standard_char',
        'description': 'standard_text',
        'subject': 'standard_char',
        'name': 'standard_char',
        'body': 'modified_text',
    }




