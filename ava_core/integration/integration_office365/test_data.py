# Rest Imports
from rest_framework import status
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.integration.integration_office365.models import Office365IntegrationAdapter, Office365AuthorizationStore


# Implementation
class Office365IntegrationAdapterTestData(AvaCoreTestData):
    """
    Test data for Office365IntegrationAdapter
    """

    @staticmethod
    def init_requirements():
        # Import the required model and data
        from ava_core.gather.gather_office365.models import Office365GatherHistory
        from ava_core.gather.gather_office365.test_data import Office365GatherHistoryTestData
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if Office365GatherHistory.objects.count() == 0:
            Office365GatherHistoryTestData.init_requirements()
            model = Office365GatherHistory.objects.create(**Office365GatherHistoryTestData.get_data('standard'))
            model.save()
            model = Office365GatherHistory.objects.create(**Office365GatherHistoryTestData.get_data('unique'))
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
    model = Office365IntegrationAdapter
    url = '/example'

    standard = {
        'office365_integration_history': '/example/1/',
        'domain': 'standard_char',
        'integrationadapter_ptr': 'default',
        'description': 'standard_char',
    }

    unique = {
        'office365_integration_history': '/example/2/',
        'domain': 'unique_char',
        'integrationadapter_ptr': 'default',
        'description': 'unique_char',
    }

    modified_office365_integration_history = {
        'office365_integration_history': '/example/2/',
        'domain': 'standard_char',
        'integrationadapter_ptr': 'default',
        'description': 'standard_char',
    }
    missing_office365_integration_history = {
        'domain': 'standard_char',
        'integrationadapter_ptr': 'default',
        'description': 'standard_char',
    }

    missing_domain = {
        'office365_integration_history': '/example/1/',
        'integrationadapter_ptr': 'default',
        'description': 'standard_char',
    }
    modified_domain = {
        'office365_integration_history': '/example/1/',
        'domain': 'modified_char',
        'integrationadapter_ptr': 'default',
        'description': 'standard_char',
    }

    modified_integrationadapter_ptr = {
        'office365_integration_history': '/example/1/',
        'domain': 'standard_char',
        'integrationadapter_ptr': 'default',
        'description': 'standard_char',
    }
    missing_integrationadapter_ptr = {
        'office365_integration_history': '/example/1/',
        'domain': 'standard_char',
        'description': 'standard_char',
    }

    modified_description = {
        'office365_integration_history': '/example/1/',
        'domain': 'standard_char',
        'integrationadapter_ptr': 'default',
        'description': 'modified_char',
    }
    missing_description = {
        'office365_integration_history': '/example/1/',
        'domain': 'standard_char',
        'integrationadapter_ptr': 'default',
    }



class Office365AuthorizationStoreTestData(AvaCoreTestData):
    """
    Test data for Office365AuthorizationStore
    """

    @staticmethod
    def init_requirements():
        pass

    # Store self information
    model = Office365AuthorizationStore
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




