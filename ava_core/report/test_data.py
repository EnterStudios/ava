# Rest Imports
from rest_framework import status
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.report.models import ReportResponse, Suspicious, Question


# Implementation
class ReportResponseTestData(AvaCoreTestData):
    """
    Test data for ReportResponse
    """

    @staticmethod
    def init_requirements():
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if ReportResponse.objects.count() == 0:
            ReportResponseTestData.init_requirements()
            model = ReportResponse.objects.create(**ReportResponseTestData.get_data('standard'))
            model.save()
            model = ReportResponse.objects.create(**ReportResponseTestData.get_data('unique'))
            model.save()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if Question.objects.count() == 0:
            QuestionTestData.init_requirements()
            model = Question.objects.create(**QuestionTestData.get_data('standard'))
            model.save()
            model = Question.objects.create(**QuestionTestData.get_data('unique'))
            model.save()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if ReportResponse.objects.count() == 0:
            ReportResponseTestData.init_requirements()
            model = ReportResponse.objects.create(**ReportResponseTestData.get_data('standard'))
            model.save()
            model = ReportResponse.objects.create(**ReportResponseTestData.get_data('unique'))
            model.save()

    # Store self information
    model = ReportResponse
    url = '/example'

    standard = {
        'reportresponse': '/example/1/',
        'question': '/example/1/',
        'message': 'standard_text',
        'owner': '',
        'parent_response': '/example/1/',
    }

    unique = {
        'reportresponse': '/example/2/',
        'question': '/example/2/',
        'message': 'unique_text',
        'owner': '',
        'parent_response': '/example/2/',
    }

    modified_reportresponse = {
        'reportresponse': '/example/2/',
        'question': '/example/1/',
        'message': 'standard_text',
        'owner': '',
        'parent_response': '/example/1/',
    }
    missing_reportresponse = {
        'question': '/example/1/',
        'message': 'standard_text',
        'owner': '',
        'parent_response': '/example/1/',
    }

    modified_question = {
        'reportresponse': '/example/1/',
        'question': '/example/2/',
        'message': 'standard_text',
        'owner': '',
        'parent_response': '/example/1/',
    }
    missing_question = {
        'reportresponse': '/example/1/',
        'message': 'standard_text',
        'owner': '',
        'parent_response': '/example/1/',
    }

    missing_message = {
        'reportresponse': '/example/1/',
        'question': '/example/1/',
        'owner': '',
        'parent_response': '/example/1/',
    }
    modified_message = {
        'reportresponse': '/example/1/',
        'question': '/example/1/',
        'message': 'modified_text',
        'owner': '',
        'parent_response': '/example/1/',
    }

    modified_owner = {
        'reportresponse': '/example/1/',
        'question': '/example/1/',
        'message': 'standard_text',
        'owner': '',
        'parent_response': '/example/1/',
    }
    missing_owner = {
        'reportresponse': '/example/1/',
        'question': '/example/1/',
        'message': 'standard_text',
        'parent_response': '/example/1/',
    }

    modified_parent_response = {
        'reportresponse': '/example/1/',
        'question': '/example/1/',
        'message': 'standard_text',
        'owner': '',
        'parent_response': '/example/2/',
    }
    missing_parent_response = {
        'reportresponse': '/example/1/',
        'question': '/example/1/',
        'message': 'standard_text',
        'owner': '',
    }



