# Rest Imports
from rest_framework import status
# Local Imports
from ava.abstract.test_data import AvaTestData
from ava_core.my.models import LearningQueue, LearningHistory, ActivityLog, LearningProfile, ScoreCard, People, Friend


# Implementation
class LearningQueueTestData(AvaTestData):
    """
    Test data for LearningQueue
    """

    model = LearningQueue
    url = '/example'

    standard = {
        'profile_queue': 'REQUIRES: ava_core.my.models.LearningProfile',
        'module': 'REQUIRES: ava_core.learn.models.Module',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
    }

    modified = {
        'profile_queue': 'REQUIRES: ava_core.my.models.LearningProfile',
        'module': 'REQUIRES: ava_core.learn.models.Module',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
    }

    modified_profile_queue = {
        'profile_queue': 'REQUIRES: ava_core.my.models.LearningProfile',
        'module': 'REQUIRES: ava_core.learn.models.Module',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
    }

    missing_profile_queue = {
        'module': 'REQUIRES: ava_core.learn.models.Module',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
    }

    missing_module = {
        'profile_queue': 'REQUIRES: ava_core.my.models.LearningProfile',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
    }

    modified_module = {
        'profile_queue': 'REQUIRES: ava_core.my.models.LearningProfile',
        'module': 'REQUIRES: ava_core.learn.models.Module',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
    }

    missing_owner = {
        'profile_queue': 'REQUIRES: ava_core.my.models.LearningProfile',
        'module': 'REQUIRES: ava_core.learn.models.Module',
    }

    modified_owner = {
        'profile_queue': 'REQUIRES: ava_core.my.models.LearningProfile',
        'module': 'REQUIRES: ava_core.learn.models.Module',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
    }



class LearningHistoryTestData(AvaTestData):
    """
    Test data for LearningHistory
    """

    model = LearningHistory
    url = '/example'

    standard = {
        'completed': True,
        'module': 'REQUIRES: ava_core.learn.models.Module',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'score': 12345,
        'profile_history': 'REQUIRES: ava_core.my.models.LearningProfile',
    }

    modified = {
        'completed': True,
        'module': 'REQUIRES: ava_core.learn.models.Module',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'score': 12345,
        'profile_history': 'REQUIRES: ava_core.my.models.LearningProfile',
    }

    modified_completed = {
        'completed': False,
        'module': 'REQUIRES: ava_core.learn.models.Module',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'score': 12345,
        'profile_history': 'REQUIRES: ava_core.my.models.LearningProfile',
    }

    missing_completed = {
        'module': 'REQUIRES: ava_core.learn.models.Module',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'score': 12345,
        'profile_history': 'REQUIRES: ava_core.my.models.LearningProfile',
    }

    missing_module = {
        'completed': True,
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'score': 12345,
        'profile_history': 'REQUIRES: ava_core.my.models.LearningProfile',
    }

    modified_module = {
        'completed': True,
        'module': 'REQUIRES: ava_core.learn.models.Module',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'score': 12345,
        'profile_history': 'REQUIRES: ava_core.my.models.LearningProfile',
    }

    missing_owner = {
        'completed': True,
        'module': 'REQUIRES: ava_core.learn.models.Module',
        'score': 12345,
        'profile_history': 'REQUIRES: ava_core.my.models.LearningProfile',
    }

    modified_owner = {
        'completed': True,
        'module': 'REQUIRES: ava_core.learn.models.Module',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'score': 12345,
        'profile_history': 'REQUIRES: ava_core.my.models.LearningProfile',
    }

    modified_score = {
        'completed': True,
        'module': 'REQUIRES: ava_core.learn.models.Module',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'score': 54321,
        'profile_history': 'REQUIRES: ava_core.my.models.LearningProfile',
    }

    missing_score = {
        'completed': True,
        'module': 'REQUIRES: ava_core.learn.models.Module',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'profile_history': 'REQUIRES: ava_core.my.models.LearningProfile',
    }

    missing_profile_history = {
        'completed': True,
        'module': 'REQUIRES: ava_core.learn.models.Module',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'score': 12345,
    }

    modified_profile_history = {
        'completed': True,
        'module': 'REQUIRES: ava_core.learn.models.Module',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'score': 12345,
        'profile_history': 'REQUIRES: ava_core.my.models.LearningProfile',
    }



class ActivityLogTestData(AvaTestData):
    """
    Test data for ActivityLog
    """

    model = ActivityLog
    url = '/example'

    standard = {
        'log_entry': 'standard_char',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
    }

    modified = {
        'log_entry': 'standard_char',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
    }

    missing_log_entry = {
        'owner': 'REQUIRES: django.contrib.auth.models.User',
    }

    modified_log_entry = {
        'log_entry': 'modified_char',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
    }

    missing_owner = {
        'log_entry': 'standard_char',
    }

    modified_owner = {
        'log_entry': 'standard_char',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
    }



