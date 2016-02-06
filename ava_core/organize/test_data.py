# Rest Imports
from rest_framework import status
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.organize.models import GroupIdentifierAttribute, PersonIdentifierAttribute, GroupReport, PersonIdentifierReport, Person, PersonAttribute, Group, GroupIdentifier, PersonIdentifier


# Implementation
class GroupIdentifierAttributeTestData(AvaCoreTestData):
    """
    Test data for GroupIdentifierAttribute
    """

    @staticmethod
    def init_requirements(owner):
        # Grab data for object creation, with owner if required.
        data_model = GroupIdentifierTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = GroupIdentifier.objects.filter(owner=owner['email']) if 'email' in standard_data else GroupIdentifier.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            GroupIdentifierTestData.init_requirements(owner)
            model = GroupIdentifier.objects.create(**standard_data)
            model = GroupIdentifier.objects.create(**unique_data)

    # Store self information
    model = GroupIdentifierAttribute
    url = 'example/'

    standard = {
        'identifier': 'example//1/',
        'ignore_type': 0,
    }

    unique = {
        'identifier': 'example//2/',
        'ignore_type': 1,
    }

    missing_identifier = {
        'ignore_type': 0,
    }
    modified_identifier = {
        'identifier': 'example//2/',
        'ignore_type': 0,
    }

    modified_ignore_type = {
        'identifier': 'example//1/',
        'ignore_type': 1,
    }
    missing_ignore_type = {
        'identifier': 'example//1/',
    }



class PersonIdentifierAttributeTestData(AvaCoreTestData):
    """
    Test data for PersonIdentifierAttribute
    """

    @staticmethod
    def init_requirements(owner):
        # Grab data for object creation, with owner if required.
        data_model = PersonIdentifierTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = PersonIdentifier.objects.filter(owner=owner['email']) if 'email' in standard_data else PersonIdentifier.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            PersonIdentifierTestData.init_requirements(owner)
            model = PersonIdentifier.objects.create(**standard_data)
            model = PersonIdentifier.objects.create(**unique_data)

    # Store self information
    model = PersonIdentifierAttribute
    url = 'example/'

    standard = {
        'identifier': 'example//1/',
        'ignore_type': 0,
    }

    unique = {
        'identifier': 'example//2/',
        'ignore_type': 2,
    }

    missing_identifier = {
        'ignore_type': 0,
    }
    modified_identifier = {
        'identifier': 'example//2/',
        'ignore_type': 0,
    }

    modified_ignore_type = {
        'identifier': 'example//1/',
        'ignore_type': 2,
    }
    missing_ignore_type = {
        'identifier': 'example//1/',
    }



class GroupReportTestData(AvaCoreTestData):
    """
    Test data for GroupReport
    """

    @staticmethod
    def init_requirements(owner):
        # Grab data for object creation, with owner if required.
        data_model = GroupTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = Group.objects.filter(owner=owner['email']) if 'email' in standard_data else Group.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            GroupTestData.init_requirements(owner)
            model = Group.objects.create(**standard_data)
            model = Group.objects.create(**unique_data)

    # Store self information
    model = GroupReport
    url = 'example/'

    standard = {
        'is_resolved': True,
        'group': 'example//1/',
        'description': 'standard_text',
        'owner': '',
        'reason_type': 0,
        'priority_type': 0,
    }

    unique = {
        'is_resolved': False,
        'group': 'example//2/',
        'description': 'unique_text',
        'owner': '',
        'reason_type': 0,
        'priority_type': 3,
    }

    missing_is_resolved = {
        'group': 'example//1/',
        'description': 'standard_text',
        'owner': '',
        'reason_type': 0,
        'priority_type': 0,
    }
    modified_is_resolved = {
        'is_resolved': False,
        'group': 'example//1/',
        'description': 'standard_text',
        'owner': '',
        'reason_type': 0,
        'priority_type': 0,
    }

    modified_group = {
        'is_resolved': True,
        'group': 'example//2/',
        'description': 'standard_text',
        'owner': '',
        'reason_type': 0,
        'priority_type': 0,
    }
    missing_group = {
        'is_resolved': True,
        'description': 'standard_text',
        'owner': '',
        'reason_type': 0,
        'priority_type': 0,
    }

    missing_description = {
        'is_resolved': True,
        'group': 'example//1/',
        'owner': '',
        'reason_type': 0,
        'priority_type': 0,
    }
    modified_description = {
        'is_resolved': True,
        'group': 'example//1/',
        'description': 'modified_text',
        'owner': '',
        'reason_type': 0,
        'priority_type': 0,
    }

    missing_owner = {
        'is_resolved': True,
        'group': 'example//1/',
        'description': 'standard_text',
        'reason_type': 0,
        'priority_type': 0,
    }
    modified_owner = {
        'is_resolved': True,
        'group': 'example//1/',
        'description': 'standard_text',
        'owner': '',
        'reason_type': 0,
        'priority_type': 0,
    }

    missing_reason_type = {
        'is_resolved': True,
        'group': 'example//1/',
        'description': 'standard_text',
        'owner': '',
        'priority_type': 0,
    }
    modified_reason_type = {
        'is_resolved': True,
        'group': 'example//1/',
        'description': 'standard_text',
        'owner': '',
        'reason_type': 0,
        'priority_type': 0,
    }

    missing_priority_type = {
        'is_resolved': True,
        'group': 'example//1/',
        'description': 'standard_text',
        'owner': '',
        'reason_type': 0,
    }
    modified_priority_type = {
        'is_resolved': True,
        'group': 'example//1/',
        'description': 'standard_text',
        'owner': '',
        'reason_type': 0,
        'priority_type': 3,
    }



