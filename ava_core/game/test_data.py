# Rest Imports
from rest_framework import status
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.game.models import Achievement


# Implementation
class AchievementTestData(AvaCoreTestData):
    """
    Test data for Achievement
    """

    @staticmethod
    def init_requirements():
        # Import the required model and data
        from ava_core.my.models import ScoreCard
        from ava_core.my.test_data import ScoreCardTestData
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if ScoreCard.objects.count() == 0:
            ScoreCardTestData.init_requirements()
            model = ScoreCard.objects.create(**ScoreCardTestData.get_data('standard'))
            model.save()
            model = ScoreCard.objects.create(**ScoreCardTestData.get_data('unique'))
            model.save()

    # Store self information
    model = Achievement
    url = '/example'

    standard = {
        'user_achievements': '/example/1/',
        'icon_url': 'standard_char',
        'description': 'standard_text',
        'score': 12345,
        'name': 'standard_char',
    }

    unique = {
        'user_achievements': '/example/2/',
        'icon_url': 'unique_char',
        'description': 'unique_text',
        'score': 54321,
        'name': 'unique_char',
    }

    missing_user_achievements = {
        'icon_url': 'standard_char',
        'description': 'standard_text',
        'score': 12345,
        'name': 'standard_char',
    }
    modified_user_achievements = {
        'user_achievements': '/example/2/',
        'icon_url': 'standard_char',
        'description': 'standard_text',
        'score': 12345,
        'name': 'standard_char',
    }

    modified_icon_url = {
        'user_achievements': '/example/1/',
        'icon_url': 'modified_char',
        'description': 'standard_text',
        'score': 12345,
        'name': 'standard_char',
    }
    missing_icon_url = {
        'user_achievements': '/example/1/',
        'description': 'standard_text',
        'score': 12345,
        'name': 'standard_char',
    }

    modified_description = {
        'user_achievements': '/example/1/',
        'icon_url': 'standard_char',
        'description': 'modified_text',
        'score': 12345,
        'name': 'standard_char',
    }
    missing_description = {
        'user_achievements': '/example/1/',
        'icon_url': 'standard_char',
        'score': 12345,
        'name': 'standard_char',
    }

    missing_score = {
        'user_achievements': '/example/1/',
        'icon_url': 'standard_char',
        'description': 'standard_text',
        'name': 'standard_char',
    }
    modified_score = {
        'user_achievements': '/example/1/',
        'icon_url': 'standard_char',
        'description': 'standard_text',
        'score': 54321,
        'name': 'standard_char',
    }

    modified_name = {
        'user_achievements': '/example/1/',
        'icon_url': 'standard_char',
        'description': 'standard_text',
        'score': 12345,
        'name': 'modified_char',
    }
    missing_name = {
        'user_achievements': '/example/1/',
        'icon_url': 'standard_char',
        'description': 'standard_text',
        'score': 12345,
    }




