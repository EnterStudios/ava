# Rest Imports
# Local Imports
from ava_core.abstract.test import AvaCoreTest
from ava_core.outreach.test_data import SuspiciousTestData, QuestionTestData


# Implementation
class SuspiciousTest(AvaCoreTest):
    """
    Suspicious Test
    """

    def setUp(self):
        # Make call to super.
        super(SuspiciousTest, self).setUp()

        # Set the data type.
        self.data = SuspiciousTestData()

    def test_suspicious_create_as_user(self):
        pass

    def test_suspicious_create_as_admin(self):
        pass

    def test_suspicious_create_as_unauthenticated(self):
        pass

    def test_suspicious_retrieve_single_as_user(self):
        pass

    def test_suspicious_retrieve_all_as_user(self):
        pass

    def test_suspicious_retrieve_single_as_admin(self):
        pass

    def test_suspicious_retrieve_all_as_admin(self):
        pass

    def test_suspicious_retrieve_single_as_unauthorized(self):
        pass

    def test_suspicious_retrieve_all_as_unauthorized(self):
        pass

    def test_suspicious_update_exists_as_user(self):
        pass

    def test_suspicious_update_does_not_exist_as_user(self):
        pass

    def test_suspicious_update_exists_as_admin(self):
        pass

    def test_suspicious_update_does_not_exist_as_admin(self):
        pass

    def test_suspicious_update_exists_as_unauthorized(self):
        pass

    def test_suspicious_update_does_not_exist_as_unauthorized(self):
        pass

    def test_suspicious_delete_does_not_exist_as_user(self):
        pass

    def test_suspicious_delete_exists_as_admin(self):
        pass

    def test_suspicious_delete_does_not_exist_as_admin(self):
        pass

    def test_suspicious_delete_exists_as_unauthorized(self):
        pass

    def test_suspicious_delete_does_not_exist_as_unauthorized(self):
        pass


class ReportResponseTest(AvaCoreTest):
    """
    ReportResponse Test
    """

    def setUp(self):
        pass
        # # Make call to super.
        # super(ReportResponseTest, self).setUp()
        #
        # # Set the data type.
        # self.data = ReportResponseTestData()
        #
        # question_standard_url = self.create_model_logout(QuestionTestData(), data_name='standard', owner=self.user_user)
        # question_unique_url = self.create_model_logout(QuestionTestData(), data_name='unique', owner=self.user_user)
        #
        # response_unique_url = self.create_model_logout(ReportResponseTestData(), data_name='unique',
        #                                                owner=self.user_user)
        #
        # self.data.standard['question'] = question_standard_url
        # self.data.unique['question'] = question_unique_url
        #
        # self.data.standard['parent_response'] = response_unique_url
        # self.data.unique['parent_response'] = response_unique_url

    def test_report_response_create_as_user(self):
        pass

    def test_report_response_create_as_admin(self):
        pass

    def test_report_response_create_as_unauthenticated(self):
        pass

    def test_report_response_retrieve_single_as_user(self):
        pass

    def test_report_response_retrieve_all_as_user(self):
        pass

    def test_report_response_retrieve_single_as_admin(self):
        pass

    def test_report_response_retrieve_all_as_admin(self):
        pass

    def test_report_response_retrieve_single_as_unauthorized(self):
        pass

    def test_report_response_retrieve_all_as_unauthorized(self):
        pass

    def test_report_response_update_exists_as_user(self):
        pass

    def test_report_response_update_does_not_exist_as_user(self):
        pass

    def test_report_response_update_exists_as_admin(self):
        pass

    def test_report_response_update_does_not_exist_as_admin(self):
        pass

    def test_report_response_update_exists_as_unauthorized(self):
        pass

    def test_report_response_update_does_not_exist_as_unauthorized(self):
        pass

    def test_report_response_delete_does_not_exist_as_user(self):
        pass

    def test_report_response_delete_exists_as_admin(self):
        pass

    def test_report_response_delete_does_not_exist_as_admin(self):
        pass

    def test_report_response_delete_exists_as_unauthorized(self):
        pass

    def test_report_response_delete_does_not_exist_as_unauthorized(self):
        pass


class QuestionTest(AvaCoreTest):
    """
    Question Test
    """

    def setUp(self):
        # Make call to super.
        super(QuestionTest, self).setUp()

        # Set the data type.
        self.data = QuestionTestData()

    def test_question_create_as_user(self):
        pass

    def test_question_create_as_admin(self):
        pass

    def test_question_create_as_unauthenticated(self):
        pass

    def test_question_retrieve_single_as_user(self):
        pass

    def test_question_retrieve_all_as_user(self):
        pass

    def test_question_retrieve_single_as_admin(self):
        pass

    def test_question_retrieve_all_as_admin(self):
        pass

    def test_question_retrieve_single_as_unauthorized(self):
        pass

    def test_question_retrieve_all_as_unauthorized(self):
        pass

    def test_question_update_exists_as_user(self):
        pass

    def test_question_update_does_not_exist_as_user(self):
        pass

    def test_question_update_exists_as_admin(self):
        pass

    def test_question_update_does_not_exist_as_admin(self):
        pass

    def test_question_update_exists_as_unauthorized(self):
        pass

    def test_question_update_does_not_exist_as_unauthorized(self):
        pass

    def test_question_delete_does_not_exist_as_user(self):
        pass

    def test_question_delete_exists_as_admin(self):
        pass

    def test_question_delete_does_not_exist_as_admin(self):
        pass

    def test_question_delete_exists_as_unauthorized(self):
        pass

    def test_question_delete_does_not_exist_as_unauthorized(self):
        pass
