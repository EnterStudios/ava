# Rest Imports
from rest_framework import status
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
        # Grab data for object creation, with owner if required.
        data_model = EvaluateControllerTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = EvaluateController.objects.filter(owner=owner['email']) if 'email' in standard_data else EvaluateController.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            EvaluateControllerTestData.init_requirements(owner)
            model = EvaluateController.objects.create(**standard_data)
            model = EvaluateController.objects.create(**unique_data)

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

    modified_last_name = {
        'last_name': 'modified_char',
        'email_address': 'standard_char',
        'hidden': True,
        'evaluatecontroller': 'example//1/',
        'slack_name': 'standard_char',
        'first_name': 'standard_char',
    }
    missing_last_name = {
        'email_address': 'standard_char',
        'hidden': True,
        'evaluatecontroller': 'example//1/',
        'slack_name': 'standard_char',
        'first_name': 'standard_char',
    }

    modified_email_address = {
        'last_name': 'standard_char',
        'email_address': 'modified_char',
        'hidden': True,
        'evaluatecontroller': 'example//1/',
        'slack_name': 'standard_char',
        'first_name': 'standard_char',
    }
    missing_email_address = {
        'last_name': 'standard_char',
        'hidden': True,
        'evaluatecontroller': 'example//1/',
        'slack_name': 'standard_char',
        'first_name': 'standard_char',
    }

    modified_hidden = {
        'last_name': 'standard_char',
        'email_address': 'standard_char',
        'hidden': False,
        'evaluatecontroller': 'example//1/',
        'slack_name': 'standard_char',
        'first_name': 'standard_char',
    }
    missing_hidden = {
        'last_name': 'standard_char',
        'email_address': 'standard_char',
        'evaluatecontroller': 'example//1/',
        'slack_name': 'standard_char',
        'first_name': 'standard_char',
    }

    missing_evaluatecontroller = {
        'last_name': 'standard_char',
        'email_address': 'standard_char',
        'hidden': True,
        'slack_name': 'standard_char',
        'first_name': 'standard_char',
    }
    modified_evaluatecontroller = {
        'last_name': 'standard_char',
        'email_address': 'standard_char',
        'hidden': True,
        'evaluatecontroller': 'example//2/',
        'slack_name': 'standard_char',
        'first_name': 'standard_char',
    }

    missing_slack_name = {
        'last_name': 'standard_char',
        'email_address': 'standard_char',
        'hidden': True,
        'evaluatecontroller': 'example//1/',
        'first_name': 'standard_char',
    }
    modified_slack_name = {
        'last_name': 'standard_char',
        'email_address': 'standard_char',
        'hidden': True,
        'evaluatecontroller': 'example//1/',
        'slack_name': 'modified_char',
        'first_name': 'standard_char',
    }

    missing_first_name = {
        'last_name': 'standard_char',
        'email_address': 'standard_char',
        'hidden': True,
        'evaluatecontroller': 'example//1/',
        'slack_name': 'standard_char',
    }
    modified_first_name = {
        'last_name': 'standard_char',
        'email_address': 'standard_char',
        'hidden': True,
        'evaluatecontroller': 'example//1/',
        'slack_name': 'standard_char',
        'first_name': 'modified_char',
    }



class EvaluateResultTestData(AvaCoreTestData):
    """
    Test data for EvaluateResult
    """

    @staticmethod
    def init_requirements(owner):
        # Grab data for object creation, with owner if required.
        data_model = EvaluateTestTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = EvaluateTest.objects.filter(owner=owner['email']) if 'email' in standard_data else EvaluateTest.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            EvaluateTestTestData.init_requirements(owner)
            model = EvaluateTest.objects.create(**standard_data)
            model = EvaluateTest.objects.create(**unique_data)

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

    missing_result = {
        'target_profile': 'example//1/',
    }
    modified_result = {
        'result': 1,
        'target_profile': 'example//1/',
    }

    modified_target_profile = {
        'result': 0,
        'target_profile': 'example//2/',
    }
    missing_target_profile = {
        'result': 0,
    }



