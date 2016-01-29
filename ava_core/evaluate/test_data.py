# Rest Imports
from rest_framework import status
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.organize.models import Person
from ava_core.organize.test_data import PersonTestData
from ava_core.evaluate.models import EvaluateTest, EvaluateResult, EvaluateController, EvaluateTemplate, EvaluateSender


# Implementation
class EvaluateTestTestData(AvaCoreTestData):
    """
    Test data for EvaluateTest
    """

    def __init__(self):
        # Store self information
        self.model = EvaluateTest
        self.url = '/example'

        # Create any necessary required models.
        self.init_requirements()

    def init_requirements(self):
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if EvaluateResult.objects.count() == 0:
            EvaluateResultTestData.init_requirements()
            EvaluateResult.objects.create(**EvaluateResultTestData.get_data('standard'))
            EvaluateResult.objects.create(**EvaluateResultTestData.get_data('unique'))
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if Person.objects.count() == 0:
            PersonTestData.init_requirements()
            Person.objects.create(**PersonTestData.get_data('standard'))
            Person.objects.create(**PersonTestData.get_data('unique'))
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if EvaluateController.objects.count() == 0:
            EvaluateControllerTestData.init_requirements()
            EvaluateController.objects.create(**EvaluateControllerTestData.get_data('standard'))
            EvaluateController.objects.create(**EvaluateControllerTestData.get_data('unique'))

    standard = {
        'evaluateresult': '/example/1/',
        'token': 'standard_char',
        'delivery_status': 0,
        'target': '/example/1/',
        'controller': '/example/1/',
    }

    unique = {
        'evaluateresult': '/example/2/',
        'token': 'unique_char',
        'delivery_status': 3,
        'target': '/example/2/',
        'controller': '/example/2/',
    }

    missing_evaluateresult = {
        'token': 'standard_char',
        'delivery_status': 0,
        'target': '/example/1/',
        'controller': '/example/1/',
    }
    modified_evaluateresult = {
        'evaluateresult': '/example/2/',
        'token': 'standard_char',
        'delivery_status': 0,
        'target': '/example/1/',
        'controller': '/example/1/',
    }

    modified_token = {
        'evaluateresult': '/example/1/',
        'token': 'modified_char',
        'delivery_status': 0,
        'target': '/example/1/',
        'controller': '/example/1/',
    }
    missing_token = {
        'evaluateresult': '/example/1/',
        'delivery_status': 0,
        'target': '/example/1/',
        'controller': '/example/1/',
    }

    missing_delivery_status = {
        'evaluateresult': '/example/1/',
        'token': 'standard_char',
        'target': '/example/1/',
        'controller': '/example/1/',
    }
    modified_delivery_status = {
        'evaluateresult': '/example/1/',
        'token': 'standard_char',
        'delivery_status': 3,
        'target': '/example/1/',
        'controller': '/example/1/',
    }

    missing_target = {
        'evaluateresult': '/example/1/',
        'token': 'standard_char',
        'delivery_status': 0,
        'controller': '/example/1/',
    }
    modified_target = {
        'evaluateresult': '/example/1/',
        'token': 'standard_char',
        'delivery_status': 0,
        'target': '/example/2/',
        'controller': '/example/1/',
    }

    missing_controller = {
        'evaluateresult': '/example/1/',
        'token': 'standard_char',
        'delivery_status': 0,
        'target': '/example/1/',
    }
    modified_controller = {
        'evaluateresult': '/example/1/',
        'token': 'standard_char',
        'delivery_status': 0,
        'target': '/example/1/',
        'controller': '/example/2/',
    }



class EvaluateResultTestData(AvaCoreTestData):
    """
    Test data for EvaluateResult
    """

    def __init__(self):
        # Store self information
        self.model = EvaluateResult
        self.url = '/example'

        # Create any necessary required models.
        self.init_requirements()

    def init_requirements(self):
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if EvaluateTest.objects.count() == 0:
            EvaluateTestTestData.init_requirements()
            EvaluateTest.objects.create(**EvaluateTestTestData.get_data('standard'))
            EvaluateTest.objects.create(**EvaluateTestTestData.get_data('unique'))

    standard = {
        'target_profile': '/example/1/',
        'result': 0,
    }

    unique = {
        'target_profile': '/example/2/',
        'result': 1,
    }

    modified_target_profile = {
        'target_profile': '/example/2/',
        'result': 0,
    }
    missing_target_profile = {
        'result': 0,
    }

    missing_result = {
        'target_profile': '/example/1/',
    }
    modified_result = {
        'target_profile': '/example/1/',
        'result': 1,
    }



