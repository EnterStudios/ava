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

    # Store self information
    model = LDAPIntegrationAdapter
    url = 'example/'

    standard = {
        'name': 'standard_char',
        'salt': 'standard_char',
        'ldap_password': 'standard_char',
        'dump_dn': 'standard_char',
        'ldap_user': 'standard_char',
        'server': 'standard_char',
    }

    unique = {
        'name': 'unique_char',
        'salt': 'unique_char',
        'ldap_password': 'unique_char',
        'dump_dn': 'unique_char',
        'ldap_user': 'unique_char',
        'server': 'unique_char',
    }