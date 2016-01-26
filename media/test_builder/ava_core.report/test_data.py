# Rest Imports
# Local Imports
from ava_core.abstract.test_data import AvaTestData
from ava_core.report.models import Suspicious, ReportResponse, Question


# Implementation
class SuspiciousTestData(AvaTestData):
    """
    Test data for Suspicious
    """

    model = Suspicious
    url = '/example'

    standard = {
        'url': 'standard_char',
        'incident_date': 'default',
        'question_ptr': 'default',
    }

    modified = {
        'url': 'standard_char',
        'incident_date': 'default',
        'question_ptr': 'default',
    }

    missing_url = {
        'incident_date': 'default',
        'question_ptr': 'default',
    }

    modified_url = {
        'url': 'modified_char',
        'incident_date': 'default',
        'question_ptr': 'default',
    }

    modified_incident_date = {
        'url': 'standard_char',
        'incident_date': 'default',
        'question_ptr': 'default',
    }

    missing_incident_date = {
        'url': 'standard_char',
        'question_ptr': 'default',
    }

    modified_question_ptr = {
        'url': 'standard_char',
        'incident_date': 'default',
        'question_ptr': 'default',
    }

    missing_question_ptr = {
        'url': 'standard_char',
        'incident_date': 'default',
    }



class ReportResponseTestData(AvaTestData):
    """
    Test data for ReportResponse
    """

    model = ReportResponse
    url = '/example'

    standard = {
        'question': 'REQUIRES: ava_core.report.models.Question',
        'message': 'standard_text',
        'reportresponse': 'REQUIRES: ava_core.report.models.ReportResponse',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'parent_response': 'REQUIRES: ava_core.report.models.ReportResponse',
    }

    modified = {
        'question': 'REQUIRES: ava_core.report.models.Question',
        'message': 'standard_text',
        'reportresponse': 'REQUIRES: ava_core.report.models.ReportResponse',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'parent_response': 'REQUIRES: ava_core.report.models.ReportResponse',
    }

    modified_question = {
        'question': 'REQUIRES: ava_core.report.models.Question',
        'message': 'standard_text',
        'reportresponse': 'REQUIRES: ava_core.report.models.ReportResponse',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'parent_response': 'REQUIRES: ava_core.report.models.ReportResponse',
    }

    missing_question = {
        'message': 'standard_text',
        'reportresponse': 'REQUIRES: ava_core.report.models.ReportResponse',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'parent_response': 'REQUIRES: ava_core.report.models.ReportResponse',
    }

    modified_message = {
        'question': 'REQUIRES: ava_core.report.models.Question',
        'message': 'modified_text',
        'reportresponse': 'REQUIRES: ava_core.report.models.ReportResponse',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'parent_response': 'REQUIRES: ava_core.report.models.ReportResponse',
    }

    missing_message = {
        'question': 'REQUIRES: ava_core.report.models.Question',
        'reportresponse': 'REQUIRES: ava_core.report.models.ReportResponse',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'parent_response': 'REQUIRES: ava_core.report.models.ReportResponse',
    }

    missing_reportresponse = {
        'question': 'REQUIRES: ava_core.report.models.Question',
        'message': 'standard_text',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'parent_response': 'REQUIRES: ava_core.report.models.ReportResponse',
    }

    modified_reportresponse = {
        'question': 'REQUIRES: ava_core.report.models.Question',
        'message': 'standard_text',
        'reportresponse': 'REQUIRES: ava_core.report.models.ReportResponse',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'parent_response': 'REQUIRES: ava_core.report.models.ReportResponse',
    }

    missing_owner = {
        'question': 'REQUIRES: ava_core.report.models.Question',
        'message': 'standard_text',
        'reportresponse': 'REQUIRES: ava_core.report.models.ReportResponse',
        'parent_response': 'REQUIRES: ava_core.report.models.ReportResponse',
    }

    modified_owner = {
        'question': 'REQUIRES: ava_core.report.models.Question',
        'message': 'standard_text',
        'reportresponse': 'REQUIRES: ava_core.report.models.ReportResponse',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'parent_response': 'REQUIRES: ava_core.report.models.ReportResponse',
    }

    missing_parent_response = {
        'question': 'REQUIRES: ava_core.report.models.Question',
        'message': 'standard_text',
        'reportresponse': 'REQUIRES: ava_core.report.models.ReportResponse',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
    }

    modified_parent_response = {
        'question': 'REQUIRES: ava_core.report.models.Question',
        'message': 'standard_text',
        'reportresponse': 'REQUIRES: ava_core.report.models.ReportResponse',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'parent_response': 'REQUIRES: ava_core.report.models.ReportResponse',
    }



