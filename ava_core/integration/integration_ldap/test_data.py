# Rest Imports
from rest_framework import status
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.integration.integration_abstract.models import IntegrationAdapter
from ava_core.integration.integration_abstract.test_data import IntegrationAdapterTestData
from ava_core.integration.integration_ldap.models import LDAPIntegrationAdapter
from ava_core.gather.gather_ldap.models import LDAPGatherHistory
from ava_core.gather.gather_ldap.test_data import LDAPGatherHistoryTestData


# Implementation
class LDAPIntegrationAdapterTestData(AvaCoreTestData):
    """
    Test data for LDAPIntegrationAdapter
    """

    def __init__(self):
        # Store self information
        self.model = LDAPIntegrationAdapter
        self.url = '/example'

        # Create any necessary required models.
        self.init_requirements()

    def init_requirements(self):
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if LDAPGatherHistory.objects.count() == 0:
            LDAPGatherHistoryTestData.init_requirements()
            LDAPGatherHistory.objects.create(**LDAPGatherHistoryTestData.get_data('standard'))
            LDAPGatherHistory.objects.create(**LDAPGatherHistoryTestData.get_data('unique'))
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if IntegrationAdapter.objects.count() == 0:
            IntegrationAdapterTestData.init_requirements()
            IntegrationAdapter.objects.create(**IntegrationAdapterTestData.get_data('standard'))
            IntegrationAdapter.objects.create(**IntegrationAdapterTestData.get_data('unique'))

    standard = {
        'ldap_integration_history': '/example/1/',
        'server': 'standard_char',
        'dump_dn': 'standard_char',
        'ldap_password': 'standard_char',
        'integrationadapter_ptr': 'default',
        'ldap_user': 'standard_char',
        'salt': 'standard_char',
    }

    unique = {
        'ldap_integration_history': '/example/2/',
        'server': 'unique_char',
        'dump_dn': 'unique_char',
        'ldap_password': 'unique_char',
        'integrationadapter_ptr': 'default',
        'ldap_user': 'unique_char',
        'salt': 'unique_char',
    }

    missing_ldap_integration_history = {
        'server': 'standard_char',
        'dump_dn': 'standard_char',
        'ldap_password': 'standard_char',
        'integrationadapter_ptr': 'default',
        'ldap_user': 'standard_char',
        'salt': 'standard_char',
    }
    modified_ldap_integration_history = {
        'ldap_integration_history': '/example/2/',
        'server': 'standard_char',
        'dump_dn': 'standard_char',
        'ldap_password': 'standard_char',
        'integrationadapter_ptr': 'default',
        'ldap_user': 'standard_char',
        'salt': 'standard_char',
    }

    modified_server = {
        'ldap_integration_history': '/example/1/',
        'server': 'modified_char',
        'dump_dn': 'standard_char',
        'ldap_password': 'standard_char',
        'integrationadapter_ptr': 'default',
        'ldap_user': 'standard_char',
        'salt': 'standard_char',
    }
    missing_server = {
        'ldap_integration_history': '/example/1/',
        'dump_dn': 'standard_char',
        'ldap_password': 'standard_char',
        'integrationadapter_ptr': 'default',
        'ldap_user': 'standard_char',
        'salt': 'standard_char',
    }

    missing_dump_dn = {
        'ldap_integration_history': '/example/1/',
        'server': 'standard_char',
        'ldap_password': 'standard_char',
        'integrationadapter_ptr': 'default',
        'ldap_user': 'standard_char',
        'salt': 'standard_char',
    }
    modified_dump_dn = {
        'ldap_integration_history': '/example/1/',
        'server': 'standard_char',
        'dump_dn': 'modified_char',
        'ldap_password': 'standard_char',
        'integrationadapter_ptr': 'default',
        'ldap_user': 'standard_char',
        'salt': 'standard_char',
    }

    missing_ldap_password = {
        'ldap_integration_history': '/example/1/',
        'server': 'standard_char',
        'dump_dn': 'standard_char',
        'integrationadapter_ptr': 'default',
        'ldap_user': 'standard_char',
        'salt': 'standard_char',
    }
    modified_ldap_password = {
        'ldap_integration_history': '/example/1/',
        'server': 'standard_char',
        'dump_dn': 'standard_char',
        'ldap_password': 'modified_char',
        'integrationadapter_ptr': 'default',
        'ldap_user': 'standard_char',
        'salt': 'standard_char',
    }

    missing_integrationadapter_ptr = {
        'ldap_integration_history': '/example/1/',
        'server': 'standard_char',
        'dump_dn': 'standard_char',
        'ldap_password': 'standard_char',
        'ldap_user': 'standard_char',
        'salt': 'standard_char',
    }
    modified_integrationadapter_ptr = {
        'ldap_integration_history': '/example/1/',
        'server': 'standard_char',
        'dump_dn': 'standard_char',
        'ldap_password': 'standard_char',
        'integrationadapter_ptr': 'default',
        'ldap_user': 'standard_char',
        'salt': 'standard_char',
    }

    missing_ldap_user = {
        'ldap_integration_history': '/example/1/',
        'server': 'standard_char',
        'dump_dn': 'standard_char',
        'ldap_password': 'standard_char',
        'integrationadapter_ptr': 'default',
        'salt': 'standard_char',
    }
    modified_ldap_user = {
        'ldap_integration_history': '/example/1/',
        'server': 'standard_char',
        'dump_dn': 'standard_char',
        'ldap_password': 'standard_char',
        'integrationadapter_ptr': 'default',
        'ldap_user': 'modified_char',
        'salt': 'standard_char',
    }

    missing_salt = {
        'ldap_integration_history': '/example/1/',
        'server': 'standard_char',
        'dump_dn': 'standard_char',
        'ldap_password': 'standard_char',
        'integrationadapter_ptr': 'default',
        'ldap_user': 'standard_char',
    }
    modified_salt = {
        'ldap_integration_history': '/example/1/',
        'server': 'standard_char',
        'dump_dn': 'standard_char',
        'ldap_password': 'standard_char',
        'integrationadapter_ptr': 'default',
        'ldap_user': 'standard_char',
        'salt': 'modified_char',
    }




