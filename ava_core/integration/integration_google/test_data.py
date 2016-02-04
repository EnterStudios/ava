# Rest Imports
from rest_framework import status
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.integration.integration_google.models import GoogleAuthorizationStore, GoogleIntegrationAdapter


# Implementation
class GoogleAuthorizationStoreTestData(AvaCoreTestData):
    """
    Test data for GoogleAuthorizationStore
    """

    @staticmethod
    def init_requirements():
        pass

    # Store self information
    model = GoogleAuthorizationStore
    url = '/example'

    standard = {
        'integration_id': 12345,
    }

    unique = {
        'integration_id': 54321,
    }

    modified_integration_id = {
        'integration_id': 54321,
    }
    missing_integration_id = {
    }



class GoogleIntegrationAdapterTestData(AvaCoreTestData):
    """
    Test data for GoogleIntegrationAdapter
    """

    @staticmethod
    def init_requirements():
        # Import the required model and data
        from ava_core.gather.gather_google.models import GoogleGatherHistory
        from ava_core.gather.gather_google.test_data import GoogleGatherHistoryTestData
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if GoogleGatherHistory.objects.count() == 0:
            GoogleGatherHistoryTestData.init_requirements()
            model = GoogleGatherHistory.objects.create(**GoogleGatherHistoryTestData.get_data('standard'))
            model.save()
            model = GoogleGatherHistory.objects.create(**GoogleGatherHistoryTestData.get_data('unique'))
            model.save()

        # Import the required model and data
        from ava_core.integration.integration_abstract.models import IntegrationAdapter
        from ava_core.integration.integration_abstract.test_data import IntegrationAdapterTestData
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if IntegrationAdapter.objects.count() == 0:
            IntegrationAdapterTestData.init_requirements()
            model = IntegrationAdapter.objects.create(**IntegrationAdapterTestData.get_data('standard'))
            model.save()
            model = IntegrationAdapter.objects.create(**IntegrationAdapterTestData.get_data('unique'))
            model.save()

    # Store self information
    model = GoogleIntegrationAdapter
    url = '/example'

    standard = {
        'google_integration_history': '/example/1/',
        'domain': 'standard_char',
        'integrationadapter_ptr': 'default',
        'description': 'standard_char',
    }

    unique = {
        'google_integration_history': '/example/2/',
        'domain': 'unique_char',
        'integrationadapter_ptr': 'default',
        'description': 'unique_char',
    }

    modified_google_integration_history = {
        'google_integration_history': '/example/2/',
        'domain': 'standard_char',
        'integrationadapter_ptr': 'default',
        'description': 'standard_char',
    }
    missing_google_integration_history = {
        'domain': 'standard_char',
        'integrationadapter_ptr': 'default',
        'description': 'standard_char',
    }

    missing_domain = {
        'google_integration_history': '/example/1/',
        'integrationadapter_ptr': 'default',
        'description': 'standard_char',
    }
    modified_domain = {
        'google_integration_history': '/example/1/',
        'domain': 'modified_char',
        'integrationadapter_ptr': 'default',
        'description': 'standard_char',
    }

    modified_integrationadapter_ptr = {
        'google_integration_history': '/example/1/',
        'domain': 'standard_char',
        'integrationadapter_ptr': 'default',
        'description': 'standard_char',
    }
    missing_integrationadapter_ptr = {
        'google_integration_history': '/example/1/',
        'domain': 'standard_char',
        'description': 'standard_char',
    }

    modified_description = {
        'google_integration_history': '/example/1/',
        'domain': 'standard_char',
        'integrationadapter_ptr': 'default',
        'description': 'modified_char',
    }
    missing_description = {
        'google_integration_history': '/example/1/',
        'domain': 'standard_char',
        'integrationadapter_ptr': 'default',
    }




