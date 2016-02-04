# Rest Imports
from rest_framework import status
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.my.models import ActivityLog, LearningQueue, ScoreCard, Friend, People, LearningProfile, LearningHistory


# Implementation
class ActivityLogTestData(AvaCoreTestData):
    """
    Test data for ActivityLog
    """

    @staticmethod
    def init_requirements():
        pass

    # Store self information
    model = ActivityLog
    url = '/example'

    standard = {
        'owner': '',
        'log_entry': 'standard_char',
    }

    unique = {
        'owner': '',
        'log_entry': 'unique_char',
    }

    modified_owner = {
        'owner': '',
        'log_entry': 'standard_char',
    }
    missing_owner = {
        'log_entry': 'standard_char',
    }

    missing_log_entry = {
        'owner': '',
    }
    modified_log_entry = {
        'owner': '',
        'log_entry': 'modified_char',
    }



class LearningQueueTestData(AvaCoreTestData):
    """
    Test data for LearningQueue
    """

    @staticmethod
    def init_requirements():
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if LearningProfile.objects.count() == 0:
            LearningProfileTestData.init_requirements()
            model = LearningProfile.objects.create(**LearningProfileTestData.get_data('standard'))
            model.save()
            model = LearningProfile.objects.create(**LearningProfileTestData.get_data('unique'))
            model.save()

        # Import the required model and data
        from ava_core.learn.models import Module
        from ava_core.learn.test_data import ModuleTestData
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if Module.objects.count() == 0:
            ModuleTestData.init_requirements()
            model = Module.objects.create(**ModuleTestData.get_data('standard'))
            model.save()
            model = Module.objects.create(**ModuleTestData.get_data('unique'))
            model.save()

    # Store self information
    model = LearningQueue
    url = '/example'

    standard = {
        'profile_queue': '/example/1/',
        'module': '/example/1/',
        'owner': '',
    }

    unique = {
        'profile_queue': '/example/2/',
        'module': '/example/2/',
        'owner': '',
    }

    modified_profile_queue = {
        'profile_queue': '/example/2/',
        'module': '/example/1/',
        'owner': '',
    }
    missing_profile_queue = {
        'module': '/example/1/',
        'owner': '',
    }

    missing_module = {
        'profile_queue': '/example/1/',
        'owner': '',
    }
    modified_module = {
        'profile_queue': '/example/1/',
        'module': '/example/2/',
        'owner': '',
    }

    modified_owner = {
        'profile_queue': '/example/1/',
        'module': '/example/1/',
        'owner': '',
    }
    missing_owner = {
        'profile_queue': '/example/1/',
        'module': '/example/1/',
    }



