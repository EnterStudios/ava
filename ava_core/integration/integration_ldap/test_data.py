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
        # Import the required model and data
        from ava_core.gather.gather_ldap.models import LDAPGatherHistory
        from ava_core.gather.gather_ldap.test_data import LDAPGatherHistoryTestData
        # Grab data for object creation, with owner if required.
        data_model = LDAPGatherHistoryTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = LDAPGatherHistory.objects.filter(owner=owner['email']) if 'email' in standard_data else LDAPGatherHistory.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            LDAPGatherHistoryTestData.init_requirements(owner)
            model = LDAPGatherHistory.objects.create(**standard_data)
            model = LDAPGatherHistory.objects.create(**unique_data)

        # Import the required model and data
        from ava_core.integration.integration_abstract.models import IntegrationAdapter
        from ava_core.integration.integration_abstract.test_data import IntegrationAdapterTestData
        # Grab data for object creation, with owner if required.
        data_model = IntegrationAdapterTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = IntegrationAdapter.objects.filter(owner=owner['email']) if 'email' in standard_data else IntegrationAdapter.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            IntegrationAdapterTestData.init_requirements(owner)
            model = IntegrationAdapter.objects.create(**standard_data)
            model = IntegrationAdapter.objects.create(**unique_data)

    # Store self information
    model = LDAPIntegrationAdapter
    url = 'example/'

    standard = {
        'ldap_integration_history': 'example//1/',
        'ldap_user': 'standard_char',
        'ldap_password': 'standard_char',
        'integrationadapter_ptr': 'default',
        'salt': 'standard_char',
        'dump_dn': 'standard_char',
        'server': 'standard_char',
    }

    unique = {
        'ldap_integration_history': 'example//2/',
        'ldap_user': 'unique_char',
        'ldap_password': 'unique_char',
        'integrationadapter_ptr': 'default',
        'salt': 'unique_char',
        'dump_dn': 'unique_char',
        'server': 'unique_char',
    }

    modified_ldap_integration_history = {
        'ldap_integration_history': 'example//2/',
        'ldap_user': 'standard_char',
        'ldap_password': 'standard_char',
        'integrationadapter_ptr': 'default',
        'salt': 'standard_char',
        'dump_dn': 'standard_char',
        'server': 'standard_char',
    }
    missing_ldap_integration_history = {
        'ldap_user': 'standard_char',
        'ldap_password': 'standard_char',
        'integrationadapter_ptr': 'default',
        'salt': 'standard_char',
        'dump_dn': 'standard_char',
        'server': 'standard_char',
    }

    missing_ldap_user = {
        'ldap_integration_history': 'example//1/',
        'ldap_password': 'standard_char',
        'integrationadapter_ptr': 'default',
        'salt': 'standard_char',
        'dump_dn': 'standard_char',
        'server': 'standard_char',
    }
    modified_ldap_user = {
        'ldap_integration_history': 'example//1/',
        'ldap_user': 'modified_char',
        'ldap_password': 'standard_char',
        'integrationadapter_ptr': 'default',
        'salt': 'standard_char',
        'dump_dn': 'standard_char',
        'server': 'standard_char',
    }

    modified_ldap_password = {
        'ldap_integration_history': 'example//1/',
        'ldap_user': 'standard_char',
        'ldap_password': 'modified_char',
        'integrationadapter_ptr': 'default',
        'salt': 'standard_char',
        'dump_dn': 'standard_char',
        'server': 'standard_char',
    }
    missing_ldap_password = {
        'ldap_integration_history': 'example//1/',
        'ldap_user': 'standard_char',
        'integrationadapter_ptr': 'default',
        'salt': 'standard_char',
        'dump_dn': 'standard_char',
        'server': 'standard_char',
    }

    missing_integrationadapter_ptr = {
        'ldap_integration_history': 'example//1/',
        'ldap_user': 'standard_char',
        'ldap_password': 'standard_char',
        'salt': 'standard_char',
        'dump_dn': 'standard_char',
        'server': 'standard_char',
    }
    modified_integrationadapter_ptr = {
        'ldap_integration_history': 'example//1/',
        'ldap_user': 'standard_char',
        'ldap_password': 'standard_char',
        'integrationadapter_ptr': 'default',
        'salt': 'standard_char',
        'dump_dn': 'standard_char',
        'server': 'standard_char',
    }

    missing_salt = {
        'ldap_integration_history': 'example//1/',
        'ldap_user': 'standard_char',
        'ldap_password': 'standard_char',
        'integrationadapter_ptr': 'default',
        'dump_dn': 'standard_char',
        'server': 'standard_char',
    }
    modified_salt = {
        'ldap_integration_history': 'example//1/',
        'ldap_user': 'standard_char',
        'ldap_password': 'standard_char',
        'integrationadapter_ptr': 'default',
        'salt': 'modified_char',
        'dump_dn': 'standard_char',
        'server': 'standard_char',
    }

    modified_dump_dn = {
        'ldap_integration_history': 'example//1/',
        'ldap_user': 'standard_char',
        'ldap_password': 'standard_char',
        'integrationadapter_ptr': 'default',
        'salt': 'standard_char',
        'dump_dn': 'modified_char',
        'server': 'standard_char',
    }
    missing_dump_dn = {
        'ldap_integration_history': 'example//1/',
        'ldap_user': 'standard_char',
        'ldap_password': 'standard_char',
        'integrationadapter_ptr': 'default',
        'salt': 'standard_char',
        'server': 'standard_char',
    }

    missing_server = {
        'ldap_integration_history': 'example//1/',
        'ldap_user': 'standard_char',
        'ldap_password': 'standard_char',
        'integrationadapter_ptr': 'default',
        'salt': 'standard_char',
        'dump_dn': 'standard_char',
    }
    modified_server = {
        'ldap_integration_history': 'example//1/',
        'ldap_user': 'standard_char',
        'ldap_password': 'standard_char',
        'integrationadapter_ptr': 'default',
        'salt': 'standard_char',
        'dump_dn': 'standard_char',
        'server': 'modified_char',
    }




