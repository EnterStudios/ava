# Rest Imports
from rest_framework import status
# Local Imports
from ava_core.abstract.tests import AvaTest
from ava_core.my.models import LearningQueue, LearningHistory, ActivityLog, LearningProfile, ScoreCard, People, Friend
from ava_core.my.test_data import LearningQueueTestData, LearningHistoryTestData, ActivityLogTestData, LearningProfileTestData, ScoreCardTestData, PeopleTestData, FriendTestData


# Implementation
class LearningQueueTest(AvaTest):
    """
LearningQueue Test    """

    def setUp(self):
        # Make call to super.        super(LearningQueueTest, self).setUp()

        # Set the data type.
        self.data = LearningQueueTestData

    def test_learning_queue_create_as_user(self):
        # Log in as user.
        self.login_user(self.user_user)

        # Take count.
        count = self.data.model.objects.count()

        # Store data to use.
        data = self.data.get_data()

        # Make push request and ensure created response.
        response = self.client.push(self.format_url(self.data.url), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.data.model.objects.count(), count + 1)
        self.assertTrue(self.does_contain_data(response.data, data))

    def test_learning_queue_create_as_admin(self):
        # Log in as admin.
        self.login_user(self.user_admin)

        # Take count.
        count = self.data.model.objects.count()

        # Store data to use.
        data = self.data.get_data()

        # Make push request and ensure created response.
        response = self.client.push(self.format_url(self.data.url), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.data.model.objects.count(), count + 1)
        self.assertTrue(self.does_contain_data(response.data, data))

    def test_learning_queue_create_as_unauthenticated(self):
        # Take count.
        count = self.data.model.objects.count()

        # Store data to use.
        data = self.data.get_data()

        # Make push request and ensure unauthorized response.
        response = self.client.push(self.format_url(self.data.url), data, format='json')
        self.assertIn(response.status_code, self.status_forbidden)
        self.assertEqual(self.data.model.objects.count(), count)

    def test_learning_queue_retrieve_single_as_user(self):
        # Create new LearningQueue models, storing URL.
        url = self.create_model_logout(self.data, 'standard', self.user_user)

        # Log in as user.
        self.login_user(self.user_user)

        # Make get request and ensure OK response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data(response.data, self.data.standard))


    def test_learning_queue_retrieve_all_as_user(self):
        # Create new LearningQueue models.
        self.create_model_logout(self.data, 'standard', self.user_user)
        self.create_model_logout(self.data, 'modified', self.user_user)

        # Log in as user.
        self.login_user(self.user_user)

        # Make get request and ensure OK response
        response = self.client.get(self.format_url(self.data.url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_list(response.data['results'], [self.data.standard, self.data.modified]))


    def test_learning_queue_retrieve_single_as_admin(self):
        # Create new LearningQueue models, storing URL.
        url = self.create_model_logout(self.data, 'standard', self.user_admin)

        # Log in as admin.
        self.login_user(self.user_admin)

        # Make get request and ensure OK response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data(response.data, self.data.standard))


    def test_learning_queue_retrieve_all_as_admin(self):
        # Create new LearningQueue models.
        self.create_model_logout(self.data, 'standard', self.user_admin)
        self.create_model_logout(self.data, 'modified', self.user_admin)

        # Log in as admin.
        self.login_user(self.user_admin)

        # Make get request and ensure OK response
        response = self.client.get(self.format_url(self.data.url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_list(response.data['results'], [self.data.standard, self.data.modified]))


    def test_learning_queue_retrieve_single_as_unauthorized(self):
        # Create new LearningQueue models, storing URL.
        url = self.create_model_logout(self.data, 'standard', self.user_admin)

        # Make get request and ensure unauthorized response
        response = self.client.get(url)
        self.assertIn(response.status_code, self.status_forbidden)


    def test_learning_queue_retrieve_all_as_unauthorized(self):
        # Create new LearningQueue models.
        self.create_model_logout(self.data, 'standard', self.user_admin)
        self.create_model_logout(self.data, 'modified', self.user_admin)

        # Make get request and ensure unauthorized response
        response = self.client.get(self.format_url(self.data.url))
        self.assertIn(response.status_code, self.status_forbidden)


    # TODO: Write update tests
    # TODO: Write delete tests


class LearningHistoryTest(AvaTest):
    """
LearningHistory Test    """

    def setUp(self):
        # Make call to super.        super(LearningHistoryTest, self).setUp()

        # Set the data type.
        self.data = LearningHistoryTestData

    def test_learning_history_create_as_user(self):
        # Log in as user.
        self.login_user(self.user_user)

        # Take count.
        count = self.data.model.objects.count()

        # Store data to use.
        data = self.data.get_data()

        # Make push request and ensure created response.
        response = self.client.push(self.format_url(self.data.url), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.data.model.objects.count(), count + 1)
        self.assertTrue(self.does_contain_data(response.data, data))

    def test_learning_history_create_as_admin(self):
        # Log in as admin.
        self.login_user(self.user_admin)

        # Take count.
        count = self.data.model.objects.count()

        # Store data to use.
        data = self.data.get_data()

        # Make push request and ensure created response.
        response = self.client.push(self.format_url(self.data.url), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.data.model.objects.count(), count + 1)
        self.assertTrue(self.does_contain_data(response.data, data))

    def test_learning_history_create_as_unauthenticated(self):
        # Take count.
        count = self.data.model.objects.count()

        # Store data to use.
        data = self.data.get_data()

        # Make push request and ensure unauthorized response.
        response = self.client.push(self.format_url(self.data.url), data, format='json')
        self.assertIn(response.status_code, self.status_forbidden)
        self.assertEqual(self.data.model.objects.count(), count)

    def test_learning_history_retrieve_single_as_user(self):
        # Create new LearningHistory models, storing URL.
        url = self.create_model_logout(self.data, 'standard', self.user_user)

        # Log in as user.
        self.login_user(self.user_user)

        # Make get request and ensure OK response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data(response.data, self.data.standard))


    def test_learning_history_retrieve_all_as_user(self):
        # Create new LearningHistory models.
        self.create_model_logout(self.data, 'standard', self.user_user)
        self.create_model_logout(self.data, 'modified', self.user_user)

        # Log in as user.
        self.login_user(self.user_user)

        # Make get request and ensure OK response
        response = self.client.get(self.format_url(self.data.url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_list(response.data['results'], [self.data.standard, self.data.modified]))


    def test_learning_history_retrieve_single_as_admin(self):
        # Create new LearningHistory models, storing URL.
        url = self.create_model_logout(self.data, 'standard', self.user_admin)

        # Log in as admin.
        self.login_user(self.user_admin)

        # Make get request and ensure OK response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data(response.data, self.data.standard))


    def test_learning_history_retrieve_all_as_admin(self):
        # Create new LearningHistory models.
        self.create_model_logout(self.data, 'standard', self.user_admin)
        self.create_model_logout(self.data, 'modified', self.user_admin)

        # Log in as admin.
        self.login_user(self.user_admin)

        # Make get request and ensure OK response
        response = self.client.get(self.format_url(self.data.url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_list(response.data['results'], [self.data.standard, self.data.modified]))


    def test_learning_history_retrieve_single_as_unauthorized(self):
        # Create new LearningHistory models, storing URL.
        url = self.create_model_logout(self.data, 'standard', self.user_admin)

        # Make get request and ensure unauthorized response
        response = self.client.get(url)
        self.assertIn(response.status_code, self.status_forbidden)


    def test_learning_history_retrieve_all_as_unauthorized(self):
        # Create new LearningHistory models.
        self.create_model_logout(self.data, 'standard', self.user_admin)
        self.create_model_logout(self.data, 'modified', self.user_admin)

        # Make get request and ensure unauthorized response
        response = self.client.get(self.format_url(self.data.url))
        self.assertIn(response.status_code, self.status_forbidden)


    # TODO: Write update tests
    # TODO: Write delete tests


class ActivityLogTest(AvaTest):
    """
ActivityLog Test    """

    def setUp(self):
        # Make call to super.        super(ActivityLogTest, self).setUp()

        # Set the data type.
        self.data = ActivityLogTestData

    def test_activity_log_create_as_user(self):
        # Log in as user.
        self.login_user(self.user_user)

        # Take count.
        count = self.data.model.objects.count()

        # Store data to use.
        data = self.data.get_data()

        # Make push request and ensure created response.
        response = self.client.push(self.format_url(self.data.url), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.data.model.objects.count(), count + 1)
        self.assertTrue(self.does_contain_data(response.data, data))

    def test_activity_log_create_as_admin(self):
        # Log in as admin.
        self.login_user(self.user_admin)

        # Take count.
        count = self.data.model.objects.count()

        # Store data to use.
        data = self.data.get_data()

        # Make push request and ensure created response.
        response = self.client.push(self.format_url(self.data.url), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.data.model.objects.count(), count + 1)
        self.assertTrue(self.does_contain_data(response.data, data))

    def test_activity_log_create_as_unauthenticated(self):
        # Take count.
        count = self.data.model.objects.count()

        # Store data to use.
        data = self.data.get_data()

        # Make push request and ensure unauthorized response.
        response = self.client.push(self.format_url(self.data.url), data, format='json')
        self.assertIn(response.status_code, self.status_forbidden)
        self.assertEqual(self.data.model.objects.count(), count)

    def test_activity_log_retrieve_single_as_user(self):
        # Create new ActivityLog models, storing URL.
        url = self.create_model_logout(self.data, 'standard', self.user_user)

        # Log in as user.
        self.login_user(self.user_user)

        # Make get request and ensure OK response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data(response.data, self.data.standard))


    def test_activity_log_retrieve_all_as_user(self):
        # Create new ActivityLog models.
        self.create_model_logout(self.data, 'standard', self.user_user)
        self.create_model_logout(self.data, 'modified', self.user_user)

        # Log in as user.
        self.login_user(self.user_user)

        # Make get request and ensure OK response
        response = self.client.get(self.format_url(self.data.url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_list(response.data['results'], [self.data.standard, self.data.modified]))


    def test_activity_log_retrieve_single_as_admin(self):
        # Create new ActivityLog models, storing URL.
        url = self.create_model_logout(self.data, 'standard', self.user_admin)

        # Log in as admin.
        self.login_user(self.user_admin)

        # Make get request and ensure OK response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data(response.data, self.data.standard))


    def test_activity_log_retrieve_all_as_admin(self):
        # Create new ActivityLog models.
        self.create_model_logout(self.data, 'standard', self.user_admin)
        self.create_model_logout(self.data, 'modified', self.user_admin)

        # Log in as admin.
        self.login_user(self.user_admin)

        # Make get request and ensure OK response
        response = self.client.get(self.format_url(self.data.url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_list(response.data['results'], [self.data.standard, self.data.modified]))


    def test_activity_log_retrieve_single_as_unauthorized(self):
        # Create new ActivityLog models, storing URL.
        url = self.create_model_logout(self.data, 'standard', self.user_admin)

        # Make get request and ensure unauthorized response
        response = self.client.get(url)
        self.assertIn(response.status_code, self.status_forbidden)


    def test_activity_log_retrieve_all_as_unauthorized(self):
        # Create new ActivityLog models.
        self.create_model_logout(self.data, 'standard', self.user_admin)
        self.create_model_logout(self.data, 'modified', self.user_admin)

        # Make get request and ensure unauthorized response
        response = self.client.get(self.format_url(self.data.url))
        self.assertIn(response.status_code, self.status_forbidden)


    # TODO: Write update tests
    # TODO: Write delete tests


class LearningProfileTest(AvaTest):
    """
LearningProfile Test    """

    def setUp(self):
        # Make call to super.        super(LearningProfileTest, self).setUp()

        # Set the data type.
        self.data = LearningProfileTestData

    def test_learning_profile_create_as_user(self):
        # Log in as user.
        self.login_user(self.user_user)

        # Take count.
        count = self.data.model.objects.count()

        # Store data to use.
        data = self.data.get_data()

        # Make push request and ensure created response.
        response = self.client.push(self.format_url(self.data.url), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.data.model.objects.count(), count + 1)
        self.assertTrue(self.does_contain_data(response.data, data))

    def test_learning_profile_create_as_admin(self):
        # Log in as admin.
        self.login_user(self.user_admin)

        # Take count.
        count = self.data.model.objects.count()

        # Store data to use.
        data = self.data.get_data()

        # Make push request and ensure created response.
        response = self.client.push(self.format_url(self.data.url), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.data.model.objects.count(), count + 1)
        self.assertTrue(self.does_contain_data(response.data, data))

    def test_learning_profile_create_as_unauthenticated(self):
        # Take count.
        count = self.data.model.objects.count()

        # Store data to use.
        data = self.data.get_data()

        # Make push request and ensure unauthorized response.
        response = self.client.push(self.format_url(self.data.url), data, format='json')
        self.assertIn(response.status_code, self.status_forbidden)
        self.assertEqual(self.data.model.objects.count(), count)

    def test_learning_profile_retrieve_single_as_user(self):
        # Create new LearningProfile models, storing URL.
        url = self.create_model_logout(self.data, 'standard', self.user_user)

        # Log in as user.
        self.login_user(self.user_user)

        # Make get request and ensure OK response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data(response.data, self.data.standard))


    def test_learning_profile_retrieve_all_as_user(self):
        # Create new LearningProfile models.
        self.create_model_logout(self.data, 'standard', self.user_user)
        self.create_model_logout(self.data, 'modified', self.user_user)

        # Log in as user.
        self.login_user(self.user_user)

        # Make get request and ensure OK response
        response = self.client.get(self.format_url(self.data.url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_list(response.data['results'], [self.data.standard, self.data.modified]))


    def test_learning_profile_retrieve_single_as_admin(self):
        # Create new LearningProfile models, storing URL.
        url = self.create_model_logout(self.data, 'standard', self.user_admin)

        # Log in as admin.
        self.login_user(self.user_admin)

        # Make get request and ensure OK response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data(response.data, self.data.standard))


    def test_learning_profile_retrieve_all_as_admin(self):
        # Create new LearningProfile models.
        self.create_model_logout(self.data, 'standard', self.user_admin)
        self.create_model_logout(self.data, 'modified', self.user_admin)

        # Log in as admin.
        self.login_user(self.user_admin)

        # Make get request and ensure OK response
        response = self.client.get(self.format_url(self.data.url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_list(response.data['results'], [self.data.standard, self.data.modified]))


    def test_learning_profile_retrieve_single_as_unauthorized(self):
        # Create new LearningProfile models, storing URL.
        url = self.create_model_logout(self.data, 'standard', self.user_admin)

        # Make get request and ensure unauthorized response
        response = self.client.get(url)
        self.assertIn(response.status_code, self.status_forbidden)


    def test_learning_profile_retrieve_all_as_unauthorized(self):
        # Create new LearningProfile models.
        self.create_model_logout(self.data, 'standard', self.user_admin)
        self.create_model_logout(self.data, 'modified', self.user_admin)

        # Make get request and ensure unauthorized response
        response = self.client.get(self.format_url(self.data.url))
        self.assertIn(response.status_code, self.status_forbidden)


    # TODO: Write update tests
    # TODO: Write delete tests


class ScoreCardTest(AvaTest):
    """
ScoreCard Test    """

    def setUp(self):
        # Make call to super.        super(ScoreCardTest, self).setUp()

        # Set the data type.
        self.data = ScoreCardTestData

    def test_score_card_create_as_user(self):
        # Log in as user.
        self.login_user(self.user_user)

        # Take count.
        count = self.data.model.objects.count()

        # Store data to use.
        data = self.data.get_data()

        # Make push request and ensure created response.
        response = self.client.push(self.format_url(self.data.url), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.data.model.objects.count(), count + 1)
        self.assertTrue(self.does_contain_data(response.data, data))

    def test_score_card_create_as_admin(self):
        # Log in as admin.
        self.login_user(self.user_admin)

        # Take count.
        count = self.data.model.objects.count()

        # Store data to use.
        data = self.data.get_data()

        # Make push request and ensure created response.
        response = self.client.push(self.format_url(self.data.url), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.data.model.objects.count(), count + 1)
        self.assertTrue(self.does_contain_data(response.data, data))

    def test_score_card_create_as_unauthenticated(self):
        # Take count.
        count = self.data.model.objects.count()

        # Store data to use.
        data = self.data.get_data()

        # Make push request and ensure unauthorized response.
        response = self.client.push(self.format_url(self.data.url), data, format='json')
        self.assertIn(response.status_code, self.status_forbidden)
        self.assertEqual(self.data.model.objects.count(), count)

    def test_score_card_retrieve_single_as_user(self):
        # Create new ScoreCard models, storing URL.
        url = self.create_model_logout(self.data, 'standard', self.user_user)

        # Log in as user.
        self.login_user(self.user_user)

        # Make get request and ensure OK response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data(response.data, self.data.standard))


    def test_score_card_retrieve_all_as_user(self):
        # Create new ScoreCard models.
        self.create_model_logout(self.data, 'standard', self.user_user)
        self.create_model_logout(self.data, 'modified', self.user_user)

        # Log in as user.
        self.login_user(self.user_user)

        # Make get request and ensure OK response
        response = self.client.get(self.format_url(self.data.url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_list(response.data['results'], [self.data.standard, self.data.modified]))


    def test_score_card_retrieve_single_as_admin(self):
        # Create new ScoreCard models, storing URL.
        url = self.create_model_logout(self.data, 'standard', self.user_admin)

        # Log in as admin.
        self.login_user(self.user_admin)

        # Make get request and ensure OK response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data(response.data, self.data.standard))


    def test_score_card_retrieve_all_as_admin(self):
        # Create new ScoreCard models.
        self.create_model_logout(self.data, 'standard', self.user_admin)
        self.create_model_logout(self.data, 'modified', self.user_admin)

        # Log in as admin.
        self.login_user(self.user_admin)

        # Make get request and ensure OK response
        response = self.client.get(self.format_url(self.data.url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_list(response.data['results'], [self.data.standard, self.data.modified]))


    def test_score_card_retrieve_single_as_unauthorized(self):
        # Create new ScoreCard models, storing URL.
        url = self.create_model_logout(self.data, 'standard', self.user_admin)

        # Make get request and ensure unauthorized response
        response = self.client.get(url)
        self.assertIn(response.status_code, self.status_forbidden)


    def test_score_card_retrieve_all_as_unauthorized(self):
        # Create new ScoreCard models.
        self.create_model_logout(self.data, 'standard', self.user_admin)
        self.create_model_logout(self.data, 'modified', self.user_admin)

        # Make get request and ensure unauthorized response
        response = self.client.get(self.format_url(self.data.url))
        self.assertIn(response.status_code, self.status_forbidden)


    # TODO: Write update tests
    # TODO: Write delete tests


class PeopleTest(AvaTest):
    """
People Test    """

    def setUp(self):
        # Make call to super.        super(PeopleTest, self).setUp()

        # Set the data type.
        self.data = PeopleTestData

    def test_people_create_as_user(self):
        # Log in as user.
        self.login_user(self.user_user)

        # Take count.
        count = self.data.model.objects.count()

        # Store data to use.
        data = self.data.get_data()

        # Make push request and ensure created response.
        response = self.client.push(self.format_url(self.data.url), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.data.model.objects.count(), count + 1)
        self.assertTrue(self.does_contain_data(response.data, data))

    def test_people_create_as_admin(self):
        # Log in as admin.
        self.login_user(self.user_admin)

        # Take count.
        count = self.data.model.objects.count()

        # Store data to use.
        data = self.data.get_data()

        # Make push request and ensure created response.
        response = self.client.push(self.format_url(self.data.url), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.data.model.objects.count(), count + 1)
        self.assertTrue(self.does_contain_data(response.data, data))

    def test_people_create_as_unauthenticated(self):
        # Take count.
        count = self.data.model.objects.count()

        # Store data to use.
        data = self.data.get_data()

        # Make push request and ensure unauthorized response.
        response = self.client.push(self.format_url(self.data.url), data, format='json')
        self.assertIn(response.status_code, self.status_forbidden)
        self.assertEqual(self.data.model.objects.count(), count)

    def test_people_retrieve_single_as_user(self):
        # Create new People models, storing URL.
        url = self.create_model_logout(self.data, 'standard', self.user_user)

        # Log in as user.
        self.login_user(self.user_user)

        # Make get request and ensure OK response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data(response.data, self.data.standard))


    def test_people_retrieve_all_as_user(self):
        # Create new People models.
        self.create_model_logout(self.data, 'standard', self.user_user)
        self.create_model_logout(self.data, 'modified', self.user_user)

        # Log in as user.
        self.login_user(self.user_user)

        # Make get request and ensure OK response
        response = self.client.get(self.format_url(self.data.url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_list(response.data['results'], [self.data.standard, self.data.modified]))


    def test_people_retrieve_single_as_admin(self):
        # Create new People models, storing URL.
        url = self.create_model_logout(self.data, 'standard', self.user_admin)

        # Log in as admin.
        self.login_user(self.user_admin)

        # Make get request and ensure OK response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data(response.data, self.data.standard))


    def test_people_retrieve_all_as_admin(self):
        # Create new People models.
        self.create_model_logout(self.data, 'standard', self.user_admin)
        self.create_model_logout(self.data, 'modified', self.user_admin)

        # Log in as admin.
        self.login_user(self.user_admin)

        # Make get request and ensure OK response
        response = self.client.get(self.format_url(self.data.url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_list(response.data['results'], [self.data.standard, self.data.modified]))


    def test_people_retrieve_single_as_unauthorized(self):
        # Create new People models, storing URL.
        url = self.create_model_logout(self.data, 'standard', self.user_admin)

        # Make get request and ensure unauthorized response
        response = self.client.get(url)
        self.assertIn(response.status_code, self.status_forbidden)


    def test_people_retrieve_all_as_unauthorized(self):
        # Create new People models.
        self.create_model_logout(self.data, 'standard', self.user_admin)
        self.create_model_logout(self.data, 'modified', self.user_admin)

        # Make get request and ensure unauthorized response
        response = self.client.get(self.format_url(self.data.url))
        self.assertIn(response.status_code, self.status_forbidden)


    # TODO: Write update tests
    # TODO: Write delete tests


class FriendTest(AvaTest):
    """
Friend Test    """

    def setUp(self):
        # Make call to super.        super(FriendTest, self).setUp()

        # Set the data type.
        self.data = FriendTestData

    def test_friend_create_as_user(self):
        # Log in as user.
        self.login_user(self.user_user)

        # Take count.
        count = self.data.model.objects.count()

        # Store data to use.
        data = self.data.get_data()

        # Make push request and ensure created response.
        response = self.client.push(self.format_url(self.data.url), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.data.model.objects.count(), count + 1)
        self.assertTrue(self.does_contain_data(response.data, data))

    def test_friend_create_as_admin(self):
        # Log in as admin.
        self.login_user(self.user_admin)

        # Take count.
        count = self.data.model.objects.count()

        # Store data to use.
        data = self.data.get_data()

        # Make push request and ensure created response.
        response = self.client.push(self.format_url(self.data.url), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.data.model.objects.count(), count + 1)
        self.assertTrue(self.does_contain_data(response.data, data))

    def test_friend_create_as_unauthenticated(self):
        # Take count.
        count = self.data.model.objects.count()

        # Store data to use.
        data = self.data.get_data()

        # Make push request and ensure unauthorized response.
        response = self.client.push(self.format_url(self.data.url), data, format='json')
        self.assertIn(response.status_code, self.status_forbidden)
        self.assertEqual(self.data.model.objects.count(), count)

    def test_friend_retrieve_single_as_user(self):
        # Create new Friend models, storing URL.
        url = self.create_model_logout(self.data, 'standard', self.user_user)

        # Log in as user.
        self.login_user(self.user_user)

        # Make get request and ensure OK response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data(response.data, self.data.standard))


    def test_friend_retrieve_all_as_user(self):
        # Create new Friend models.
        self.create_model_logout(self.data, 'standard', self.user_user)
        self.create_model_logout(self.data, 'modified', self.user_user)

        # Log in as user.
        self.login_user(self.user_user)

        # Make get request and ensure OK response
        response = self.client.get(self.format_url(self.data.url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_list(response.data['results'], [self.data.standard, self.data.modified]))


    def test_friend_retrieve_single_as_admin(self):
        # Create new Friend models, storing URL.
        url = self.create_model_logout(self.data, 'standard', self.user_admin)

        # Log in as admin.
        self.login_user(self.user_admin)

        # Make get request and ensure OK response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data(response.data, self.data.standard))


    def test_friend_retrieve_all_as_admin(self):
        # Create new Friend models.
        self.create_model_logout(self.data, 'standard', self.user_admin)
        self.create_model_logout(self.data, 'modified', self.user_admin)

        # Log in as admin.
        self.login_user(self.user_admin)

        # Make get request and ensure OK response
        response = self.client.get(self.format_url(self.data.url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_list(response.data['results'], [self.data.standard, self.data.modified]))


    def test_friend_retrieve_single_as_unauthorized(self):
        # Create new Friend models, storing URL.
        url = self.create_model_logout(self.data, 'standard', self.user_admin)

        # Make get request and ensure unauthorized response
        response = self.client.get(url)
        self.assertIn(response.status_code, self.status_forbidden)


    def test_friend_retrieve_all_as_unauthorized(self):
        # Create new Friend models.
        self.create_model_logout(self.data, 'standard', self.user_admin)
        self.create_model_logout(self.data, 'modified', self.user_admin)

        # Make get request and ensure unauthorized response
        response = self.client.get(self.format_url(self.data.url))
        self.assertIn(response.status_code, self.status_forbidden)


    # TODO: Write update tests
    # TODO: Write delete tests



