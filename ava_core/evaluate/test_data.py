# Rest Imports
from rest_framework import status
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.evaluate.models import EvaluateController, EvaluateTest, EvaluateTemplate, EvaluateSender, EvaluateResult


# Implementation
class EvaluateControllerTestData(AvaCoreTestData):
    """
    Test data for EvaluateController
    """

    @staticmethod
    def init_requirements():
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if EvaluateTemplate.objects.count() == 0:
            EvaluateTemplateTestData.init_requirements()
            model = EvaluateTemplate.objects.create(**EvaluateTemplateTestData.get_data('standard'))
            model.save()
            model = EvaluateTemplate.objects.create(**EvaluateTemplateTestData.get_data('unique'))
            model.save()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if EvaluateSender.objects.count() == 0:
            EvaluateSenderTestData.init_requirements()
            model = EvaluateSender.objects.create(**EvaluateSenderTestData.get_data('standard'))
            model.save()
            model = EvaluateSender.objects.create(**EvaluateSenderTestData.get_data('unique'))
            model.save()

        # Import the required model and data
        from ava_core.organize.models import Person
        from ava_core.organize.test_data import PersonTestData
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if Person.objects.count() == 0:
            PersonTestData.init_requirements()
            model = Person.objects.create(**PersonTestData.get_data('standard'))
            model.save()
            model = Person.objects.create(**PersonTestData.get_data('unique'))
            model.save()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if EvaluateTest.objects.count() == 0:
            EvaluateTestTestData.init_requirements()
            model = EvaluateTest.objects.create(**EvaluateTestTestData.get_data('standard'))
            model.save()
            model = EvaluateTest.objects.create(**EvaluateTestTestData.get_data('unique'))
            model.save()

    # Store self information
    model = EvaluateController
    url = '/example'

    standard = {
        'template': '/example/1/',
        'sender': '/example/1/',
        'expiry_type': 0,
        'status': 0,
        'scheduled_time': 'default',
        'scheduled_type': 0,
        'targets': 'default',
        'description': 'standard_text',
        'expiry_time': 'default',
        'target_controller': '/example/1/',
        'name': 'standard_char',
    }

    unique = {
        'template': '/example/2/',
        'sender': '/example/2/',
        'expiry_type': 2,
        'status': 4,
        'scheduled_time': 'default',
        'scheduled_type': 1,
        'targets': 'default',
        'description': 'unique_text',
        'expiry_time': 'default',
        'target_controller': '/example/2/',
        'name': 'unique_char',
    }

    modified_template = {
        'template': '/example/2/',
        'sender': '/example/1/',
        'expiry_type': 0,
        'status': 0,
        'scheduled_time': 'default',
        'scheduled_type': 0,
        'targets': 'default',
        'description': 'standard_text',
        'expiry_time': 'default',
        'target_controller': '/example/1/',
        'name': 'standard_char',
    }
    missing_template = {
        'sender': '/example/1/',
        'expiry_type': 0,
        'status': 0,
        'scheduled_time': 'default',
        'scheduled_type': 0,
        'targets': 'default',
        'description': 'standard_text',
        'expiry_time': 'default',
        'target_controller': '/example/1/',
        'name': 'standard_char',
    }

    missing_sender = {
        'template': '/example/1/',
        'expiry_type': 0,
        'status': 0,
        'scheduled_time': 'default',
        'scheduled_type': 0,
        'targets': 'default',
        'description': 'standard_text',
        'expiry_time': 'default',
        'target_controller': '/example/1/',
        'name': 'standard_char',
    }
    modified_sender = {
        'template': '/example/1/',
        'sender': '/example/2/',
        'expiry_type': 0,
        'status': 0,
        'scheduled_time': 'default',
        'scheduled_type': 0,
        'targets': 'default',
        'description': 'standard_text',
        'expiry_time': 'default',
        'target_controller': '/example/1/',
        'name': 'standard_char',
    }

    modified_expiry_type = {
        'template': '/example/1/',
        'sender': '/example/1/',
        'expiry_type': 2,
        'status': 0,
        'scheduled_time': 'default',
        'scheduled_type': 0,
        'targets': 'default',
        'description': 'standard_text',
        'expiry_time': 'default',
        'target_controller': '/example/1/',
        'name': 'standard_char',
    }
    missing_expiry_type = {
        'template': '/example/1/',
        'sender': '/example/1/',
        'status': 0,
        'scheduled_time': 'default',
        'scheduled_type': 0,
        'targets': 'default',
        'description': 'standard_text',
        'expiry_time': 'default',
        'target_controller': '/example/1/',
        'name': 'standard_char',
    }

    missing_status = {
        'template': '/example/1/',
        'sender': '/example/1/',
        'expiry_type': 0,
        'scheduled_time': 'default',
        'scheduled_type': 0,
        'targets': 'default',
        'description': 'standard_text',
        'expiry_time': 'default',
        'target_controller': '/example/1/',
        'name': 'standard_char',
    }
    modified_status = {
        'template': '/example/1/',
        'sender': '/example/1/',
        'expiry_type': 0,
        'status': 4,
        'scheduled_time': 'default',
        'scheduled_type': 0,
        'targets': 'default',
        'description': 'standard_text',
        'expiry_time': 'default',
        'target_controller': '/example/1/',
        'name': 'standard_char',
    }

    missing_scheduled_time = {
        'template': '/example/1/',
        'sender': '/example/1/',
        'expiry_type': 0,
        'status': 0,
        'scheduled_type': 0,
        'targets': 'default',
        'description': 'standard_text',
        'expiry_time': 'default',
        'target_controller': '/example/1/',
        'name': 'standard_char',
    }
    modified_scheduled_time = {
        'template': '/example/1/',
        'sender': '/example/1/',
        'expiry_type': 0,
        'status': 0,
        'scheduled_time': 'default',
        'scheduled_type': 0,
        'targets': 'default',
        'description': 'standard_text',
        'expiry_time': 'default',
        'target_controller': '/example/1/',
        'name': 'standard_char',
    }

    missing_scheduled_type = {
        'template': '/example/1/',
        'sender': '/example/1/',
        'expiry_type': 0,
        'status': 0,
        'scheduled_time': 'default',
        'targets': 'default',
        'description': 'standard_text',
        'expiry_time': 'default',
        'target_controller': '/example/1/',
        'name': 'standard_char',
    }
    modified_scheduled_type = {
        'template': '/example/1/',
        'sender': '/example/1/',
        'expiry_type': 0,
        'status': 0,
        'scheduled_time': 'default',
        'scheduled_type': 1,
        'targets': 'default',
        'description': 'standard_text',
        'expiry_time': 'default',
        'target_controller': '/example/1/',
        'name': 'standard_char',
    }

    missing_targets = {
        'template': '/example/1/',
        'sender': '/example/1/',
        'expiry_type': 0,
        'status': 0,
        'scheduled_time': 'default',
        'scheduled_type': 0,
        'description': 'standard_text',
        'expiry_time': 'default',
        'target_controller': '/example/1/',
        'name': 'standard_char',
    }
    modified_targets = {
        'template': '/example/1/',
        'sender': '/example/1/',
        'expiry_type': 0,
        'status': 0,
        'scheduled_time': 'default',
        'scheduled_type': 0,
        'targets': 'default',
        'description': 'standard_text',
        'expiry_time': 'default',
        'target_controller': '/example/1/',
        'name': 'standard_char',
    }

    modified_description = {
        'template': '/example/1/',
        'sender': '/example/1/',
        'expiry_type': 0,
        'status': 0,
        'scheduled_time': 'default',
        'scheduled_type': 0,
        'targets': 'default',
        'description': 'modified_text',
        'expiry_time': 'default',
        'target_controller': '/example/1/',
        'name': 'standard_char',
    }
    missing_description = {
        'template': '/example/1/',
        'sender': '/example/1/',
        'expiry_type': 0,
        'status': 0,
        'scheduled_time': 'default',
        'scheduled_type': 0,
        'targets': 'default',
        'expiry_time': 'default',
        'target_controller': '/example/1/',
        'name': 'standard_char',
    }

    missing_expiry_time = {
        'template': '/example/1/',
        'sender': '/example/1/',
        'expiry_type': 0,
        'status': 0,
        'scheduled_time': 'default',
        'scheduled_type': 0,
        'targets': 'default',
        'description': 'standard_text',
        'target_controller': '/example/1/',
        'name': 'standard_char',
    }
    modified_expiry_time = {
        'template': '/example/1/',
        'sender': '/example/1/',
        'expiry_type': 0,
        'status': 0,
        'scheduled_time': 'default',
        'scheduled_type': 0,
        'targets': 'default',
        'description': 'standard_text',
        'expiry_time': 'default',
        'target_controller': '/example/1/',
        'name': 'standard_char',
    }

    missing_target_controller = {
        'template': '/example/1/',
        'sender': '/example/1/',
        'expiry_type': 0,
        'status': 0,
        'scheduled_time': 'default',
        'scheduled_type': 0,
        'targets': 'default',
        'description': 'standard_text',
        'expiry_time': 'default',
        'name': 'standard_char',
    }
    modified_target_controller = {
        'template': '/example/1/',
        'sender': '/example/1/',
        'expiry_type': 0,
        'status': 0,
        'scheduled_time': 'default',
        'scheduled_type': 0,
        'targets': 'default',
        'description': 'standard_text',
        'expiry_time': 'default',
        'target_controller': '/example/2/',
        'name': 'standard_char',
    }

    modified_name = {
        'template': '/example/1/',
        'sender': '/example/1/',
        'expiry_type': 0,
        'status': 0,
        'scheduled_time': 'default',
        'scheduled_type': 0,
        'targets': 'default',
        'description': 'standard_text',
        'expiry_time': 'default',
        'target_controller': '/example/1/',
        'name': 'modified_char',
    }
    missing_name = {
        'template': '/example/1/',
        'sender': '/example/1/',
        'expiry_type': 0,
        'status': 0,
        'scheduled_time': 'default',
        'scheduled_type': 0,
        'targets': 'default',
        'description': 'standard_text',
        'expiry_time': 'default',
        'target_controller': '/example/1/',
    }