class QuestionTestData(AvaTestData):
    """
    Test data for Question
    """

    model = Question
    url = '/example'

    standard = {
        'is_resolved': True,
        'status_type': 0,
        'description': 'standard_text',
        'suspicious': 'default',
        'question_responses': 'REQUIRES: ava_core.report.models.ReportResponse',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'priority_type': 0,
    }

    modified = {
        'is_resolved': True,
        'status_type': 0,
        'description': 'standard_text',
        'suspicious': 'default',
        'question_responses': 'REQUIRES: ava_core.report.models.ReportResponse',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'priority_type': 0,
    }

    modified_is_resolved = {
        'is_resolved': False,
        'status_type': 0,
        'description': 'standard_text',
        'suspicious': 'default',
        'question_responses': 'REQUIRES: ava_core.report.models.ReportResponse',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'priority_type': 0,
    }

    missing_is_resolved = {
        'status_type': 0,
        'description': 'standard_text',
        'suspicious': 'default',
        'question_responses': 'REQUIRES: ava_core.report.models.ReportResponse',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'priority_type': 0,
    }

    missing_status_type = {
        'is_resolved': True,
        'description': 'standard_text',
        'suspicious': 'default',
        'question_responses': 'REQUIRES: ava_core.report.models.ReportResponse',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'priority_type': 0,
    }

    modified_status_type = {
        'is_resolved': True,
        'status_type': 4,
        'description': 'standard_text',
        'suspicious': 'default',
        'question_responses': 'REQUIRES: ava_core.report.models.ReportResponse',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'priority_type': 0,
    }

    modified_description = {
        'is_resolved': True,
        'status_type': 0,
        'description': 'modified_text',
        'suspicious': 'default',
        'question_responses': 'REQUIRES: ava_core.report.models.ReportResponse',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'priority_type': 0,
    }

    missing_description = {
        'is_resolved': True,
        'status_type': 0,
        'suspicious': 'default',
        'question_responses': 'REQUIRES: ava_core.report.models.ReportResponse',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'priority_type': 0,
    }

    missing_suspicious = {
        'is_resolved': True,
        'status_type': 0,
        'description': 'standard_text',
        'question_responses': 'REQUIRES: ava_core.report.models.ReportResponse',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'priority_type': 0,
    }

    modified_suspicious = {
        'is_resolved': True,
        'status_type': 0,
        'description': 'standard_text',
        'suspicious': 'default',
        'question_responses': 'REQUIRES: ava_core.report.models.ReportResponse',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'priority_type': 0,
    }

    modified_question_responses = {
        'is_resolved': True,
        'status_type': 0,
        'description': 'standard_text',
        'suspicious': 'default',
        'question_responses': 'REQUIRES: ava_core.report.models.ReportResponse',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'priority_type': 0,
    }

    missing_question_responses = {
        'is_resolved': True,
        'status_type': 0,
        'description': 'standard_text',
        'suspicious': 'default',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'priority_type': 0,
    }

    missing_owner = {
        'is_resolved': True,
        'status_type': 0,
        'description': 'standard_text',
        'suspicious': 'default',
        'question_responses': 'REQUIRES: ava_core.report.models.ReportResponse',
        'priority_type': 0,
    }

    modified_owner = {
        'is_resolved': True,
        'status_type': 0,
        'description': 'standard_text',
        'suspicious': 'default',
        'question_responses': 'REQUIRES: ava_core.report.models.ReportResponse',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'priority_type': 0,
    }

    missing_priority_type = {
        'is_resolved': True,
        'status_type': 0,
        'description': 'standard_text',
        'suspicious': 'default',
        'question_responses': 'REQUIRES: ava_core.report.models.ReportResponse',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
    }

    modified_priority_type = {
        'is_resolved': True,
        'status_type': 0,
        'description': 'standard_text',
        'suspicious': 'default',
        'question_responses': 'REQUIRES: ava_core.report.models.ReportResponse',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'priority_type': 3,
    }




