# Rest Imports
from rest_framework import status
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.learn.models import Module, Role
from ava_core.learn.test_data import ModuleTestData, RoleTestData
from ava_core.game.models import Achievement
from ava_core.game.test_data import AchievementTestData
from ava_core.organize.models import Person
from ava_core.organize.test_data import PersonTestData
from ava_core.my.models import LearningHistory, LearningProfile, ScoreCard, Friend, LearningQueue, People, ActivityLog


# Implementation
class LearningHistoryTestData(AvaCoreTestData):
    """
    Test data for LearningHistory
    """

    def __init__(self):
        # Store self information
        self.model = LearningHistory
        self.url = '/example'

        # Create any necessary required models.
        self.init_requirements()

    def init_requirements(self):
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if Module.objects.count() == 0:
            ModuleTestData.init_requirements()
            Module.objects.create(**ModuleTestData.get_data('standard'))
            Module.objects.create(**ModuleTestData.get_data('unique'))
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if LearningProfile.objects.count() == 0:
            LearningProfileTestData.init_requirements()
            LearningProfile.objects.create(**LearningProfileTestData.get_data('standard'))
            LearningProfile.objects.create(**LearningProfileTestData.get_data('unique'))

    standard = {
        'module': '/example/1/',
        'score': 12345,
        'completed': True,
        'profile_history': '/example/1/',
        'owner': '',
    }

    unique = {
        'module': '/example/2/',
        'score': 54321,
        'completed': False,
        'profile_history': '/example/2/',
        'owner': '',
    }

    missing_module = {
        'score': 12345,
        'completed': True,
        'profile_history': '/example/1/',
        'owner': '',
    }
    modified_module = {
        'module': '/example/2/',
        'score': 12345,
        'completed': True,
        'profile_history': '/example/1/',
        'owner': '',
    }

    missing_score = {
        'module': '/example/1/',
        'completed': True,
        'profile_history': '/example/1/',
        'owner': '',
    }
    modified_score = {
        'module': '/example/1/',
        'score': 54321,
        'completed': True,
        'profile_history': '/example/1/',
        'owner': '',
    }

    modified_completed = {
        'module': '/example/1/',
        'score': 12345,
        'completed': False,
        'profile_history': '/example/1/',
        'owner': '',
    }
    missing_completed = {
        'module': '/example/1/',
        'score': 12345,
        'profile_history': '/example/1/',
        'owner': '',
    }

    missing_profile_history = {
        'module': '/example/1/',
        'score': 12345,
        'completed': True,
        'owner': '',
    }
    modified_profile_history = {
        'module': '/example/1/',
        'score': 12345,
        'completed': True,
        'profile_history': '/example/2/',
        'owner': '',
    }

    modified_owner = {
        'module': '/example/1/',
        'score': 12345,
        'completed': True,
        'profile_history': '/example/1/',
        'owner': '',
    }
    missing_owner = {
        'module': '/example/1/',
        'score': 12345,
        'completed': True,
        'profile_history': '/example/1/',
    }



class ScoreCardTestData(AvaCoreTestData):
    """
    Test data for ScoreCard
    """

    def __init__(self):
        # Store self information
        self.model = ScoreCard
        self.url = '/example'

        # Create any necessary required models.
        self.init_requirements()

    def init_requirements(self):
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if Achievement.objects.count() == 0:
            AchievementTestData.init_requirements()
            Achievement.objects.create(**AchievementTestData.get_data('standard'))
            Achievement.objects.create(**AchievementTestData.get_data('unique'))

    standard = {
        'achievement': '/example/1/',
        'owner': '',
    }

    unique = {
        'achievement': '/example/2/',
        'owner': '',
    }

    modified_achievement = {
        'achievement': '/example/2/',
        'owner': '',
    }
    missing_achievement = {
        'owner': '',
    }

    modified_owner = {
        'achievement': '/example/1/',
        'owner': '',
    }
    missing_owner = {
        'achievement': '/example/1/',
    }



class FriendTestData(AvaCoreTestData):
    """
    Test data for Friend
    """

    def __init__(self):
        # Store self information
        self.model = Friend
        self.url = '/example'

        # Create any necessary required models.
        self.init_requirements()

    def init_requirements(self):
        pass

    standard = {
        'friend': 'default',
        'owner': '',
    }

    unique = {
        'friend': 'default',
        'owner': '',
    }

    missing_friend = {
        'owner': '',
    }
    modified_friend = {
        'friend': 'default',
        'owner': '',
    }

    modified_owner = {
        'friend': 'default',
        'owner': '',
    }
    missing_owner = {
        'friend': 'default',
    }