class EvaluateTemplateTestData(AvaCoreTestData):
    """
    Test data for EvaluateTemplate
    """

    def __init__(self):
        # Store self information
        self.model = EvaluateTemplate
        self.url = '/example'

        # Create any necessary required models.
        self.init_requirements()

    def init_requirements(self):
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if EvaluateController.objects.count() == 0:
            EvaluateControllerTestData.init_requirements()
            EvaluateController.objects.create(**EvaluateControllerTestData.get_data('standard'))
            EvaluateController.objects.create(**EvaluateControllerTestData.get_data('unique'))

    standard = {
        'template_type': 0,
        'email_subject': 'standard_char',
        'description': 'standard_text',
        'name': 'standard_char',
        'hidden': True,
        'evaluatecontroller': '/example/1/',
        'email_body': 'standard_text',
    }

    unique = {
        'template_type': 1,
        'email_subject': 'unique_char',
        'description': 'unique_text',
        'name': 'unique_char',
        'hidden': False,
        'evaluatecontroller': '/example/2/',
        'email_body': 'unique_text',
    }

    modified_template_type = {
        'template_type': 1,
        'email_subject': 'standard_char',
        'description': 'standard_text',
        'name': 'standard_char',
        'hidden': True,
        'evaluatecontroller': '/example/1/',
        'email_body': 'standard_text',
    }
    missing_template_type = {
        'email_subject': 'standard_char',
        'description': 'standard_text',
        'name': 'standard_char',
        'hidden': True,
        'evaluatecontroller': '/example/1/',
        'email_body': 'standard_text',
    }

    modified_email_subject = {
        'template_type': 0,
        'email_subject': 'modified_char',
        'description': 'standard_text',
        'name': 'standard_char',
        'hidden': True,
        'evaluatecontroller': '/example/1/',
        'email_body': 'standard_text',
    }
    missing_email_subject = {
        'template_type': 0,
        'description': 'standard_text',
        'name': 'standard_char',
        'hidden': True,
        'evaluatecontroller': '/example/1/',
        'email_body': 'standard_text',
    }

    missing_description = {
        'template_type': 0,
        'email_subject': 'standard_char',
        'name': 'standard_char',
        'hidden': True,
        'evaluatecontroller': '/example/1/',
        'email_body': 'standard_text',
    }
    modified_description = {
        'template_type': 0,
        'email_subject': 'standard_char',
        'description': 'modified_text',
        'name': 'standard_char',
        'hidden': True,
        'evaluatecontroller': '/example/1/',
        'email_body': 'standard_text',
    }

    modified_name = {
        'template_type': 0,
        'email_subject': 'standard_char',
        'description': 'standard_text',
        'name': 'modified_char',
        'hidden': True,
        'evaluatecontroller': '/example/1/',
        'email_body': 'standard_text',
    }
    missing_name = {
        'template_type': 0,
        'email_subject': 'standard_char',
        'description': 'standard_text',
        'hidden': True,
        'evaluatecontroller': '/example/1/',
        'email_body': 'standard_text',
    }

    missing_hidden = {
        'template_type': 0,
        'email_subject': 'standard_char',
        'description': 'standard_text',
        'name': 'standard_char',
        'evaluatecontroller': '/example/1/',
        'email_body': 'standard_text',
    }
    modified_hidden = {
        'template_type': 0,
        'email_subject': 'standard_char',
        'description': 'standard_text',
        'name': 'standard_char',
        'hidden': False,
        'evaluatecontroller': '/example/1/',
        'email_body': 'standard_text',
    }

    missing_evaluatecontroller = {
        'template_type': 0,
        'email_subject': 'standard_char',
        'description': 'standard_text',
        'name': 'standard_char',
        'hidden': True,
        'email_body': 'standard_text',
    }
    modified_evaluatecontroller = {
        'template_type': 0,
        'email_subject': 'standard_char',
        'description': 'standard_text',
        'name': 'standard_char',
        'hidden': True,
        'evaluatecontroller': '/example/2/',
        'email_body': 'standard_text',
    }

    missing_email_body = {
        'template_type': 0,
        'email_subject': 'standard_char',
        'description': 'standard_text',
        'name': 'standard_char',
        'hidden': True,
        'evaluatecontroller': '/example/1/',
    }
    modified_email_body = {
        'template_type': 0,
        'email_subject': 'standard_char',
        'description': 'standard_text',
        'name': 'standard_char',
        'hidden': True,
        'evaluatecontroller': '/example/1/',
        'email_body': 'modified_text',
    }



