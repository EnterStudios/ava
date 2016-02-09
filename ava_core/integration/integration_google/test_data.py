# Rest Imports
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.integration.integration_google.models import GoogleAuthorizationStore, GoogleIntegrationAdapter


# Implementation
class GoogleAuthorizationStoreTestData(AvaCoreTestData):
    """
    Test data for GoogleAuthorizationStore
    """

    @staticmethod
    def init_requirements(owner):
        pass

    # Store self information
    model = GoogleAuthorizationStore
    url = 'example/'

    standard = {
        'integration_id': 12345,
    }

    unique = {
        'integration_id': 54321,
    }


class GoogleIntegrationAdapterTestData(AvaCoreTestData):

    # Store self information
    model = GoogleIntegrationAdapter
    url = 'example/'

    standard = {
        'name': 'standard_char',
        'description': 'standard_char',
        'domain': 'http://www.example.com',
        'credential': 'standard_char',
    }

    unique = {
        'name': 'unique_char',
        'description': 'unique_char',
        'domain': 'http://www.example.com',
        'credential': 'unique_char',
    }

