# Rest Imports
from rest_framework import status
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.my.models import LearningQueue, LearningHistory, LearningProfile, ActivityLog, People, ScoreCard, Friend


# Implementation
class LearningQueueTestData(AvaCoreTestData):
    """
    Test data for LearningQueue
    """

    @staticmethod
    def init_requirements(owner):
        # Import the required model and data
        from ava_core.learn.models import Module
        from ava_core.learn.test_data import ModuleTestData
        # Grab data for object creation, with owner if required.
        data_model = ModuleTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = Module.objects.filter(owner=owner['email']) if 'email' in standard_data else Module.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            ModuleTestData.init_requirements(owner)
            model = Module.objects.create(**standard_data)
            model = Module.objects.create(**unique_data)

        # Grab data for object creation, with owner if required.
        data_model = LearningProfileTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = LearningProfile.objects.filter(owner=owner['email']) if 'email' in standard_data else LearningProfile.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            LearningProfileTestData.init_requirements(owner)
            model = LearningProfile.objects.create(**standard_data)
            model = LearningProfile.objects.create(**unique_data)

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

    modified_module = {
        'module': 'example//2/',
        'profile_queue': 'example//1/',
        'owner': '',
    }
    missing_module = {
        'profile_queue': 'example//1/',
        'owner': '',
    }

    missing_profile_queue = {
        'module': 'example//1/',
        'owner': '',
    }
    modified_profile_queue = {
        'module': 'example//1/',
        'profile_queue': 'example//2/',
        'owner': '',
    }

    missing_owner = {
        'module': 'example//1/',
        'profile_queue': 'example//1/',
    }
    modified_owner = {
        'module': 'example//1/',
        'profile_queue': 'example//1/',
        'owner': '',
    }



class LearningHistoryTestData(AvaCoreTestData):
    """
    Test data for LearningHistory
    """

    @staticmethod
    def init_requirements(owner):
        # Grab data for object creation, with owner if required.
        data_model = LearningProfileTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = LearningProfile.objects.filter(owner=owner['email']) if 'email' in standard_data else LearningProfile.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            LearningProfileTestData.init_requirements(owner)
            model = LearningProfile.objects.create(**standard_data)
            model = LearningProfile.objects.create(**unique_data)

        # Import the required model and data
        from ava_core.learn.models import Module
        from ava_core.learn.test_data import ModuleTestData
        # Grab data for object creation, with owner if required.
        data_model = ModuleTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = Module.objects.filter(owner=owner['email']) if 'email' in standard_data else Module.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            ModuleTestData.init_requirements(owner)
            model = Module.objects.create(**standard_data)
            model = Module.objects.create(**unique_data)

    # Store self information
    model = LearningHistory
    url = 'example/'

    standard = {
        'profile_history': 'example//1/',
        'score': 12345,
        'module': 'example//1/',
        'completed': True,
        'owner': '',
    }

    unique = {
        'profile_history': 'example//2/',
        'score': 54321,
        'module': 'example//2/',
        'completed': False,
        'owner': '',
    }

    missing_profile_history = {
        'score': 12345,
        'module': 'example//1/',
        'completed': True,
        'owner': '',
    }
    modified_profile_history = {
        'profile_history': 'example//2/',
        'score': 12345,
        'module': 'example//1/',
        'completed': True,
        'owner': '',
    }

    modified_score = {
        'profile_history': 'example//1/',
        'score': 54321,
        'module': 'example//1/',
        'completed': True,
        'owner': '',
    }
    missing_score = {
        'profile_history': 'example//1/',
        'module': 'example//1/',
        'completed': True,
        'owner': '',
    }

    modified_module = {
        'profile_history': 'example//1/',
        'score': 12345,
        'module': 'example//2/',
        'completed': True,
        'owner': '',
    }
    missing_module = {
        'profile_history': 'example//1/',
        'score': 12345,
        'completed': True,
        'owner': '',
    }

    modified_completed = {
        'profile_history': 'example//1/',
        'score': 12345,
        'module': 'example//1/',
        'completed': False,
        'owner': '',
    }
    missing_completed = {
        'profile_history': 'example//1/',
        'score': 12345,
        'module': 'example//1/',
        'owner': '',
    }

    missing_owner = {
        'profile_history': 'example//1/',
        'score': 12345,
        'module': 'example//1/',
        'completed': True,
    }
    modified_owner = {
        'profile_history': 'example//1/',
        'score': 12345,
        'module': 'example//1/',
        'completed': True,
        'owner': '',
    }



