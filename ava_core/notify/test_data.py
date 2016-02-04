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
    def init_requirements():
        pass

    # Store self information
    model = NotificationEmail
    url = '/example'

    standard = {
        'notification_type': 0,
        'description': 'standard_text',
        'body': 'standard_text',
        'address_from': 'standard_char',
        'subject': 'standard_char',
        'name': 'standard_char',
    }

    unique = {
        'notification_type': 5,
        'description': 'unique_text',
        'body': 'unique_text',
        'address_from': 'unique_char',
        'subject': 'unique_char',
        'name': 'unique_char',
    }

    modified_notification_type = {
        'notification_type': 5,
        'description': 'standard_text',
        'body': 'standard_text',
        'address_from': 'standard_char',
        'subject': 'standard_char',
        'name': 'standard_char',
    }
    missing_notification_type = {
        'description': 'standard_text',
        'body': 'standard_text',
        'address_from': 'standard_char',
        'subject': 'standard_char',
        'name': 'standard_char',
    }

    modified_description = {
        'notification_type': 0,
        'description': 'modified_text',
        'body': 'standard_text',
        'address_from': 'standard_char',
        'subject': 'standard_char',
        'name': 'standard_char',
    }
    missing_description = {
        'notification_type': 0,
        'body': 'standard_text',
        'address_from': 'standard_char',
        'subject': 'standard_char',
        'name': 'standard_char',
    }

    modified_body = {
        'notification_type': 0,
        'description': 'standard_text',
        'body': 'modified_text',
        'address_from': 'standard_char',
        'subject': 'standard_char',
        'name': 'standard_char',
    }
    missing_body = {
        'notification_type': 0,
        'description': 'standard_text',
        'address_from': 'standard_char',
        'subject': 'standard_char',
        'name': 'standard_char',
    }

    modified_address_from = {
        'notification_type': 0,
        'description': 'standard_text',
        'body': 'standard_text',
        'address_from': 'modified_char',
        'subject': 'standard_char',
        'name': 'standard_char',
    }
    missing_address_from = {
        'notification_type': 0,
        'description': 'standard_text',
        'body': 'standard_text',
        'subject': 'standard_char',
        'name': 'standard_char',
    }

    missing_subject = {
        'notification_type': 0,
        'description': 'standard_text',
        'body': 'standard_text',
        'address_from': 'standard_char',
        'name': 'standard_char',
    }
    modified_subject = {
        'notification_type': 0,
        'description': 'standard_text',
        'body': 'standard_text',
        'address_from': 'standard_char',
        'subject': 'modified_char',
        'name': 'standard_char',
    }

    modified_name = {
        'notification_type': 0,
        'description': 'standard_text',
        'body': 'standard_text',
        'address_from': 'standard_char',
        'subject': 'standard_char',
        'name': 'modified_char',
    }
    missing_name = {
        'notification_type': 0,
        'description': 'standard_text',
        'body': 'standard_text',
        'address_from': 'standard_char',
        'subject': 'standard_char',
    }




