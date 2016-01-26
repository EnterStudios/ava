# Rest Imports
# Local Imports
from ava_core.abstract.test_data import AvaTestData
from ava_core.evaluate.models import EvaluateSender, EvaluateTemplate, EvaluateResult, EvaluateTest, EvaluateController


# Implementation
class EvaluateSenderTestData(AvaTestData):
    """
    Test data for EvaluateSender
    """

    model = EvaluateSender
    url = '/example'

    standard = {
        'last_name': 'standard_char',
        'evaluatecontroller': 'REQUIRES: ava_core.evaluate.models.EvaluateController',
        'slack_name': 'standard_char',
        'first_name': 'standard_char',
        'hidden': True,
        'email_address': 'standard_char',
    }

    modified = {
        'last_name': 'standard_char',
        'evaluatecontroller': 'REQUIRES: ava_core.evaluate.models.EvaluateController',
        'slack_name': 'standard_char',
        'first_name': 'standard_char',
        'hidden': True,
        'email_address': 'standard_char',
    }

    modified_last_name = {
        'last_name': 'modified_char',
        'evaluatecontroller': 'REQUIRES: ava_core.evaluate.models.EvaluateController',
        'slack_name': 'standard_char',
        'first_name': 'standard_char',
        'hidden': True,
        'email_address': 'standard_char',
    }

    missing_last_name = {
        'evaluatecontroller': 'REQUIRES: ava_core.evaluate.models.EvaluateController',
        'slack_name': 'standard_char',
        'first_name': 'standard_char',
        'hidden': True,
        'email_address': 'standard_char',
    }

    missing_evaluatecontroller = {
        'last_name': 'standard_char',
        'slack_name': 'standard_char',
        'first_name': 'standard_char',
        'hidden': True,
        'email_address': 'standard_char',
    }

    modified_evaluatecontroller = {
        'last_name': 'standard_char',
        'evaluatecontroller': 'REQUIRES: ava_core.evaluate.models.EvaluateController',
        'slack_name': 'standard_char',
        'first_name': 'standard_char',
        'hidden': True,
        'email_address': 'standard_char',
    }

    modified_slack_name = {
        'last_name': 'standard_char',
        'evaluatecontroller': 'REQUIRES: ava_core.evaluate.models.EvaluateController',
        'slack_name': 'modified_char',
        'first_name': 'standard_char',
        'hidden': True,
        'email_address': 'standard_char',
    }

    missing_slack_name = {
        'last_name': 'standard_char',
        'evaluatecontroller': 'REQUIRES: ava_core.evaluate.models.EvaluateController',
        'first_name': 'standard_char',
        'hidden': True,
        'email_address': 'standard_char',
    }

    modified_first_name = {
        'last_name': 'standard_char',
        'evaluatecontroller': 'REQUIRES: ava_core.evaluate.models.EvaluateController',
        'slack_name': 'standard_char',
        'first_name': 'modified_char',
        'hidden': True,
        'email_address': 'standard_char',
    }

    missing_first_name = {
        'last_name': 'standard_char',
        'evaluatecontroller': 'REQUIRES: ava_core.evaluate.models.EvaluateController',
        'slack_name': 'standard_char',
        'hidden': True,
        'email_address': 'standard_char',
    }

    modified_hidden = {
        'last_name': 'standard_char',
        'evaluatecontroller': 'REQUIRES: ava_core.evaluate.models.EvaluateController',
        'slack_name': 'standard_char',
        'first_name': 'standard_char',
        'hidden': False,
        'email_address': 'standard_char',
    }

    missing_hidden = {
        'last_name': 'standard_char',
        'evaluatecontroller': 'REQUIRES: ava_core.evaluate.models.EvaluateController',
        'slack_name': 'standard_char',
        'first_name': 'standard_char',
        'email_address': 'standard_char',
    }

    modified_email_address = {
        'last_name': 'standard_char',
        'evaluatecontroller': 'REQUIRES: ava_core.evaluate.models.EvaluateController',
        'slack_name': 'standard_char',
        'first_name': 'standard_char',
        'hidden': True,
        'email_address': 'modified_char',
    }

    missing_email_address = {
        'last_name': 'standard_char',
        'evaluatecontroller': 'REQUIRES: ava_core.evaluate.models.EvaluateController',
        'slack_name': 'standard_char',
        'first_name': 'standard_char',
        'hidden': True,
    }



