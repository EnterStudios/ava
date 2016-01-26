# Rest Imports
# Local Imports
from ava_core.abstract.test_data import AvaTestData
from ava_core.integration.integration_google.models import GoogleIntegrationAdapter, GoogleAuthorizationStore


# Implementation
class GoogleIntegrationAdapterTestData(AvaTestData):
    """
    Test data for GoogleIntegrationAdapter
    """

    model = GoogleIntegrationAdapter
    url = '/example'

    standard = {
        'integrationadapter_ptr': 'default',
        'domain': 'standard_char',
        'google_integration_history': 'REQUIRES: ava_core.gather.gather_google.models.GoogleGatherHistory',
        'description': 'standard_char',
    }

    modified = {
        'integrationadapter_ptr': 'default',
        'domain': 'standard_char',
        'google_integration_history': 'REQUIRES: ava_core.gather.gather_google.models.GoogleGatherHistory',
        'description': 'standard_char',
    }

    modified_integrationadapter_ptr = {
        'integrationadapter_ptr': 'default',
        'domain': 'standard_char',
        'google_integration_history': 'REQUIRES: ava_core.gather.gather_google.models.GoogleGatherHistory',
        'description': 'standard_char',
    }

    missing_integrationadapter_ptr = {
        'domain': 'standard_char',
        'google_integration_history': 'REQUIRES: ava_core.gather.gather_google.models.GoogleGatherHistory',
        'description': 'standard_char',
    }

    modified_domain = {
        'integrationadapter_ptr': 'default',
        'domain': 'modified_char',
        'google_integration_history': 'REQUIRES: ava_core.gather.gather_google.models.GoogleGatherHistory',
        'description': 'standard_char',
    }

    missing_domain = {
        'integrationadapter_ptr': 'default',
        'google_integration_history': 'REQUIRES: ava_core.gather.gather_google.models.GoogleGatherHistory',
        'description': 'standard_char',
    }

    missing_google_integration_history = {
        'integrationadapter_ptr': 'default',
        'domain': 'standard_char',
        'description': 'standard_char',
    }

    modified_google_integration_history = {
        'integrationadapter_ptr': 'default',
        'domain': 'standard_char',
        'google_integration_history': 'REQUIRES: ava_core.gather.gather_google.models.GoogleGatherHistory',
        'description': 'standard_char',
    }

    modified_description = {
        'integrationadapter_ptr': 'default',
        'domain': 'standard_char',
        'google_integration_history': 'REQUIRES: ava_core.gather.gather_google.models.GoogleGatherHistory',
        'description': 'modified_char',
    }

    missing_description = {
        'integrationadapter_ptr': 'default',
        'domain': 'standard_char',
        'google_integration_history': 'REQUIRES: ava_core.gather.gather_google.models.GoogleGatherHistory',
    }



class GoogleAuthorizationStoreTestData(AvaTestData):
    """
    Test data for GoogleAuthorizationStore
    """

    model = GoogleAuthorizationStore
    url = '/example'

    standard = {
        'integration_id': 12345,
    }

    modified = {
        'integration_id': 12345,
    }

    missing_integration_id = {
    }

    modified_integration_id = {
        'integration_id': 54321,
    }




