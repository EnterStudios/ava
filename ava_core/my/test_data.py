# Rest Imports
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.my.models import Friend, LearningHistory, People, LearningQueue, ActivityLog, LearningProfile, ScoreCard


# Implementation
class FriendTestData(AvaCoreTestData):
    """
    Test data for Friend
    """

    @staticmethod
    def init_requirements(owner):
        pass

    # Store self information
    model = Friend
    url = 'example/'

    standard = {
        'friend': 'default',
        'owner': '',
    }

    unique = {
        'friend': 'default',
        'owner': '',
    }


class LearningHistoryTestData(AvaCoreTestData):
    """
    Test data for LearningHistory
    """

    @staticmethod
    def init_requirements(owner):
        pass

    # Store self information
    model = LearningHistory
    url = 'example/'

    standard = {
        'module': 'example//1/',
        'score': 12345,
        'profile_history': 'example//1/',
        'completed': True,
        'owner': '',
    }

    unique = {
        'module': 'example//2/',
        'score': 54321,
        'profile_history': 'example//2/',
        'completed': False,
        'owner': '',
    }


class PeopleTestData(AvaCoreTestData):
    """
    Test data for People
    """

    @staticmethod
    def init_requirements(owner):
        pass

    # Store self information
    model = People
    url = 'example/'

    standard = {
        'person': 'example//1/',
        'owner': '',
    }

    unique = {
        'person': 'example//2/',
        'owner': '',
    }


class LearningQueueTestData(AvaCoreTestData):
    """
    Test data for LearningQueue
    """

    @staticmethod
    def init_requirements(owner):
        pass

    # Store self information
    model = LearningQueue
    url = 'example/'

    standard = {
        'module': 'example//1/',
        'profile_queue': 'example//1/',
        'owner': '',
    }

    unique = {
        'module': 'example//2/',
        'profile_queue': 'example//2/',
        'owner': '',
    }


class ActivityLogTestData(AvaCoreTestData):
    """
    Test data for ActivityLog
    """

    @staticmethod
    def init_requirements(owner):
        pass

    # Store self information
    model = ActivityLog
    url = 'example/'

    standard = {
        'log_entry': 'standard_char',
        'owner': '',
    }

    unique = {
        'log_entry': 'unique_char',
        'owner': '',
    }


class LearningProfileTestData(AvaCoreTestData):
    """
    Test data for LearningProfile
    """

    @staticmethod
    def init_requirements(owner):
        pass

    # Store self information
    model = LearningProfile
    url = 'example/'

    standard = {
        'learning_queue': 'example//1/',
        'owner': '',
        'role': 'example//1/',
        'learning_history': 'example//1/',
    }

    unique = {
        'learning_queue': 'example//2/',
        'owner': '',
        'role': 'example//2/',
        'learning_history': 'example//2/',
    }


class ScoreCardTestData(AvaCoreTestData):
    """
    Test data for ScoreCard
    """

    @staticmethod
    def init_requirements(owner):
        pass

    # Store self information
    model = ScoreCard
    url = 'example/'

    standard = {
        'achievement': 'example//1/',
        'owner': '',
    }

    unique = {
        'achievement': 'example//2/',
        'owner': '',
    }
