# Rest Imports
from rest_framework import status
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.evaluate.models import EvaluateSender, EvaluateTest, EvaluateController, EvaluateTemplate, EvaluateResult


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
        'evaluatecontroller': 'example//1/',
        'first_name': 'standard_char',
        'slack_name': 'standard_char',
        'last_name': 'standard_char',
        'email_address': 'standard_char',
        'hidden': True,
    }

    unique = {
        'evaluatecontroller': 'example//2/',
        'first_name': 'unique_char',
        'slack_name': 'unique_char',
        'last_name': 'unique_char',
        'email_address': 'unique_char',
        'hidden': False,
    }

    missing_evaluatecontroller = {
        'first_name': 'standard_char',
        'slack_name': 'standard_char',
        'last_name': 'standard_char',
        'email_address': 'standard_char',
        'hidden': True,
    }
    modified_evaluatecontroller = {
        'evaluatecontroller': 'example//2/',
        'first_name': 'standard_char',
        'slack_name': 'standard_char',
        'last_name': 'standard_char',
        'email_address': 'standard_char',
        'hidden': True,
    }

    modified_first_name = {
        'evaluatecontroller': 'example//1/',
        'first_name': 'modified_char',
        'slack_name': 'standard_char',
        'last_name': 'standard_char',
        'email_address': 'standard_char',
        'hidden': True,
    }
    missing_first_name = {
        'evaluatecontroller': 'example//1/',
        'slack_name': 'standard_char',
        'last_name': 'standard_char',
        'email_address': 'standard_char',
        'hidden': True,
    }

    missing_slack_name = {
        'evaluatecontroller': 'example//1/',
        'first_name': 'standard_char',
        'last_name': 'standard_char',
        'email_address': 'standard_char',
        'hidden': True,
    }
    modified_slack_name = {
        'evaluatecontroller': 'example//1/',
        'first_name': 'standard_char',
        'slack_name': 'modified_char',
        'last_name': 'standard_char',
        'email_address': 'standard_char',
        'hidden': True,
    }

    missing_last_name = {
        'evaluatecontroller': 'example//1/',
        'first_name': 'standard_char',
        'slack_name': 'standard_char',
        'email_address': 'standard_char',
        'hidden': True,
    }
    modified_last_name = {
        'evaluatecontroller': 'example//1/',
        'first_name': 'standard_char',
        'slack_name': 'standard_char',
        'last_name': 'modified_char',
        'email_address': 'standard_char',
        'hidden': True,
    }

    missing_email_address = {
        'evaluatecontroller': 'example//1/',
        'first_name': 'standard_char',
        'slack_name': 'standard_char',
        'last_name': 'standard_char',
        'hidden': True,
    }
    modified_email_address = {
        'evaluatecontroller': 'example//1/',
        'first_name': 'standard_char',
        'slack_name': 'standard_char',
        'last_name': 'standard_char',
        'email_address': 'modified_char',
        'hidden': True,
    }

    missing_hidden = {
        'evaluatecontroller': 'example//1/',
        'first_name': 'standard_char',
        'slack_name': 'standard_char',
        'last_name': 'standard_char',
        'email_address': 'standard_char',
    }
    modified_hidden = {
        'evaluatecontroller': 'example//1/',
        'first_name': 'standard_char',
        'slack_name': 'standard_char',
        'last_name': 'standard_char',
        'email_address': 'standard_char',
        'hidden': False,
    }



class EvaluateTestTestData(AvaCoreTestData):
    """
    Test data for EvaluateTest
    """

    @staticmethod
    def init_requirements(owner):
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

    # Store self information
    model = EvaluateTest
    url = 'example/'

    standard = {
        'token': 'standard_char',
        'evaluateresult': 'example//1/',
        'delivery_status': 0,
        'controller': 'example//1/',
        'target': 'example//1/',
    }

    unique = {
        'token': 'unique_char',
        'evaluateresult': 'example//2/',
        'delivery_status': 3,
        'controller': 'example//2/',
        'target': 'example//2/',
    }

    modified_token = {
        'token': 'modified_char',
        'evaluateresult': 'example//1/',
        'delivery_status': 0,
        'controller': 'example//1/',
        'target': 'example//1/',
    }
    missing_token = {
        'evaluateresult': 'example//1/',
        'delivery_status': 0,
        'controller': 'example//1/',
        'target': 'example//1/',
    }

    modified_evaluateresult = {
        'token': 'standard_char',
        'evaluateresult': 'example//2/',
        'delivery_status': 0,
        'controller': 'example//1/',
        'target': 'example//1/',
    }
    missing_evaluateresult = {
        'token': 'standard_char',
        'delivery_status': 0,
        'controller': 'example//1/',
        'target': 'example//1/',
    }

    modified_delivery_status = {
        'token': 'standard_char',
        'evaluateresult': 'example//1/',
        'delivery_status': 3,
        'controller': 'example//1/',
        'target': 'example//1/',
    }
    missing_delivery_status = {
        'token': 'standard_char',
        'evaluateresult': 'example//1/',
        'controller': 'example//1/',
        'target': 'example//1/',
    }

    modified_controller = {
        'token': 'standard_char',
        'evaluateresult': 'example//1/',
        'delivery_status': 0,
        'controller': 'example//2/',
        'target': 'example//1/',
    }
    missing_controller = {
        'token': 'standard_char',
        'evaluateresult': 'example//1/',
        'delivery_status': 0,
        'target': 'example//1/',
    }

    modified_target = {
        'token': 'standard_char',
        'evaluateresult': 'example//1/',
        'delivery_status': 0,
        'controller': 'example//1/',
        'target': 'example//2/',
    }
    missing_target = {
        'token': 'standard_char',
        'evaluateresult': 'example//1/',
        'delivery_status': 0,
        'controller': 'example//1/',
    }