class EvaluateSenderTestData(AvaCoreTestData):
    """
    Test data for EvaluateSender
    """

    def __init__(self):
        # Store self information
        self.model = EvaluateSender
        self.url = '/example'

        # Create any necessary required models.
        self.init_requirements()

    def init_requirements(self):
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if EvaluateController.objects.count() == 0:
            EvaluateControllerTestData.init_requirements()
            EvaluateController.objects.create(**EvaluateControllerTestData.get_data('standard'))
            EvaluateController.objects.create(**EvaluateControllerTestData.get_data('unique'))

    standard = {
        'email_address': 'standard_char',
        'last_name': 'standard_char',
        'first_name': 'standard_char',
        'hidden': True,
        'evaluatecontroller': '/example/1/',
        'slack_name': 'standard_char',
    }

    unique = {
        'email_address': 'unique_char',
        'last_name': 'unique_char',
        'first_name': 'unique_char',
        'hidden': False,
        'evaluatecontroller': '/example/2/',
        'slack_name': 'unique_char',
    }

    modified_email_address = {
        'email_address': 'modified_char',
        'last_name': 'standard_char',
        'first_name': 'standard_char',
        'hidden': True,
        'evaluatecontroller': '/example/1/',
        'slack_name': 'standard_char',
    }
    missing_email_address = {
        'last_name': 'standard_char',
        'first_name': 'standard_char',
        'hidden': True,
        'evaluatecontroller': '/example/1/',
        'slack_name': 'standard_char',
    }

    modified_last_name = {
        'email_address': 'standard_char',
        'last_name': 'modified_char',
        'first_name': 'standard_char',
        'hidden': True,
        'evaluatecontroller': '/example/1/',
        'slack_name': 'standard_char',
    }
    missing_last_name = {
        'email_address': 'standard_char',
        'first_name': 'standard_char',
        'hidden': True,
        'evaluatecontroller': '/example/1/',
        'slack_name': 'standard_char',
    }

    modified_first_name = {
        'email_address': 'standard_char',
        'last_name': 'standard_char',
        'first_name': 'modified_char',
        'hidden': True,
        'evaluatecontroller': '/example/1/',
        'slack_name': 'standard_char',
    }
    missing_first_name = {
        'email_address': 'standard_char',
        'last_name': 'standard_char',
        'hidden': True,
        'evaluatecontroller': '/example/1/',
        'slack_name': 'standard_char',
    }

    missing_hidden = {
        'email_address': 'standard_char',
        'last_name': 'standard_char',
        'first_name': 'standard_char',
        'evaluatecontroller': '/example/1/',
        'slack_name': 'standard_char',
    }
    modified_hidden = {
        'email_address': 'standard_char',
        'last_name': 'standard_char',
        'first_name': 'standard_char',
        'hidden': False,
        'evaluatecontroller': '/example/1/',
        'slack_name': 'standard_char',
    }

    missing_evaluatecontroller = {
        'email_address': 'standard_char',
        'last_name': 'standard_char',
        'first_name': 'standard_char',
        'hidden': True,
        'slack_name': 'standard_char',
    }
    modified_evaluatecontroller = {
        'email_address': 'standard_char',
        'last_name': 'standard_char',
        'first_name': 'standard_char',
        'hidden': True,
        'evaluatecontroller': '/example/2/',
        'slack_name': 'standard_char',
    }

    missing_slack_name = {
        'email_address': 'standard_char',
        'last_name': 'standard_char',
        'first_name': 'standard_char',
        'hidden': True,
        'evaluatecontroller': '/example/1/',
    }
    modified_slack_name = {
        'email_address': 'standard_char',
        'last_name': 'standard_char',
        'first_name': 'standard_char',
        'hidden': True,
        'evaluatecontroller': '/example/1/',
        'slack_name': 'modified_char',
    }



