# Rest Imports
# Local Imports
from ava_core.abstract.test_data import AvaTestData
from ava_core.gather.gather_ldap.models import LDAPGatherHistory


# Implementation
class LDAPGatherHistoryTestData(AvaTestData):
    """
    Test data for LDAPGatherHistory
    """

    model = LDAPGatherHistory
    url = '/example'

    standard = {
        'integration': 'REQUIRES: ava_core.integration.integration_ldap.models.LDAPIntegrationAdapter',
        'gatherhistory_ptr': 'default',
    }

    modified = {
        'integration': 'REQUIRES: ava_core.integration.integration_ldap.models.LDAPIntegrationAdapter',
        'gatherhistory_ptr': 'default',
    }

    missing_integration = {
        'gatherhistory_ptr': 'default',
    }

    modified_integration = {
        'integration': 'REQUIRES: ava_core.integration.integration_ldap.models.LDAPIntegrationAdapter',
        'gatherhistory_ptr': 'default',
    }

    modified_gatherhistory_ptr = {
        'integration': 'REQUIRES: ava_core.integration.integration_ldap.models.LDAPIntegrationAdapter',
        'gatherhistory_ptr': 'default',
    }

    missing_gatherhistory_ptr = {
        'integration': 'REQUIRES: ava_core.integration.integration_ldap.models.LDAPIntegrationAdapter',
    }