class ScoreCardTestData(AvaCoreTestData):
    """
    Test data for ScoreCard
    """

    @staticmethod
    def init_requirements():
        # Import the required model and data
        from ava_core.game.models import Achievement
        from ava_core.game.test_data import AchievementTestData
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if Achievement.objects.count() == 0:
            AchievementTestData.init_requirements()
            model = Achievement.objects.create(**AchievementTestData.get_data('standard'))
            model.save()
            model = Achievement.objects.create(**AchievementTestData.get_data('unique'))
            model.save()

    # Store self information
    model = ScoreCard
    url = '/example'

    standard = {
        'achievement': '/example/1/',
        'owner': '',
    }

    unique = {
        'achievement': '/example/2/',
        'owner': '',
    }

    missing_achievement = {
        'owner': '',
    }
    modified_achievement = {
        'achievement': '/example/2/',
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

    @staticmethod
    def init_requirements():
        pass

    # Store self information
    model = Friend
    url = '/example'

    standard = {
        'owner': '',
        'friend': 'default',
    }

    unique = {
        'owner': '',
        'friend': 'default',
    }

    modified_owner = {
        'owner': '',
        'friend': 'default',
    }
    missing_owner = {
        'friend': 'default',
    }

    modified_friend = {
        'owner': '',
        'friend': 'default',
    }
    missing_friend = {
        'owner': '',
    }



class PeopleTestData(AvaCoreTestData):
    """
    Test data for People
    """

    @staticmethod
    def init_requirements():
        # Import the required model and data
        from ava_core.organize.models import Person
        from ava_core.organize.test_data import PersonTestData
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if Person.objects.count() == 0:
            PersonTestData.init_requirements()
            model = Person.objects.create(**PersonTestData.get_data('standard'))
            model.save()
            model = Person.objects.create(**PersonTestData.get_data('unique'))
            model.save()

    # Store self information
    model = People
    url = '/example'

    standard = {
        'person': '/example/1/',
        'owner': '',
    }

    unique = {
        'person': '/example/2/',
        'owner': '',
    }

    missing_person = {
        'owner': '',
    }
    modified_person = {
        'person': '/example/2/',
        'owner': '',
    }

    modified_owner = {
        'person': '/example/1/',
        'owner': '',
    }
    missing_owner = {
        'person': '/example/1/',
    }



class LearningProfileTestData(AvaCoreTestData):
    """
    Test data for LearningProfile
    """

    @staticmethod
    def init_requirements():
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if LearningHistory.objects.count() == 0:
            LearningHistoryTestData.init_requirements()
            model = LearningHistory.objects.create(**LearningHistoryTestData.get_data('standard'))
            model.save()
            model = LearningHistory.objects.create(**LearningHistoryTestData.get_data('unique'))
            model.save()

        # Import the required model and data
        from ava_core.learn.models import Role
        from ava_core.learn.test_data import RoleTestData
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if Role.objects.count() == 0:
            RoleTestData.init_requirements()
            model = Role.objects.create(**RoleTestData.get_data('standard'))
            model.save()
            model = Role.objects.create(**RoleTestData.get_data('unique'))
            model.save()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if LearningQueue.objects.count() == 0:
            LearningQueueTestData.init_requirements()
            model = LearningQueue.objects.create(**LearningQueueTestData.get_data('standard'))
            model.save()
            model = LearningQueue.objects.create(**LearningQueueTestData.get_data('unique'))
            model.save()

    # Store self information
    model = LearningProfile
    url = '/example'

    standard = {
        'learning_history': '/example/1/',
        'role': '/example/1/',
        'owner': '',
        'learning_queue': '/example/1/',
    }

    unique = {
        'learning_history': '/example/2/',
        'role': '/example/2/',
        'owner': '',
        'learning_queue': '/example/2/',
    }

    modified_learning_history = {
        'learning_history': '/example/2/',
        'role': '/example/1/',
        'owner': '',
        'learning_queue': '/example/1/',
    }
    missing_learning_history = {
        'role': '/example/1/',
        'owner': '',
        'learning_queue': '/example/1/',
    }

    modified_role = {
        'learning_history': '/example/1/',
        'role': '/example/2/',
        'owner': '',
        'learning_queue': '/example/1/',
    }
    missing_role = {
        'learning_history': '/example/1/',
        'owner': '',
        'learning_queue': '/example/1/',
    }

    modified_owner = {
        'learning_history': '/example/1/',
        'role': '/example/1/',
        'owner': '',
        'learning_queue': '/example/1/',
    }
    missing_owner = {
        'learning_history': '/example/1/',
        'role': '/example/1/',
        'learning_queue': '/example/1/',
    }

    missing_learning_queue = {
        'learning_history': '/example/1/',
        'role': '/example/1/',
        'owner': '',
    }
    modified_learning_queue = {
        'learning_history': '/example/1/',
        'role': '/example/1/',
        'owner': '',
        'learning_queue': '/example/2/',
    }



class LearningHistoryTestData(AvaCoreTestData):
    """
    Test data for LearningHistory
    """

    @staticmethod
    def init_requirements():
        # Import the required model and data
        from ava_core.learn.models import Module
        from ava_core.learn.test_data import ModuleTestData
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if Module.objects.count() == 0:
            ModuleTestData.init_requirements()
            model = Module.objects.create(**ModuleTestData.get_data('standard'))
            model.save()
            model = Module.objects.create(**ModuleTestData.get_data('unique'))
            model.save()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if LearningProfile.objects.count() == 0:
            LearningProfileTestData.init_requirements()
            model = LearningProfile.objects.create(**LearningProfileTestData.get_data('standard'))
            model.save()
            model = LearningProfile.objects.create(**LearningProfileTestData.get_data('unique'))
            model.save()

    # Store self information
    model = LearningHistory
    url = '/example'

    standard = {
        'completed': True,
        'module': '/example/1/',
        'profile_history': '/example/1/',
        'score': 12345,
        'owner': '',
    }

    unique = {
        'completed': False,
        'module': '/example/2/',
        'profile_history': '/example/2/',
        'score': 54321,
        'owner': '',
    }

    modified_completed = {
        'completed': False,
        'module': '/example/1/',
        'profile_history': '/example/1/',
        'score': 12345,
        'owner': '',
    }
    missing_completed = {
        'module': '/example/1/',
        'profile_history': '/example/1/',
        'score': 12345,
        'owner': '',
    }

    missing_module = {
        'completed': True,
        'profile_history': '/example/1/',
        'score': 12345,
        'owner': '',
    }
    modified_module = {
        'completed': True,
        'module': '/example/2/',
        'profile_history': '/example/1/',
        'score': 12345,
        'owner': '',
    }

    missing_profile_history = {
        'completed': True,
        'module': '/example/1/',
        'score': 12345,
        'owner': '',
    }
    modified_profile_history = {
        'completed': True,
        'module': '/example/1/',
        'profile_history': '/example/2/',
        'score': 12345,
        'owner': '',
    }

    missing_score = {
        'completed': True,
        'module': '/example/1/',
        'profile_history': '/example/1/',
        'owner': '',
    }
    modified_score = {
        'completed': True,
        'module': '/example/1/',
        'profile_history': '/example/1/',
        'score': 54321,
        'owner': '',
    }

    modified_owner = {
        'completed': True,
        'module': '/example/1/',
        'profile_history': '/example/1/',
        'score': 12345,
        'owner': '',
    }
    missing_owner = {
        'completed': True,
        'module': '/example/1/',
        'profile_history': '/example/1/',
        'score': 12345,
    }