class EvaluateTestTestData(AvaCoreTestData):
    """
    Test data for EvaluateTest
    """

    @staticmethod
    def init_requirements():
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if EvaluateResult.objects.count() == 0:
            EvaluateResultTestData.init_requirements()
            model = EvaluateResult.objects.create(**EvaluateResultTestData.get_data('standard'))
            model.save()
            model = EvaluateResult.objects.create(**EvaluateResultTestData.get_data('unique'))
            model.save()

        # Import the required model and data
        from ava_core.organize.models import Person
        from ava_core.organize.test_data import PersonTestData
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if Person.objects.count() == 0:
            PersonTestData.init_requirements()
            model = Person.objects.create(**PersonTestData.get_data('standard'))
            model.save()
            model = Person.objects.create(**PersonTestData.get_data('unique'))
            model.save()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if EvaluateController.objects.count() == 0:
            EvaluateControllerTestData.init_requirements()
            model = EvaluateController.objects.create(**EvaluateControllerTestData.get_data('standard'))
            model.save()
            model = EvaluateController.objects.create(**EvaluateControllerTestData.get_data('unique'))
            model.save()

    # Store self information
    model = EvaluateTest
    url = '/example'

    standard = {
        'evaluateresult': '/example/1/',
        'target': '/example/1/',
        'delivery_status': 0,
        'token': 'standard_char',
        'controller': '/example/1/',
    }

    unique = {
        'evaluateresult': '/example/2/',
        'target': '/example/2/',
        'delivery_status': 3,
        'token': 'unique_char',
        'controller': '/example/2/',
    }

    missing_evaluateresult = {
        'target': '/example/1/',
        'delivery_status': 0,
        'token': 'standard_char',
        'controller': '/example/1/',
    }
    modified_evaluateresult = {
        'evaluateresult': '/example/2/',
        'target': '/example/1/',
        'delivery_status': 0,
        'token': 'standard_char',
        'controller': '/example/1/',
    }

    modified_target = {
        'evaluateresult': '/example/1/',
        'target': '/example/2/',
        'delivery_status': 0,
        'token': 'standard_char',
        'controller': '/example/1/',
    }
    missing_target = {
        'evaluateresult': '/example/1/',
        'delivery_status': 0,
        'token': 'standard_char',
        'controller': '/example/1/',
    }

    modified_delivery_status = {
        'evaluateresult': '/example/1/',
        'target': '/example/1/',
        'delivery_status': 3,
        'token': 'standard_char',
        'controller': '/example/1/',
    }
    missing_delivery_status = {
        'evaluateresult': '/example/1/',
        'target': '/example/1/',
        'token': 'standard_char',
        'controller': '/example/1/',
    }

    missing_token = {
        'evaluateresult': '/example/1/',
        'target': '/example/1/',
        'delivery_status': 0,
        'controller': '/example/1/',
    }
    modified_token = {
        'evaluateresult': '/example/1/',
        'target': '/example/1/',
        'delivery_status': 0,
        'token': 'modified_char',
        'controller': '/example/1/',
    }

    missing_controller = {
        'evaluateresult': '/example/1/',
        'target': '/example/1/',
        'delivery_status': 0,
        'token': 'standard_char',
    }
    modified_controller = {
        'evaluateresult': '/example/1/',
        'target': '/example/1/',
        'delivery_status': 0,
        'token': 'standard_char',
        'controller': '/example/2/',
    }



