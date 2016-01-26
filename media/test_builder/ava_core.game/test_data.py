# Rest Imports
from rest_framework import status
# Local Imports
from ava.abstract.test_data import AvaTestData
from ava_core.game.models import Achievement


# Implementation
class AchievementTestData(AvaTestData):
    """
    Test data for Achievement
    """

    model = Achievement
    url = '/example'

    standard = {
        'score': 12345,
        'icon_url': 'standard_char',
        'name': 'standard_char',
        'user_achievements': 'REQUIRES: ava_core.my.models.ScoreCard',
        'description': 'standard_text',
    }

    modified = {
        'score': 12345,
        'icon_url': 'standard_char',
        'name': 'standard_char',
        'user_achievements': 'REQUIRES: ava_core.my.models.ScoreCard',
        'description': 'standard_text',
    }

    modified_score = {
        'score': 54321,
        'icon_url': 'standard_char',
        'name': 'standard_char',
        'user_achievements': 'REQUIRES: ava_core.my.models.ScoreCard',
        'description': 'standard_text',
    }

    missing_score = {
        'icon_url': 'standard_char',
        'name': 'standard_char',
        'user_achievements': 'REQUIRES: ava_core.my.models.ScoreCard',
        'description': 'standard_text',
    }

    missing_icon_url = {
        'score': 12345,
        'name': 'standard_char',
        'user_achievements': 'REQUIRES: ava_core.my.models.ScoreCard',
        'description': 'standard_text',
    }

    modified_icon_url = {
        'score': 12345,
        'icon_url': 'modified_char',
        'name': 'standard_char',
        'user_achievements': 'REQUIRES: ava_core.my.models.ScoreCard',
        'description': 'standard_text',
    }

    modified_name = {
        'score': 12345,
        'icon_url': 'standard_char',
        'name': 'modified_char',
        'user_achievements': 'REQUIRES: ava_core.my.models.ScoreCard',
        'description': 'standard_text',
    }

    missing_name = {
        'score': 12345,
        'icon_url': 'standard_char',
        'user_achievements': 'REQUIRES: ava_core.my.models.ScoreCard',
        'description': 'standard_text',
    }

    missing_user_achievements = {
        'score': 12345,
        'icon_url': 'standard_char',
        'name': 'standard_char',
        'description': 'standard_text',
    }

    modified_user_achievements = {
        'score': 12345,
        'icon_url': 'standard_char',
        'name': 'standard_char',
        'user_achievements': 'REQUIRES: ava_core.my.models.ScoreCard',
        'description': 'standard_text',
    }

    modified_description = {
        'score': 12345,
        'icon_url': 'standard_char',
        'name': 'standard_char',
        'user_achievements': 'REQUIRES: ava_core.my.models.ScoreCard',
        'description': 'modified_text',
    }

    missing_description = {
        'score': 12345,
        'icon_url': 'standard_char',
        'name': 'standard_char',
        'user_achievements': 'REQUIRES: ava_core.my.models.ScoreCard',
    }




