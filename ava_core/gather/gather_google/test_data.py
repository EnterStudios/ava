# Rest Imports
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.gather.gather_google.models import GoogleGatherHistory


# Implementation
class GoogleGatherHistoryTestData(AvaCoreTestData):
    """
    Test data for GoogleGatherHistory
    """

    @staticmethod
    def init_requirements(owner):
        pass

    # Store self information
    model = GoogleGatherHistory
    url = 'example/'

    standard = {
        'gatherhistory_ptr': 'default',
        'integration': 'example//1/',
    }

    unique = {
        'gatherhistory_ptr': 'default',
        'integration': 'example//2/',
    }