class EvaluateTemplateTestData(AvaTestData):
    """
    Test data for EvaluateTemplate
    """

    model = EvaluateTemplate
    url = '/example'

    standard = {
        'email_body': 'standard_text',
        'evaluatecontroller': 'REQUIRES: ava_core.evaluate.models.EvaluateController',
        'name': 'standard_char',
        'description': 'standard_text',
        'email_subject': 'standard_char',
        'hidden': True,
        'template_type': 0,
    }

    modified = {
        'email_body': 'standard_text',
        'evaluatecontroller': 'REQUIRES: ava_core.evaluate.models.EvaluateController',
        'name': 'standard_char',
        'description': 'standard_text',
        'email_subject': 'standard_char',
        'hidden': True,
        'template_type': 0,
    }

    missing_email_body = {
        'evaluatecontroller': 'REQUIRES: ava_core.evaluate.models.EvaluateController',
        'name': 'standard_char',
        'description': 'standard_text',
        'email_subject': 'standard_char',
        'hidden': True,
        'template_type': 0,
    }

    modified_email_body = {
        'email_body': 'modified_text',
        'evaluatecontroller': 'REQUIRES: ava_core.evaluate.models.EvaluateController',
        'name': 'standard_char',
        'description': 'standard_text',
        'email_subject': 'standard_char',
        'hidden': True,
        'template_type': 0,
    }

    missing_evaluatecontroller = {
        'email_body': 'standard_text',
        'name': 'standard_char',
        'description': 'standard_text',
        'email_subject': 'standard_char',
        'hidden': True,
        'template_type': 0,
    }

    modified_evaluatecontroller = {
        'email_body': 'standard_text',
        'evaluatecontroller': 'REQUIRES: ava_core.evaluate.models.EvaluateController',
        'name': 'standard_char',
        'description': 'standard_text',
        'email_subject': 'standard_char',
        'hidden': True,
        'template_type': 0,
    }

    modified_name = {
        'email_body': 'standard_text',
        'evaluatecontroller': 'REQUIRES: ava_core.evaluate.models.EvaluateController',
        'name': 'modified_char',
        'description': 'standard_text',
        'email_subject': 'standard_char',
        'hidden': True,
        'template_type': 0,
    }

    missing_name = {
        'email_body': 'standard_text',
        'evaluatecontroller': 'REQUIRES: ava_core.evaluate.models.EvaluateController',
        'description': 'standard_text',
        'email_subject': 'standard_char',
        'hidden': True,
        'template_type': 0,
    }

    modified_description = {
        'email_body': 'standard_text',
        'evaluatecontroller': 'REQUIRES: ava_core.evaluate.models.EvaluateController',
        'name': 'standard_char',
        'description': 'modified_text',
        'email_subject': 'standard_char',
        'hidden': True,
        'template_type': 0,
    }

    missing_description = {
        'email_body': 'standard_text',
        'evaluatecontroller': 'REQUIRES: ava_core.evaluate.models.EvaluateController',
        'name': 'standard_char',
        'email_subject': 'standard_char',
        'hidden': True,
        'template_type': 0,
    }

    modified_email_subject = {
        'email_body': 'standard_text',
        'evaluatecontroller': 'REQUIRES: ava_core.evaluate.models.EvaluateController',
        'name': 'standard_char',
        'description': 'standard_text',
        'email_subject': 'modified_char',
        'hidden': True,
        'template_type': 0,
    }

    missing_email_subject = {
        'email_body': 'standard_text',
        'evaluatecontroller': 'REQUIRES: ava_core.evaluate.models.EvaluateController',
        'name': 'standard_char',
        'description': 'standard_text',
        'hidden': True,
        'template_type': 0,
    }

    modified_hidden = {
        'email_body': 'standard_text',
        'evaluatecontroller': 'REQUIRES: ava_core.evaluate.models.EvaluateController',
        'name': 'standard_char',
        'description': 'standard_text',
        'email_subject': 'standard_char',
        'hidden': False,
        'template_type': 0,
    }

    missing_hidden = {
        'email_body': 'standard_text',
        'evaluatecontroller': 'REQUIRES: ava_core.evaluate.models.EvaluateController',
        'name': 'standard_char',
        'description': 'standard_text',
        'email_subject': 'standard_char',
        'template_type': 0,
    }

    missing_template_type = {
        'email_body': 'standard_text',
        'evaluatecontroller': 'REQUIRES: ava_core.evaluate.models.EvaluateController',
        'name': 'standard_char',
        'description': 'standard_text',
        'email_subject': 'standard_char',
        'hidden': True,
    }

    modified_template_type = {
        'email_body': 'standard_text',
        'evaluatecontroller': 'REQUIRES: ava_core.evaluate.models.EvaluateController',
        'name': 'standard_char',
        'description': 'standard_text',
        'email_subject': 'standard_char',
        'hidden': True,
        'template_type': 1,
    }



