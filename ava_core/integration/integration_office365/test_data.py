# Rest Imports
from rest_framework import status
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

    missing_integration_id = {
    }
    modified_integration_id = {
        'integration_id': 54321,
    }



class Office365IntegrationAdapterTestData(AvaCoreTestData):
    """
    Test data for Office365IntegrationAdapter
    """

    @staticmethod
    def init_requirements(owner):
        # Import the required model and data
        from ava_core.gather.gather_office365.models import Office365GatherHistory
        from ava_core.gather.gather_office365.test_data import Office365GatherHistoryTestData
        # Grab data for object creation, with owner if required.
        data_model = Office365GatherHistoryTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = Office365GatherHistory.objects.filter(owner=owner['email']) if 'email' in standard_data else Office365GatherHistory.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            Office365GatherHistoryTestData.init_requirements(owner)
            model = Office365GatherHistory.objects.create(**standard_data)
            model = Office365GatherHistory.objects.create(**unique_data)

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
    model = Office365IntegrationAdapter
    url = 'example/'

    standard = {
        'office365_integration_history': 'example//1/',
        'description': 'standard_char',
        'domain': 'standard_char',
        'integrationadapter_ptr': 'default',
    }

    unique = {
        'office365_integration_history': 'example//2/',
        'description': 'unique_char',
        'domain': 'unique_char',
        'integrationadapter_ptr': 'default',
    }

    missing_office365_integration_history = {
        'description': 'standard_char',
        'domain': 'standard_char',
        'integrationadapter_ptr': 'default',
    }
    modified_office365_integration_history = {
        'office365_integration_history': 'example//2/',
        'description': 'standard_char',
        'domain': 'standard_char',
        'integrationadapter_ptr': 'default',
    }

    missing_description = {
        'office365_integration_history': 'example//1/',
        'domain': 'standard_char',
        'integrationadapter_ptr': 'default',
    }
    modified_description = {
        'office365_integration_history': 'example//1/',
        'description': 'modified_char',
        'domain': 'standard_char',
        'integrationadapter_ptr': 'default',
    }

    modified_domain = {
        'office365_integration_history': 'example//1/',
        'description': 'standard_char',
        'domain': 'modified_char',
        'integrationadapter_ptr': 'default',
    }
    missing_domain = {
        'office365_integration_history': 'example//1/',
        'description': 'standard_char',
        'integrationadapter_ptr': 'default',
    }

    missing_integrationadapter_ptr = {
        'office365_integration_history': 'example//1/',
        'description': 'standard_char',
        'domain': 'standard_char',
    }
    modified_integrationadapter_ptr = {
        'office365_integration_history': 'example//1/',
        'description': 'standard_char',
        'domain': 'standard_char',
        'integrationadapter_ptr': 'default',
    }




