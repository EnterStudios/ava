# Rest Imports
from rest_framework import status
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.game.models import Achievement
from ava_core.my.models import ScoreCard
from ava_core.my.test_data import ScoreCardTestData


# Implementation
class AchievementTestData(AvaCoreTestData):
    """
    Test data for Achievement
    """

    def __init__(self):
        # Store self information
        self.model = Achievement
        self.url = '/example'

        # Create any necessary required models.
        self.init_requirements()

    def init_requirements(self):
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if ScoreCard.objects.count() == 0:
            ScoreCardTestData.init_requirements()
            ScoreCard.objects.create(**ScoreCardTestData.get_data('standard'))
            ScoreCard.objects.create(**ScoreCardTestData.get_data('unique'))

    standard = {
        'user_achievements': '/example/1/',
        'name': 'standard_char',
        'score': 12345,
        'description': 'standard_text',
        'icon_url': 'standard_char',
    }

    unique = {
        'user_achievements': '/example/2/',
        'name': 'unique_char',
        'score': 54321,
        'description': 'unique_text',
        'icon_url': 'unique_char',
    }

    missing_user_achievements = {
        'name': 'standard_char',
        'score': 12345,
        'description': 'standard_text',
        'icon_url': 'standard_char',
    }
    modified_user_achievements = {
        'user_achievements': '/example/2/',
        'name': 'standard_char',
        'score': 12345,
        'description': 'standard_text',
        'icon_url': 'standard_char',
    }

    modified_name = {
        'user_achievements': '/example/1/',
        'name': 'modified_char',
        'score': 12345,
        'description': 'standard_text',
        'icon_url': 'standard_char',
    }
    missing_name = {
        'user_achievements': '/example/1/',
        'score': 12345,
        'description': 'standard_text',
        'icon_url': 'standard_char',
    }

    missing_score = {
        'user_achievements': '/example/1/',
        'name': 'standard_char',
        'description': 'standard_text',
        'icon_url': 'standard_char',
    }
    modified_score = {
        'user_achievements': '/example/1/',
        'name': 'standard_char',
        'score': 54321,
        'description': 'standard_text',
        'icon_url': 'standard_char',
    }

    missing_description = {
        'user_achievements': '/example/1/',
        'name': 'standard_char',
        'score': 12345,
        'icon_url': 'standard_char',
    }
    modified_description = {
        'user_achievements': '/example/1/',
        'name': 'standard_char',
        'score': 12345,
        'description': 'modified_text',
        'icon_url': 'standard_char',
    }

    modified_icon_url = {
        'user_achievements': '/example/1/',
        'name': 'standard_char',
        'score': 12345,
        'description': 'standard_text',
        'icon_url': 'modified_char',
    }
    missing_icon_url = {
        'user_achievements': '/example/1/',
        'name': 'standard_char',
        'score': 12345,
        'description': 'standard_text',
    }