class PersonIdentifierReportTestData(AvaCoreTestData):
    """
    Test data for PersonIdentifierReport
    """

    @staticmethod
    def init_requirements(owner):
        # Grab data for object creation, with owner if required.
        data_model = PersonIdentifierTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = PersonIdentifier.objects.filter(owner=owner['email']) if 'email' in standard_data else PersonIdentifier.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            PersonIdentifierTestData.init_requirements(owner)
            model = PersonIdentifier.objects.create(**standard_data)
            model = PersonIdentifier.objects.create(**unique_data)

    # Store self information
    model = PersonIdentifierReport
    url = 'example/'

    standard = {
        'is_resolved': True,
        'description': 'standard_text',
        'owner': '',
        'identifier': 'example//1/',
        'reason_type': 0,
        'priority_type': 0,
    }

    unique = {
        'is_resolved': False,
        'description': 'unique_text',
        'owner': '',
        'identifier': 'example//2/',
        'reason_type': 3,
        'priority_type': 3,
    }

    missing_is_resolved = {
        'description': 'standard_text',
        'owner': '',
        'identifier': 'example//1/',
        'reason_type': 0,
        'priority_type': 0,
    }
    modified_is_resolved = {
        'is_resolved': False,
        'description': 'standard_text',
        'owner': '',
        'identifier': 'example//1/',
        'reason_type': 0,
        'priority_type': 0,
    }

    missing_description = {
        'is_resolved': True,
        'owner': '',
        'identifier': 'example//1/',
        'reason_type': 0,
        'priority_type': 0,
    }
    modified_description = {
        'is_resolved': True,
        'description': 'modified_text',
        'owner': '',
        'identifier': 'example//1/',
        'reason_type': 0,
        'priority_type': 0,
    }

    missing_owner = {
        'is_resolved': True,
        'description': 'standard_text',
        'identifier': 'example//1/',
        'reason_type': 0,
        'priority_type': 0,
    }
    modified_owner = {
        'is_resolved': True,
        'description': 'standard_text',
        'owner': '',
        'identifier': 'example//1/',
        'reason_type': 0,
        'priority_type': 0,
    }

    missing_identifier = {
        'is_resolved': True,
        'description': 'standard_text',
        'owner': '',
        'reason_type': 0,
        'priority_type': 0,
    }
    modified_identifier = {
        'is_resolved': True,
        'description': 'standard_text',
        'owner': '',
        'identifier': 'example//2/',
        'reason_type': 0,
        'priority_type': 0,
    }

    missing_reason_type = {
        'is_resolved': True,
        'description': 'standard_text',
        'owner': '',
        'identifier': 'example//1/',
        'priority_type': 0,
    }
    modified_reason_type = {
        'is_resolved': True,
        'description': 'standard_text',
        'owner': '',
        'identifier': 'example//1/',
        'reason_type': 3,
        'priority_type': 0,
    }

    missing_priority_type = {
        'is_resolved': True,
        'description': 'standard_text',
        'owner': '',
        'identifier': 'example//1/',
        'reason_type': 0,
    }
    modified_priority_type = {
        'is_resolved': True,
        'description': 'standard_text',
        'owner': '',
        'identifier': 'example//1/',
        'reason_type': 0,
        'priority_type': 3,
    }



