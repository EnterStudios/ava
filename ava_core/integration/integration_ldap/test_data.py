# Rest Imports
from rest_framework import status
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.integration.integration_ldap.models import LDAPIntegrationAdapter


# Implementation
class LDAPIntegrationAdapterTestData(AvaCoreTestData):
    """
    Test data for LDAPIntegrationAdapter
    """

    @staticmethod
    def init_requirements():
        # Import the required model and data
        from ava_core.gather.gather_ldap.models import LDAPGatherHistory
        from ava_core.gather.gather_ldap.test_data import LDAPGatherHistoryTestData
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if LDAPGatherHistory.objects.count() == 0:
            LDAPGatherHistoryTestData.init_requirements()
            model = LDAPGatherHistory.objects.create(**LDAPGatherHistoryTestData.get_data('standard'))
            model.save()
            model = LDAPGatherHistory.objects.create(**LDAPGatherHistoryTestData.get_data('unique'))
            model.save()

        # Import the required model and data
        from ava_core.integration.integration_abstract.models import IntegrationAdapter
        from ava_core.integration.integration_abstract.test_data import IntegrationAdapterTestData
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if IntegrationAdapter.objects.count() == 0:
            IntegrationAdapterTestData.init_requirements()
            model = IntegrationAdapter.objects.create(**IntegrationAdapterTestData.get_data('standard'))
            model.save()
            model = IntegrationAdapter.objects.create(**IntegrationAdapterTestData.get_data('unique'))
            model.save()

    # Store self information
    model = LDAPIntegrationAdapter
    url = '/example'

    standard = {
        'ldap_password': 'standard_char',
        'salt': 'standard_char',
        'dump_dn': 'standard_char',
        'ldap_user': 'standard_char',
        'ldap_integration_history': '/example/1/',
        'integrationadapter_ptr': 'default',
        'server': 'standard_char',
    }

    unique = {
        'ldap_password': 'unique_char',
        'salt': 'unique_char',
        'dump_dn': 'unique_char',
        'ldap_user': 'unique_char',
        'ldap_integration_history': '/example/2/',
        'integrationadapter_ptr': 'default',
        'server': 'unique_char',
    }

    missing_ldap_password = {
        'salt': 'standard_char',
        'dump_dn': 'standard_char',
        'ldap_user': 'standard_char',
        'ldap_integration_history': '/example/1/',
        'integrationadapter_ptr': 'default',
        'server': 'standard_char',
    }
    modified_ldap_password = {
        'ldap_password': 'modified_char',
        'salt': 'standard_char',
        'dump_dn': 'standard_char',
        'ldap_user': 'standard_char',
        'ldap_integration_history': '/example/1/',
        'integrationadapter_ptr': 'default',
        'server': 'standard_char',
    }

    modified_salt = {
        'ldap_password': 'standard_char',
        'salt': 'modified_char',
        'dump_dn': 'standard_char',
        'ldap_user': 'standard_char',
        'ldap_integration_history': '/example/1/',
        'integrationadapter_ptr': 'default',
        'server': 'standard_char',
    }
    missing_salt = {
        'ldap_password': 'standard_char',
        'dump_dn': 'standard_char',
        'ldap_user': 'standard_char',
        'ldap_integration_history': '/example/1/',
        'integrationadapter_ptr': 'default',
        'server': 'standard_char',
    }

    modified_dump_dn = {
        'ldap_password': 'standard_char',
        'salt': 'standard_char',
        'dump_dn': 'modified_char',
        'ldap_user': 'standard_char',
        'ldap_integration_history': '/example/1/',
        'integrationadapter_ptr': 'default',
        'server': 'standard_char',
    }
    missing_dump_dn = {
        'ldap_password': 'standard_char',
        'salt': 'standard_char',
        'ldap_user': 'standard_char',
        'ldap_integration_history': '/example/1/',
        'integrationadapter_ptr': 'default',
        'server': 'standard_char',
    }

    missing_ldap_user = {
        'ldap_password': 'standard_char',
        'salt': 'standard_char',
        'dump_dn': 'standard_char',
        'ldap_integration_history': '/example/1/',
        'integrationadapter_ptr': 'default',
        'server': 'standard_char',
    }
    modified_ldap_user = {
        'ldap_password': 'standard_char',
        'salt': 'standard_char',
        'dump_dn': 'standard_char',
        'ldap_user': 'modified_char',
        'ldap_integration_history': '/example/1/',
        'integrationadapter_ptr': 'default',
        'server': 'standard_char',
    }

    modified_ldap_integration_history = {
        'ldap_password': 'standard_char',
        'salt': 'standard_char',
        'dump_dn': 'standard_char',
        'ldap_user': 'standard_char',
        'ldap_integration_history': '/example/2/',
        'integrationadapter_ptr': 'default',
        'server': 'standard_char',
    }
    missing_ldap_integration_history = {
        'ldap_password': 'standard_char',
        'salt': 'standard_char',
        'dump_dn': 'standard_char',
        'ldap_user': 'standard_char',
        'integrationadapter_ptr': 'default',
        'server': 'standard_char',
    }

    modified_integrationadapter_ptr = {
        'ldap_password': 'standard_char',
        'salt': 'standard_char',
        'dump_dn': 'standard_char',
        'ldap_user': 'standard_char',
        'ldap_integration_history': '/example/1/',
        'integrationadapter_ptr': 'default',
        'server': 'standard_char',
    }
    missing_integrationadapter_ptr = {
        'ldap_password': 'standard_char',
        'salt': 'standard_char',
        'dump_dn': 'standard_char',
        'ldap_user': 'standard_char',
        'ldap_integration_history': '/example/1/',
        'server': 'standard_char',
    }

    missing_server = {
        'ldap_password': 'standard_char',
        'salt': 'standard_char',
        'dump_dn': 'standard_char',
        'ldap_user': 'standard_char',
        'ldap_integration_history': '/example/1/',
        'integrationadapter_ptr': 'default',
    }
    modified_server = {
        'ldap_password': 'standard_char',
        'salt': 'standard_char',
        'dump_dn': 'standard_char',
        'ldap_user': 'standard_char',
        'ldap_integration_history': '/example/1/',
        'integrationadapter_ptr': 'default',
        'server': 'modified_char',
    }




