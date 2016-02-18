# Rest Imports
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.game.models import Achievement


# Implementation
class AchievementTestData(AvaCoreTestData):
    """
    Test data for Achievement
    """

    # Store self information
    model = Achievement
    url = 'example/'

    standard = {
        'name': 'standard_char',
        'score': 12345,
        'description': 'standard_text',
        'icon_url': 'http://example.com',
        'user_achievements': 'example//1/',
    }

    unique = {
        'name': 'unique_char',
        'score': 54321,
        'description': 'unique_text',
        'icon_url': 'http://www.example2.com',
        'user_achievements': 'example//2/',
    }
