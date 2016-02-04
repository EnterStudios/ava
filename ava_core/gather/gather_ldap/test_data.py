# Rest Imports
from rest_framework import status
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.gather.gather_ldap.models import LDAPGatherHistory


# Implementation
class LDAPGatherHistoryTestData(AvaCoreTestData):
    """
    Test data for LDAPGatherHistory
    """

    @staticmethod
    def init_requirements():
        # Import the required model and data
        from ava_core.integration.integration_ldap.models import LDAPIntegrationAdapter
        from ava_core.integration.integration_ldap.test_data import LDAPIntegrationAdapterTestData
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if LDAPIntegrationAdapter.objects.count() == 0:
            LDAPIntegrationAdapterTestData.init_requirements()
            model = LDAPIntegrationAdapter.objects.create(**LDAPIntegrationAdapterTestData.get_data('standard'))
            model.save()
            model = LDAPIntegrationAdapter.objects.create(**LDAPIntegrationAdapterTestData.get_data('unique'))
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
    model = LDAPGatherHistory
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




