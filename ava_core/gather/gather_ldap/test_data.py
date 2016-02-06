# Rest Imports
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.gather.gather_ldap.models import LDAPGatherHistory


# Implementation
class LDAPGatherHistoryTestData(AvaCoreTestData):
    """
    Test data for LDAPGatherHistory
    """

    @staticmethod
    def init_requirements(owner):
        pass

    # Store self information
    model = LDAPGatherHistory
    url = 'example/'

    standard = {
        'gatherhistory_ptr': 'default',
        'integration': 'example//1/',
    }

    unique = {
        'gatherhistory_ptr': 'default',
        'integration': 'example//2/',
    }