class PersonTestData(AvaCoreTestData):
    """
    Test data for Person
    """

    @staticmethod
    def init_requirements(owner):
        # Import the required model and data
        from ava_core.my.models import People
        from ava_core.my.test_data import PeopleTestData
        # Grab data for object creation, with owner if required.
        data_model = PeopleTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = People.objects.filter(owner=owner['email']) if 'email' in standard_data else People.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            PeopleTestData.init_requirements(owner)
            model = People.objects.create(**standard_data)
            model = People.objects.create(**unique_data)

        # Grab data for object creation, with owner if required.
        data_model = GroupTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = Group.objects.filter(owner=owner['email']) if 'email' in standard_data else Group.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            GroupTestData.init_requirements(owner)
            model = Group.objects.create(**standard_data)
            model = Group.objects.create(**unique_data)

        # Grab data for object creation, with owner if required.
        data_model = PersonAttributeTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = PersonAttribute.objects.filter(owner=owner['email']) if 'email' in standard_data else PersonAttribute.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            PersonAttributeTestData.init_requirements(owner)
            model = PersonAttribute.objects.create(**standard_data)
            model = PersonAttribute.objects.create(**unique_data)

        # Import the required model and data
        from ava_core.evaluate.models import EvaluateController
        from ava_core.evaluate.test_data import EvaluateControllerTestData
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
        from ava_core.evaluate.models import EvaluateTest
        from ava_core.evaluate.test_data import EvaluateTestTestData
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
        data_model = PersonIdentifierTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = PersonIdentifier.objects.filter(owner=owner['email']) if 'email' in standard_data else PersonIdentifier.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            PersonIdentifierTestData.init_requirements(owner)
            model = PersonIdentifier.objects.create(**standard_data)
            model = PersonIdentifier.objects.create(**unique_data)

    # Store self information
    model = Person
    url = 'example/'

    standard = {
        'people': 'example//1/',
        'groups': 'default',
        'personattribute': 'example//1/',
        'surname': 'standard_char',
        'ldap_identity_data': 'default',
        'evaluatecontroller': 'default',
        'evaluatetest': 'example//1/',
        'person_ids': 'example//1/',
        'first_name': 'standard_char',
        'google_identity_data': 'default',
    }

    unique = {
        'people': 'example//2/',
        'groups': 'default',
        'personattribute': 'example//2/',
        'surname': 'unique_char',
        'ldap_identity_data': 'default',
        'evaluatecontroller': 'default',
        'evaluatetest': 'example//2/',
        'person_ids': 'example//2/',
        'first_name': 'unique_char',
        'google_identity_data': 'default',
    }

    missing_people = {
        'groups': 'default',
        'personattribute': 'example//1/',
        'surname': 'standard_char',
        'ldap_identity_data': 'default',
        'evaluatecontroller': 'default',
        'evaluatetest': 'example//1/',
        'person_ids': 'example//1/',
        'first_name': 'standard_char',
        'google_identity_data': 'default',
    }
    modified_people = {
        'people': 'example//2/',
        'groups': 'default',
        'personattribute': 'example//1/',
        'surname': 'standard_char',
        'ldap_identity_data': 'default',
        'evaluatecontroller': 'default',
        'evaluatetest': 'example//1/',
        'person_ids': 'example//1/',
        'first_name': 'standard_char',
        'google_identity_data': 'default',
    }

    missing_groups = {
        'people': 'example//1/',
        'personattribute': 'example//1/',
        'surname': 'standard_char',
        'ldap_identity_data': 'default',
        'evaluatecontroller': 'default',
        'evaluatetest': 'example//1/',
        'person_ids': 'example//1/',
        'first_name': 'standard_char',
        'google_identity_data': 'default',
    }
    modified_groups = {
        'people': 'example//1/',
        'groups': 'default',
        'personattribute': 'example//1/',
        'surname': 'standard_char',
        'ldap_identity_data': 'default',
        'evaluatecontroller': 'default',
        'evaluatetest': 'example//1/',
        'person_ids': 'example//1/',
        'first_name': 'standard_char',
        'google_identity_data': 'default',
    }

    missing_personattribute = {
        'people': 'example//1/',
        'groups': 'default',
        'surname': 'standard_char',
        'ldap_identity_data': 'default',
        'evaluatecontroller': 'default',
        'evaluatetest': 'example//1/',
        'person_ids': 'example//1/',
        'first_name': 'standard_char',
        'google_identity_data': 'default',
    }
    modified_personattribute = {
        'people': 'example//1/',
        'groups': 'default',
        'personattribute': 'example//2/',
        'surname': 'standard_char',
        'ldap_identity_data': 'default',
        'evaluatecontroller': 'default',
        'evaluatetest': 'example//1/',
        'person_ids': 'example//1/',
        'first_name': 'standard_char',
        'google_identity_data': 'default',
    }

    missing_surname = {
        'people': 'example//1/',
        'groups': 'default',
        'personattribute': 'example//1/',
        'ldap_identity_data': 'default',
        'evaluatecontroller': 'default',
        'evaluatetest': 'example//1/',
        'person_ids': 'example//1/',
        'first_name': 'standard_char',
        'google_identity_data': 'default',
    }
    modified_surname = {
        'people': 'example//1/',
        'groups': 'default',
        'personattribute': 'example//1/',
        'surname': 'modified_char',
        'ldap_identity_data': 'default',
        'evaluatecontroller': 'default',
        'evaluatetest': 'example//1/',
        'person_ids': 'example//1/',
        'first_name': 'standard_char',
        'google_identity_data': 'default',
    }

    modified_ldap_identity_data = {
        'people': 'example//1/',
        'groups': 'default',
        'personattribute': 'example//1/',
        'surname': 'standard_char',
        'ldap_identity_data': 'default',
        'evaluatecontroller': 'default',
        'evaluatetest': 'example//1/',
        'person_ids': 'example//1/',
        'first_name': 'standard_char',
        'google_identity_data': 'default',
    }
    missing_ldap_identity_data = {
        'people': 'example//1/',
        'groups': 'default',
        'personattribute': 'example//1/',
        'surname': 'standard_char',
        'evaluatecontroller': 'default',
        'evaluatetest': 'example//1/',
        'person_ids': 'example//1/',
        'first_name': 'standard_char',
        'google_identity_data': 'default',
    }

    missing_evaluatecontroller = {
        'people': 'example//1/',
        'groups': 'default',
        'personattribute': 'example//1/',
        'surname': 'standard_char',
        'ldap_identity_data': 'default',
        'evaluatetest': 'example//1/',
        'person_ids': 'example//1/',
        'first_name': 'standard_char',
        'google_identity_data': 'default',
    }
    modified_evaluatecontroller = {
        'people': 'example//1/',
        'groups': 'default',
        'personattribute': 'example//1/',
        'surname': 'standard_char',
        'ldap_identity_data': 'default',
        'evaluatecontroller': 'default',
        'evaluatetest': 'example//1/',
        'person_ids': 'example//1/',
        'first_name': 'standard_char',
        'google_identity_data': 'default',
    }

    modified_evaluatetest = {
        'people': 'example//1/',
        'groups': 'default',
        'personattribute': 'example//1/',
        'surname': 'standard_char',
        'ldap_identity_data': 'default',
        'evaluatecontroller': 'default',
        'evaluatetest': 'example//2/',
        'person_ids': 'example//1/',
        'first_name': 'standard_char',
        'google_identity_data': 'default',
    }
    missing_evaluatetest = {
        'people': 'example//1/',
        'groups': 'default',
        'personattribute': 'example//1/',
        'surname': 'standard_char',
        'ldap_identity_data': 'default',
        'evaluatecontroller': 'default',
        'person_ids': 'example//1/',
        'first_name': 'standard_char',
        'google_identity_data': 'default',
    }

    modified_person_ids = {
        'people': 'example//1/',
        'groups': 'default',
        'personattribute': 'example//1/',
        'surname': 'standard_char',
        'ldap_identity_data': 'default',
        'evaluatecontroller': 'default',
        'evaluatetest': 'example//1/',
        'person_ids': 'example//2/',
        'first_name': 'standard_char',
        'google_identity_data': 'default',
    }
    missing_person_ids = {
        'people': 'example//1/',
        'groups': 'default',
        'personattribute': 'example//1/',
        'surname': 'standard_char',
        'ldap_identity_data': 'default',
        'evaluatecontroller': 'default',
        'evaluatetest': 'example//1/',
        'first_name': 'standard_char',
        'google_identity_data': 'default',
    }

    missing_first_name = {
        'people': 'example//1/',
        'groups': 'default',
        'personattribute': 'example//1/',
        'surname': 'standard_char',
        'ldap_identity_data': 'default',
        'evaluatecontroller': 'default',
        'evaluatetest': 'example//1/',
        'person_ids': 'example//1/',
        'google_identity_data': 'default',
    }
    modified_first_name = {
        'people': 'example//1/',
        'groups': 'default',
        'personattribute': 'example//1/',
        'surname': 'standard_char',
        'ldap_identity_data': 'default',
        'evaluatecontroller': 'default',
        'evaluatetest': 'example//1/',
        'person_ids': 'example//1/',
        'first_name': 'modified_char',
        'google_identity_data': 'default',
    }

    missing_google_identity_data = {
        'people': 'example//1/',
        'groups': 'default',
        'personattribute': 'example//1/',
        'surname': 'standard_char',
        'ldap_identity_data': 'default',
        'evaluatecontroller': 'default',
        'evaluatetest': 'example//1/',
        'person_ids': 'example//1/',
        'first_name': 'standard_char',
    }
    modified_google_identity_data = {
        'people': 'example//1/',
        'groups': 'default',
        'personattribute': 'example//1/',
        'surname': 'standard_char',
        'ldap_identity_data': 'default',
        'evaluatecontroller': 'default',
        'evaluatetest': 'example//1/',
        'person_ids': 'example//1/',
        'first_name': 'standard_char',
        'google_identity_data': 'default',
    }



