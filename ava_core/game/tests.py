# Rest Imports
# Local Imports
from ava_core.abstract.test import AvaCoreTest
from ava_core.game.test_data import AchievementTestData


# Implementation
class AchievementTest(AvaCoreTest):
    """
    Achievement Test
    """

    def setUp(self):
        # Make call to super.
        super(AchievementTest, self).setUp()

        # Set the data type.
        self.data = AchievementTestData()

    def test_achievement_create_as_user(self):
        pass

    def test_achievement_create_as_admin(self):
        pass

    def test_achievement_create_as_unauthenticated(self):
        pass

    def test_achievement_retrieve_single_as_user(self):
        pass

    def test_achievement_retrieve_all_as_user(self):
        pass

    def test_achievement_retrieve_single_as_admin(self):
        pass

    def test_achievement_retrieve_all_as_admin(self):
        pass

    def test_achievement_retrieve_single_as_unauthorized(self):
        pass

    def test_achievement_retrieve_all_as_unauthorized(self):
        pass

    def test_achievement_update_exists_as_user(self):
        pass

    def test_achievement_update_does_not_exist_as_user(self):
        pass

    def test_achievement_update_exists_as_admin(self):
        pass

    def test_achievement_update_does_not_exist_as_admin(self):
        pass

    def test_achievement_update_exists_as_unauthorized(self):
        pass

    def test_achievement_update_does_not_exist_as_unauthorized(self):
        pass

    def test_achievement_delete_does_not_exist_as_user(self):
        pass

    def test_achievement_delete_exists_as_admin(self):
        pass

    def test_achievement_delete_does_not_exist_as_admin(self):
        pass

    def test_achievement_delete_exists_as_unauthorized(self):
        pass

    def test_achievement_delete_does_not_exist_as_unauthorized(self):
        pass
