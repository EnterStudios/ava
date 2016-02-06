# Rest Imports
from rest_framework import status
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.gather.gather_google.models import GoogleGatherHistory


# Implementation
class GoogleGatherHistoryTestData(AvaCoreTestData):
    """
    Test data for GoogleGatherHistory
    """

    @staticmethod
    def init_requirements(owner):
        # Import the required model and data
        from ava_core.gather.gather_abstract.models import GatherHistory
        from ava_core.gather.gather_abstract.test_data import GatherHistoryTestData
        # Grab data for object creation, with owner if required.
        data_model = GatherHistoryTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = GatherHistory.objects.filter(owner=owner['email']) if 'email' in standard_data else GatherHistory.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            GatherHistoryTestData.init_requirements(owner)
            model = GatherHistory.objects.create(**standard_data)
            model = GatherHistory.objects.create(**unique_data)

        # Import the required model and data
        from ava_core.integration.integration_google.models import GoogleIntegrationAdapter
        from ava_core.integration.integration_google.test_data import GoogleIntegrationAdapterTestData
        # Grab data for object creation, with owner if required.
        data_model = GoogleIntegrationAdapterTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = GoogleIntegrationAdapter.objects.filter(owner=owner['email']) if 'email' in standard_data else GoogleIntegrationAdapter.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            GoogleIntegrationAdapterTestData.init_requirements(owner)
            model = GoogleIntegrationAdapter.objects.create(**standard_data)
            model = GoogleIntegrationAdapter.objects.create(**unique_data)

    # Store self information
    model = GoogleGatherHistory
    url = 'example/'

    standard = {
        'gatherhistory_ptr': 'default',
        'integration': 'example//1/',
    }

    unique = {
        'gatherhistory_ptr': 'default',
        'integration': 'example//2/',
    }

    missing_gatherhistory_ptr = {
        'integration': 'example//1/',
    }
    modified_gatherhistory_ptr = {
        'gatherhistory_ptr': 'default',
        'integration': 'example//1/',
    }

    missing_integration = {
        'gatherhistory_ptr': 'default',
    }
    modified_integration = {
        'gatherhistory_ptr': 'default',
        'integration': 'example//2/',
    }




