# Rest Imports
from rest_framework import status
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.gather.gather_abstract.models import GatherHistory
from ava_core.gather.gather_google.models import GoogleGatherHistory
from ava_core.gather.gather_google.test_data import GoogleGatherHistoryTestData
from ava_core.gather.gather_ldap.models import LDAPGatherHistory
from ava_core.gather.gather_ldap.test_data import LDAPGatherHistoryTestData


# Implementation
class GatherHistoryTestData(AvaCoreTestData):
    """
    Test data for GatherHistory
    """

    def __init__(self):
        # Store self information
        self.model = GatherHistory
        self.url = '/example'

        # Create any necessary required models.
        self.init_requirements()

    def init_requirements(self):
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if GoogleGatherHistory.objects.count() == 0:
            GoogleGatherHistoryTestData.init_requirements()
            GoogleGatherHistory.objects.create(**GoogleGatherHistoryTestData.get_data('standard'))
            GoogleGatherHistory.objects.create(**GoogleGatherHistoryTestData.get_data('unique'))
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if LDAPGatherHistory.objects.count() == 0:
            LDAPGatherHistoryTestData.init_requirements()
            LDAPGatherHistory.objects.create(**LDAPGatherHistoryTestData.get_data('standard'))
            LDAPGatherHistory.objects.create(**LDAPGatherHistoryTestData.get_data('unique'))

    standard = {
        'googlegatherhistory': 'default',
        'import_status': 0,
        'ldapgatherhistory': 'default',
        'message': 'standard_char',
        'no_people': 12345,
        'no_identifiers': 12345,
        'next_scheduled': 'default',
        'no_groups': 12345,
    }

    unique = {
        'googlegatherhistory': 'default',
        'import_status': 1,
        'ldapgatherhistory': 'default',
        'message': 'unique_char',
        'no_people': 54321,
        'no_identifiers': 54321,
        'next_scheduled': 'default',
        'no_groups': 54321,
    }

    modified_googlegatherhistory = {
        'googlegatherhistory': 'default',
        'import_status': 0,
        'ldapgatherhistory': 'default',
        'message': 'standard_char',
        'no_people': 12345,
        'no_identifiers': 12345,
        'next_scheduled': 'default',
        'no_groups': 12345,
    }
    missing_googlegatherhistory = {
        'import_status': 0,
        'ldapgatherhistory': 'default',
        'message': 'standard_char',
        'no_people': 12345,
        'no_identifiers': 12345,
        'next_scheduled': 'default',
        'no_groups': 12345,
    }

    missing_import_status = {
        'googlegatherhistory': 'default',
        'ldapgatherhistory': 'default',
        'message': 'standard_char',
        'no_people': 12345,
        'no_identifiers': 12345,
        'next_scheduled': 'default',
        'no_groups': 12345,
    }
    modified_import_status = {
        'googlegatherhistory': 'default',
        'import_status': 1,
        'ldapgatherhistory': 'default',
        'message': 'standard_char',
        'no_people': 12345,
        'no_identifiers': 12345,
        'next_scheduled': 'default',
        'no_groups': 12345,
    }

    missing_ldapgatherhistory = {
        'googlegatherhistory': 'default',
        'import_status': 0,
        'message': 'standard_char',
        'no_people': 12345,
        'no_identifiers': 12345,
        'next_scheduled': 'default',
        'no_groups': 12345,
    }
    modified_ldapgatherhistory = {
        'googlegatherhistory': 'default',
        'import_status': 0,
        'ldapgatherhistory': 'default',
        'message': 'standard_char',
        'no_people': 12345,
        'no_identifiers': 12345,
        'next_scheduled': 'default',
        'no_groups': 12345,
    }

    modified_message = {
        'googlegatherhistory': 'default',
        'import_status': 0,
        'ldapgatherhistory': 'default',
        'message': 'modified_char',
        'no_people': 12345,
        'no_identifiers': 12345,
        'next_scheduled': 'default',
        'no_groups': 12345,
    }
    missing_message = {
        'googlegatherhistory': 'default',
        'import_status': 0,
        'ldapgatherhistory': 'default',
        'no_people': 12345,
        'no_identifiers': 12345,
        'next_scheduled': 'default',
        'no_groups': 12345,
    }

    missing_no_people = {
        'googlegatherhistory': 'default',
        'import_status': 0,
        'ldapgatherhistory': 'default',
        'message': 'standard_char',
        'no_identifiers': 12345,
        'next_scheduled': 'default',
        'no_groups': 12345,
    }
    modified_no_people = {
        'googlegatherhistory': 'default',
        'import_status': 0,
        'ldapgatherhistory': 'default',
        'message': 'standard_char',
        'no_people': 54321,
        'no_identifiers': 12345,
        'next_scheduled': 'default',
        'no_groups': 12345,
    }

    modified_no_identifiers = {
        'googlegatherhistory': 'default',
        'import_status': 0,
        'ldapgatherhistory': 'default',
        'message': 'standard_char',
        'no_people': 12345,
        'no_identifiers': 54321,
        'next_scheduled': 'default',
        'no_groups': 12345,
    }
    missing_no_identifiers = {
        'googlegatherhistory': 'default',
        'import_status': 0,
        'ldapgatherhistory': 'default',
        'message': 'standard_char',
        'no_people': 12345,
        'next_scheduled': 'default',
        'no_groups': 12345,
    }

    modified_next_scheduled = {
        'googlegatherhistory': 'default',
        'import_status': 0,
        'ldapgatherhistory': 'default',
        'message': 'standard_char',
        'no_people': 12345,
        'no_identifiers': 12345,
        'next_scheduled': 'default',
        'no_groups': 12345,
    }
    missing_next_scheduled = {
        'googlegatherhistory': 'default',
        'import_status': 0,
        'ldapgatherhistory': 'default',
        'message': 'standard_char',
        'no_people': 12345,
        'no_identifiers': 12345,
        'no_groups': 12345,
    }

    modified_no_groups = {
        'googlegatherhistory': 'default',
        'import_status': 0,
        'ldapgatherhistory': 'default',
        'message': 'standard_char',
        'no_people': 12345,
        'no_identifiers': 12345,
        'next_scheduled': 'default',
        'no_groups': 54321,
    }
    missing_no_groups = {
        'googlegatherhistory': 'default',
        'import_status': 0,
        'ldapgatherhistory': 'default',
        'message': 'standard_char',
        'no_people': 12345,
        'no_identifiers': 12345,
        'next_scheduled': 'default',
    }




