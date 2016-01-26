# Rest Imports
# Local Imports
from ava_core.abstract.test_data import AvaTestData
from ava_core.integration.integration_ldap.models import LDAPIntegrationAdapter


# Implementation
class LDAPIntegrationAdapterTestData(AvaTestData):
    """
    Test data for LDAPIntegrationAdapter
    """

    model = LDAPIntegrationAdapter
    url = '/example'

    standard = {
        'server': 'standard_char',
        'ldap_password': 'standard_char',
        'salt': 'standard_char',
        'integrationadapter_ptr': 'default',
        'dump_dn': 'standard_char',
        'ldap_user': 'standard_char',
        'ldap_integration_history': 'REQUIRES: ava_core.gather.gather_ldap.models.LDAPGatherHistory',
    }

    modified = {
        'server': 'standard_char',
        'ldap_password': 'standard_char',
        'salt': 'standard_char',
        'integrationadapter_ptr': 'default',
        'dump_dn': 'standard_char',
        'ldap_user': 'standard_char',
        'ldap_integration_history': 'REQUIRES: ava_core.gather.gather_ldap.models.LDAPGatherHistory',
    }

    missing_server = {
        'ldap_password': 'standard_char',
        'salt': 'standard_char',
        'integrationadapter_ptr': 'default',
        'dump_dn': 'standard_char',
        'ldap_user': 'standard_char',
        'ldap_integration_history': 'REQUIRES: ava_core.gather.gather_ldap.models.LDAPGatherHistory',
    }

    modified_server = {
        'server': 'modified_char',
        'ldap_password': 'standard_char',
        'salt': 'standard_char',
        'integrationadapter_ptr': 'default',
        'dump_dn': 'standard_char',
        'ldap_user': 'standard_char',
        'ldap_integration_history': 'REQUIRES: ava_core.gather.gather_ldap.models.LDAPGatherHistory',
    }

    missing_ldap_password = {
        'server': 'standard_char',
        'salt': 'standard_char',
        'integrationadapter_ptr': 'default',
        'dump_dn': 'standard_char',
        'ldap_user': 'standard_char',
        'ldap_integration_history': 'REQUIRES: ava_core.gather.gather_ldap.models.LDAPGatherHistory',
    }

    modified_ldap_password = {
        'server': 'standard_char',
        'ldap_password': 'modified_char',
        'salt': 'standard_char',
        'integrationadapter_ptr': 'default',
        'dump_dn': 'standard_char',
        'ldap_user': 'standard_char',
        'ldap_integration_history': 'REQUIRES: ava_core.gather.gather_ldap.models.LDAPGatherHistory',
    }

    missing_salt = {
        'server': 'standard_char',
        'ldap_password': 'standard_char',
        'integrationadapter_ptr': 'default',
        'dump_dn': 'standard_char',
        'ldap_user': 'standard_char',
        'ldap_integration_history': 'REQUIRES: ava_core.gather.gather_ldap.models.LDAPGatherHistory',
    }

    modified_salt = {
        'server': 'standard_char',
        'ldap_password': 'standard_char',
        'salt': 'modified_char',
        'integrationadapter_ptr': 'default',
        'dump_dn': 'standard_char',
        'ldap_user': 'standard_char',
        'ldap_integration_history': 'REQUIRES: ava_core.gather.gather_ldap.models.LDAPGatherHistory',
    }

    modified_integrationadapter_ptr = {
        'server': 'standard_char',
        'ldap_password': 'standard_char',
        'salt': 'standard_char',
        'integrationadapter_ptr': 'default',
        'dump_dn': 'standard_char',
        'ldap_user': 'standard_char',
        'ldap_integration_history': 'REQUIRES: ava_core.gather.gather_ldap.models.LDAPGatherHistory',
    }

    missing_integrationadapter_ptr = {
        'server': 'standard_char',
        'ldap_password': 'standard_char',
        'salt': 'standard_char',
        'dump_dn': 'standard_char',
        'ldap_user': 'standard_char',
        'ldap_integration_history': 'REQUIRES: ava_core.gather.gather_ldap.models.LDAPGatherHistory',
    }

    modified_dump_dn = {
        'server': 'standard_char',
        'ldap_password': 'standard_char',
        'salt': 'standard_char',
        'integrationadapter_ptr': 'default',
        'dump_dn': 'modified_char',
        'ldap_user': 'standard_char',
        'ldap_integration_history': 'REQUIRES: ava_core.gather.gather_ldap.models.LDAPGatherHistory',
    }

    missing_dump_dn = {
        'server': 'standard_char',
        'ldap_password': 'standard_char',
        'salt': 'standard_char',
        'integrationadapter_ptr': 'default',
        'ldap_user': 'standard_char',
        'ldap_integration_history': 'REQUIRES: ava_core.gather.gather_ldap.models.LDAPGatherHistory',
    }

    modified_ldap_user = {
        'server': 'standard_char',
        'ldap_password': 'standard_char',
        'salt': 'standard_char',
        'integrationadapter_ptr': 'default',
        'dump_dn': 'standard_char',
        'ldap_user': 'modified_char',
        'ldap_integration_history': 'REQUIRES: ava_core.gather.gather_ldap.models.LDAPGatherHistory',
    }

    missing_ldap_user = {
        'server': 'standard_char',
        'ldap_password': 'standard_char',
        'salt': 'standard_char',
        'integrationadapter_ptr': 'default',
        'dump_dn': 'standard_char',
        'ldap_integration_history': 'REQUIRES: ava_core.gather.gather_ldap.models.LDAPGatherHistory',
    }

    missing_ldap_integration_history = {
        'server': 'standard_char',
        'ldap_password': 'standard_char',
        'salt': 'standard_char',
        'integrationadapter_ptr': 'default',
        'dump_dn': 'standard_char',
        'ldap_user': 'standard_char',
    }

    modified_ldap_integration_history = {
        'server': 'standard_char',
        'ldap_password': 'standard_char',
        'salt': 'standard_char',
        'integrationadapter_ptr': 'default',
        'dump_dn': 'standard_char',
        'ldap_user': 'standard_char',
        'ldap_integration_history': 'REQUIRES: ava_core.gather.gather_ldap.models.LDAPGatherHistory',
    }