class EvaluateTemplateTestData(AvaCoreTestData):
    """
    Test data for EvaluateTemplate
    """

    @staticmethod
    def init_requirements(owner):
        # Grab data for object creation, with owner if required.
        data_model = EvaluateControllerTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = EvaluateController.objects.filter(owner=owner['email']) if 'email' in standard_data else EvaluateController.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            EvaluateControllerTestData.init_requirements(owner)
            model = EvaluateController.objects.create(**standard_data)
            model = EvaluateController.objects.create(**unique_data)

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

    modified_name = {
        'name': 'modified_char',
        'template_type': 0,
        'description': 'standard_text',
        'hidden': True,
        'evaluatecontroller': 'example//1/',
        'email_body': 'standard_text',
        'email_subject': 'standard_char',
    }
    missing_name = {
        'template_type': 0,
        'description': 'standard_text',
        'hidden': True,
        'evaluatecontroller': 'example//1/',
        'email_body': 'standard_text',
        'email_subject': 'standard_char',
    }

    modified_template_type = {
        'name': 'standard_char',
        'template_type': 1,
        'description': 'standard_text',
        'hidden': True,
        'evaluatecontroller': 'example//1/',
        'email_body': 'standard_text',
        'email_subject': 'standard_char',
    }
    missing_template_type = {
        'name': 'standard_char',
        'description': 'standard_text',
        'hidden': True,
        'evaluatecontroller': 'example//1/',
        'email_body': 'standard_text',
        'email_subject': 'standard_char',
    }

    missing_description = {
        'name': 'standard_char',
        'template_type': 0,
        'hidden': True,
        'evaluatecontroller': 'example//1/',
        'email_body': 'standard_text',
        'email_subject': 'standard_char',
    }
    modified_description = {
        'name': 'standard_char',
        'template_type': 0,
        'description': 'modified_text',
        'hidden': True,
        'evaluatecontroller': 'example//1/',
        'email_body': 'standard_text',
        'email_subject': 'standard_char',
    }

    modified_hidden = {
        'name': 'standard_char',
        'template_type': 0,
        'description': 'standard_text',
        'hidden': False,
        'evaluatecontroller': 'example//1/',
        'email_body': 'standard_text',
        'email_subject': 'standard_char',
    }
    missing_hidden = {
        'name': 'standard_char',
        'template_type': 0,
        'description': 'standard_text',
        'evaluatecontroller': 'example//1/',
        'email_body': 'standard_text',
        'email_subject': 'standard_char',
    }

    missing_evaluatecontroller = {
        'name': 'standard_char',
        'template_type': 0,
        'description': 'standard_text',
        'hidden': True,
        'email_body': 'standard_text',
        'email_subject': 'standard_char',
    }
    modified_evaluatecontroller = {
        'name': 'standard_char',
        'template_type': 0,
        'description': 'standard_text',
        'hidden': True,
        'evaluatecontroller': 'example//2/',
        'email_body': 'standard_text',
        'email_subject': 'standard_char',
    }

    modified_email_body = {
        'name': 'standard_char',
        'template_type': 0,
        'description': 'standard_text',
        'hidden': True,
        'evaluatecontroller': 'example//1/',
        'email_body': 'modified_text',
        'email_subject': 'standard_char',
    }
    missing_email_body = {
        'name': 'standard_char',
        'template_type': 0,
        'description': 'standard_text',
        'hidden': True,
        'evaluatecontroller': 'example//1/',
        'email_subject': 'standard_char',
    }

    modified_email_subject = {
        'name': 'standard_char',
        'template_type': 0,
        'description': 'standard_text',
        'hidden': True,
        'evaluatecontroller': 'example//1/',
        'email_body': 'standard_text',
        'email_subject': 'modified_char',
    }
    missing_email_subject = {
        'name': 'standard_char',
        'template_type': 0,
        'description': 'standard_text',
        'hidden': True,
        'evaluatecontroller': 'example//1/',
        'email_body': 'standard_text',
    }



