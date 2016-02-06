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
    def init_requirements(owner):
        pass

    # Store self information
    model = LDAPIntegrationAdapter
    url = 'example/'

    standard = {
        'salt': 'standard_char',
        'ldap_password': 'standard_char',
        'ldap_integration_history': 'example//1/',
        'dump_dn': 'standard_char',
        'integrationadapter_ptr': 'default',
        'ldap_user': 'standard_char',
        'server': 'standard_char',
    }

    unique = {
        'salt': 'unique_char',
        'ldap_password': 'unique_char',
        'ldap_integration_history': 'example//2/',
        'dump_dn': 'unique_char',
        'integrationadapter_ptr': 'default',
        'ldap_user': 'unique_char',
        'server': 'unique_char',
    }