# Rest Imports
from rest_framework import status
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.outreach.models import ReportResponse, Question, Suspicious


# Implementation
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

        # Grab the required data set depending on if an owner is required.
        query_set = ReportResponse.objects.filter(owner=owner['email']) if 'email' in standard_data else ReportResponse.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            ReportResponseTestData.init_requirements(owner)
            model = ReportResponse.objects.create(**standard_data)
            model = ReportResponse.objects.create(**unique_data)

        # Grab data for object creation, with owner if required.
        data_model = QuestionTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = Question.objects.filter(owner=owner['email']) if 'email' in standard_data else Question.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            QuestionTestData.init_requirements(owner)
            model = Question.objects.create(**standard_data)
            model = Question.objects.create(**unique_data)

        # Grab data for object creation, with owner if required.
        data_model = ReportResponseTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = ReportResponse.objects.filter(owner=owner['email']) if 'email' in standard_data else ReportResponse.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            ReportResponseTestData.init_requirements(owner)
            model = ReportResponse.objects.create(**standard_data)
            model = ReportResponse.objects.create(**unique_data)

    # Store self information
    model = ReportResponse
    url = 'example/'

    standard = {
        'message': 'standard_text',
        'parent_response': 'example//1/',
        'question': 'example//1/',
        'reportresponse': 'example//1/',
        'owner': '',
    }

    unique = {
        'message': 'unique_text',
        'parent_response': 'example//2/',
        'question': 'example//2/',
        'reportresponse': 'example//2/',
        'owner': '',
    }

    modified_message = {
        'message': 'modified_text',
        'parent_response': 'example//1/',
        'question': 'example//1/',
        'reportresponse': 'example//1/',
        'owner': '',
    }
    missing_message = {
        'parent_response': 'example//1/',
        'question': 'example//1/',
        'reportresponse': 'example//1/',
        'owner': '',
    }

    missing_parent_response = {
        'message': 'standard_text',
        'question': 'example//1/',
        'reportresponse': 'example//1/',
        'owner': '',
    }
    modified_parent_response = {
        'message': 'standard_text',
        'parent_response': 'example//2/',
        'question': 'example//1/',
        'reportresponse': 'example//1/',
        'owner': '',
    }

    modified_question = {
        'message': 'standard_text',
        'parent_response': 'example//1/',
        'question': 'example//2/',
        'reportresponse': 'example//1/',
        'owner': '',
    }
    missing_question = {
        'message': 'standard_text',
        'parent_response': 'example//1/',
        'reportresponse': 'example//1/',
        'owner': '',
    }

    missing_reportresponse = {
        'message': 'standard_text',
        'parent_response': 'example//1/',
        'question': 'example//1/',
        'owner': '',
    }
    modified_reportresponse = {
        'message': 'standard_text',
        'parent_response': 'example//1/',
        'question': 'example//1/',
        'reportresponse': 'example//2/',
        'owner': '',
    }

    missing_owner = {
        'message': 'standard_text',
        'parent_response': 'example//1/',
        'question': 'example//1/',
        'reportresponse': 'example//1/',
    }
    modified_owner = {
        'message': 'standard_text',
        'parent_response': 'example//1/',
        'question': 'example//1/',
        'reportresponse': 'example//1/',
        'owner': '',
    }



