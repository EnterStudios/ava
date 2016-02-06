# Rest Imports
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.outreach.models import Suspicious, ReportResponse, Question


# Implementation
class SuspiciousTestData(AvaCoreTestData):
    """
    Test data for Suspicious
    """

    @staticmethod
    def init_requirements(owner):
        # Grab data for object creation, with owner if required.
        data_model = QuestionTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = Question.objects.filter(
            owner=owner['email']) if 'email' in standard_data else Question.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        # if query_set.count() == 0:
        #     QuestionTestData.init_requirements(owner)
        #     model = Question.objects.create(**standard_data)
        #     model = Question.objects.create(**unique_data)

    # Store self information
    model = Suspicious
    url = 'report/suspicious/'

    standard = {
        'suspicious_url': 'http://example.com',
        'question_ptr': 'default',
        'incident_date': '2016-01-31T09:00',
    }

    unique = {
        'suspicious_url': 'http://example1.com',
        'question_ptr': 'default',
        'incident_date': '2016-01-31T09:00',
    }

    missing_url = {
        'question_ptr': 'default',
        'incident_date': '2016-01-31T09:00',
    }
    modified_url = {
        'suspicious_url': 'http://example.com',
        'question_ptr': 'default',
        'incident_date': '2016-01-31T09:00',
    }

    missing_question_ptr = {
        'suspicious_url': 'http://example.com',
        'incident_date': '2016-01-31T09:00',
    }
    modified_question_ptr = {
        'suspicious_url': 'http://example.com',
        'question_ptr': 'default',
        'incident_date': '2016-01-31T09:00',
    }

    missing_incident_date = {
        'suspicious_url': 'http://example.com',
        'question_ptr': 'default',
    }
    modified_incident_date = {
        'suspicious_url': 'http://example.com',
        'question_ptr': 'default',
        'incident_date': '2016-01-31T09:00',
    }


class ReportResponseTestData(AvaCoreTestData):
    """
    Test data for ReportResponse
    """

    @staticmethod
    def init_requirements(owner):
        # Grab data for object creation, with owner if required.
        data_model = ReportResponseTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # ReportResponseTestData.init_requirements(owner)
        response_standard_model = ReportResponse.create_model_logout(ReportResponse, data_name='standard', owner=owner)
        response_unique_model = ReportResponse.create_model_logout(ReportResponse, data_name='unique', owner=owner)

        # Grab data for object creation, with owner if required.
        data_model = QuestionTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')


        question_standard_model = ReportResponse.create_model_logout(Question, data_name='standard', owner=owner)
        question_unique_model = ReportResponse.create_model_logout(Question, data_name='unique', owner=owner)




    # Store self information
    model = ReportResponse
    url = 'report/response/'

    standard = {
        'parent_response': 'report/response/1/',
        'message': 'standard_text',
        'question': 'report/question/1/',
        'owner': '',
    }

    unique = {
        'parent_response': 'report/response/2/',
        'message': 'unique_text',
        'question': 'report/question/2/',
        'owner': '',
    }

    modified_reportresponse = {
        'parent_response': 'report/response/1/',
        'message': 'standard_text',
        'question': 'report/question/1/',
        'owner': '',
    }
    missing_reportresponse = {
        'parent_response': 'report/response/1/',
        'message': 'standard_text',
        'question': 'report/question/1/',
        'owner': '',
    }

    modified_parent_response = {
        'parent_response': 'report/response/2/',
        'message': 'standard_text',
        'question': 'report/question/1/',
        'owner': '',
    }
    missing_parent_response = {
        'message': 'standard_text',
        'question': 'report/question/1/',
        'owner': '',
    }

    missing_message = {
        'parent_response': 'report/response/1/',
        'question': 'report/question/1/',
        'owner': '',
    }
    modified_message = {
        'parent_response': 'report/response/1/',
        'message': 'modified_text',
        'question': 'report/question/1/',
        'owner': '',
    }

    missing_question = {
        'parent_response': 'report/response/1/',
        'message': 'standard_text',
        'owner': '',
    }
    modified_question = {
        'parent_response': 'report/response/1/',
        'message': 'standard_text',
        'question': 'report/question/2/',
        'owner': '',
    }

    missing_owner = {
        'parent_response': 'report/response/1/',
        'message': 'standard_text',
        'question': 'report/question/1/',
    }
    modified_owner = {
        'parent_response': 'report/response/1/',
        'message': 'standard_text',
        'question': 'report/question/1/',
        'owner': '',
    }


