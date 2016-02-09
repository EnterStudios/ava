# Rest Imports
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.gather.gather_ldap.models import LDAPGatherHistory


# Implementation
class LDAPGatherHistoryTestData(AvaCoreTestData):
    # Store self information
    model = LDAPGatherHistory
    url = 'gather/ldap/'

    standard = {
        'no_people': 12345,
        'message': 'standard_char',
        'no_groups': 12345,
        'no_identifiers': 12345,
        'next_scheduled': 'default',
        'import_status': 0,
        'integration_id': 1,
    }

    unique = {
        'no_people': 54321,
        'message': 'unique_char',
        'no_groups': 54321,
        'no_identifiers': 54321,
        'next_scheduled': 'default',
        'import_status': 1,
        'integration_id': 1,
    }