class LearningProfileTestData(AvaCoreTestData):
    """
    Test data for LearningProfile
    """

    @staticmethod
    def init_requirements(owner):
        # Grab data for object creation, with owner if required.
        data_model = LearningQueueTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = LearningQueue.objects.filter(owner=owner['email']) if 'email' in standard_data else LearningQueue.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            LearningQueueTestData.init_requirements(owner)
            model = LearningQueue.objects.create(**standard_data)
            model = LearningQueue.objects.create(**unique_data)

        # Grab data for object creation, with owner if required.
        data_model = LearningHistoryTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = LearningHistory.objects.filter(owner=owner['email']) if 'email' in standard_data else LearningHistory.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            LearningHistoryTestData.init_requirements(owner)
            model = LearningHistory.objects.create(**standard_data)
            model = LearningHistory.objects.create(**unique_data)

        # Import the required model and data
        from ava_core.learn.models import Role
        from ava_core.learn.test_data import RoleTestData
        # Grab data for object creation, with owner if required.
        data_model = RoleTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = Role.objects.filter(owner=owner['email']) if 'email' in standard_data else Role.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            RoleTestData.init_requirements(owner)
            model = Role.objects.create(**standard_data)
            model = Role.objects.create(**unique_data)

    # Store self information
    model = LearningProfile
    url = 'example/'

    standard = {
        'learning_queue': 'example//1/',
        'learning_history': 'example//1/',
        'role': 'example//1/',
        'owner': '',
    }

    unique = {
        'learning_queue': 'example//2/',
        'learning_history': 'example//2/',
        'role': 'example//2/',
        'owner': '',
    }

    modified_learning_queue = {
        'learning_queue': 'example//2/',
        'learning_history': 'example//1/',
        'role': 'example//1/',
        'owner': '',
    }
    missing_learning_queue = {
        'learning_history': 'example//1/',
        'role': 'example//1/',
        'owner': '',
    }

    modified_learning_history = {
        'learning_queue': 'example//1/',
        'learning_history': 'example//2/',
        'role': 'example//1/',
        'owner': '',
    }
    missing_learning_history = {
        'learning_queue': 'example//1/',
        'role': 'example//1/',
        'owner': '',
    }

    missing_role = {
        'learning_queue': 'example//1/',
        'learning_history': 'example//1/',
        'owner': '',
    }
    modified_role = {
        'learning_queue': 'example//1/',
        'learning_history': 'example//1/',
        'role': 'example//2/',
        'owner': '',
    }

    missing_owner = {
        'learning_queue': 'example//1/',
        'learning_history': 'example//1/',
        'role': 'example//1/',
    }
    modified_owner = {
        'learning_queue': 'example//1/',
        'learning_history': 'example//1/',
        'role': 'example//1/',
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

    missing_log_entry = {
        'owner': '',
    }
    modified_log_entry = {
        'log_entry': 'modified_char',
        'owner': '',
    }

    missing_owner = {
        'log_entry': 'standard_char',
    }
    modified_owner = {
        'log_entry': 'standard_char',
        'owner': '',
    }



class PeopleTestData(AvaCoreTestData):
    """
    Test data for People
    """

    @staticmethod
    def init_requirements(owner):
        # Import the required model and data
        from ava_core.organize.models import Person
        from ava_core.organize.test_data import PersonTestData
        # Grab data for object creation, with owner if required.
        data_model = PersonTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = Person.objects.filter(owner=owner['email']) if 'email' in standard_data else Person.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            PersonTestData.init_requirements(owner)
            model = Person.objects.create(**standard_data)
            model = Person.objects.create(**unique_data)

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

    missing_person = {
        'owner': '',
    }
    modified_person = {
        'person': 'example//2/',
        'owner': '',
    }

    missing_owner = {
        'person': 'example//1/',
    }
    modified_owner = {
        'person': 'example//1/',
        'owner': '',
    }



class ScoreCardTestData(AvaCoreTestData):
    """
    Test data for ScoreCard
    """

    @staticmethod
    def init_requirements(owner):
        # Import the required model and data
        from ava_core.game.models import Achievement
        from ava_core.game.test_data import AchievementTestData
        # Grab data for object creation, with owner if required.
        data_model = AchievementTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = Achievement.objects.filter(owner=owner['email']) if 'email' in standard_data else Achievement.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            AchievementTestData.init_requirements(owner)
            model = Achievement.objects.create(**standard_data)
            model = Achievement.objects.create(**unique_data)

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

    missing_achievement = {
        'owner': '',
    }
    modified_achievement = {
        'achievement': 'example//2/',
        'owner': '',
    }

    missing_owner = {
        'achievement': 'example//1/',
    }
    modified_owner = {
        'achievement': 'example//1/',
        'owner': '',
    }



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

    missing_friend = {
        'owner': '',
    }
    modified_friend = {
        'friend': 'default',
        'owner': '',
    }

    missing_owner = {
        'friend': 'default',
    }
    modified_owner = {
        'friend': 'default',
        'owner': '',
    }




