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

    modified_google_integration_history = {
        'google_integration_history': 'example//2/',
        'description': 'standard_char',
        'domain': 'standard_char',
        'integrationadapter_ptr': 'default',
    }
    missing_google_integration_history = {
        'description': 'standard_char',
        'domain': 'standard_char',
        'integrationadapter_ptr': 'default',
    }

    missing_description = {
        'google_integration_history': 'example//1/',
        'domain': 'standard_char',
        'integrationadapter_ptr': 'default',
    }
    modified_description = {
        'google_integration_history': 'example//1/',
        'description': 'modified_char',
        'domain': 'standard_char',
        'integrationadapter_ptr': 'default',
    }

    modified_domain = {
        'google_integration_history': 'example//1/',
        'description': 'standard_char',
        'domain': 'modified_char',
        'integrationadapter_ptr': 'default',
    }
    missing_domain = {
        'google_integration_history': 'example//1/',
        'description': 'standard_char',
        'integrationadapter_ptr': 'default',
    }

    missing_integrationadapter_ptr = {
        'google_integration_history': 'example//1/',
        'description': 'standard_char',
        'domain': 'standard_char',
    }
    modified_integrationadapter_ptr = {
        'google_integration_history': 'example//1/',
        'description': 'standard_char',
        'domain': 'standard_char',
        'integrationadapter_ptr': 'default',
    }