class EvaluateResultTestData(AvaTestData):
    """
    Test data for EvaluateResult
    """

    model = EvaluateResult
    url = '/example'

    standard = {
        'result': 0,
        'target_profile': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
    }

    modified = {
        'result': 0,
        'target_profile': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
    }

    modified_result = {
        'result': 1,
        'target_profile': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
    }

    missing_result = {
        'target_profile': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
    }

    modified_target_profile = {
        'result': 0,
        'target_profile': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
    }

    missing_target_profile = {
        'result': 0,
    }



class EvaluateTestTestData(AvaTestData):
    """
    Test data for EvaluateTest
    """

    model = EvaluateTest
    url = '/example'

    standard = {
        'controller': 'REQUIRES: ava_core.evaluate.models.EvaluateController',
        'token': 'standard_char',
        'evaluateresult': 'REQUIRES: ava_core.evaluate.models.EvaluateResult',
        'delivery_status': 0,
        'target': 'REQUIRES: ava_core.organize.models.Person',
    }

    modified = {
        'controller': 'REQUIRES: ava_core.evaluate.models.EvaluateController',
        'token': 'standard_char',
        'evaluateresult': 'REQUIRES: ava_core.evaluate.models.EvaluateResult',
        'delivery_status': 0,
        'target': 'REQUIRES: ava_core.organize.models.Person',
    }

    modified_controller = {
        'controller': 'REQUIRES: ava_core.evaluate.models.EvaluateController',
        'token': 'standard_char',
        'evaluateresult': 'REQUIRES: ava_core.evaluate.models.EvaluateResult',
        'delivery_status': 0,
        'target': 'REQUIRES: ava_core.organize.models.Person',
    }

    missing_controller = {
        'token': 'standard_char',
        'evaluateresult': 'REQUIRES: ava_core.evaluate.models.EvaluateResult',
        'delivery_status': 0,
        'target': 'REQUIRES: ava_core.organize.models.Person',
    }

    missing_token = {
        'controller': 'REQUIRES: ava_core.evaluate.models.EvaluateController',
        'evaluateresult': 'REQUIRES: ava_core.evaluate.models.EvaluateResult',
        'delivery_status': 0,
        'target': 'REQUIRES: ava_core.organize.models.Person',
    }

    modified_token = {
        'controller': 'REQUIRES: ava_core.evaluate.models.EvaluateController',
        'token': 'modified_char',
        'evaluateresult': 'REQUIRES: ava_core.evaluate.models.EvaluateResult',
        'delivery_status': 0,
        'target': 'REQUIRES: ava_core.organize.models.Person',
    }

    modified_evaluateresult = {
        'controller': 'REQUIRES: ava_core.evaluate.models.EvaluateController',
        'token': 'standard_char',
        'evaluateresult': 'REQUIRES: ava_core.evaluate.models.EvaluateResult',
        'delivery_status': 0,
        'target': 'REQUIRES: ava_core.organize.models.Person',
    }

    missing_evaluateresult = {
        'controller': 'REQUIRES: ava_core.evaluate.models.EvaluateController',
        'token': 'standard_char',
        'delivery_status': 0,
        'target': 'REQUIRES: ava_core.organize.models.Person',
    }

    modified_delivery_status = {
        'controller': 'REQUIRES: ava_core.evaluate.models.EvaluateController',
        'token': 'standard_char',
        'evaluateresult': 'REQUIRES: ava_core.evaluate.models.EvaluateResult',
        'delivery_status': 3,
        'target': 'REQUIRES: ava_core.organize.models.Person',
    }

    missing_delivery_status = {
        'controller': 'REQUIRES: ava_core.evaluate.models.EvaluateController',
        'token': 'standard_char',
        'evaluateresult': 'REQUIRES: ava_core.evaluate.models.EvaluateResult',
        'target': 'REQUIRES: ava_core.organize.models.Person',
    }

    missing_target = {
        'controller': 'REQUIRES: ava_core.evaluate.models.EvaluateController',
        'token': 'standard_char',
        'evaluateresult': 'REQUIRES: ava_core.evaluate.models.EvaluateResult',
        'delivery_status': 0,
    }

    modified_target = {
        'controller': 'REQUIRES: ava_core.evaluate.models.EvaluateController',
        'token': 'standard_char',
        'evaluateresult': 'REQUIRES: ava_core.evaluate.models.EvaluateResult',
        'delivery_status': 0,
        'target': 'REQUIRES: ava_core.organize.models.Person',
    }



