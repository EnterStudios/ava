# Rest Imports
from rest_framework import status
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.gather.gather_abstract.models import GatherHistory
from ava_core.gather.gather_abstract.test_data import GatherHistoryTestData
from ava_core.integration.integration_ldap.models import LDAPIntegrationAdapter
from ava_core.integration.integration_ldap.test_data import LDAPIntegrationAdapterTestData
from ava_core.gather.gather_ldap.models import LDAPGatherHistory


# Implementation
class LDAPGatherHistoryTestData(AvaCoreTestData):
    """
    Test data for LDAPGatherHistory
    """

    def __init__(self):
        # Store self information
        self.model = LDAPGatherHistory
        self.url = '/example'

        # Create any necessary required models.
        self.init_requirements()

    def init_requirements(self):
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if LDAPIntegrationAdapter.objects.count() == 0:
            LDAPIntegrationAdapterTestData.init_requirements()
            LDAPIntegrationAdapter.objects.create(**LDAPIntegrationAdapterTestData.get_data('standard'))
            LDAPIntegrationAdapter.objects.create(**LDAPIntegrationAdapterTestData.get_data('unique'))
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if GatherHistory.objects.count() == 0:
            GatherHistoryTestData.init_requirements()
            GatherHistory.objects.create(**GatherHistoryTestData.get_data('standard'))
            GatherHistory.objects.create(**GatherHistoryTestData.get_data('unique'))

    standard = {
        'integration': '/example/1/',
        'gatherhistory_ptr': 'default',
    }

    unique = {
        'integration': '/example/2/',
        'gatherhistory_ptr': 'default',
    }

    missing_integration = {
        'gatherhistory_ptr': 'default',
    }
    modified_integration = {
        'integration': '/example/2/',
        'gatherhistory_ptr': 'default',
    }

    missing_gatherhistory_ptr = {
        'integration': '/example/1/',
    }
    modified_gatherhistory_ptr = {
        'integration': '/example/1/',
        'gatherhistory_ptr': 'default',
    }