class EvaluateControllerTestData(AvaCoreTestData):
    """
    Test data for EvaluateController
    """

    @staticmethod
    def init_requirements(owner):
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

    # Store self information
    model = EvaluateController
    url = 'example/'

    standard = {
        'template': 'example//1/',
        'scheduled_type': 0,
        'status': 0,
        'expiry_time': 'default',
        'scheduled_time': 'default',
        'targets': 'default',
        'target_controller': 'example//1/',
        'description': 'standard_text',
        'expiry_type': 0,
        'name': 'standard_char',
        'sender': 'example//1/',
    }

    unique = {
        'template': 'example//2/',
        'scheduled_type': 1,
        'status': 4,
        'expiry_time': 'default',
        'scheduled_time': 'default',
        'targets': 'default',
        'target_controller': 'example//2/',
        'description': 'unique_text',
        'expiry_type': 2,
        'name': 'unique_char',
        'sender': 'example//2/',
    }

    modified_template = {
        'template': 'example//2/',
        'scheduled_type': 0,
        'status': 0,
        'expiry_time': 'default',
        'scheduled_time': 'default',
        'targets': 'default',
        'target_controller': 'example//1/',
        'description': 'standard_text',
        'expiry_type': 0,
        'name': 'standard_char',
        'sender': 'example//1/',
    }
    missing_template = {
        'scheduled_type': 0,
        'status': 0,
        'expiry_time': 'default',
        'scheduled_time': 'default',
        'targets': 'default',
        'target_controller': 'example//1/',
        'description': 'standard_text',
        'expiry_type': 0,
        'name': 'standard_char',
        'sender': 'example//1/',
    }

    modified_scheduled_type = {
        'template': 'example//1/',
        'scheduled_type': 1,
        'status': 0,
        'expiry_time': 'default',
        'scheduled_time': 'default',
        'targets': 'default',
        'target_controller': 'example//1/',
        'description': 'standard_text',
        'expiry_type': 0,
        'name': 'standard_char',
        'sender': 'example//1/',
    }
    missing_scheduled_type = {
        'template': 'example//1/',
        'status': 0,
        'expiry_time': 'default',
        'scheduled_time': 'default',
        'targets': 'default',
        'target_controller': 'example//1/',
        'description': 'standard_text',
        'expiry_type': 0,
        'name': 'standard_char',
        'sender': 'example//1/',
    }

    modified_status = {
        'template': 'example//1/',
        'scheduled_type': 0,
        'status': 4,
        'expiry_time': 'default',
        'scheduled_time': 'default',
        'targets': 'default',
        'target_controller': 'example//1/',
        'description': 'standard_text',
        'expiry_type': 0,
        'name': 'standard_char',
        'sender': 'example//1/',
    }
    missing_status = {
        'template': 'example//1/',
        'scheduled_type': 0,
        'expiry_time': 'default',
        'scheduled_time': 'default',
        'targets': 'default',
        'target_controller': 'example//1/',
        'description': 'standard_text',
        'expiry_type': 0,
        'name': 'standard_char',
        'sender': 'example//1/',
    }

    modified_expiry_time = {
        'template': 'example//1/',
        'scheduled_type': 0,
        'status': 0,
        'expiry_time': 'default',
        'scheduled_time': 'default',
        'targets': 'default',
        'target_controller': 'example//1/',
        'description': 'standard_text',
        'expiry_type': 0,
        'name': 'standard_char',
        'sender': 'example//1/',
    }
    missing_expiry_time = {
        'template': 'example//1/',
        'scheduled_type': 0,
        'status': 0,
        'scheduled_time': 'default',
        'targets': 'default',
        'target_controller': 'example//1/',
        'description': 'standard_text',
        'expiry_type': 0,
        'name': 'standard_char',
        'sender': 'example//1/',
    }

    missing_scheduled_time = {
        'template': 'example//1/',
        'scheduled_type': 0,
        'status': 0,
        'expiry_time': 'default',
        'targets': 'default',
        'target_controller': 'example//1/',
        'description': 'standard_text',
        'expiry_type': 0,
        'name': 'standard_char',
        'sender': 'example//1/',
    }
    modified_scheduled_time = {
        'template': 'example//1/',
        'scheduled_type': 0,
        'status': 0,
        'expiry_time': 'default',
        'scheduled_time': 'default',
        'targets': 'default',
        'target_controller': 'example//1/',
        'description': 'standard_text',
        'expiry_type': 0,
        'name': 'standard_char',
        'sender': 'example//1/',
    }

    missing_targets = {
        'template': 'example//1/',
        'scheduled_type': 0,
        'status': 0,
        'expiry_time': 'default',
        'scheduled_time': 'default',
        'target_controller': 'example//1/',
        'description': 'standard_text',
        'expiry_type': 0,
        'name': 'standard_char',
        'sender': 'example//1/',
    }
    modified_targets = {
        'template': 'example//1/',
        'scheduled_type': 0,
        'status': 0,
        'expiry_time': 'default',
        'scheduled_time': 'default',
        'targets': 'default',
        'target_controller': 'example//1/',
        'description': 'standard_text',
        'expiry_type': 0,
        'name': 'standard_char',
        'sender': 'example//1/',
    }

    missing_target_controller = {
        'template': 'example//1/',
        'scheduled_type': 0,
        'status': 0,
        'expiry_time': 'default',
        'scheduled_time': 'default',
        'targets': 'default',
        'description': 'standard_text',
        'expiry_type': 0,
        'name': 'standard_char',
        'sender': 'example//1/',
    }
    modified_target_controller = {
        'template': 'example//1/',
        'scheduled_type': 0,
        'status': 0,
        'expiry_time': 'default',
        'scheduled_time': 'default',
        'targets': 'default',
        'target_controller': 'example//2/',
        'description': 'standard_text',
        'expiry_type': 0,
        'name': 'standard_char',
        'sender': 'example//1/',
    }

    missing_description = {
        'template': 'example//1/',
        'scheduled_type': 0,
        'status': 0,
        'expiry_time': 'default',
        'scheduled_time': 'default',
        'targets': 'default',
        'target_controller': 'example//1/',
        'expiry_type': 0,
        'name': 'standard_char',
        'sender': 'example//1/',
    }
    modified_description = {
        'template': 'example//1/',
        'scheduled_type': 0,
        'status': 0,
        'expiry_time': 'default',
        'scheduled_time': 'default',
        'targets': 'default',
        'target_controller': 'example//1/',
        'description': 'modified_text',
        'expiry_type': 0,
        'name': 'standard_char',
        'sender': 'example//1/',
    }

    modified_expiry_type = {
        'template': 'example//1/',
        'scheduled_type': 0,
        'status': 0,
        'expiry_time': 'default',
        'scheduled_time': 'default',
        'targets': 'default',
        'target_controller': 'example//1/',
        'description': 'standard_text',
        'expiry_type': 2,
        'name': 'standard_char',
        'sender': 'example//1/',
    }
    missing_expiry_type = {
        'template': 'example//1/',
        'scheduled_type': 0,
        'status': 0,
        'expiry_time': 'default',
        'scheduled_time': 'default',
        'targets': 'default',
        'target_controller': 'example//1/',
        'description': 'standard_text',
        'name': 'standard_char',
        'sender': 'example//1/',
    }

    modified_name = {
        'template': 'example//1/',
        'scheduled_type': 0,
        'status': 0,
        'expiry_time': 'default',
        'scheduled_time': 'default',
        'targets': 'default',
        'target_controller': 'example//1/',
        'description': 'standard_text',
        'expiry_type': 0,
        'name': 'modified_char',
        'sender': 'example//1/',
    }
    missing_name = {
        'template': 'example//1/',
        'scheduled_type': 0,
        'status': 0,
        'expiry_time': 'default',
        'scheduled_time': 'default',
        'targets': 'default',
        'target_controller': 'example//1/',
        'description': 'standard_text',
        'expiry_type': 0,
        'sender': 'example//1/',
    }

    modified_sender = {
        'template': 'example//1/',
        'scheduled_type': 0,
        'status': 0,
        'expiry_time': 'default',
        'scheduled_time': 'default',
        'targets': 'default',
        'target_controller': 'example//1/',
        'description': 'standard_text',
        'expiry_type': 0,
        'name': 'standard_char',
        'sender': 'example//2/',
    }
    missing_sender = {
        'template': 'example//1/',
        'scheduled_type': 0,
        'status': 0,
        'expiry_time': 'default',
        'scheduled_time': 'default',
        'targets': 'default',
        'target_controller': 'example//1/',
        'description': 'standard_text',
        'expiry_type': 0,
        'name': 'standard_char',
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
        'evaluatecontroller': 'example//1/',
        'hidden': True,
        'email_subject': 'standard_char',
        'email_body': 'standard_text',
        'template_type': 0,
        'description': 'standard_text',
        'name': 'standard_char',
    }

    unique = {
        'evaluatecontroller': 'example//2/',
        'hidden': False,
        'email_subject': 'unique_char',
        'email_body': 'unique_text',
        'template_type': 1,
        'description': 'unique_text',
        'name': 'unique_char',
    }

    missing_evaluatecontroller = {
        'hidden': True,
        'email_subject': 'standard_char',
        'email_body': 'standard_text',
        'template_type': 0,
        'description': 'standard_text',
        'name': 'standard_char',
    }
    modified_evaluatecontroller = {
        'evaluatecontroller': 'example//2/',
        'hidden': True,
        'email_subject': 'standard_char',
        'email_body': 'standard_text',
        'template_type': 0,
        'description': 'standard_text',
        'name': 'standard_char',
    }

    missing_hidden = {
        'evaluatecontroller': 'example//1/',
        'email_subject': 'standard_char',
        'email_body': 'standard_text',
        'template_type': 0,
        'description': 'standard_text',
        'name': 'standard_char',
    }
    modified_hidden = {
        'evaluatecontroller': 'example//1/',
        'hidden': False,
        'email_subject': 'standard_char',
        'email_body': 'standard_text',
        'template_type': 0,
        'description': 'standard_text',
        'name': 'standard_char',
    }

    modified_email_subject = {
        'evaluatecontroller': 'example//1/',
        'hidden': True,
        'email_subject': 'modified_char',
        'email_body': 'standard_text',
        'template_type': 0,
        'description': 'standard_text',
        'name': 'standard_char',
    }
    missing_email_subject = {
        'evaluatecontroller': 'example//1/',
        'hidden': True,
        'email_body': 'standard_text',
        'template_type': 0,
        'description': 'standard_text',
        'name': 'standard_char',
    }

    missing_email_body = {
        'evaluatecontroller': 'example//1/',
        'hidden': True,
        'email_subject': 'standard_char',
        'template_type': 0,
        'description': 'standard_text',
        'name': 'standard_char',
    }
    modified_email_body = {
        'evaluatecontroller': 'example//1/',
        'hidden': True,
        'email_subject': 'standard_char',
        'email_body': 'modified_text',
        'template_type': 0,
        'description': 'standard_text',
        'name': 'standard_char',
    }

    missing_template_type = {
        'evaluatecontroller': 'example//1/',
        'hidden': True,
        'email_subject': 'standard_char',
        'email_body': 'standard_text',
        'description': 'standard_text',
        'name': 'standard_char',
    }
    modified_template_type = {
        'evaluatecontroller': 'example//1/',
        'hidden': True,
        'email_subject': 'standard_char',
        'email_body': 'standard_text',
        'template_type': 1,
        'description': 'standard_text',
        'name': 'standard_char',
    }

    missing_description = {
        'evaluatecontroller': 'example//1/',
        'hidden': True,
        'email_subject': 'standard_char',
        'email_body': 'standard_text',
        'template_type': 0,
        'name': 'standard_char',
    }
    modified_description = {
        'evaluatecontroller': 'example//1/',
        'hidden': True,
        'email_subject': 'standard_char',
        'email_body': 'standard_text',
        'template_type': 0,
        'description': 'modified_text',
        'name': 'standard_char',
    }

    modified_name = {
        'evaluatecontroller': 'example//1/',
        'hidden': True,
        'email_subject': 'standard_char',
        'email_body': 'standard_text',
        'template_type': 0,
        'description': 'standard_text',
        'name': 'modified_char',
    }
    missing_name = {
        'evaluatecontroller': 'example//1/',
        'hidden': True,
        'email_subject': 'standard_char',
        'email_body': 'standard_text',
        'template_type': 0,
        'description': 'standard_text',
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

    modified_result = {
        'result': 1,
        'target_profile': 'example//1/',
    }
    missing_result = {
        'target_profile': 'example//1/',
    }

    modified_target_profile = {
        'result': 0,
        'target_profile': 'example//2/',
    }
    missing_target_profile = {
        'result': 0,
    }