class PersonAttributeTestData(AvaCoreTestData):
    """
    Test data for PersonAttribute
    """

    @staticmethod
    def init_requirements(owner):
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
    model = PersonAttribute
    url = 'example/'

    standard = {
        'non_human': True,
        'person': 'example//1/',
    }

    unique = {
        'non_human': False,
        'person': 'example//2/',
    }

    modified_non_human = {
        'non_human': False,
        'person': 'example//1/',
    }
    missing_non_human = {
        'person': 'example//1/',
    }

    modified_person = {
        'non_human': True,
        'person': 'example//2/',
    }
    missing_person = {
        'non_human': True,
    }



class GroupTestData(AvaCoreTestData):
    """
    Test data for Group
    """

    @staticmethod
    def init_requirements(owner):
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
        data_model = GroupIdentifierTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = GroupIdentifier.objects.filter(owner=owner['email']) if 'email' in standard_data else GroupIdentifier.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            GroupIdentifierTestData.init_requirements(owner)
            model = GroupIdentifier.objects.create(**standard_data)
            model = GroupIdentifier.objects.create(**unique_data)

        # Grab data for object creation, with owner if required.
        data_model = GroupReportTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = GroupReport.objects.filter(owner=owner['email']) if 'email' in standard_data else GroupReport.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            GroupReportTestData.init_requirements(owner)
            model = GroupReport.objects.create(**standard_data)
            model = GroupReport.objects.create(**unique_data)

        # Grab data for object creation, with owner if required.
        data_model = GroupTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = Group.objects.filter(owner=owner['email']) if 'email' in standard_data else Group.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            GroupTestData.init_requirements(owner)
            model = Group.objects.create(**standard_data)
            model = Group.objects.create(**unique_data)

        # Grab data for object creation, with owner if required.
        data_model = GroupTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = Group.objects.filter(owner=owner['email']) if 'email' in standard_data else Group.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            GroupTestData.init_requirements(owner)
            model = Group.objects.create(**standard_data)
            model = Group.objects.create(**unique_data)

    # Store self information
    model = Group
    url = 'example/'

    standard = {
        'members': 'default',
        'name': 'standard_char',
        'ldap_group_data': 'default',
        'group_ids': 'example//1/',
        'description': 'standard_text',
        'google_group_data': 'default',
        'groupreport': 'example//1/',
        'parent_group': 'example//1/',
        'parent': 'example//1/',
        'group_type': 'ACTIVE DIRECTORY',
    }

    unique = {
        'members': 'default',
        'name': 'unique_char',
        'ldap_group_data': 'default',
        'group_ids': 'example//2/',
        'description': 'unique_text',
        'google_group_data': 'default',
        'groupreport': 'example//2/',
        'parent_group': 'example//2/',
        'parent': 'example//2/',
        'group_type': 'GOOGLE APPS',
    }

    modified_members = {
        'members': 'default',
        'name': 'standard_char',
        'ldap_group_data': 'default',
        'group_ids': 'example//1/',
        'description': 'standard_text',
        'google_group_data': 'default',
        'groupreport': 'example//1/',
        'parent_group': 'example//1/',
        'parent': 'example//1/',
        'group_type': 'ACTIVE DIRECTORY',
    }
    missing_members = {
        'name': 'standard_char',
        'ldap_group_data': 'default',
        'group_ids': 'example//1/',
        'description': 'standard_text',
        'google_group_data': 'default',
        'groupreport': 'example//1/',
        'parent_group': 'example//1/',
        'parent': 'example//1/',
        'group_type': 'ACTIVE DIRECTORY',
    }

    modified_name = {
        'members': 'default',
        'name': 'modified_char',
        'ldap_group_data': 'default',
        'group_ids': 'example//1/',
        'description': 'standard_text',
        'google_group_data': 'default',
        'groupreport': 'example//1/',
        'parent_group': 'example//1/',
        'parent': 'example//1/',
        'group_type': 'ACTIVE DIRECTORY',
    }
    missing_name = {
        'members': 'default',
        'ldap_group_data': 'default',
        'group_ids': 'example//1/',
        'description': 'standard_text',
        'google_group_data': 'default',
        'groupreport': 'example//1/',
        'parent_group': 'example//1/',
        'parent': 'example//1/',
        'group_type': 'ACTIVE DIRECTORY',
    }

    missing_ldap_group_data = {
        'members': 'default',
        'name': 'standard_char',
        'group_ids': 'example//1/',
        'description': 'standard_text',
        'google_group_data': 'default',
        'groupreport': 'example//1/',
        'parent_group': 'example//1/',
        'parent': 'example//1/',
        'group_type': 'ACTIVE DIRECTORY',
    }
    modified_ldap_group_data = {
        'members': 'default',
        'name': 'standard_char',
        'ldap_group_data': 'default',
        'group_ids': 'example//1/',
        'description': 'standard_text',
        'google_group_data': 'default',
        'groupreport': 'example//1/',
        'parent_group': 'example//1/',
        'parent': 'example//1/',
        'group_type': 'ACTIVE DIRECTORY',
    }

    missing_group_ids = {
        'members': 'default',
        'name': 'standard_char',
        'ldap_group_data': 'default',
        'description': 'standard_text',
        'google_group_data': 'default',
        'groupreport': 'example//1/',
        'parent_group': 'example//1/',
        'parent': 'example//1/',
        'group_type': 'ACTIVE DIRECTORY',
    }
    modified_group_ids = {
        'members': 'default',
        'name': 'standard_char',
        'ldap_group_data': 'default',
        'group_ids': 'example//2/',
        'description': 'standard_text',
        'google_group_data': 'default',
        'groupreport': 'example//1/',
        'parent_group': 'example//1/',
        'parent': 'example//1/',
        'group_type': 'ACTIVE DIRECTORY',
    }

    missing_description = {
        'members': 'default',
        'name': 'standard_char',
        'ldap_group_data': 'default',
        'group_ids': 'example//1/',
        'google_group_data': 'default',
        'groupreport': 'example//1/',
        'parent_group': 'example//1/',
        'parent': 'example//1/',
        'group_type': 'ACTIVE DIRECTORY',
    }
    modified_description = {
        'members': 'default',
        'name': 'standard_char',
        'ldap_group_data': 'default',
        'group_ids': 'example//1/',
        'description': 'modified_text',
        'google_group_data': 'default',
        'groupreport': 'example//1/',
        'parent_group': 'example//1/',
        'parent': 'example//1/',
        'group_type': 'ACTIVE DIRECTORY',
    }

    missing_google_group_data = {
        'members': 'default',
        'name': 'standard_char',
        'ldap_group_data': 'default',
        'group_ids': 'example//1/',
        'description': 'standard_text',
        'groupreport': 'example//1/',
        'parent_group': 'example//1/',
        'parent': 'example//1/',
        'group_type': 'ACTIVE DIRECTORY',
    }
    modified_google_group_data = {
        'members': 'default',
        'name': 'standard_char',
        'ldap_group_data': 'default',
        'group_ids': 'example//1/',
        'description': 'standard_text',
        'google_group_data': 'default',
        'groupreport': 'example//1/',
        'parent_group': 'example//1/',
        'parent': 'example//1/',
        'group_type': 'ACTIVE DIRECTORY',
    }

    modified_groupreport = {
        'members': 'default',
        'name': 'standard_char',
        'ldap_group_data': 'default',
        'group_ids': 'example//1/',
        'description': 'standard_text',
        'google_group_data': 'default',
        'groupreport': 'example//2/',
        'parent_group': 'example//1/',
        'parent': 'example//1/',
        'group_type': 'ACTIVE DIRECTORY',
    }
    missing_groupreport = {
        'members': 'default',
        'name': 'standard_char',
        'ldap_group_data': 'default',
        'group_ids': 'example//1/',
        'description': 'standard_text',
        'google_group_data': 'default',
        'parent_group': 'example//1/',
        'parent': 'example//1/',
        'group_type': 'ACTIVE DIRECTORY',
    }

    missing_parent_group = {
        'members': 'default',
        'name': 'standard_char',
        'ldap_group_data': 'default',
        'group_ids': 'example//1/',
        'description': 'standard_text',
        'google_group_data': 'default',
        'groupreport': 'example//1/',
        'parent': 'example//1/',
        'group_type': 'ACTIVE DIRECTORY',
    }
    modified_parent_group = {
        'members': 'default',
        'name': 'standard_char',
        'ldap_group_data': 'default',
        'group_ids': 'example//1/',
        'description': 'standard_text',
        'google_group_data': 'default',
        'groupreport': 'example//1/',
        'parent_group': 'example//2/',
        'parent': 'example//1/',
        'group_type': 'ACTIVE DIRECTORY',
    }

    modified_parent = {
        'members': 'default',
        'name': 'standard_char',
        'ldap_group_data': 'default',
        'group_ids': 'example//1/',
        'description': 'standard_text',
        'google_group_data': 'default',
        'groupreport': 'example//1/',
        'parent_group': 'example//1/',
        'parent': 'example//2/',
        'group_type': 'ACTIVE DIRECTORY',
    }
    missing_parent = {
        'members': 'default',
        'name': 'standard_char',
        'ldap_group_data': 'default',
        'group_ids': 'example//1/',
        'description': 'standard_text',
        'google_group_data': 'default',
        'groupreport': 'example//1/',
        'parent_group': 'example//1/',
        'group_type': 'ACTIVE DIRECTORY',
    }

    missing_group_type = {
        'members': 'default',
        'name': 'standard_char',
        'ldap_group_data': 'default',
        'group_ids': 'example//1/',
        'description': 'standard_text',
        'google_group_data': 'default',
        'groupreport': 'example//1/',
        'parent_group': 'example//1/',
        'parent': 'example//1/',
    }
    modified_group_type = {
        'members': 'default',
        'name': 'standard_char',
        'ldap_group_data': 'default',
        'group_ids': 'example//1/',
        'description': 'standard_text',
        'google_group_data': 'default',
        'groupreport': 'example//1/',
        'parent_group': 'example//1/',
        'parent': 'example//1/',
        'group_type': 'GOOGLE APPS',
    }



