# Rest Imports
# Local Imports
from ava_core.abstract.test_data import AvaTestData
from ava_core.gather.gather_google.models import GoogleGatherHistory


# Implementation
class GoogleGatherHistoryTestData(AvaTestData):
    """
    Test data for GoogleGatherHistory
    """

    model = GoogleGatherHistory
    url = '/example'

    standard = {
        'integration': 'REQUIRES: ava_core.integration.integration_google.models.GoogleIntegrationAdapter',
        'gatherhistory_ptr': 'default',
    }

    modified = {
        'integration': 'REQUIRES: ava_core.integration.integration_google.models.GoogleIntegrationAdapter',
        'gatherhistory_ptr': 'default',
    }

    missing_integration = {
        'gatherhistory_ptr': 'default',
    }

    modified_integration = {
        'integration': 'REQUIRES: ava_core.integration.integration_google.models.GoogleIntegrationAdapter',
        'gatherhistory_ptr': 'default',
    }

    modified_gatherhistory_ptr = {
        'integration': 'REQUIRES: ava_core.integration.integration_google.models.GoogleIntegrationAdapter',
        'gatherhistory_ptr': 'default',
    }

    missing_gatherhistory_ptr = {
        'integration': 'REQUIRES: ava_core.integration.integration_google.models.GoogleIntegrationAdapter',
    }




