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
    def init_requirements():
        # Import the required model and data
        from ava_core.integration.integration_google.models import GoogleIntegrationAdapter
        from ava_core.integration.integration_google.test_data import GoogleIntegrationAdapterTestData
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if GoogleIntegrationAdapter.objects.count() == 0:
            GoogleIntegrationAdapterTestData.init_requirements()
            model = GoogleIntegrationAdapter.objects.create(**GoogleIntegrationAdapterTestData.get_data('standard'))
            model.save()
            model = GoogleIntegrationAdapter.objects.create(**GoogleIntegrationAdapterTestData.get_data('unique'))
            model.save()

        # Import the required model and data
        from ava_core.gather.gather_abstract.models import GatherHistory
        from ava_core.gather.gather_abstract.test_data import GatherHistoryTestData
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if GatherHistory.objects.count() == 0:
            GatherHistoryTestData.init_requirements()
            model = GatherHistory.objects.create(**GatherHistoryTestData.get_data('standard'))
            model.save()
            model = GatherHistory.objects.create(**GatherHistoryTestData.get_data('unique'))
            model.save()

    # Store self information
    model = GoogleGatherHistory
    url = '/example'

    standard = {
        'integration': '/example/1/',
        'gatherhistory_ptr': 'default',
    }

    unique = {
        'integration': '/example/2/',
        'gatherhistory_ptr': 'default',
    }

    modified_integration = {
        'integration': '/example/2/',
        'gatherhistory_ptr': 'default',
    }
    missing_integration = {
        'gatherhistory_ptr': 'default',
    }

    modified_gatherhistory_ptr = {
        'integration': '/example/1/',
        'gatherhistory_ptr': 'default',
    }
    missing_gatherhistory_ptr = {
        'integration': '/example/1/',
    }




