# Rest Imports
from rest_framework import status
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.gather.gather_office365.models import Office365GatherHistory


# Implementation
class Office365GatherHistoryTestData(AvaCoreTestData):
    """
    Test data for Office365GatherHistory
    """

    @staticmethod
    def init_requirements():
        # Import the required model and data
        from ava_core.integration.integration_office365.models import Office365IntegrationAdapter
        from ava_core.integration.integration_office365.test_data import Office365IntegrationAdapterTestData
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if Office365IntegrationAdapter.objects.count() == 0:
            Office365IntegrationAdapterTestData.init_requirements()
            model = Office365IntegrationAdapter.objects.create(**Office365IntegrationAdapterTestData.get_data('standard'))
            model.save()
            model = Office365IntegrationAdapter.objects.create(**Office365IntegrationAdapterTestData.get_data('unique'))
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
    model = Office365GatherHistory
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