class EvaluateTemplateTestData(AvaCoreTestData):
    """
    Test data for EvaluateTemplate
    """

    @staticmethod
    def init_requirements():
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if EvaluateController.objects.count() == 0:
            EvaluateControllerTestData.init_requirements()
            model = EvaluateController.objects.create(**EvaluateControllerTestData.get_data('standard'))
            model.save()
            model = EvaluateController.objects.create(**EvaluateControllerTestData.get_data('unique'))
            model.save()

    # Store self information
    model = EvaluateTemplate
    url = '/example'

    standard = {
        'email_subject': 'standard_char',
        'hidden': True,
        'template_type': 0,
        'description': 'standard_text',
        'email_body': 'standard_text',
        'evaluatecontroller': '/example/1/',
        'name': 'standard_char',
    }

    unique = {
        'email_subject': 'unique_char',
        'hidden': False,
        'template_type': 1,
        'description': 'unique_text',
        'email_body': 'unique_text',
        'evaluatecontroller': '/example/2/',
        'name': 'unique_char',
    }

    modified_email_subject = {
        'email_subject': 'modified_char',
        'hidden': True,
        'template_type': 0,
        'description': 'standard_text',
        'email_body': 'standard_text',
        'evaluatecontroller': '/example/1/',
        'name': 'standard_char',
    }
    missing_email_subject = {
        'hidden': True,
        'template_type': 0,
        'description': 'standard_text',
        'email_body': 'standard_text',
        'evaluatecontroller': '/example/1/',
        'name': 'standard_char',
    }

    missing_hidden = {
        'email_subject': 'standard_char',
        'template_type': 0,
        'description': 'standard_text',
        'email_body': 'standard_text',
        'evaluatecontroller': '/example/1/',
        'name': 'standard_char',
    }
    modified_hidden = {
        'email_subject': 'standard_char',
        'hidden': False,
        'template_type': 0,
        'description': 'standard_text',
        'email_body': 'standard_text',
        'evaluatecontroller': '/example/1/',
        'name': 'standard_char',
    }

    missing_template_type = {
        'email_subject': 'standard_char',
        'hidden': True,
        'description': 'standard_text',
        'email_body': 'standard_text',
        'evaluatecontroller': '/example/1/',
        'name': 'standard_char',
    }
    modified_template_type = {
        'email_subject': 'standard_char',
        'hidden': True,
        'template_type': 1,
        'description': 'standard_text',
        'email_body': 'standard_text',
        'evaluatecontroller': '/example/1/',
        'name': 'standard_char',
    }

    modified_description = {
        'email_subject': 'standard_char',
        'hidden': True,
        'template_type': 0,
        'description': 'modified_text',
        'email_body': 'standard_text',
        'evaluatecontroller': '/example/1/',
        'name': 'standard_char',
    }
    missing_description = {
        'email_subject': 'standard_char',
        'hidden': True,
        'template_type': 0,
        'email_body': 'standard_text',
        'evaluatecontroller': '/example/1/',
        'name': 'standard_char',
    }

    modified_email_body = {
        'email_subject': 'standard_char',
        'hidden': True,
        'template_type': 0,
        'description': 'standard_text',
        'email_body': 'modified_text',
        'evaluatecontroller': '/example/1/',
        'name': 'standard_char',
    }
    missing_email_body = {
        'email_subject': 'standard_char',
        'hidden': True,
        'template_type': 0,
        'description': 'standard_text',
        'evaluatecontroller': '/example/1/',
        'name': 'standard_char',
    }

    modified_evaluatecontroller = {
        'email_subject': 'standard_char',
        'hidden': True,
        'template_type': 0,
        'description': 'standard_text',
        'email_body': 'standard_text',
        'evaluatecontroller': '/example/2/',
        'name': 'standard_char',
    }
    missing_evaluatecontroller = {
        'email_subject': 'standard_char',
        'hidden': True,
        'template_type': 0,
        'description': 'standard_text',
        'email_body': 'standard_text',
        'name': 'standard_char',
    }

    modified_name = {
        'email_subject': 'standard_char',
        'hidden': True,
        'template_type': 0,
        'description': 'standard_text',
        'email_body': 'standard_text',
        'evaluatecontroller': '/example/1/',
        'name': 'modified_char',
    }
    missing_name = {
        'email_subject': 'standard_char',
        'hidden': True,
        'template_type': 0,
        'description': 'standard_text',
        'email_body': 'standard_text',
        'evaluatecontroller': '/example/1/',
    }



