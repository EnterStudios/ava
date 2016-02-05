# Rest Imports
from rest_framework import status
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.integration.integration_abstract.models import IntegrationAdapter


# Implementation
class IntegrationAdapterTestData(AvaCoreTestData):
    """
    Test data for IntegrationAdapter
    """

    @staticmethod
    def init_requirements(owner):
        # Import the required model and data
        from ava_core.integration.integration_office365.models import Office365IntegrationAdapter
        from ava_core.integration.integration_office365.test_data import Office365IntegrationAdapterTestData
        # Grab data for object creation, with owner if required.
        data_model = Office365IntegrationAdapterTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = Office365IntegrationAdapter.objects.filter(owner=owner['email']) if 'email' in standard_data else Office365IntegrationAdapter.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            Office365IntegrationAdapterTestData.init_requirements(owner)
            model = Office365IntegrationAdapter.objects.create(**standard_data)
            model = Office365IntegrationAdapter.objects.create(**unique_data)

        # Import the required model and data
        from ava_core.integration.integration_google.models import GoogleIntegrationAdapter
        from ava_core.integration.integration_google.test_data import GoogleIntegrationAdapterTestData
        # Grab data for object creation, with owner if required.
        data_model = GoogleIntegrationAdapterTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = GoogleIntegrationAdapter.objects.filter(owner=owner['email']) if 'email' in standard_data else GoogleIntegrationAdapter.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            GoogleIntegrationAdapterTestData.init_requirements(owner)
            model = GoogleIntegrationAdapter.objects.create(**standard_data)
            model = GoogleIntegrationAdapter.objects.create(**unique_data)

        # Import the required model and data
        from ava_core.integration.integration_ldap.models import LDAPIntegrationAdapter
        from ava_core.integration.integration_ldap.test_data import LDAPIntegrationAdapterTestData
        # Grab data for object creation, with owner if required.
        data_model = LDAPIntegrationAdapterTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = LDAPIntegrationAdapter.objects.filter(owner=owner['email']) if 'email' in standard_data else LDAPIntegrationAdapter.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            LDAPIntegrationAdapterTestData.init_requirements(owner)
            model = LDAPIntegrationAdapter.objects.create(**standard_data)
            model = LDAPIntegrationAdapter.objects.create(**unique_data)

    # Store self information
    model = IntegrationAdapter
    url = 'example/'

    standard = {
        'office365integrationadapter': 'default',
        'googleintegrationadapter': 'default',
        'credential': 'default',
        'name': 'standard_char',
        'ldapintegrationadapter': 'default',
    }

    unique = {
        'office365integrationadapter': 'default',
        'googleintegrationadapter': 'default',
        'credential': 'default',
        'name': 'unique_char',
        'ldapintegrationadapter': 'default',
    }

    missing_office365integrationadapter = {
        'googleintegrationadapter': 'default',
        'credential': 'default',
        'name': 'standard_char',
        'ldapintegrationadapter': 'default',
    }
    modified_office365integrationadapter = {
        'office365integrationadapter': 'default',
        'googleintegrationadapter': 'default',
        'credential': 'default',
        'name': 'standard_char',
        'ldapintegrationadapter': 'default',
    }

    missing_googleintegrationadapter = {
        'office365integrationadapter': 'default',
        'credential': 'default',
        'name': 'standard_char',
        'ldapintegrationadapter': 'default',
    }
    modified_googleintegrationadapter = {
        'office365integrationadapter': 'default',
        'googleintegrationadapter': 'default',
        'credential': 'default',
        'name': 'standard_char',
        'ldapintegrationadapter': 'default',
    }

    missing_credential = {
        'office365integrationadapter': 'default',
        'googleintegrationadapter': 'default',
        'name': 'standard_char',
        'ldapintegrationadapter': 'default',
    }
    modified_credential = {
        'office365integrationadapter': 'default',
        'googleintegrationadapter': 'default',
        'credential': 'default',
        'name': 'standard_char',
        'ldapintegrationadapter': 'default',
    }

    modified_name = {
        'office365integrationadapter': 'default',
        'googleintegrationadapter': 'default',
        'credential': 'default',
        'name': 'modified_char',
        'ldapintegrationadapter': 'default',
    }
    missing_name = {
        'office365integrationadapter': 'default',
        'googleintegrationadapter': 'default',
        'credential': 'default',
        'ldapintegrationadapter': 'default',
    }

    missing_ldapintegrationadapter = {
        'office365integrationadapter': 'default',
        'googleintegrationadapter': 'default',
        'credential': 'default',
        'name': 'standard_char',
    }
    modified_ldapintegrationadapter = {
        'office365integrationadapter': 'default',
        'googleintegrationadapter': 'default',
        'credential': 'default',
        'name': 'standard_char',
        'ldapintegrationadapter': 'default',
    }




