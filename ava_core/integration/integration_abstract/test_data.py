# Rest Imports
from rest_framework import status
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.integration.integration_abstract.models import IntegrationAdapter


# Implementation
class IntegrationAdapterTestData(AvaCoreTestData):
    """
    Test data for IntegrationAdapter
    """

    @staticmethod
    def init_requirements(owner):
        pass

    # Store self information
    model = IntegrationAdapter
    url = 'example/'

    standard = {
        'name': 'standard_char',
        'credential': 'default',
        'googleintegrationadapter': 'default',
        'ldapintegrationadapter': 'default',
        'office365integrationadapter': 'default',
    }

    unique = {
        'name': 'unique_char',
        'credential': 'default',
        'googleintegrationadapter': 'default',
        'ldapintegrationadapter': 'default',
        'office365integrationadapter': 'default',
    }
