# Rest Imports
from rest_framework import status
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.integration.integration_google.models import GoogleIntegrationAdapter, GoogleAuthorizationStore


# Implementation
class GoogleIntegrationAdapterTestData(AvaCoreTestData):
    """
    Test data for GoogleIntegrationAdapter
    """

    @staticmethod
    def init_requirements(owner):
        # Import the required model and data
        from ava_core.gather.gather_google.models import GoogleGatherHistory
        from ava_core.gather.gather_google.test_data import GoogleGatherHistoryTestData
        # Grab data for object creation, with owner if required.
        data_model = GoogleGatherHistoryTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = GoogleGatherHistory.objects.filter(owner=owner['email']) if 'email' in standard_data else GoogleGatherHistory.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            GoogleGatherHistoryTestData.init_requirements(owner)
            model = GoogleGatherHistory.objects.create(**standard_data)
            model = GoogleGatherHistory.objects.create(**unique_data)

        # Import the required model and data
        from ava_core.integration.integration_abstract.models import IntegrationAdapter
        from ava_core.integration.integration_abstract.test_data import IntegrationAdapterTestData
        # Grab data for object creation, with owner if required.
        data_model = IntegrationAdapterTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = IntegrationAdapter.objects.filter(owner=owner['email']) if 'email' in standard_data else IntegrationAdapter.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            IntegrationAdapterTestData.init_requirements(owner)
            model = IntegrationAdapter.objects.create(**standard_data)
            model = IntegrationAdapter.objects.create(**unique_data)

    # Store self information
    model = GoogleIntegrationAdapter
    url = 'example/'

    standard = {
        'domain': 'standard_char',
        'google_integration_history': 'example//1/',
        'integrationadapter_ptr': 'default',
        'description': 'standard_char',
    }

    unique = {
        'domain': 'unique_char',
        'google_integration_history': 'example//2/',
        'integrationadapter_ptr': 'default',
        'description': 'unique_char',
    }

    missing_domain = {
        'google_integration_history': 'example//1/',
        'integrationadapter_ptr': 'default',
        'description': 'standard_char',
    }
    modified_domain = {
        'domain': 'modified_char',
        'google_integration_history': 'example//1/',
        'integrationadapter_ptr': 'default',
        'description': 'standard_char',
    }

    missing_google_integration_history = {
        'domain': 'standard_char',
        'integrationadapter_ptr': 'default',
        'description': 'standard_char',
    }
    modified_google_integration_history = {
        'domain': 'standard_char',
        'google_integration_history': 'example//2/',
        'integrationadapter_ptr': 'default',
        'description': 'standard_char',
    }

    missing_integrationadapter_ptr = {
        'domain': 'standard_char',
        'google_integration_history': 'example//1/',
        'description': 'standard_char',
    }
    modified_integrationadapter_ptr = {
        'domain': 'standard_char',
        'google_integration_history': 'example//1/',
        'integrationadapter_ptr': 'default',
        'description': 'standard_char',
    }

    missing_description = {
        'domain': 'standard_char',
        'google_integration_history': 'example//1/',
        'integrationadapter_ptr': 'default',
    }
    modified_description = {
        'domain': 'standard_char',
        'google_integration_history': 'example//1/',
        'integrationadapter_ptr': 'default',
        'description': 'modified_char',
    }



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

    missing_integration_id = {
    }
    modified_integration_id = {
        'integration_id': 54321,
    }




