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
    url = 'notify/'

    standard = {
        'name': 'standard_char',
        'notification_type': 0,
        'description': 'standard_text',
        'subject': 'standard_char',
        'address_from': 'standard_char',
        'body': 'standard_text',
    }

    unique = {
        'name': 'unique_char',
        'notification_type': 5,
        'description': 'unique_text',
        'subject': 'unique_char',
        'address_from': 'unique_char',
        'body': 'unique_text',
    }

    modified_name = {
        'name': 'modified_char',
        'notification_type': 0,
        'description': 'standard_text',
        'subject': 'standard_char',
        'address_from': 'standard_char',
        'body': 'standard_text',
    }
    missing_name = {
        'notification_type': 0,
        'description': 'standard_text',
        'subject': 'standard_char',
        'address_from': 'standard_char',
        'body': 'standard_text',
    }

    modified_notification_type = {
        'name': 'standard_char',
        'notification_type': 5,
        'description': 'standard_text',
        'subject': 'standard_char',
        'address_from': 'standard_char',
        'body': 'standard_text',
    }
    missing_notification_type = {
        'name': 'standard_char',
        'description': 'standard_text',
        'subject': 'standard_char',
        'address_from': 'standard_char',
        'body': 'standard_text',
    }

    missing_description = {
        'name': 'standard_char',
        'notification_type': 0,
        'subject': 'standard_char',
        'address_from': 'standard_char',
        'body': 'standard_text',
    }
    modified_description = {
        'name': 'standard_char',
        'notification_type': 0,
        'description': 'modified_text',
        'subject': 'standard_char',
        'address_from': 'standard_char',
        'body': 'standard_text',
    }

    modified_subject = {
        'name': 'standard_char',
        'notification_type': 0,
        'description': 'standard_text',
        'subject': 'modified_char',
        'address_from': 'standard_char',
        'body': 'standard_text',
    }
    missing_subject = {
        'name': 'standard_char',
        'notification_type': 0,
        'description': 'standard_text',
        'address_from': 'standard_char',
        'body': 'standard_text',
    }

    missing_address_from = {
        'name': 'standard_char',
        'notification_type': 0,
        'description': 'standard_text',
        'subject': 'standard_char',
        'body': 'standard_text',
    }
    modified_address_from = {
        'name': 'standard_char',
        'notification_type': 0,
        'description': 'standard_text',
        'subject': 'standard_char',
        'address_from': 'modified_char',
        'body': 'standard_text',
    }

    missing_body = {
        'name': 'standard_char',
        'notification_type': 0,
        'description': 'standard_text',
        'subject': 'standard_char',
        'address_from': 'standard_char',
    }
    modified_body = {
        'name': 'standard_char',
        'notification_type': 0,
        'description': 'standard_text',
        'subject': 'standard_char',
        'address_from': 'standard_char',
        'body': 'modified_text',
    }