class EvaluateControllerTestData(AvaTestData):
    """
    Test data for EvaluateController
    """

    model = EvaluateController
    url = '/example'

    standard = {
        'targets': 'default',
        'scheduled_type': 0,
        'scheduled_time': 'default',
        'expiry_time': 'default',
        'name': 'standard_char',
        'target_controller': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
        'sender': 'REQUIRES: ava_core.evaluate.models.EvaluateSender',
        'expiry_type': 0,
        'description': 'standard_text',
        'status': 0,
        'template': 'REQUIRES: ava_core.evaluate.models.EvaluateTemplate',
    }

    modified = {
        'targets': 'default',
        'scheduled_type': 0,
        'scheduled_time': 'default',
        'expiry_time': 'default',
        'name': 'standard_char',
        'target_controller': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
        'sender': 'REQUIRES: ava_core.evaluate.models.EvaluateSender',
        'expiry_type': 0,
        'description': 'standard_text',
        'status': 0,
        'template': 'REQUIRES: ava_core.evaluate.models.EvaluateTemplate',
    }

    modified_targets = {
        'targets': 'default',
        'scheduled_type': 0,
        'scheduled_time': 'default',
        'expiry_time': 'default',
        'name': 'standard_char',
        'target_controller': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
        'sender': 'REQUIRES: ava_core.evaluate.models.EvaluateSender',
        'expiry_type': 0,
        'description': 'standard_text',
        'status': 0,
        'template': 'REQUIRES: ava_core.evaluate.models.EvaluateTemplate',
    }

    missing_targets = {
        'scheduled_type': 0,
        'scheduled_time': 'default',
        'expiry_time': 'default',
        'name': 'standard_char',
        'target_controller': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
        'sender': 'REQUIRES: ava_core.evaluate.models.EvaluateSender',
        'expiry_type': 0,
        'description': 'standard_text',
        'status': 0,
        'template': 'REQUIRES: ava_core.evaluate.models.EvaluateTemplate',
    }

    modified_scheduled_type = {
        'targets': 'default',
        'scheduled_type': 1,
        'scheduled_time': 'default',
        'expiry_time': 'default',
        'name': 'standard_char',
        'target_controller': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
        'sender': 'REQUIRES: ava_core.evaluate.models.EvaluateSender',
        'expiry_type': 0,
        'description': 'standard_text',
        'status': 0,
        'template': 'REQUIRES: ava_core.evaluate.models.EvaluateTemplate',
    }

    missing_scheduled_type = {
        'targets': 'default',
        'scheduled_time': 'default',
        'expiry_time': 'default',
        'name': 'standard_char',
        'target_controller': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
        'sender': 'REQUIRES: ava_core.evaluate.models.EvaluateSender',
        'expiry_type': 0,
        'description': 'standard_text',
        'status': 0,
        'template': 'REQUIRES: ava_core.evaluate.models.EvaluateTemplate',
    }

    missing_scheduled_time = {
        'targets': 'default',
        'scheduled_type': 0,
        'expiry_time': 'default',
        'name': 'standard_char',
        'target_controller': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
        'sender': 'REQUIRES: ava_core.evaluate.models.EvaluateSender',
        'expiry_type': 0,
        'description': 'standard_text',
        'status': 0,
        'template': 'REQUIRES: ava_core.evaluate.models.EvaluateTemplate',
    }

    modified_scheduled_time = {
        'targets': 'default',
        'scheduled_type': 0,
        'scheduled_time': 'default',
        'expiry_time': 'default',
        'name': 'standard_char',
        'target_controller': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
        'sender': 'REQUIRES: ava_core.evaluate.models.EvaluateSender',
        'expiry_type': 0,
        'description': 'standard_text',
        'status': 0,
        'template': 'REQUIRES: ava_core.evaluate.models.EvaluateTemplate',
    }

    missing_expiry_time = {
        'targets': 'default',
        'scheduled_type': 0,
        'scheduled_time': 'default',
        'name': 'standard_char',
        'target_controller': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
        'sender': 'REQUIRES: ava_core.evaluate.models.EvaluateSender',
        'expiry_type': 0,
        'description': 'standard_text',
        'status': 0,
        'template': 'REQUIRES: ava_core.evaluate.models.EvaluateTemplate',
    }

    modified_expiry_time = {
        'targets': 'default',
        'scheduled_type': 0,
        'scheduled_time': 'default',
        'expiry_time': 'default',
        'name': 'standard_char',
        'target_controller': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
        'sender': 'REQUIRES: ava_core.evaluate.models.EvaluateSender',
        'expiry_type': 0,
        'description': 'standard_text',
        'status': 0,
        'template': 'REQUIRES: ava_core.evaluate.models.EvaluateTemplate',
    }

    modified_name = {
        'targets': 'default',
        'scheduled_type': 0,
        'scheduled_time': 'default',
        'expiry_time': 'default',
        'name': 'modified_char',
        'target_controller': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
        'sender': 'REQUIRES: ava_core.evaluate.models.EvaluateSender',
        'expiry_type': 0,
        'description': 'standard_text',
        'status': 0,
        'template': 'REQUIRES: ava_core.evaluate.models.EvaluateTemplate',
    }

    missing_name = {
        'targets': 'default',
        'scheduled_type': 0,
        'scheduled_time': 'default',
        'expiry_time': 'default',
        'target_controller': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
        'sender': 'REQUIRES: ava_core.evaluate.models.EvaluateSender',
        'expiry_type': 0,
        'description': 'standard_text',
        'status': 0,
        'template': 'REQUIRES: ava_core.evaluate.models.EvaluateTemplate',
    }

    missing_target_controller = {
        'targets': 'default',
        'scheduled_type': 0,
        'scheduled_time': 'default',
        'expiry_time': 'default',
        'name': 'standard_char',
        'sender': 'REQUIRES: ava_core.evaluate.models.EvaluateSender',
        'expiry_type': 0,
        'description': 'standard_text',
        'status': 0,
        'template': 'REQUIRES: ava_core.evaluate.models.EvaluateTemplate',
    }

    modified_target_controller = {
        'targets': 'default',
        'scheduled_type': 0,
        'scheduled_time': 'default',
        'expiry_time': 'default',
        'name': 'standard_char',
        'target_controller': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
        'sender': 'REQUIRES: ava_core.evaluate.models.EvaluateSender',
        'expiry_type': 0,
        'description': 'standard_text',
        'status': 0,
        'template': 'REQUIRES: ava_core.evaluate.models.EvaluateTemplate',
    }

    missing_sender = {
        'targets': 'default',
        'scheduled_type': 0,
        'scheduled_time': 'default',
        'expiry_time': 'default',
        'name': 'standard_char',
        'target_controller': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
        'expiry_type': 0,
        'description': 'standard_text',
        'status': 0,
        'template': 'REQUIRES: ava_core.evaluate.models.EvaluateTemplate',
    }

    modified_sender = {
        'targets': 'default',
        'scheduled_type': 0,
        'scheduled_time': 'default',
        'expiry_time': 'default',
        'name': 'standard_char',
        'target_controller': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
        'sender': 'REQUIRES: ava_core.evaluate.models.EvaluateSender',
        'expiry_type': 0,
        'description': 'standard_text',
        'status': 0,
        'template': 'REQUIRES: ava_core.evaluate.models.EvaluateTemplate',
    }

    missing_expiry_type = {
        'targets': 'default',
        'scheduled_type': 0,
        'scheduled_time': 'default',
        'expiry_time': 'default',
        'name': 'standard_char',
        'target_controller': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
        'sender': 'REQUIRES: ava_core.evaluate.models.EvaluateSender',
        'description': 'standard_text',
        'status': 0,
        'template': 'REQUIRES: ava_core.evaluate.models.EvaluateTemplate',
    }

    modified_expiry_type = {
        'targets': 'default',
        'scheduled_type': 0,
        'scheduled_time': 'default',
        'expiry_time': 'default',
        'name': 'standard_char',
        'target_controller': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
        'sender': 'REQUIRES: ava_core.evaluate.models.EvaluateSender',
        'expiry_type': 2,
        'description': 'standard_text',
        'status': 0,
        'template': 'REQUIRES: ava_core.evaluate.models.EvaluateTemplate',
    }

    modified_description = {
        'targets': 'default',
        'scheduled_type': 0,
        'scheduled_time': 'default',
        'expiry_time': 'default',
        'name': 'standard_char',
        'target_controller': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
        'sender': 'REQUIRES: ava_core.evaluate.models.EvaluateSender',
        'expiry_type': 0,
        'description': 'modified_text',
        'status': 0,
        'template': 'REQUIRES: ava_core.evaluate.models.EvaluateTemplate',
    }

    missing_description = {
        'targets': 'default',
        'scheduled_type': 0,
        'scheduled_time': 'default',
        'expiry_time': 'default',
        'name': 'standard_char',
        'target_controller': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
        'sender': 'REQUIRES: ava_core.evaluate.models.EvaluateSender',
        'expiry_type': 0,
        'status': 0,
        'template': 'REQUIRES: ava_core.evaluate.models.EvaluateTemplate',
    }

    missing_status = {
        'targets': 'default',
        'scheduled_type': 0,
        'scheduled_time': 'default',
        'expiry_time': 'default',
        'name': 'standard_char',
        'target_controller': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
        'sender': 'REQUIRES: ava_core.evaluate.models.EvaluateSender',
        'expiry_type': 0,
        'description': 'standard_text',
        'template': 'REQUIRES: ava_core.evaluate.models.EvaluateTemplate',
    }

    modified_status = {
        'targets': 'default',
        'scheduled_type': 0,
        'scheduled_time': 'default',
        'expiry_time': 'default',
        'name': 'standard_char',
        'target_controller': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
        'sender': 'REQUIRES: ava_core.evaluate.models.EvaluateSender',
        'expiry_type': 0,
        'description': 'standard_text',
        'status': 4,
        'template': 'REQUIRES: ava_core.evaluate.models.EvaluateTemplate',
    }

    modified_template = {
        'targets': 'default',
        'scheduled_type': 0,
        'scheduled_time': 'default',
        'expiry_time': 'default',
        'name': 'standard_char',
        'target_controller': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
        'sender': 'REQUIRES: ava_core.evaluate.models.EvaluateSender',
        'expiry_type': 0,
        'description': 'standard_text',
        'status': 0,
        'template': 'REQUIRES: ava_core.evaluate.models.EvaluateTemplate',
    }

    missing_template = {
        'targets': 'default',
        'scheduled_type': 0,
        'scheduled_time': 'default',
        'expiry_time': 'default',
        'name': 'standard_char',
        'target_controller': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
        'sender': 'REQUIRES: ava_core.evaluate.models.EvaluateSender',
        'expiry_type': 0,
        'description': 'standard_text',
        'status': 0,
    }




