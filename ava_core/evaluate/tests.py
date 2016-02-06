# Rest Imports
# Local Imports
from ava_core.abstract.test import AvaCoreTest
from ava_core.evaluate.test_data import EvaluateSenderTestData, EvaluateResultTestData, EvaluateTemplateTestData, \
    EvaluateControllerTestData, EvaluateTestTestData


# Implementation
class EvaluateSenderTest(AvaCoreTest):
    """
    EvaluateSender Test
    """

    def setUp(self):
        # Make call to super.
        super(EvaluateSenderTest, self).setUp()

        # Set the data type.
        self.data = EvaluateSenderTestData()

    def test_evaluate_sender_create_as_admin(self):
        pass

    def test_evaluate_sender_create_as_unauthenticated(self):
        pass

    def test_evaluate_sender_retrieve_single_as_user(self):
        pass

    def test_evaluate_sender_retrieve_all_as_user(self):
        pass

    def test_evaluate_sender_retrieve_single_as_admin(self):
        pass

    def test_evaluate_sender_retrieve_all_as_admin(self):
        pass

    def test_evaluate_sender_retrieve_single_as_unauthorized(self):
        pass

    def test_evaluate_sender_retrieve_all_as_unauthorized(self):
        pass

    def test_evaluate_sender_update_exists_as_user(self):
        pass

    def test_evaluate_sender_update_does_not_exist_as_user(self):
        pass

    def test_evaluate_sender_update_exists_as_admin(self):
        pass

    def test_evaluate_sender_update_does_not_exist_as_admin(self):
        pass

    def test_evaluate_sender_update_exists_as_unauthorized(self):
        pass

    def test_evaluate_sender_update_does_not_exist_as_unauthorized(self):
        pass

    def test_evaluate_sender_delete_does_not_exist_as_user(self):
        pass

    def test_evaluate_sender_delete_exists_as_admin(self):
        pass

    def test_evaluate_sender_delete_does_not_exist_as_admin(self):
        pass

    def test_evaluate_sender_delete_exists_as_unauthorized(self):
        pass

    def test_evaluate_sender_delete_does_not_exist_as_unauthorized(self):
        pass


class EvaluateResultTest(AvaCoreTest):
    """
    EvaluateResult Test
    """

    def setUp(self):
        # Make call to super.
        super(EvaluateResultTest, self).setUp()

        # Set the data type.
        self.data = EvaluateResultTestData()

    def test_evaluate_result_create_as_admin(self):
        pass

    def test_evaluate_result_create_as_unauthenticated(self):
        pass

    def test_evaluate_result_retrieve_single_as_user(self):
        pass

    def test_evaluate_result_retrieve_all_as_user(self):
        pass

    def test_evaluate_result_retrieve_single_as_admin(self):
        pass

    def test_evaluate_result_retrieve_all_as_admin(self):
        pass

    def test_evaluate_result_retrieve_single_as_unauthorized(self):
        pass

    def test_evaluate_result_retrieve_all_as_unauthorized(self):
        pass

    def test_evaluate_result_update_exists_as_user(self):
        pass

    def test_evaluate_result_update_does_not_exist_as_user(self):
        pass

    def test_evaluate_result_update_exists_as_admin(self):
        pass

    def test_evaluate_result_update_does_not_exist_as_admin(self):
        pass

    def test_evaluate_result_update_exists_as_unauthorized(self):
        pass

    def test_evaluate_result_update_does_not_exist_as_unauthorized(self):
        pass

    def test_evaluate_result_delete_does_not_exist_as_user(self):
        pass

    def test_evaluate_result_delete_exists_as_admin(self):
        pass

    def test_evaluate_result_delete_does_not_exist_as_admin(self):
        pass

    def test_evaluate_result_delete_exists_as_unauthorized(self):
        pass

    def test_evaluate_result_delete_does_not_exist_as_unauthorized(self):
        pass


