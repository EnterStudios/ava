# Rest Imports
from rest_framework import status
# Local Imports
from ava.abstract.test_data import AvaTestData
from ava_core.notify.models import NotificationEmail


# Implementation
class NotificationEmailTestData(AvaTestData):
    """
    Test data for NotificationEmail
    """

    model = NotificationEmail
    url = '/example'

    standard = {
        'description': 'standard_text',
        'name': 'standard_char',
        'notification_type': 0,
        'body': 'standard_text',
        'subject': 'standard_char',
        'address_from': 'standard_char',
    }

    modified = {
        'description': 'standard_text',
        'name': 'standard_char',
        'notification_type': 0,
        'body': 'standard_text',
        'subject': 'standard_char',
        'address_from': 'standard_char',
    }

    modified_description = {
        'description': 'modified_text',
        'name': 'standard_char',
        'notification_type': 0,
        'body': 'standard_text',
        'subject': 'standard_char',
        'address_from': 'standard_char',
    }

    missing_description = {
        'name': 'standard_char',
        'notification_type': 0,
        'body': 'standard_text',
        'subject': 'standard_char',
        'address_from': 'standard_char',
    }

    modified_name = {
        'description': 'standard_text',
        'name': 'modified_char',
        'notification_type': 0,
        'body': 'standard_text',
        'subject': 'standard_char',
        'address_from': 'standard_char',
    }

    missing_name = {
        'description': 'standard_text',
        'notification_type': 0,
        'body': 'standard_text',
        'subject': 'standard_char',
        'address_from': 'standard_char',
    }

    missing_notification_type = {
        'description': 'standard_text',
        'name': 'standard_char',
        'body': 'standard_text',
        'subject': 'standard_char',
        'address_from': 'standard_char',
    }

    modified_notification_type = {
        'description': 'standard_text',
        'name': 'standard_char',
        'notification_type': 5,
        'body': 'standard_text',
        'subject': 'standard_char',
        'address_from': 'standard_char',
    }

    missing_body = {
        'description': 'standard_text',
        'name': 'standard_char',
        'notification_type': 0,
        'subject': 'standard_char',
        'address_from': 'standard_char',
    }

    modified_body = {
        'description': 'standard_text',
        'name': 'standard_char',
        'notification_type': 0,
        'body': 'modified_text',
        'subject': 'standard_char',
        'address_from': 'standard_char',
    }

    missing_subject = {
        'description': 'standard_text',
        'name': 'standard_char',
        'notification_type': 0,
        'body': 'standard_text',
        'address_from': 'standard_char',
    }

    modified_subject = {
        'description': 'standard_text',
        'name': 'standard_char',
        'notification_type': 0,
        'body': 'standard_text',
        'subject': 'modified_char',
        'address_from': 'standard_char',
    }

    modified_address_from = {
        'description': 'standard_text',
        'name': 'standard_char',
        'notification_type': 0,
        'body': 'standard_text',
        'subject': 'standard_char',
        'address_from': 'modified_char',
    }

    missing_address_from = {
        'description': 'standard_text',
        'name': 'standard_char',
        'notification_type': 0,
        'body': 'standard_text',
        'subject': 'standard_char',
    }




