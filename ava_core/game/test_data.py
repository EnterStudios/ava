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
    def init_requirements(owner):
        # Import the required model and data
        from ava_core.my.models import ScoreCard
        from ava_core.my.test_data import ScoreCardTestData
        # Grab data for object creation, with owner if required.
        data_model = ScoreCardTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = ScoreCard.objects.filter(owner=owner['email']) if 'email' in standard_data else ScoreCard.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            ScoreCardTestData.init_requirements(owner)
            model = ScoreCard.objects.create(**standard_data)
            model = ScoreCard.objects.create(**unique_data)

    # Store self information
    model = Achievement
    url = 'example/'

    standard = {
        'name': 'standard_char',
        'score': 12345,
        'description': 'standard_text',
        'icon_url': 'standard_char',
        'user_achievements': 'example//1/',
    }

    unique = {
        'name': 'unique_char',
        'score': 54321,
        'description': 'unique_text',
        'icon_url': 'unique_char',
        'user_achievements': 'example//2/',
    }

    modified_name = {
        'name': 'modified_char',
        'score': 12345,
        'description': 'standard_text',
        'icon_url': 'standard_char',
        'user_achievements': 'example//1/',
    }
    missing_name = {
        'score': 12345,
        'description': 'standard_text',
        'icon_url': 'standard_char',
        'user_achievements': 'example//1/',
    }

    missing_score = {
        'name': 'standard_char',
        'description': 'standard_text',
        'icon_url': 'standard_char',
        'user_achievements': 'example//1/',
    }
    modified_score = {
        'name': 'standard_char',
        'score': 54321,
        'description': 'standard_text',
        'icon_url': 'standard_char',
        'user_achievements': 'example//1/',
    }

    missing_description = {
        'name': 'standard_char',
        'score': 12345,
        'icon_url': 'standard_char',
        'user_achievements': 'example//1/',
    }
    modified_description = {
        'name': 'standard_char',
        'score': 12345,
        'description': 'modified_text',
        'icon_url': 'standard_char',
        'user_achievements': 'example//1/',
    }

    missing_icon_url = {
        'name': 'standard_char',
        'score': 12345,
        'description': 'standard_text',
        'user_achievements': 'example//1/',
    }
    modified_icon_url = {
        'name': 'standard_char',
        'score': 12345,
        'description': 'standard_text',
        'icon_url': 'modified_char',
        'user_achievements': 'example//1/',
    }

    missing_user_achievements = {
        'name': 'standard_char',
        'score': 12345,
        'description': 'standard_text',
        'icon_url': 'standard_char',
    }
    modified_user_achievements = {
        'name': 'standard_char',
        'score': 12345,
        'description': 'standard_text',
        'icon_url': 'standard_char',
        'user_achievements': 'example//2/',
    }