class LearningProfileTestData(AvaTestData):
    """
    Test data for LearningProfile
    """

    model = LearningProfile
    url = '/example'

    standard = {
        'learning_queue': 'REQUIRES: ava_core.my.models.LearningQueue',
        'role': 'REQUIRES: ava_core.learn.models.Role',
        'learning_history': 'REQUIRES: ava_core.my.models.LearningHistory',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
    }

    modified = {
        'learning_queue': 'REQUIRES: ava_core.my.models.LearningQueue',
        'role': 'REQUIRES: ava_core.learn.models.Role',
        'learning_history': 'REQUIRES: ava_core.my.models.LearningHistory',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
    }

    modified_learning_queue = {
        'learning_queue': 'REQUIRES: ava_core.my.models.LearningQueue',
        'role': 'REQUIRES: ava_core.learn.models.Role',
        'learning_history': 'REQUIRES: ava_core.my.models.LearningHistory',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
    }

    missing_learning_queue = {
        'role': 'REQUIRES: ava_core.learn.models.Role',
        'learning_history': 'REQUIRES: ava_core.my.models.LearningHistory',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
    }

    missing_role = {
        'learning_queue': 'REQUIRES: ava_core.my.models.LearningQueue',
        'learning_history': 'REQUIRES: ava_core.my.models.LearningHistory',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
    }

    modified_role = {
        'learning_queue': 'REQUIRES: ava_core.my.models.LearningQueue',
        'role': 'REQUIRES: ava_core.learn.models.Role',
        'learning_history': 'REQUIRES: ava_core.my.models.LearningHistory',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
    }

    modified_learning_history = {
        'learning_queue': 'REQUIRES: ava_core.my.models.LearningQueue',
        'role': 'REQUIRES: ava_core.learn.models.Role',
        'learning_history': 'REQUIRES: ava_core.my.models.LearningHistory',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
    }

    missing_learning_history = {
        'learning_queue': 'REQUIRES: ava_core.my.models.LearningQueue',
        'role': 'REQUIRES: ava_core.learn.models.Role',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
    }

    missing_owner = {
        'learning_queue': 'REQUIRES: ava_core.my.models.LearningQueue',
        'role': 'REQUIRES: ava_core.learn.models.Role',
        'learning_history': 'REQUIRES: ava_core.my.models.LearningHistory',
    }

    modified_owner = {
        'learning_queue': 'REQUIRES: ava_core.my.models.LearningQueue',
        'role': 'REQUIRES: ava_core.learn.models.Role',
        'learning_history': 'REQUIRES: ava_core.my.models.LearningHistory',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
    }



class ScoreCardTestData(AvaTestData):
    """
    Test data for ScoreCard
    """

    model = ScoreCard
    url = '/example'

    standard = {
        'achievement': 'REQUIRES: ava_core.game.models.Achievement',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
    }

    modified = {
        'achievement': 'REQUIRES: ava_core.game.models.Achievement',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
    }

    missing_achievement = {
        'owner': 'REQUIRES: django.contrib.auth.models.User',
    }

    modified_achievement = {
        'achievement': 'REQUIRES: ava_core.game.models.Achievement',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
    }

    missing_owner = {
        'achievement': 'REQUIRES: ava_core.game.models.Achievement',
    }

    modified_owner = {
        'achievement': 'REQUIRES: ava_core.game.models.Achievement',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
    }



class PeopleTestData(AvaTestData):
    """
    Test data for People
    """

    model = People
    url = '/example'

    standard = {
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'person': 'REQUIRES: ava_core.organize.models.Person',
    }

    modified = {
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'person': 'REQUIRES: ava_core.organize.models.Person',
    }

    missing_owner = {
        'person': 'REQUIRES: ava_core.organize.models.Person',
    }

    modified_owner = {
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'person': 'REQUIRES: ava_core.organize.models.Person',
    }

    modified_person = {
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'person': 'REQUIRES: ava_core.organize.models.Person',
    }

    missing_person = {
        'owner': 'REQUIRES: django.contrib.auth.models.User',
    }



class FriendTestData(AvaTestData):
    """
    Test data for Friend
    """

    model = Friend
    url = '/example'

    standard = {
        'friend': 'default',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
    }

    modified = {
        'friend': 'default',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
    }

    missing_friend = {
        'owner': 'REQUIRES: django.contrib.auth.models.User',
    }

    modified_friend = {
        'friend': 'default',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
    }

    missing_owner = {
        'friend': 'default',
    }

    modified_owner = {
        'friend': 'default',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
    }




