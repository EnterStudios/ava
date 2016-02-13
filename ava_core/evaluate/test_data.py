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
    url = 'evaluate/sender/'

    standard = {
        'last_name': 'standard_char',
        'email_address': 'test@example.com',
        'hidden': True,
        'slack_name': 'standard_char',
        'first_name': 'standard_char',
    }

    unique = {
        'last_name': 'unique_char',
        'email_address': 'second@example.com',
        'hidden': False,
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
    url = 'evaluate/result/'

    standard = {
        'result': 0,
        'target_profile': 'REPLACE',
    }

    unique = {
        'result': 1,
        'target_profile': 'REPLACE',
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
    url = 'evaluate/template/'

    standard = {
        'name': 'standard_char',
        'template_type': 0,
        'description': 'standard_text',
        'hidden': True,
        'email_body': 'standard_text',
        'email_subject': 'standard_char',
    }

    unique = {
        'name': 'unique_char',
        'template_type': 1,
        'description': 'unique_text',
        'hidden': False,
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
    url = 'evaluate/controller/'

    standard = {
        'expiry_type': 0,
        'name': 'standard_char',
        'sender': 'REPLACE',
        'status': 0,
        'description': 'standard_text',
        'scheduled_time': '2016-01-31T09:00',
        'template': 'REPLACE',
        'scheduled_type': 0,
        'target_controller': 'REPLACE',
        'expiry_time': '2016-01-31T09:00',
        'targets': [],
    }

    unique = {
        'expiry_type': 2,
        'name': 'unique_char',
        'sender': 'REPLACE',
        'status': 4,
        'description': 'unique_text',
        'scheduled_time': '2016-01-31T09:00',
        'template': 'REPLACE',
        'scheduled_type': 1,
        'target_controller': 'REPLACE',
        'expiry_time': '2016-01-31T09:00',
        'targets': [],
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
    url = 'evaluate/test/'

    standard = {
        'token': 'standard_char',
        'controller': 'REPLACE',
        'target': 'REPLACE',
        'delivery_status': 0,
    }

    unique = {
        'token': 'unique_char',
        'controller': 'REPLACE',
        'target': 'REPLACE',
        'delivery_status': 3,
    }