class QuestionTestData(AvaCoreTestData):
    """
    Test data for Question
    """

    @staticmethod
    def init_requirements(owner):
        # Grab data for object creation, with owner if required.
        data_model = ReportResponseTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = ReportResponse.objects.filter(owner=owner['email']) if 'email' in standard_data else ReportResponse.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            ReportResponseTestData.init_requirements(owner)
            model = ReportResponse.objects.create(**standard_data)
            model = ReportResponse.objects.create(**unique_data)

        # Grab data for object creation, with owner if required.
        data_model = SuspiciousTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = Suspicious.objects.filter(owner=owner['email']) if 'email' in standard_data else Suspicious.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            SuspiciousTestData.init_requirements(owner)
            model = Suspicious.objects.create(**standard_data)
            model = Suspicious.objects.create(**unique_data)

    # Store self information
    model = Question
    url = 'example/'

    standard = {
        'status_type': 0,
        'question_responses': 'example//1/',
        'is_resolved': True,
        'suspicious': 'default',
        'priority_type': 0,
        'description': 'standard_text',
        'owner': '',
    }

    unique = {
        'status_type': 4,
        'question_responses': 'example//2/',
        'is_resolved': False,
        'suspicious': 'default',
        'priority_type': 3,
        'description': 'unique_text',
        'owner': '',
    }

    missing_status_type = {
        'question_responses': 'example//1/',
        'is_resolved': True,
        'suspicious': 'default',
        'priority_type': 0,
        'description': 'standard_text',
        'owner': '',
    }
    modified_status_type = {
        'status_type': 4,
        'question_responses': 'example//1/',
        'is_resolved': True,
        'suspicious': 'default',
        'priority_type': 0,
        'description': 'standard_text',
        'owner': '',
    }

    missing_question_responses = {
        'status_type': 0,
        'is_resolved': True,
        'suspicious': 'default',
        'priority_type': 0,
        'description': 'standard_text',
        'owner': '',
    }
    modified_question_responses = {
        'status_type': 0,
        'question_responses': 'example//2/',
        'is_resolved': True,
        'suspicious': 'default',
        'priority_type': 0,
        'description': 'standard_text',
        'owner': '',
    }

    modified_is_resolved = {
        'status_type': 0,
        'question_responses': 'example//1/',
        'is_resolved': False,
        'suspicious': 'default',
        'priority_type': 0,
        'description': 'standard_text',
        'owner': '',
    }
    missing_is_resolved = {
        'status_type': 0,
        'question_responses': 'example//1/',
        'suspicious': 'default',
        'priority_type': 0,
        'description': 'standard_text',
        'owner': '',
    }

    missing_suspicious = {
        'status_type': 0,
        'question_responses': 'example//1/',
        'is_resolved': True,
        'priority_type': 0,
        'description': 'standard_text',
        'owner': '',
    }
    modified_suspicious = {
        'status_type': 0,
        'question_responses': 'example//1/',
        'is_resolved': True,
        'suspicious': 'default',
        'priority_type': 0,
        'description': 'standard_text',
        'owner': '',
    }

    missing_priority_type = {
        'status_type': 0,
        'question_responses': 'example//1/',
        'is_resolved': True,
        'suspicious': 'default',
        'description': 'standard_text',
        'owner': '',
    }
    modified_priority_type = {
        'status_type': 0,
        'question_responses': 'example//1/',
        'is_resolved': True,
        'suspicious': 'default',
        'priority_type': 3,
        'description': 'standard_text',
        'owner': '',
    }

    missing_description = {
        'status_type': 0,
        'question_responses': 'example//1/',
        'is_resolved': True,
        'suspicious': 'default',
        'priority_type': 0,
        'owner': '',
    }
    modified_description = {
        'status_type': 0,
        'question_responses': 'example//1/',
        'is_resolved': True,
        'suspicious': 'default',
        'priority_type': 0,
        'description': 'modified_text',
        'owner': '',
    }

    missing_owner = {
        'status_type': 0,
        'question_responses': 'example//1/',
        'is_resolved': True,
        'suspicious': 'default',
        'priority_type': 0,
        'description': 'standard_text',
    }
    modified_owner = {
        'status_type': 0,
        'question_responses': 'example//1/',
        'is_resolved': True,
        'suspicious': 'default',
        'priority_type': 0,
        'description': 'standard_text',
        'owner': '',
    }



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
        query_set = Question.objects.filter(owner=owner['email']) if 'email' in standard_data else Question.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            QuestionTestData.init_requirements(owner)
            model = Question.objects.create(**standard_data)
            model = Question.objects.create(**unique_data)

    # Store self information
    model = Suspicious
    url = 'example/'

    standard = {
        'incident_date': 'default',
        'question_ptr': 'default',
        'url': 'standard_char',
    }

    unique = {
        'incident_date': 'default',
        'question_ptr': 'default',
        'url': 'unique_char',
    }

    modified_incident_date = {
        'incident_date': 'default',
        'question_ptr': 'default',
        'url': 'standard_char',
    }
    missing_incident_date = {
        'question_ptr': 'default',
        'url': 'standard_char',
    }

    modified_question_ptr = {
        'incident_date': 'default',
        'question_ptr': 'default',
        'url': 'standard_char',
    }
    missing_question_ptr = {
        'incident_date': 'default',
        'url': 'standard_char',
    }

    modified_url = {
        'incident_date': 'default',
        'question_ptr': 'default',
        'url': 'modified_char',
    }
    missing_url = {
        'incident_date': 'default',
        'question_ptr': 'default',
    }




