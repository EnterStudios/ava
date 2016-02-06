# Rest Imports
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.gather.gather_office365.models import Office365GatherHistory


# Implementation
class Office365GatherHistoryTestData(AvaCoreTestData):
    """
    Test data for Office365GatherHistory
    """

    @staticmethod
    def init_requirements(owner):
        pass

    # Store self information
    model = Office365GatherHistory
    url = 'example/'

    standard = {
        'gatherhistory_ptr': 'default',
        'integration': 'example//1/',
    }

    unique = {
        'gatherhistory_ptr': 'default',
        'integration': 'example//2/',
    }
