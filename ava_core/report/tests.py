# Rest Imports
from rest_framework import status
# Local Imports
from ava_core.abstract.tests import AvaTest
from ava_core.report.models import Suspicious, ReportResponse, Question
from ava_core.report.test_data import SuspiciousTestData, ReportResponseTestData, QuestionTestData


# Implementation
class SuspiciousTest(AvaTest):
    """
    Suspicious Test
    """

    def setUp(self):
        # Make call to super.
        super(SuspiciousTest, self).setUp()

        # Set the data type.
        self.data = SuspiciousTestData

    def test_suspicious_create_as_user(self):
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

    def test_suspicious_create_as_admin(self):
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

    def test_suspicious_create_as_unauthenticated(self):
        # Take count.
        count = self.data.model.objects.count()

        # Store data to use.
        data = self.data.get_data()

        # Make push request and ensure unauthorized response.
        response = self.client.push(self.format_url(self.data.url), data, format='json')
        self.assertIn(response.status_code, self.status_forbidden)
        self.assertEqual(self.data.model.objects.count(), count)

    def test_suspicious_retrieve_single_as_user(self):
        # Create new Suspicious models, storing URL.
        url = self.create_model_logout(self.data, 'standard', self.user_user)

        # Log in as user.
        self.login_user(self.user_user)

        # Make get request and ensure OK response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data(response.data, self.data.standard))


    def test_suspicious_retrieve_all_as_user(self):
        # Create new Suspicious models.
        self.create_model_logout(self.data, 'standard', self.user_user)
        self.create_model_logout(self.data, 'modified', self.user_user)

        # Log in as user.
        self.login_user(self.user_user)

        # Make get request and ensure OK response
        response = self.client.get(self.format_url(self.data.url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_list(response.data['results'], [self.data.standard, self.data.modified]))


    def test_suspicious_retrieve_single_as_admin(self):
        # Create new Suspicious models, storing URL.
        url = self.create_model_logout(self.data, 'standard', self.user_admin)

        # Log in as admin.
        self.login_user(self.user_admin)

        # Make get request and ensure OK response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data(response.data, self.data.standard))


    def test_suspicious_retrieve_all_as_admin(self):
        # Create new Suspicious models.
        self.create_model_logout(self.data, 'standard', self.user_admin)
        self.create_model_logout(self.data, 'modified', self.user_admin)

        # Log in as admin.
        self.login_user(self.user_admin)

        # Make get request and ensure OK response
        response = self.client.get(self.format_url(self.data.url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_list(response.data['results'], [self.data.standard, self.data.modified]))


    def test_suspicious_retrieve_single_as_unauthorized(self):
        # Create new Suspicious models, storing URL.
        url = self.create_model_logout(self.data, 'standard', self.user_admin)

        # Make get request and ensure unauthorized response
        response = self.client.get(url)
        self.assertIn(response.status_code, self.status_forbidden)


    def test_suspicious_retrieve_all_as_unauthorized(self):
        # Create new Suspicious models.
        self.create_model_logout(self.data, 'standard', self.user_admin)
        self.create_model_logout(self.data, 'modified', self.user_admin)

        # Make get request and ensure unauthorized response
        response = self.client.get(self.format_url(self.data.url))
        self.assertIn(response.status_code, self.status_forbidden)


    # TODO: Write update tests
    # TODO: Write delete tests


class ReportResponseTest(AvaTest):
    """
ReportResponse Test    """

    def setUp(self):
        # Make call to super.        super(ReportResponseTest, self).setUp()

        # Set the data type.
        self.data = ReportResponseTestData

    def test_report_response_create_as_user(self):
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

    def test_report_response_create_as_admin(self):
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

    def test_report_response_create_as_unauthenticated(self):
        # Take count.
        count = self.data.model.objects.count()

        # Store data to use.
        data = self.data.get_data()

        # Make push request and ensure unauthorized response.
        response = self.client.push(self.format_url(self.data.url), data, format='json')
        self.assertIn(response.status_code, self.status_forbidden)
        self.assertEqual(self.data.model.objects.count(), count)

    def test_report_response_retrieve_single_as_user(self):
        # Create new ReportResponse models, storing URL.
        url = self.create_model_logout(self.data, 'standard', self.user_user)

        # Log in as user.
        self.login_user(self.user_user)

        # Make get request and ensure OK response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data(response.data, self.data.standard))


    def test_report_response_retrieve_all_as_user(self):
        # Create new ReportResponse models.
        self.create_model_logout(self.data, 'standard', self.user_user)
        self.create_model_logout(self.data, 'modified', self.user_user)

        # Log in as user.
        self.login_user(self.user_user)

        # Make get request and ensure OK response
        response = self.client.get(self.format_url(self.data.url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_list(response.data['results'], [self.data.standard, self.data.modified]))


    def test_report_response_retrieve_single_as_admin(self):
        # Create new ReportResponse models, storing URL.
        url = self.create_model_logout(self.data, 'standard', self.user_admin)

        # Log in as admin.
        self.login_user(self.user_admin)

        # Make get request and ensure OK response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data(response.data, self.data.standard))


    def test_report_response_retrieve_all_as_admin(self):
        # Create new ReportResponse models.
        self.create_model_logout(self.data, 'standard', self.user_admin)
        self.create_model_logout(self.data, 'modified', self.user_admin)

        # Log in as admin.
        self.login_user(self.user_admin)

        # Make get request and ensure OK response
        response = self.client.get(self.format_url(self.data.url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_list(response.data['results'], [self.data.standard, self.data.modified]))


    def test_report_response_retrieve_single_as_unauthorized(self):
        # Create new ReportResponse models, storing URL.
        url = self.create_model_logout(self.data, 'standard', self.user_admin)

        # Make get request and ensure unauthorized response
        response = self.client.get(url)
        self.assertIn(response.status_code, self.status_forbidden)


    def test_report_response_retrieve_all_as_unauthorized(self):
        # Create new ReportResponse models.
        self.create_model_logout(self.data, 'standard', self.user_admin)
        self.create_model_logout(self.data, 'modified', self.user_admin)

        # Make get request and ensure unauthorized response
        response = self.client.get(self.format_url(self.data.url))
        self.assertIn(response.status_code, self.status_forbidden)


    # TODO: Write update tests
    # TODO: Write delete tests


class QuestionTest(AvaTest):
    """
Question Test    """

    def setUp(self):
        # Make call to super.        super(QuestionTest, self).setUp()

        # Set the data type.
        self.data = QuestionTestData

    def test_question_create_as_user(self):
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

    def test_question_create_as_admin(self):
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

    def test_question_create_as_unauthenticated(self):
        # Take count.
        count = self.data.model.objects.count()

        # Store data to use.
        data = self.data.get_data()

        # Make push request and ensure unauthorized response.
        response = self.client.push(self.format_url(self.data.url), data, format='json')
        self.assertIn(response.status_code, self.status_forbidden)
        self.assertEqual(self.data.model.objects.count(), count)

    def test_question_retrieve_single_as_user(self):
        # Create new Question models, storing URL.
        url = self.create_model_logout(self.data, 'standard', self.user_user)

        # Log in as user.
        self.login_user(self.user_user)

        # Make get request and ensure OK response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data(response.data, self.data.standard))


    def test_question_retrieve_all_as_user(self):
        # Create new Question models.
        self.create_model_logout(self.data, 'standard', self.user_user)
        self.create_model_logout(self.data, 'modified', self.user_user)

        # Log in as user.
        self.login_user(self.user_user)

        # Make get request and ensure OK response
        response = self.client.get(self.format_url(self.data.url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_list(response.data['results'], [self.data.standard, self.data.modified]))


    def test_question_retrieve_single_as_admin(self):
        # Create new Question models, storing URL.
        url = self.create_model_logout(self.data, 'standard', self.user_admin)

        # Log in as admin.
        self.login_user(self.user_admin)

        # Make get request and ensure OK response
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data(response.data, self.data.standard))


    def test_question_retrieve_all_as_admin(self):
        # Create new Question models.
        self.create_model_logout(self.data, 'standard', self.user_admin)
        self.create_model_logout(self.data, 'modified', self.user_admin)

        # Log in as admin.
        self.login_user(self.user_admin)

        # Make get request and ensure OK response
        response = self.client.get(self.format_url(self.data.url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.does_contain_data_list(response.data['results'], [self.data.standard, self.data.modified]))


    def test_question_retrieve_single_as_unauthorized(self):
        # Create new Question models, storing URL.
        url = self.create_model_logout(self.data, 'standard', self.user_admin)

        # Make get request and ensure unauthorized response
        response = self.client.get(url)
        self.assertIn(response.status_code, self.status_forbidden)


    def test_question_retrieve_all_as_unauthorized(self):
        # Create new Question models.
        self.create_model_logout(self.data, 'standard', self.user_admin)
        self.create_model_logout(self.data, 'modified', self.user_admin)

        # Make get request and ensure unauthorized response
        response = self.client.get(self.format_url(self.data.url))
        self.assertIn(response.status_code, self.status_forbidden)


    # TODO: Write update tests
    # TODO: Write delete tests



