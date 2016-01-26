# Rest Imports
# Local Imports
from ava_core.abstract.test_data import AvaTestData
from ava_core.gather.gather_abstract.models import GatherHistory


# Implementation
class GatherHistoryTestData(AvaTestData):
    """
    Test data for GatherHistory
    """

    model = GatherHistory
    url = '/example'

    standard = {
        'no_identifiers': 12345,
        'googlegatherhistory': 'default',
        'ldapgatherhistory': 'default',
        'next_scheduled': 'default',
        'no_groups': 12345,
        'message': 'standard_char',
        'import_status': 0,
        'no_people': 12345,
    }

    modified = {
        'no_identifiers': 12345,
        'googlegatherhistory': 'default',
        'ldapgatherhistory': 'default',
        'next_scheduled': 'default',
        'no_groups': 12345,
        'message': 'standard_char',
        'import_status': 0,
        'no_people': 12345,
    }

    missing_no_identifiers = {
        'googlegatherhistory': 'default',
        'ldapgatherhistory': 'default',
        'next_scheduled': 'default',
        'no_groups': 12345,
        'message': 'standard_char',
        'import_status': 0,
        'no_people': 12345,
    }

    modified_no_identifiers = {
        'no_identifiers': 54321,
        'googlegatherhistory': 'default',
        'ldapgatherhistory': 'default',
        'next_scheduled': 'default',
        'no_groups': 12345,
        'message': 'standard_char',
        'import_status': 0,
        'no_people': 12345,
    }

    modified_googlegatherhistory = {
        'no_identifiers': 12345,
        'googlegatherhistory': 'default',
        'ldapgatherhistory': 'default',
        'next_scheduled': 'default',
        'no_groups': 12345,
        'message': 'standard_char',
        'import_status': 0,
        'no_people': 12345,
    }

    missing_googlegatherhistory = {
        'no_identifiers': 12345,
        'ldapgatherhistory': 'default',
        'next_scheduled': 'default',
        'no_groups': 12345,
        'message': 'standard_char',
        'import_status': 0,
        'no_people': 12345,
    }

    modified_ldapgatherhistory = {
        'no_identifiers': 12345,
        'googlegatherhistory': 'default',
        'ldapgatherhistory': 'default',
        'next_scheduled': 'default',
        'no_groups': 12345,
        'message': 'standard_char',
        'import_status': 0,
        'no_people': 12345,
    }

    missing_ldapgatherhistory = {
        'no_identifiers': 12345,
        'googlegatherhistory': 'default',
        'next_scheduled': 'default',
        'no_groups': 12345,
        'message': 'standard_char',
        'import_status': 0,
        'no_people': 12345,
    }

    modified_next_scheduled = {
        'no_identifiers': 12345,
        'googlegatherhistory': 'default',
        'ldapgatherhistory': 'default',
        'next_scheduled': 'default',
        'no_groups': 12345,
        'message': 'standard_char',
        'import_status': 0,
        'no_people': 12345,
    }

    missing_next_scheduled = {
        'no_identifiers': 12345,
        'googlegatherhistory': 'default',
        'ldapgatherhistory': 'default',
        'no_groups': 12345,
        'message': 'standard_char',
        'import_status': 0,
        'no_people': 12345,
    }

    missing_no_groups = {
        'no_identifiers': 12345,
        'googlegatherhistory': 'default',
        'ldapgatherhistory': 'default',
        'next_scheduled': 'default',
        'message': 'standard_char',
        'import_status': 0,
        'no_people': 12345,
    }

    modified_no_groups = {
        'no_identifiers': 12345,
        'googlegatherhistory': 'default',
        'ldapgatherhistory': 'default',
        'next_scheduled': 'default',
        'no_groups': 54321,
        'message': 'standard_char',
        'import_status': 0,
        'no_people': 12345,
    }

    modified_message = {
        'no_identifiers': 12345,
        'googlegatherhistory': 'default',
        'ldapgatherhistory': 'default',
        'next_scheduled': 'default',
        'no_groups': 12345,
        'message': 'modified_char',
        'import_status': 0,
        'no_people': 12345,
    }

    missing_message = {
        'no_identifiers': 12345,
        'googlegatherhistory': 'default',
        'ldapgatherhistory': 'default',
        'next_scheduled': 'default',
        'no_groups': 12345,
        'import_status': 0,
        'no_people': 12345,
    }

    missing_import_status = {
        'no_identifiers': 12345,
        'googlegatherhistory': 'default',
        'ldapgatherhistory': 'default',
        'next_scheduled': 'default',
        'no_groups': 12345,
        'message': 'standard_char',
        'no_people': 12345,
    }

    modified_import_status = {
        'no_identifiers': 12345,
        'googlegatherhistory': 'default',
        'ldapgatherhistory': 'default',
        'next_scheduled': 'default',
        'no_groups': 12345,
        'message': 'standard_char',
        'import_status': 1,
        'no_people': 12345,
    }

    modified_no_people = {
        'no_identifiers': 12345,
        'googlegatherhistory': 'default',
        'ldapgatherhistory': 'default',
        'next_scheduled': 'default',
        'no_groups': 12345,
        'message': 'standard_char',
        'import_status': 0,
        'no_people': 54321,
    }

    missing_no_people = {
        'no_identifiers': 12345,
        'googlegatherhistory': 'default',
        'ldapgatherhistory': 'default',
        'next_scheduled': 'default',
        'no_groups': 12345,
        'message': 'standard_char',
        'import_status': 0,
    }




