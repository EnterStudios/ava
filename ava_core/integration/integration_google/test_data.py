# Rest Imports
from rest_framework import status
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.gather.gather_google.models import GoogleGatherHistory
from ava_core.gather.gather_google.test_data import GoogleGatherHistoryTestData
from ava_core.integration.integration_google.models import GoogleAuthorizationStore, GoogleIntegrationAdapter
from ava_core.integration.integration_abstract.models import IntegrationAdapter
from ava_core.integration.integration_abstract.test_data import IntegrationAdapterTestData


# Implementation
class GoogleAuthorizationStoreTestData(AvaCoreTestData):
    """
    Test data for GoogleAuthorizationStore
    """

    def __init__(self):
        # Store self information
        self.model = GoogleAuthorizationStore
        self.url = '/example'

        # Create any necessary required models.
        self.init_requirements()

    def init_requirements(self):
        pass

    standard = {
        'integration_id': 12345,
    }

    unique = {
        'integration_id': 54321,
    }

    missing_integration_id = {
    }
    modified_integration_id = {
        'integration_id': 54321,
    }



class GoogleIntegrationAdapterTestData(AvaCoreTestData):
    """
    Test data for GoogleIntegrationAdapter
    """

    def __init__(self):
        # Store self information
        self.model = GoogleIntegrationAdapter
        self.url = '/example'

        # Create any necessary required models.
        self.init_requirements()

    def init_requirements(self):
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if GoogleGatherHistory.objects.count() == 0:
            GoogleGatherHistoryTestData.init_requirements()
            GoogleGatherHistory.objects.create(**GoogleGatherHistoryTestData.get_data('standard'))
            GoogleGatherHistory.objects.create(**GoogleGatherHistoryTestData.get_data('unique'))
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if IntegrationAdapter.objects.count() == 0:
            IntegrationAdapterTestData.init_requirements()
            IntegrationAdapter.objects.create(**IntegrationAdapterTestData.get_data('standard'))
            IntegrationAdapter.objects.create(**IntegrationAdapterTestData.get_data('unique'))

    standard = {
        'google_integration_history': '/example/1/',
        'description': 'standard_char',
        'integrationadapter_ptr': 'default',
        'domain': 'standard_char',
    }

    unique = {
        'google_integration_history': '/example/2/',
        'description': 'unique_char',
        'integrationadapter_ptr': 'default',
        'domain': 'unique_char',
    }

    missing_google_integration_history = {
        'description': 'standard_char',
        'integrationadapter_ptr': 'default',
        'domain': 'standard_char',
    }
    modified_google_integration_history = {
        'google_integration_history': '/example/2/',
        'description': 'standard_char',
        'integrationadapter_ptr': 'default',
        'domain': 'standard_char',
    }

    missing_description = {
        'google_integration_history': '/example/1/',
        'integrationadapter_ptr': 'default',
        'domain': 'standard_char',
    }
    modified_description = {
        'google_integration_history': '/example/1/',
        'description': 'modified_char',
        'integrationadapter_ptr': 'default',
        'domain': 'standard_char',
    }

    missing_integrationadapter_ptr = {
        'google_integration_history': '/example/1/',
        'description': 'standard_char',
        'domain': 'standard_char',
    }
    modified_integrationadapter_ptr = {
        'google_integration_history': '/example/1/',
        'description': 'standard_char',
        'integrationadapter_ptr': 'default',
        'domain': 'standard_char',
    }

    modified_domain = {
        'google_integration_history': '/example/1/',
        'description': 'standard_char',
        'integrationadapter_ptr': 'default',
        'domain': 'modified_char',
    }
    missing_domain = {
        'google_integration_history': '/example/1/',
        'description': 'standard_char',
        'integrationadapter_ptr': 'default',
    }