class LearningQueueTestData(AvaCoreTestData):
    """
    Test data for LearningQueue
    """

    def __init__(self):
        # Store self information
        self.model = LearningQueue
        self.url = '/example'

        # Create any necessary required models.
        self.init_requirements()

    def init_requirements(self):
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if Module.objects.count() == 0:
            ModuleTestData.init_requirements()
            Module.objects.create(**ModuleTestData.get_data('standard'))
            Module.objects.create(**ModuleTestData.get_data('unique'))
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if LearningProfile.objects.count() == 0:
            LearningProfileTestData.init_requirements()
            LearningProfile.objects.create(**LearningProfileTestData.get_data('standard'))
            LearningProfile.objects.create(**LearningProfileTestData.get_data('unique'))

    standard = {
        'module': '/example/1/',
        'profile_queue': '/example/1/',
        'owner': '',
    }

    unique = {
        'module': '/example/2/',
        'profile_queue': '/example/2/',
        'owner': '',
    }

    missing_module = {
        'profile_queue': '/example/1/',
        'owner': '',
    }
    modified_module = {
        'module': '/example/2/',
        'profile_queue': '/example/1/',
        'owner': '',
    }

    missing_profile_queue = {
        'module': '/example/1/',
        'owner': '',
    }
    modified_profile_queue = {
        'module': '/example/1/',
        'profile_queue': '/example/2/',
        'owner': '',
    }

    modified_owner = {
        'module': '/example/1/',
        'profile_queue': '/example/1/',
        'owner': '',
    }
    missing_owner = {
        'module': '/example/1/',
        'profile_queue': '/example/1/',
    }



class PeopleTestData(AvaCoreTestData):
    """
    Test data for People
    """

    def __init__(self):
        # Store self information
        self.model = People
        self.url = '/example'

        # Create any necessary required models.
        self.init_requirements()

    def init_requirements(self):
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if Person.objects.count() == 0:
            PersonTestData.init_requirements()
            Person.objects.create(**PersonTestData.get_data('standard'))
            Person.objects.create(**PersonTestData.get_data('unique'))

    standard = {
        'person': '/example/1/',
        'owner': '',
    }

    unique = {
        'person': '/example/2/',
        'owner': '',
    }

    modified_person = {
        'person': '/example/2/',
        'owner': '',
    }
    missing_person = {
        'owner': '',
    }

    modified_owner = {
        'person': '/example/1/',
        'owner': '',
    }
    missing_owner = {
        'person': '/example/1/',
    }



class ActivityLogTestData(AvaCoreTestData):
    """
    Test data for ActivityLog
    """

    def __init__(self):
        # Store self information
        self.model = ActivityLog
        self.url = '/example'

        # Create any necessary required models.
        self.init_requirements()

    def init_requirements(self):
        pass

    standard = {
        'log_entry': 'standard_char',
        'owner': '',
    }

    unique = {
        'log_entry': 'unique_char',
        'owner': '',
    }

    missing_log_entry = {
        'owner': '',
    }
    modified_log_entry = {
        'log_entry': 'modified_char',
        'owner': '',
    }

    modified_owner = {
        'log_entry': 'standard_char',
        'owner': '',
    }
    missing_owner = {
        'log_entry': 'standard_char',
    }



class LearningProfileTestData(AvaCoreTestData):
    """
    Test data for LearningProfile
    """

    def __init__(self):
        # Store self information
        self.model = LearningProfile
        self.url = '/example'

        # Create any necessary required models.
        self.init_requirements()

    def init_requirements(self):
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if LearningHistory.objects.count() == 0:
            LearningHistoryTestData.init_requirements()
            LearningHistory.objects.create(**LearningHistoryTestData.get_data('standard'))
            LearningHistory.objects.create(**LearningHistoryTestData.get_data('unique'))
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if LearningQueue.objects.count() == 0:
            LearningQueueTestData.init_requirements()
            LearningQueue.objects.create(**LearningQueueTestData.get_data('standard'))
            LearningQueue.objects.create(**LearningQueueTestData.get_data('unique'))
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if Role.objects.count() == 0:
            RoleTestData.init_requirements()
            Role.objects.create(**RoleTestData.get_data('standard'))
            Role.objects.create(**RoleTestData.get_data('unique'))

    standard = {
        'learning_history': '/example/1/',
        'learning_queue': '/example/1/',
        'role': '/example/1/',
        'owner': '',
    }

    unique = {
        'learning_history': '/example/2/',
        'learning_queue': '/example/2/',
        'role': '/example/2/',
        'owner': '',
    }

    modified_learning_history = {
        'learning_history': '/example/2/',
        'learning_queue': '/example/1/',
        'role': '/example/1/',
        'owner': '',
    }
    missing_learning_history = {
        'learning_queue': '/example/1/',
        'role': '/example/1/',
        'owner': '',
    }

    missing_learning_queue = {
        'learning_history': '/example/1/',
        'role': '/example/1/',
        'owner': '',
    }
    modified_learning_queue = {
        'learning_history': '/example/1/',
        'learning_queue': '/example/2/',
        'role': '/example/1/',
        'owner': '',
    }

    modified_role = {
        'learning_history': '/example/1/',
        'learning_queue': '/example/1/',
        'role': '/example/2/',
        'owner': '',
    }
    missing_role = {
        'learning_history': '/example/1/',
        'learning_queue': '/example/1/',
        'owner': '',
    }

    modified_owner = {
        'learning_history': '/example/1/',
        'learning_queue': '/example/1/',
        'role': '/example/1/',
        'owner': '',
    }
    missing_owner = {
        'learning_history': '/example/1/',
        'learning_queue': '/example/1/',
        'role': '/example/1/',
    }