class SuspiciousTestData(AvaCoreTestData):
    """
    Test data for Suspicious
    """

    @staticmethod
    def init_requirements():
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if Question.objects.count() == 0:
            QuestionTestData.init_requirements()
            model = Question.objects.create(**QuestionTestData.get_data('standard'))
            model.save()
            model = Question.objects.create(**QuestionTestData.get_data('unique'))
            model.save()

    # Store self information
    model = Suspicious
    url = '/example'

    standard = {
        'url': 'standard_char',
        'incident_date': 'default',
        'question_ptr': 'default',
    }

    unique = {
        'url': 'unique_char',
        'incident_date': 'default',
        'question_ptr': 'default',
    }

    modified_url = {
        'url': 'modified_char',
        'incident_date': 'default',
        'question_ptr': 'default',
    }
    missing_url = {
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

    missing_question_ptr = {
        'url': 'standard_char',
        'incident_date': 'default',
    }
    modified_question_ptr = {
        'url': 'standard_char',
        'incident_date': 'default',
        'question_ptr': 'default',
    }



class QuestionTestData(AvaCoreTestData):
    """
    Test data for Question
    """

    @staticmethod
    def init_requirements():
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if Suspicious.objects.count() == 0:
            SuspiciousTestData.init_requirements()
            model = Suspicious.objects.create(**SuspiciousTestData.get_data('standard'))
            model.save()
            model = Suspicious.objects.create(**SuspiciousTestData.get_data('unique'))
            model.save()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if ReportResponse.objects.count() == 0:
            ReportResponseTestData.init_requirements()
            model = ReportResponse.objects.create(**ReportResponseTestData.get_data('standard'))
            model.save()
            model = ReportResponse.objects.create(**ReportResponseTestData.get_data('unique'))
            model.save()

    # Store self information
    model = Question
    url = '/example'

    standard = {
        'description': 'standard_text',
        'status_type': 0,
        'is_resolved': True,
        'priority_type': 0,
        'suspicious': 'default',
        'owner': '',
        'question_responses': '/example/1/',
    }

    unique = {
        'description': 'unique_text',
        'status_type': 4,
        'is_resolved': False,
        'priority_type': 3,
        'suspicious': 'default',
        'owner': '',
        'question_responses': '/example/2/',
    }

    modified_description = {
        'description': 'modified_text',
        'status_type': 0,
        'is_resolved': True,
        'priority_type': 0,
        'suspicious': 'default',
        'owner': '',
        'question_responses': '/example/1/',
    }
    missing_description = {
        'status_type': 0,
        'is_resolved': True,
        'priority_type': 0,
        'suspicious': 'default',
        'owner': '',
        'question_responses': '/example/1/',
    }

    modified_status_type = {
        'description': 'standard_text',
        'status_type': 4,
        'is_resolved': True,
        'priority_type': 0,
        'suspicious': 'default',
        'owner': '',
        'question_responses': '/example/1/',
    }
    missing_status_type = {
        'description': 'standard_text',
        'is_resolved': True,
        'priority_type': 0,
        'suspicious': 'default',
        'owner': '',
        'question_responses': '/example/1/',
    }

    missing_is_resolved = {
        'description': 'standard_text',
        'status_type': 0,
        'priority_type': 0,
        'suspicious': 'default',
        'owner': '',
        'question_responses': '/example/1/',
    }
    modified_is_resolved = {
        'description': 'standard_text',
        'status_type': 0,
        'is_resolved': False,
        'priority_type': 0,
        'suspicious': 'default',
        'owner': '',
        'question_responses': '/example/1/',
    }

    modified_priority_type = {
        'description': 'standard_text',
        'status_type': 0,
        'is_resolved': True,
        'priority_type': 3,
        'suspicious': 'default',
        'owner': '',
        'question_responses': '/example/1/',
    }
    missing_priority_type = {
        'description': 'standard_text',
        'status_type': 0,
        'is_resolved': True,
        'suspicious': 'default',
        'owner': '',
        'question_responses': '/example/1/',
    }

    missing_suspicious = {
        'description': 'standard_text',
        'status_type': 0,
        'is_resolved': True,
        'priority_type': 0,
        'owner': '',
        'question_responses': '/example/1/',
    }
    modified_suspicious = {
        'description': 'standard_text',
        'status_type': 0,
        'is_resolved': True,
        'priority_type': 0,
        'suspicious': 'default',
        'owner': '',
        'question_responses': '/example/1/',
    }

    modified_owner = {
        'description': 'standard_text',
        'status_type': 0,
        'is_resolved': True,
        'priority_type': 0,
        'suspicious': 'default',
        'owner': '',
        'question_responses': '/example/1/',
    }
    missing_owner = {
        'description': 'standard_text',
        'status_type': 0,
        'is_resolved': True,
        'priority_type': 0,
        'suspicious': 'default',
        'question_responses': '/example/1/',
    }

    modified_question_responses = {
        'description': 'standard_text',
        'status_type': 0,
        'is_resolved': True,
        'priority_type': 0,
        'suspicious': 'default',
        'owner': '',
        'question_responses': '/example/2/',
    }
    missing_question_responses = {
        'description': 'standard_text',
        'status_type': 0,
        'is_resolved': True,
        'priority_type': 0,
        'suspicious': 'default',
        'owner': '',
    }