class EvaluateSenderTestData(AvaCoreTestData):
    """
    Test data for EvaluateSender
    """

    @staticmethod
    def init_requirements():
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if EvaluateController.objects.count() == 0:
            EvaluateControllerTestData.init_requirements()
            model = EvaluateController.objects.create(**EvaluateControllerTestData.get_data('standard'))
            model.save()
            model = EvaluateController.objects.create(**EvaluateControllerTestData.get_data('unique'))
            model.save()

    # Store self information
    model = EvaluateSender
    url = '/example'

    standard = {
        'hidden': True,
        'slack_name': 'standard_char',
        'evaluatecontroller': '/example/1/',
        'last_name': 'standard_char',
        'first_name': 'standard_char',
        'email_address': 'standard_char',
    }

    unique = {
        'hidden': False,
        'slack_name': 'unique_char',
        'evaluatecontroller': '/example/2/',
        'last_name': 'unique_char',
        'first_name': 'unique_char',
        'email_address': 'unique_char',
    }

    missing_hidden = {
        'slack_name': 'standard_char',
        'evaluatecontroller': '/example/1/',
        'last_name': 'standard_char',
        'first_name': 'standard_char',
        'email_address': 'standard_char',
    }
    modified_hidden = {
        'hidden': False,
        'slack_name': 'standard_char',
        'evaluatecontroller': '/example/1/',
        'last_name': 'standard_char',
        'first_name': 'standard_char',
        'email_address': 'standard_char',
    }

    missing_slack_name = {
        'hidden': True,
        'evaluatecontroller': '/example/1/',
        'last_name': 'standard_char',
        'first_name': 'standard_char',
        'email_address': 'standard_char',
    }
    modified_slack_name = {
        'hidden': True,
        'slack_name': 'modified_char',
        'evaluatecontroller': '/example/1/',
        'last_name': 'standard_char',
        'first_name': 'standard_char',
        'email_address': 'standard_char',
    }

    modified_evaluatecontroller = {
        'hidden': True,
        'slack_name': 'standard_char',
        'evaluatecontroller': '/example/2/',
        'last_name': 'standard_char',
        'first_name': 'standard_char',
        'email_address': 'standard_char',
    }
    missing_evaluatecontroller = {
        'hidden': True,
        'slack_name': 'standard_char',
        'last_name': 'standard_char',
        'first_name': 'standard_char',
        'email_address': 'standard_char',
    }

    missing_last_name = {
        'hidden': True,
        'slack_name': 'standard_char',
        'evaluatecontroller': '/example/1/',
        'first_name': 'standard_char',
        'email_address': 'standard_char',
    }
    modified_last_name = {
        'hidden': True,
        'slack_name': 'standard_char',
        'evaluatecontroller': '/example/1/',
        'last_name': 'modified_char',
        'first_name': 'standard_char',
        'email_address': 'standard_char',
    }

    missing_first_name = {
        'hidden': True,
        'slack_name': 'standard_char',
        'evaluatecontroller': '/example/1/',
        'last_name': 'standard_char',
        'email_address': 'standard_char',
    }
    modified_first_name = {
        'hidden': True,
        'slack_name': 'standard_char',
        'evaluatecontroller': '/example/1/',
        'last_name': 'standard_char',
        'first_name': 'modified_char',
        'email_address': 'standard_char',
    }

    modified_email_address = {
        'hidden': True,
        'slack_name': 'standard_char',
        'evaluatecontroller': '/example/1/',
        'last_name': 'standard_char',
        'first_name': 'standard_char',
        'email_address': 'modified_char',
    }
    missing_email_address = {
        'hidden': True,
        'slack_name': 'standard_char',
        'evaluatecontroller': '/example/1/',
        'last_name': 'standard_char',
        'first_name': 'standard_char',
    }



class EvaluateResultTestData(AvaCoreTestData):
    """
    Test data for EvaluateResult
    """

    @staticmethod
    def init_requirements():
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if EvaluateTest.objects.count() == 0:
            EvaluateTestTestData.init_requirements()
            model = EvaluateTest.objects.create(**EvaluateTestTestData.get_data('standard'))
            model.save()
            model = EvaluateTest.objects.create(**EvaluateTestTestData.get_data('unique'))
            model.save()

    # Store self information
    model = EvaluateResult
    url = '/example'

    standard = {
        'target_profile': '/example/1/',
        'result': 0,
    }

    unique = {
        'target_profile': '/example/2/',
        'result': 1,
    }

    missing_target_profile = {
        'result': 0,
    }
    modified_target_profile = {
        'target_profile': '/example/2/',
        'result': 0,
    }

    modified_result = {
        'target_profile': '/example/1/',
        'result': 1,
    }
    missing_result = {
        'target_profile': '/example/1/',
    }