class GroupIdentifierTestData(AvaCoreTestData):
    """
    Test data for GroupIdentifier
    """

    @staticmethod
    def init_requirements(owner):
        # Grab data for object creation, with owner if required.
        data_model = GroupIdentifierAttributeTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = GroupIdentifierAttribute.objects.filter(owner=owner['email']) if 'email' in standard_data else GroupIdentifierAttribute.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            GroupIdentifierAttributeTestData.init_requirements(owner)
            model = GroupIdentifierAttribute.objects.create(**standard_data)
            model = GroupIdentifierAttribute.objects.create(**unique_data)

        # Grab data for object creation, with owner if required.
        data_model = GroupTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = Group.objects.filter(owner=owner['email']) if 'email' in standard_data else Group.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            GroupTestData.init_requirements(owner)
            model = Group.objects.create(**standard_data)
            model = Group.objects.create(**unique_data)

    # Store self information
    model = GroupIdentifier
    url = 'example/'

    standard = {
        'identifier': 'standard_char',
        'identifier_type': 'EMAIL',
        'primary_identifier': True,
        'groupidentifierattribute': 'example//1/',
        'belongs_to': 'example//1/',
    }

    unique = {
        'identifier': 'unique_char',
        'identifier_type': 'SID',
        'primary_identifier': False,
        'groupidentifierattribute': 'example//2/',
        'belongs_to': 'example//2/',
    }

    missing_identifier = {
        'identifier_type': 'EMAIL',
        'primary_identifier': True,
        'groupidentifierattribute': 'example//1/',
        'belongs_to': 'example//1/',
    }
    modified_identifier = {
        'identifier': 'modified_char',
        'identifier_type': 'EMAIL',
        'primary_identifier': True,
        'groupidentifierattribute': 'example//1/',
        'belongs_to': 'example//1/',
    }

    modified_identifier_type = {
        'identifier': 'standard_char',
        'identifier_type': 'SID',
        'primary_identifier': True,
        'groupidentifierattribute': 'example//1/',
        'belongs_to': 'example//1/',
    }
    missing_identifier_type = {
        'identifier': 'standard_char',
        'primary_identifier': True,
        'groupidentifierattribute': 'example//1/',
        'belongs_to': 'example//1/',
    }

    modified_primary_identifier = {
        'identifier': 'standard_char',
        'identifier_type': 'EMAIL',
        'primary_identifier': False,
        'groupidentifierattribute': 'example//1/',
        'belongs_to': 'example//1/',
    }
    missing_primary_identifier = {
        'identifier': 'standard_char',
        'identifier_type': 'EMAIL',
        'groupidentifierattribute': 'example//1/',
        'belongs_to': 'example//1/',
    }

    modified_groupidentifierattribute = {
        'identifier': 'standard_char',
        'identifier_type': 'EMAIL',
        'primary_identifier': True,
        'groupidentifierattribute': 'example//2/',
        'belongs_to': 'example//1/',
    }
    missing_groupidentifierattribute = {
        'identifier': 'standard_char',
        'identifier_type': 'EMAIL',
        'primary_identifier': True,
        'belongs_to': 'example//1/',
    }

    missing_belongs_to = {
        'identifier': 'standard_char',
        'identifier_type': 'EMAIL',
        'primary_identifier': True,
        'groupidentifierattribute': 'example//1/',
    }
    modified_belongs_to = {
        'identifier': 'standard_char',
        'identifier_type': 'EMAIL',
        'primary_identifier': True,
        'groupidentifierattribute': 'example//1/',
        'belongs_to': 'example//2/',
    }



