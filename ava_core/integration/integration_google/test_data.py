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
    """
    Test data for GoogleIntegrationAdapter
    """

    @staticmethod
    def init_requirements(owner):
        pass

    # Store self information
    model = GoogleIntegrationAdapter
    url = 'example/'

    standard = {
        'google_integration_history': 'example//1/',
        'description': 'standard_char',
        'domain': 'standard_char',
        'integrationadapter_ptr': 'default',
    }

    unique = {
        'google_integration_history': 'example//2/',
        'description': 'unique_char',
        'domain': 'unique_char',
        'integrationadapter_ptr': 'default',
    }