class EvaluateControllerTestData(AvaCoreTestData):
    """
    Test data for EvaluateController
    """

    def __init__(self):
        # Store self information
        self.model = EvaluateController
        self.url = '/example'

        # Create any necessary required models.
        self.init_requirements()

    def init_requirements(self):
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if EvaluateTest.objects.count() == 0:
            EvaluateTestTestData.init_requirements()
            EvaluateTest.objects.create(**EvaluateTestTestData.get_data('standard'))
            EvaluateTest.objects.create(**EvaluateTestTestData.get_data('unique'))
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if Person.objects.count() == 0:
            PersonTestData.init_requirements()
            Person.objects.create(**PersonTestData.get_data('standard'))
            Person.objects.create(**PersonTestData.get_data('unique'))
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if EvaluateSender.objects.count() == 0:
            EvaluateSenderTestData.init_requirements()
            EvaluateSender.objects.create(**EvaluateSenderTestData.get_data('standard'))
            EvaluateSender.objects.create(**EvaluateSenderTestData.get_data('unique'))
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if EvaluateTemplate.objects.count() == 0:
            EvaluateTemplateTestData.init_requirements()
            EvaluateTemplate.objects.create(**EvaluateTemplateTestData.get_data('standard'))
            EvaluateTemplate.objects.create(**EvaluateTemplateTestData.get_data('unique'))

    standard = {
        'target_controller': '/example/1/',
        'description': 'standard_text',
        'targets': 'default',
        'sender': '/example/1/',
        'template': '/example/1/',
        'name': 'standard_char',
        'scheduled_time': 'default',
        'expiry_type': 0,
        'expiry_time': 'default',
        'status': 0,
        'scheduled_type': 0,
    }

    unique = {
        'target_controller': '/example/2/',
        'description': 'unique_text',
        'targets': 'default',
        'sender': '/example/2/',
        'template': '/example/2/',
        'name': 'unique_char',
        'scheduled_time': 'default',
        'expiry_type': 2,
        'expiry_time': 'default',
        'status': 4,
        'scheduled_type': 1,
    }

    missing_target_controller = {
        'description': 'standard_text',
        'targets': 'default',
        'sender': '/example/1/',
        'template': '/example/1/',
        'name': 'standard_char',
        'scheduled_time': 'default',
        'expiry_type': 0,
        'expiry_time': 'default',
        'status': 0,
        'scheduled_type': 0,
    }
    modified_target_controller = {
        'target_controller': '/example/2/',
        'description': 'standard_text',
        'targets': 'default',
        'sender': '/example/1/',
        'template': '/example/1/',
        'name': 'standard_char',
        'scheduled_time': 'default',
        'expiry_type': 0,
        'expiry_time': 'default',
        'status': 0,
        'scheduled_type': 0,
    }

    missing_description = {
        'target_controller': '/example/1/',
        'targets': 'default',
        'sender': '/example/1/',
        'template': '/example/1/',
        'name': 'standard_char',
        'scheduled_time': 'default',
        'expiry_type': 0,
        'expiry_time': 'default',
        'status': 0,
        'scheduled_type': 0,
    }
    modified_description = {
        'target_controller': '/example/1/',
        'description': 'modified_text',
        'targets': 'default',
        'sender': '/example/1/',
        'template': '/example/1/',
        'name': 'standard_char',
        'scheduled_time': 'default',
        'expiry_type': 0,
        'expiry_time': 'default',
        'status': 0,
        'scheduled_type': 0,
    }

    modified_targets = {
        'target_controller': '/example/1/',
        'description': 'standard_text',
        'targets': 'default',
        'sender': '/example/1/',
        'template': '/example/1/',
        'name': 'standard_char',
        'scheduled_time': 'default',
        'expiry_type': 0,
        'expiry_time': 'default',
        'status': 0,
        'scheduled_type': 0,
    }
    missing_targets = {
        'target_controller': '/example/1/',
        'description': 'standard_text',
        'sender': '/example/1/',
        'template': '/example/1/',
        'name': 'standard_char',
        'scheduled_time': 'default',
        'expiry_type': 0,
        'expiry_time': 'default',
        'status': 0,
        'scheduled_type': 0,
    }

    modified_sender = {
        'target_controller': '/example/1/',
        'description': 'standard_text',
        'targets': 'default',
        'sender': '/example/2/',
        'template': '/example/1/',
        'name': 'standard_char',
        'scheduled_time': 'default',
        'expiry_type': 0,
        'expiry_time': 'default',
        'status': 0,
        'scheduled_type': 0,
    }
    missing_sender = {
        'target_controller': '/example/1/',
        'description': 'standard_text',
        'targets': 'default',
        'template': '/example/1/',
        'name': 'standard_char',
        'scheduled_time': 'default',
        'expiry_type': 0,
        'expiry_time': 'default',
        'status': 0,
        'scheduled_type': 0,
    }

    missing_template = {
        'target_controller': '/example/1/',
        'description': 'standard_text',
        'targets': 'default',
        'sender': '/example/1/',
        'name': 'standard_char',
        'scheduled_time': 'default',
        'expiry_type': 0,
        'expiry_time': 'default',
        'status': 0,
        'scheduled_type': 0,
    }
    modified_template = {
        'target_controller': '/example/1/',
        'description': 'standard_text',
        'targets': 'default',
        'sender': '/example/1/',
        'template': '/example/2/',
        'name': 'standard_char',
        'scheduled_time': 'default',
        'expiry_type': 0,
        'expiry_time': 'default',
        'status': 0,
        'scheduled_type': 0,
    }

    modified_name = {
        'target_controller': '/example/1/',
        'description': 'standard_text',
        'targets': 'default',
        'sender': '/example/1/',
        'template': '/example/1/',
        'name': 'modified_char',
        'scheduled_time': 'default',
        'expiry_type': 0,
        'expiry_time': 'default',
        'status': 0,
        'scheduled_type': 0,
    }
    missing_name = {
        'target_controller': '/example/1/',
        'description': 'standard_text',
        'targets': 'default',
        'sender': '/example/1/',
        'template': '/example/1/',
        'scheduled_time': 'default',
        'expiry_type': 0,
        'expiry_time': 'default',
        'status': 0,
        'scheduled_type': 0,
    }

    missing_scheduled_time = {
        'target_controller': '/example/1/',
        'description': 'standard_text',
        'targets': 'default',
        'sender': '/example/1/',
        'template': '/example/1/',
        'name': 'standard_char',
        'expiry_type': 0,
        'expiry_time': 'default',
        'status': 0,
        'scheduled_type': 0,
    }
    modified_scheduled_time = {
        'target_controller': '/example/1/',
        'description': 'standard_text',
        'targets': 'default',
        'sender': '/example/1/',
        'template': '/example/1/',
        'name': 'standard_char',
        'scheduled_time': 'default',
        'expiry_type': 0,
        'expiry_time': 'default',
        'status': 0,
        'scheduled_type': 0,
    }

    modified_expiry_type = {
        'target_controller': '/example/1/',
        'description': 'standard_text',
        'targets': 'default',
        'sender': '/example/1/',
        'template': '/example/1/',
        'name': 'standard_char',
        'scheduled_time': 'default',
        'expiry_type': 2,
        'expiry_time': 'default',
        'status': 0,
        'scheduled_type': 0,
    }
    missing_expiry_type = {
        'target_controller': '/example/1/',
        'description': 'standard_text',
        'targets': 'default',
        'sender': '/example/1/',
        'template': '/example/1/',
        'name': 'standard_char',
        'scheduled_time': 'default',
        'expiry_time': 'default',
        'status': 0,
        'scheduled_type': 0,
    }

    missing_expiry_time = {
        'target_controller': '/example/1/',
        'description': 'standard_text',
        'targets': 'default',
        'sender': '/example/1/',
        'template': '/example/1/',
        'name': 'standard_char',
        'scheduled_time': 'default',
        'expiry_type': 0,
        'status': 0,
        'scheduled_type': 0,
    }
    modified_expiry_time = {
        'target_controller': '/example/1/',
        'description': 'standard_text',
        'targets': 'default',
        'sender': '/example/1/',
        'template': '/example/1/',
        'name': 'standard_char',
        'scheduled_time': 'default',
        'expiry_type': 0,
        'expiry_time': 'default',
        'status': 0,
        'scheduled_type': 0,
    }

    modified_status = {
        'target_controller': '/example/1/',
        'description': 'standard_text',
        'targets': 'default',
        'sender': '/example/1/',
        'template': '/example/1/',
        'name': 'standard_char',
        'scheduled_time': 'default',
        'expiry_type': 0,
        'expiry_time': 'default',
        'status': 4,
        'scheduled_type': 0,
    }
    missing_status = {
        'target_controller': '/example/1/',
        'description': 'standard_text',
        'targets': 'default',
        'sender': '/example/1/',
        'template': '/example/1/',
        'name': 'standard_char',
        'scheduled_time': 'default',
        'expiry_type': 0,
        'expiry_time': 'default',
        'scheduled_type': 0,
    }

    modified_scheduled_type = {
        'target_controller': '/example/1/',
        'description': 'standard_text',
        'targets': 'default',
        'sender': '/example/1/',
        'template': '/example/1/',
        'name': 'standard_char',
        'scheduled_time': 'default',
        'expiry_type': 0,
        'expiry_time': 'default',
        'status': 0,
        'scheduled_type': 1,
    }
    missing_scheduled_type = {
        'target_controller': '/example/1/',
        'description': 'standard_text',
        'targets': 'default',
        'sender': '/example/1/',
        'template': '/example/1/',
        'name': 'standard_char',
        'scheduled_time': 'default',
        'expiry_type': 0,
        'expiry_time': 'default',
        'status': 0,
    }




