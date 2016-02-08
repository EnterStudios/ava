# Rest Imports
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.gather.gather_office365.models import Office365GatherHistory


# Implementation
class Office365GatherHistoryTestData(AvaCoreTestData):

    # Store self information
    model = Office365GatherHistory
    url = 'gather/office365/'

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
