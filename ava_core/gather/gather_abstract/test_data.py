# Rest Imports
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.gather.gather_abstract.models import GatherHistory


# Implementation
class GatherHistoryTestData(AvaCoreTestData):
    """
    Test data for GatherHistory
    """

    @staticmethod
    def init_requirements(owner):
        pass

    # Store self information
    model = GatherHistory
    url = 'example/'

    standard = {
        'no_people': 12345,
        'office365gatherhistory': 'default',
        'message': 'standard_char',
        'no_groups': 12345,
        'no_identifiers': 12345,
        'googlegatherhistory': 'default',
        'next_scheduled': 'default',
        'ldapgatherhistory': 'default',
        'import_status': 0,
    }

    unique = {
        'no_people': 54321,
        'office365gatherhistory': 'default',
        'message': 'unique_char',
        'no_groups': 54321,
        'no_identifiers': 54321,
        'googlegatherhistory': 'default',
        'next_scheduled': 'default',
        'ldapgatherhistory': 'default',
        'import_status': 1,
    }