class QuestionTestData(AvaCoreTestData):
    """
    Test data for Question
    """

    @staticmethod
    def init_requirements(owner):
        # Grab data for object creation, with owner if required.
        data_model = SuspiciousTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = Suspicious.objects.filter(
            owner=owner['email']) if 'email' in standard_data else Suspicious.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        # if query_set.count() == 0:
        #     SuspiciousTestData.init_requirements(owner)
        #     model = Suspicious.objects.create(**standard_data)
        #     model = Suspicious.objects.create(**unique_data)

        # Grab data for object creation, with owner if required.
        data_model = ReportResponseTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = ReportResponse.objects.filter(
            owner=owner['email']) if 'email' in standard_data else ReportResponse.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        # if query_set.count() == 0:
        #     ReportResponseTestData.init_requirements(owner)
        #     model = ReportResponse.objects.create(**standard_data)
        #     model = ReportResponse.objects.create(**unique_data)

    # Store self information
    model = Question
    url = 'report/question/'

    standard = {
        'is_resolved': True,
        'description': 'standard_text',
        'owner': 1,
        'status_type': 0,
        'suspicious': 'default',
        'question_responses': 'report/response/1/',
        'priority_type': 0,
    }

    unique = {
        'is_resolved': False,
        'description': 'unique_text',
        'owner': 1,
        'status_type': 4,
        'suspicious': 'default',
        'question_responses': 'report/response/2/',
        'priority_type': 3,
    }

    missing_is_resolved = {
        'description': 'standard_text',
        'owner': 1,
        'status_type': 0,
        'suspicious': 'default',
        'question_responses': 'report/response/1/',
        'priority_type': 0,
    }
    modified_is_resolved = {
        'is_resolved': False,
        'description': 'standard_text',
        'owner': 1,
        'status_type': 0,
        'suspicious': 'default',
        'question_responses': 'report/response/1/',
        'priority_type': 0,
    }

    missing_description = {
        'is_resolved': True,
        'owner': '',
        'status_type': 0,
        'suspicious': 'default',
        'question_responses': 'report/response/1/',
        'priority_type': 0,
    }
    modified_description = {
        'is_resolved': True,
        'description': 'modified_text',
        'owner': '',
        'status_type': 0,
        'suspicious': 'default',
        'question_responses': 'report/response/1/',
        'priority_type': 0,
    }

    missing_owner = {
        'is_resolved': True,
        'description': 'standard_text',
        'status_type': 0,
        'suspicious': 'default',
        'question_responses': 'report/response/1/',
        'priority_type': 0,
    }
    modified_owner = {
        'is_resolved': True,
        'description': 'standard_text',
        'owner': '',
        'status_type': 0,
        'suspicious': 'default',
        'question_responses': 'report/response/1/',
        'priority_type': 0,
    }

    modified_status_type = {
        'is_resolved': True,
        'description': 'standard_text',
        'owner': '',
        'status_type': 4,
        'suspicious': 'default',
        'question_responses': 'report/response/1/',
        'priority_type': 0,
    }
    missing_status_type = {
        'is_resolved': True,
        'description': 'standard_text',
        'owner': '',
        'suspicious': 'default',
        'question_responses': 'report/response/1/',
        'priority_type': 0,
    }

    missing_suspicious = {
        'is_resolved': True,
        'description': 'standard_text',
        'owner': '',
        'status_type': 0,
        'question_responses': 'report/response/1/',
        'priority_type': 0,
    }
    modified_suspicious = {
        'is_resolved': True,
        'description': 'standard_text',
        'owner': '',
        'status_type': 0,
        'suspicious': 'default',
        'question_responses': 'report/response/1/',
        'priority_type': 0,
    }

    missing_question_responses = {
        'is_resolved': True,
        'description': 'standard_text',
        'owner': '',
        'status_type': 0,
        'suspicious': 'default',
        'priority_type': 0,
    }
    modified_question_responses = {
        'is_resolved': True,
        'description': 'standard_text',
        'owner': '',
        'status_type': 0,
        'suspicious': 'default',
        'question_responses': 'report/response/2/',
        'priority_type': 0,
    }

    missing_priority_type = {
        'is_resolved': True,
        'description': 'standard_text',
        'owner': '',
        'status_type': 0,
        'suspicious': 'default',
        'question_responses': 'report/response/1/',
    }
    modified_priority_type = {
        'is_resolved': True,
        'description': 'standard_text',
        'owner': '',
        'status_type': 0,
        'suspicious': 'default',
        'question_responses': 'report/response/1/',
        'priority_type': 3,
    }
