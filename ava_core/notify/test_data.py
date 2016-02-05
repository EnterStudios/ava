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

    @staticmethod
    def init_requirements(owner):
        pass

    # Store self information
    model = NotificationEmail
    url = 'example/'

    standard = {
        'subject': 'standard_char',
        'address_from': 'standard_char',
        'body': 'standard_text',
        'notification_type': 0,
        'description': 'standard_text',
        'name': 'standard_char',
    }

    unique = {
        'subject': 'unique_char',
        'address_from': 'unique_char',
        'body': 'unique_text',
        'notification_type': 5,
        'description': 'unique_text',
        'name': 'unique_char',
    }

    modified_subject = {
        'subject': 'modified_char',
        'address_from': 'standard_char',
        'body': 'standard_text',
        'notification_type': 0,
        'description': 'standard_text',
        'name': 'standard_char',
    }
    missing_subject = {
        'address_from': 'standard_char',
        'body': 'standard_text',
        'notification_type': 0,
        'description': 'standard_text',
        'name': 'standard_char',
    }

    modified_address_from = {
        'subject': 'standard_char',
        'address_from': 'modified_char',
        'body': 'standard_text',
        'notification_type': 0,
        'description': 'standard_text',
        'name': 'standard_char',
    }
    missing_address_from = {
        'subject': 'standard_char',
        'body': 'standard_text',
        'notification_type': 0,
        'description': 'standard_text',
        'name': 'standard_char',
    }

    missing_body = {
        'subject': 'standard_char',
        'address_from': 'standard_char',
        'notification_type': 0,
        'description': 'standard_text',
        'name': 'standard_char',
    }
    modified_body = {
        'subject': 'standard_char',
        'address_from': 'standard_char',
        'body': 'modified_text',
        'notification_type': 0,
        'description': 'standard_text',
        'name': 'standard_char',
    }

    missing_notification_type = {
        'subject': 'standard_char',
        'address_from': 'standard_char',
        'body': 'standard_text',
        'description': 'standard_text',
        'name': 'standard_char',
    }
    modified_notification_type = {
        'subject': 'standard_char',
        'address_from': 'standard_char',
        'body': 'standard_text',
        'notification_type': 5,
        'description': 'standard_text',
        'name': 'standard_char',
    }

    missing_description = {
        'subject': 'standard_char',
        'address_from': 'standard_char',
        'body': 'standard_text',
        'notification_type': 0,
        'name': 'standard_char',
    }
    modified_description = {
        'subject': 'standard_char',
        'address_from': 'standard_char',
        'body': 'standard_text',
        'notification_type': 0,
        'description': 'modified_text',
        'name': 'standard_char',
    }

    modified_name = {
        'subject': 'standard_char',
        'address_from': 'standard_char',
        'body': 'standard_text',
        'notification_type': 0,
        'description': 'standard_text',
        'name': 'modified_char',
    }
    missing_name = {
        'subject': 'standard_char',
        'address_from': 'standard_char',
        'body': 'standard_text',
        'notification_type': 0,
        'description': 'standard_text',
    }