class EvaluateTemplateTest(AvaCoreTest):
    """
    EvaluateTemplate Test
    """

    def setUp(self):
        # Make call to super.
        super(EvaluateTemplateTest, self).setUp()

        # Set the data type.
        self.data = EvaluateTemplateTestData()

    def test_evaluate_template_create_as_admin(self):
        pass

    def test_evaluate_template_create_as_unauthenticated(self):
        pass

    def test_evaluate_template_retrieve_single_as_user(self):
        pass

    def test_evaluate_template_retrieve_all_as_user(self):
        pass

    def test_evaluate_template_retrieve_single_as_admin(self):
        pass

    def test_evaluate_template_retrieve_all_as_admin(self):
        pass

    def test_evaluate_template_retrieve_single_as_unauthorized(self):
        pass

    def test_evaluate_template_retrieve_all_as_unauthorized(self):
        pass

    def test_evaluate_template_update_exists_as_user(self):
        pass

    def test_evaluate_template_update_does_not_exist_as_user(self):
        pass

    def test_evaluate_template_update_exists_as_admin(self):
        pass

    def test_evaluate_template_update_does_not_exist_as_admin(self):
        pass

    def test_evaluate_template_update_exists_as_unauthorized(self):
        pass

    def test_evaluate_template_update_does_not_exist_as_unauthorized(self):
        pass

    def test_evaluate_template_delete_does_not_exist_as_user(self):
        pass

    def test_evaluate_template_delete_exists_as_admin(self):
        pass

    def test_evaluate_template_delete_does_not_exist_as_admin(self):
        pass

    def test_evaluate_template_delete_exists_as_unauthorized(self):
        pass

    def test_evaluate_template_delete_does_not_exist_as_unauthorized(self):
        pass


class EvaluateControllerTest(AvaCoreTest):
    """
    EvaluateController Test
    """

    def setUp(self):
        # Make call to super.
        super(EvaluateControllerTest, self).setUp()

        # Set the data type.
        self.data = EvaluateControllerTestData()

    def test_example_create_as_admin(self):
        pass

    def test_example_create_as_unauthenticated(self):
        pass

    def test_example_retrieve_single_as_user(self):
        pass

    def test_example_retrieve_all_as_user(self):
        pass

    def test_example_retrieve_single_as_admin(self):
        pass

    def test_example_retrieve_all_as_admin(self):
        pass

    def test_example_retrieve_single_as_unauthorized(self):
        pass

    def test_example_retrieve_all_as_unauthorized(self):
        pass

    def test_example_update_exists_as_user(self):
        pass

    def test_example_update_does_not_exist_as_user(self):
        pass

    def test_example_update_exists_as_admin(self):
        pass

    def test_example_update_does_not_exist_as_admin(self):
        pass

    def test_example_update_exists_as_unauthorized(self):
        pass

    def test_example_update_does_not_exist_as_unauthorized(self):
        pass

    def test_example_delete_does_not_exist_as_user(self):
        pass

    def test_example_delete_exists_as_admin(self):
        pass

    def test_example_delete_does_not_exist_as_admin(self):
        pass

    def test_example_delete_exists_as_unauthorized(self):
        pass

    def test_example_delete_does_not_exist_as_unauthorized(self):
        pass


class EvaluateTestTest(AvaCoreTest):
    """
    EvaluateTest Test
    """

    def setUp(self):
        # Make call to super.
        super(EvaluateTestTest, self).setUp()

        # Set the data type.
        self.data = EvaluateTestTestData()

    def test_evaluate_controller_create_as_admin(self):
        pass

    def test_evaluate_controller_create_as_unauthenticated(self):
        pass

    def test_evaluate_controller_retrieve_single_as_user(self):
        pass

    def test_evaluate_controller_retrieve_all_as_user(self):
        pass

    def test_evaluate_controller_retrieve_single_as_admin(self):
        pass

    def test_evaluate_controller_retrieve_all_as_admin(self):
        pass

    def test_evaluate_controller_retrieve_single_as_unauthorized(self):
        pass

    def test_evaluate_controller_retrieve_all_as_unauthorized(self):
        pass

    def test_evaluate_controller_update_exists_as_user(self):
        pass

    def test_evaluate_controller_update_does_not_exist_as_user(self):
        pass

    def test_evaluate_controller_update_exists_as_admin(self):
        pass

    def test_evaluate_controller_update_does_not_exist_as_admin(self):
        pass

    def test_evaluate_controller_update_exists_as_unauthorized(self):
        pass

    def test_evaluate_controller_update_does_not_exist_as_unauthorized(self):
        pass

    def test_evaluate_controller_delete_does_not_exist_as_user(self):
        pass

    def test_evaluate_controller_delete_exists_as_admin(self):
        pass

    def test_evaluate_controller_delete_does_not_exist_as_admin(self):
        pass

    def test_evaluate_controller_delete_exists_as_unauthorized(self):
        pass

    def test_evaluate_controller_delete_does_not_exist_as_unauthorized(self):
        pass
