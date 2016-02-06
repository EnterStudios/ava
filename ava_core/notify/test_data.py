# Rest Imports
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