class EvaluateControllerTestData(AvaCoreTestData):
    """
    Test data for EvaluateController
    """

    @staticmethod
    def init_requirements(owner):
        # Grab data for object creation, with owner if required.
        data_model = EvaluateSenderTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = EvaluateSender.objects.filter(owner=owner['email']) if 'email' in standard_data else EvaluateSender.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            EvaluateSenderTestData.init_requirements(owner)
            model = EvaluateSender.objects.create(**standard_data)
            model = EvaluateSender.objects.create(**unique_data)

        # Grab data for object creation, with owner if required.
        data_model = EvaluateTemplateTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = EvaluateTemplate.objects.filter(owner=owner['email']) if 'email' in standard_data else EvaluateTemplate.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            EvaluateTemplateTestData.init_requirements(owner)
            model = EvaluateTemplate.objects.create(**standard_data)
            model = EvaluateTemplate.objects.create(**unique_data)

        # Grab data for object creation, with owner if required.
        data_model = EvaluateTestTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = EvaluateTest.objects.filter(owner=owner['email']) if 'email' in standard_data else EvaluateTest.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            EvaluateTestTestData.init_requirements(owner)
            model = EvaluateTest.objects.create(**standard_data)
            model = EvaluateTest.objects.create(**unique_data)

        # Import the required model and data
        from ava_core.organize.models import Person
        from ava_core.organize.test_data import PersonTestData
        # Grab data for object creation, with owner if required.
        data_model = PersonTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = Person.objects.filter(owner=owner['email']) if 'email' in standard_data else Person.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            PersonTestData.init_requirements(owner)
            model = Person.objects.create(**standard_data)
            model = Person.objects.create(**unique_data)

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

    missing_expiry_type = {
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
    modified_expiry_type = {
        'expiry_type': 2,
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

    modified_name = {
        'expiry_type': 0,
        'name': 'modified_char',
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
    missing_name = {
        'expiry_type': 0,
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

    modified_sender = {
        'expiry_type': 0,
        'name': 'standard_char',
        'sender': 'example//2/',
        'status': 0,
        'description': 'standard_text',
        'scheduled_time': 'default',
        'template': 'example//1/',
        'scheduled_type': 0,
        'target_controller': 'example//1/',
        'expiry_time': 'default',
        'targets': 'default',
    }
    missing_sender = {
        'expiry_type': 0,
        'name': 'standard_char',
        'status': 0,
        'description': 'standard_text',
        'scheduled_time': 'default',
        'template': 'example//1/',
        'scheduled_type': 0,
        'target_controller': 'example//1/',
        'expiry_time': 'default',
        'targets': 'default',
    }

    missing_status = {
        'expiry_type': 0,
        'name': 'standard_char',
        'sender': 'example//1/',
        'description': 'standard_text',
        'scheduled_time': 'default',
        'template': 'example//1/',
        'scheduled_type': 0,
        'target_controller': 'example//1/',
        'expiry_time': 'default',
        'targets': 'default',
    }
    modified_status = {
        'expiry_type': 0,
        'name': 'standard_char',
        'sender': 'example//1/',
        'status': 4,
        'description': 'standard_text',
        'scheduled_time': 'default',
        'template': 'example//1/',
        'scheduled_type': 0,
        'target_controller': 'example//1/',
        'expiry_time': 'default',
        'targets': 'default',
    }

    missing_description = {
        'expiry_type': 0,
        'name': 'standard_char',
        'sender': 'example//1/',
        'status': 0,
        'scheduled_time': 'default',
        'template': 'example//1/',
        'scheduled_type': 0,
        'target_controller': 'example//1/',
        'expiry_time': 'default',
        'targets': 'default',
    }
    modified_description = {
        'expiry_type': 0,
        'name': 'standard_char',
        'sender': 'example//1/',
        'status': 0,
        'description': 'modified_text',
        'scheduled_time': 'default',
        'template': 'example//1/',
        'scheduled_type': 0,
        'target_controller': 'example//1/',
        'expiry_time': 'default',
        'targets': 'default',
    }

    missing_scheduled_time = {
        'expiry_type': 0,
        'name': 'standard_char',
        'sender': 'example//1/',
        'status': 0,
        'description': 'standard_text',
        'template': 'example//1/',
        'scheduled_type': 0,
        'target_controller': 'example//1/',
        'expiry_time': 'default',
        'targets': 'default',
    }
    modified_scheduled_time = {
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

    modified_template = {
        'expiry_type': 0,
        'name': 'standard_char',
        'sender': 'example//1/',
        'status': 0,
        'description': 'standard_text',
        'scheduled_time': 'default',
        'template': 'example//2/',
        'scheduled_type': 0,
        'target_controller': 'example//1/',
        'expiry_time': 'default',
        'targets': 'default',
    }
    missing_template = {
        'expiry_type': 0,
        'name': 'standard_char',
        'sender': 'example//1/',
        'status': 0,
        'description': 'standard_text',
        'scheduled_time': 'default',
        'scheduled_type': 0,
        'target_controller': 'example//1/',
        'expiry_time': 'default',
        'targets': 'default',
    }

    missing_scheduled_type = {
        'expiry_type': 0,
        'name': 'standard_char',
        'sender': 'example//1/',
        'status': 0,
        'description': 'standard_text',
        'scheduled_time': 'default',
        'template': 'example//1/',
        'target_controller': 'example//1/',
        'expiry_time': 'default',
        'targets': 'default',
    }
    modified_scheduled_type = {
        'expiry_type': 0,
        'name': 'standard_char',
        'sender': 'example//1/',
        'status': 0,
        'description': 'standard_text',
        'scheduled_time': 'default',
        'template': 'example//1/',
        'scheduled_type': 1,
        'target_controller': 'example//1/',
        'expiry_time': 'default',
        'targets': 'default',
    }

    missing_target_controller = {
        'expiry_type': 0,
        'name': 'standard_char',
        'sender': 'example//1/',
        'status': 0,
        'description': 'standard_text',
        'scheduled_time': 'default',
        'template': 'example//1/',
        'scheduled_type': 0,
        'expiry_time': 'default',
        'targets': 'default',
    }
    modified_target_controller = {
        'expiry_type': 0,
        'name': 'standard_char',
        'sender': 'example//1/',
        'status': 0,
        'description': 'standard_text',
        'scheduled_time': 'default',
        'template': 'example//1/',
        'scheduled_type': 0,
        'target_controller': 'example//2/',
        'expiry_time': 'default',
        'targets': 'default',
    }

    modified_expiry_time = {
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
    missing_expiry_time = {
        'expiry_type': 0,
        'name': 'standard_char',
        'sender': 'example//1/',
        'status': 0,
        'description': 'standard_text',
        'scheduled_time': 'default',
        'template': 'example//1/',
        'scheduled_type': 0,
        'target_controller': 'example//1/',
        'targets': 'default',
    }

    modified_targets = {
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
    missing_targets = {
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
    }



class EvaluateTestTestData(AvaCoreTestData):
    """
    Test data for EvaluateTest
    """

    @staticmethod
    def init_requirements(owner):
        # Grab data for object creation, with owner if required.
        data_model = EvaluateControllerTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = EvaluateController.objects.filter(owner=owner['email']) if 'email' in standard_data else EvaluateController.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            EvaluateControllerTestData.init_requirements(owner)
            model = EvaluateController.objects.create(**standard_data)
            model = EvaluateController.objects.create(**unique_data)

        # Import the required model and data
        from ava_core.organize.models import Person
        from ava_core.organize.test_data import PersonTestData
        # Grab data for object creation, with owner if required.
        data_model = PersonTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = Person.objects.filter(owner=owner['email']) if 'email' in standard_data else Person.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            PersonTestData.init_requirements(owner)
            model = Person.objects.create(**standard_data)
            model = Person.objects.create(**unique_data)

        # Grab data for object creation, with owner if required.
        data_model = EvaluateResultTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = EvaluateResult.objects.filter(owner=owner['email']) if 'email' in standard_data else EvaluateResult.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            EvaluateResultTestData.init_requirements(owner)
            model = EvaluateResult.objects.create(**standard_data)
            model = EvaluateResult.objects.create(**unique_data)

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

    missing_token = {
        'controller': 'example//1/',
        'target': 'example//1/',
        'evaluateresult': 'example//1/',
        'delivery_status': 0,
    }
    modified_token = {
        'token': 'modified_char',
        'controller': 'example//1/',
        'target': 'example//1/',
        'evaluateresult': 'example//1/',
        'delivery_status': 0,
    }

    modified_controller = {
        'token': 'standard_char',
        'controller': 'example//2/',
        'target': 'example//1/',
        'evaluateresult': 'example//1/',
        'delivery_status': 0,
    }
    missing_controller = {
        'token': 'standard_char',
        'target': 'example//1/',
        'evaluateresult': 'example//1/',
        'delivery_status': 0,
    }

    missing_target = {
        'token': 'standard_char',
        'controller': 'example//1/',
        'evaluateresult': 'example//1/',
        'delivery_status': 0,
    }
    modified_target = {
        'token': 'standard_char',
        'controller': 'example//1/',
        'target': 'example//2/',
        'evaluateresult': 'example//1/',
        'delivery_status': 0,
    }

    modified_evaluateresult = {
        'token': 'standard_char',
        'controller': 'example//1/',
        'target': 'example//1/',
        'evaluateresult': 'example//2/',
        'delivery_status': 0,
    }
    missing_evaluateresult = {
        'token': 'standard_char',
        'controller': 'example//1/',
        'target': 'example//1/',
        'delivery_status': 0,
    }

    modified_delivery_status = {
        'token': 'standard_char',
        'controller': 'example//1/',
        'target': 'example//1/',
        'evaluateresult': 'example//1/',
        'delivery_status': 3,
    }
    missing_delivery_status = {
        'token': 'standard_char',
        'controller': 'example//1/',
        'target': 'example//1/',
        'evaluateresult': 'example//1/',
    }




