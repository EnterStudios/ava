# Rest Imports
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.evaluate.models import EvaluateSender, EvaluateResult, EvaluateTemplate, EvaluateController, EvaluateTest


# Implementation
class EvaluateSenderTestData(AvaCoreTestData):
    """
    Test data for EvaluateSender
    """

    @staticmethod
    def init_requirements(owner):
        pass

    # Store self information
    model = EvaluateSender
    url = 'example/'

    standard = {
        'last_name': 'standard_char',
        'email_address': 'standard_char',
        'hidden': True,
        'evaluatecontroller': 'example//1/',
        'slack_name': 'standard_char',
        'first_name': 'standard_char',
    }

    unique = {
        'last_name': 'unique_char',
        'email_address': 'unique_char',
        'hidden': False,
        'evaluatecontroller': 'example//2/',
        'slack_name': 'unique_char',
        'first_name': 'unique_char',
    }


class EvaluateResultTestData(AvaCoreTestData):
    """
    Test data for EvaluateResult
    """

    @staticmethod
    def init_requirements(owner):
        pass

    # Store self information
    model = EvaluateResult
    url = 'example/'

    standard = {
        'result': 0,
        'target_profile': 'example//1/',
    }

    unique = {
        'result': 1,
        'target_profile': 'example//2/',
    }


class EvaluateTemplateTestData(AvaCoreTestData):
    """
    Test data for EvaluateTemplate
    """

    @staticmethod
    def init_requirements(owner):
        pass

    # Store self information
    model = EvaluateTemplate
    url = 'example/'

    standard = {
        'name': 'standard_char',
        'template_type': 0,
        'description': 'standard_text',
        'hidden': True,
        'evaluatecontroller': 'example//1/',
        'email_body': 'standard_text',
        'email_subject': 'standard_char',
    }

    unique = {
        'name': 'unique_char',
        'template_type': 1,
        'description': 'unique_text',
        'hidden': False,
        'evaluatecontroller': 'example//2/',
        'email_body': 'unique_text',
        'email_subject': 'unique_char',
    }


class EvaluateControllerTestData(AvaCoreTestData):
    """
    Test data for EvaluateController
    """

    @staticmethod
    def init_requirements(owner):
        pass

    # Store self information
    model = EvaluateController
    url = 'example/'

    standard = {
        'expiry_type': 0,
        'name': 'standard_char',
        'sender': 'example//1/',
        'status': 0,
        'description': 'standard_text',
        'scheduled_time': 'default',
        'template': 'example//1/',
        'scheduled_type': 0,
        'target_controller': 'example//1/',
        'expiry_time': 'default',
        'targets': 'default',
    }

    unique = {
        'expiry_type': 2,
        'name': 'unique_char',
        'sender': 'example//2/',
        'status': 4,
        'description': 'unique_text',
        'scheduled_time': 'default',
        'template': 'example//2/',
        'scheduled_type': 1,
        'target_controller': 'example//2/',
        'expiry_time': 'default',
        'targets': 'default',
    }


class EvaluateTestTestData(AvaCoreTestData):
    """
    Test data for EvaluateTest
    """

    @staticmethod
    def init_requirements(owner):
        pass

    # Store self information
    model = EvaluateTest
    url = 'example/'

    standard = {
        'token': 'standard_char',
        'controller': 'example//1/',
        'target': 'example//1/',
        'evaluateresult': 'example//1/',
        'delivery_status': 0,
    }

    unique = {
        'token': 'unique_char',
        'controller': 'example//2/',
        'target': 'example//2/',
        'evaluateresult': 'example//2/',
        'delivery_status': 3,
    }
