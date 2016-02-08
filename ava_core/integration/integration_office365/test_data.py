# Rest Imports
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.integration.integration_office365.models import Office365AuthorizationStore, Office365IntegrationAdapter


# Implementation
class Office365AuthorizationStoreTestData(AvaCoreTestData):
    """
    Test data for Office365AuthorizationStore
    """

    @staticmethod
    def init_requirements(owner):
        pass

    # Store self information
    model = Office365AuthorizationStore
    url = 'example/'

    standard = {
        'integration_id': 12345,
    }

    unique = {
        'integration_id': 54321,
    }


class Office365IntegrationAdapterTestData(AvaCoreTestData):
    """
    Test data for Office365IntegrationAdapter
    """

    @staticmethod
    def init_requirements(owner):
        pass

    # Store self information
    model = Office365IntegrationAdapter
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