class PersonIdentifierTestData(AvaCoreTestData):
    """
    Test data for PersonIdentifier
    """

    @staticmethod
    def init_requirements(owner):
        # Grab data for object creation, with owner if required.
        data_model = PersonIdentifierReportTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = PersonIdentifierReport.objects.filter(owner=owner['email']) if 'email' in standard_data else PersonIdentifierReport.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            PersonIdentifierReportTestData.init_requirements(owner)
            model = PersonIdentifierReport.objects.create(**standard_data)
            model = PersonIdentifierReport.objects.create(**unique_data)

        # Grab data for object creation, with owner if required.
        data_model = PersonIdentifierAttributeTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = PersonIdentifierAttribute.objects.filter(owner=owner['email']) if 'email' in standard_data else PersonIdentifierAttribute.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            PersonIdentifierAttributeTestData.init_requirements(owner)
            model = PersonIdentifierAttribute.objects.create(**standard_data)
            model = PersonIdentifierAttribute.objects.create(**unique_data)

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
    model = PersonIdentifier
    url = 'example/'

    standard = {
        'personidentifierreport': 'example//1/',
        'personidentifierattribute': 'example//1/',
        'primary_identifier': True,
        'identifier': 'standard_char',
        'identifier_type': 'EMAIL',
        'belongs_to': 'example//1/',
    }

    unique = {
        'personidentifierreport': 'example//2/',
        'personidentifierattribute': 'example//2/',
        'primary_identifier': False,
        'identifier': 'unique_char',
        'identifier_type': 'SID',
        'belongs_to': 'example//2/',
    }

    modified_personidentifierreport = {
        'personidentifierreport': 'example//2/',
        'personidentifierattribute': 'example//1/',
        'primary_identifier': True,
        'identifier': 'standard_char',
        'identifier_type': 'EMAIL',
        'belongs_to': 'example//1/',
    }
    missing_personidentifierreport = {
        'personidentifierattribute': 'example//1/',
        'primary_identifier': True,
        'identifier': 'standard_char',
        'identifier_type': 'EMAIL',
        'belongs_to': 'example//1/',
    }

    missing_personidentifierattribute = {
        'personidentifierreport': 'example//1/',
        'primary_identifier': True,
        'identifier': 'standard_char',
        'identifier_type': 'EMAIL',
        'belongs_to': 'example//1/',
    }
    modified_personidentifierattribute = {
        'personidentifierreport': 'example//1/',
        'personidentifierattribute': 'example//2/',
        'primary_identifier': True,
        'identifier': 'standard_char',
        'identifier_type': 'EMAIL',
        'belongs_to': 'example//1/',
    }

    modified_primary_identifier = {
        'personidentifierreport': 'example//1/',
        'personidentifierattribute': 'example//1/',
        'primary_identifier': False,
        'identifier': 'standard_char',
        'identifier_type': 'EMAIL',
        'belongs_to': 'example//1/',
    }
    missing_primary_identifier = {
        'personidentifierreport': 'example//1/',
        'personidentifierattribute': 'example//1/',
        'identifier': 'standard_char',
        'identifier_type': 'EMAIL',
        'belongs_to': 'example//1/',
    }

    missing_identifier = {
        'personidentifierreport': 'example//1/',
        'personidentifierattribute': 'example//1/',
        'primary_identifier': True,
        'identifier_type': 'EMAIL',
        'belongs_to': 'example//1/',
    }
    modified_identifier = {
        'personidentifierreport': 'example//1/',
        'personidentifierattribute': 'example//1/',
        'primary_identifier': True,
        'identifier': 'modified_char',
        'identifier_type': 'EMAIL',
        'belongs_to': 'example//1/',
    }

    modified_identifier_type = {
        'personidentifierreport': 'example//1/',
        'personidentifierattribute': 'example//1/',
        'primary_identifier': True,
        'identifier': 'standard_char',
        'identifier_type': 'SID',
        'belongs_to': 'example//1/',
    }
    missing_identifier_type = {
        'personidentifierreport': 'example//1/',
        'personidentifierattribute': 'example//1/',
        'primary_identifier': True,
        'identifier': 'standard_char',
        'belongs_to': 'example//1/',
    }

    missing_belongs_to = {
        'personidentifierreport': 'example//1/',
        'personidentifierattribute': 'example//1/',
        'primary_identifier': True,
        'identifier': 'standard_char',
        'identifier_type': 'EMAIL',
    }
    modified_belongs_to = {
        'personidentifierreport': 'example//1/',
        'personidentifierattribute': 'example//1/',
        'primary_identifier': True,
        'identifier': 'standard_char',
        'identifier_type': 'EMAIL',
        'belongs_to': 'example//2/',
    }




