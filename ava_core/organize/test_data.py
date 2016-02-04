# Rest Imports
from rest_framework import status
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.organize.models import Group, PersonIdentifierReport, GroupReport, GroupIdentifier, GroupIdentifierAttribute, PersonIdentifierAttribute, Person, PersonAttribute, PersonIdentifier


# Implementation
class GroupTestData(AvaCoreTestData):
    """
    Test data for Group
    """

    @staticmethod
    def init_requirements():
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if GroupReport.objects.count() == 0:
            GroupReportTestData.init_requirements()
            model = GroupReport.objects.create(**GroupReportTestData.get_data('standard'))
            model.save()
            model = GroupReport.objects.create(**GroupReportTestData.get_data('unique'))
            model.save()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if Group.objects.count() == 0:
            GroupTestData.init_requirements()
            model = Group.objects.create(**GroupTestData.get_data('standard'))
            model.save()
            model = Group.objects.create(**GroupTestData.get_data('unique'))
            model.save()

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
        if Group.objects.count() == 0:
            GroupTestData.init_requirements()
            model = Group.objects.create(**GroupTestData.get_data('standard'))
            model.save()
            model = Group.objects.create(**GroupTestData.get_data('unique'))
            model.save()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if GroupIdentifier.objects.count() == 0:
            GroupIdentifierTestData.init_requirements()
            model = GroupIdentifier.objects.create(**GroupIdentifierTestData.get_data('standard'))
            model.save()
            model = GroupIdentifier.objects.create(**GroupIdentifierTestData.get_data('unique'))
            model.save()

    # Store self information
    model = Group
    url = '/example'

    standard = {
        'group_type': 'ACTIVE DIRECTORY',
        'description': 'standard_text',
        'groupreport': '/example/1/',
        'parent_group': '/example/1/',
        'ldap_group_data': 'default',
        'members': 'default',
        'google_group_data': 'default',
        'name': 'standard_char',
        'parent': '/example/1/',
        'group_ids': '/example/1/',
    }

    unique = {
        'group_type': 'GOOGLE APPS',
        'description': 'unique_text',
        'groupreport': '/example/2/',
        'parent_group': '/example/2/',
        'ldap_group_data': 'default',
        'members': 'default',
        'google_group_data': 'default',
        'name': 'unique_char',
        'parent': '/example/2/',
        'group_ids': '/example/2/',
    }

    missing_group_type = {
        'description': 'standard_text',
        'groupreport': '/example/1/',
        'parent_group': '/example/1/',
        'ldap_group_data': 'default',
        'members': 'default',
        'google_group_data': 'default',
        'name': 'standard_char',
        'parent': '/example/1/',
        'group_ids': '/example/1/',
    }
    modified_group_type = {
        'group_type': 'GOOGLE APPS',
        'description': 'standard_text',
        'groupreport': '/example/1/',
        'parent_group': '/example/1/',
        'ldap_group_data': 'default',
        'members': 'default',
        'google_group_data': 'default',
        'name': 'standard_char',
        'parent': '/example/1/',
        'group_ids': '/example/1/',
    }

    modified_description = {
        'group_type': 'ACTIVE DIRECTORY',
        'description': 'modified_text',
        'groupreport': '/example/1/',
        'parent_group': '/example/1/',
        'ldap_group_data': 'default',
        'members': 'default',
        'google_group_data': 'default',
        'name': 'standard_char',
        'parent': '/example/1/',
        'group_ids': '/example/1/',
    }
    missing_description = {
        'group_type': 'ACTIVE DIRECTORY',
        'groupreport': '/example/1/',
        'parent_group': '/example/1/',
        'ldap_group_data': 'default',
        'members': 'default',
        'google_group_data': 'default',
        'name': 'standard_char',
        'parent': '/example/1/',
        'group_ids': '/example/1/',
    }

    modified_groupreport = {
        'group_type': 'ACTIVE DIRECTORY',
        'description': 'standard_text',
        'groupreport': '/example/2/',
        'parent_group': '/example/1/',
        'ldap_group_data': 'default',
        'members': 'default',
        'google_group_data': 'default',
        'name': 'standard_char',
        'parent': '/example/1/',
        'group_ids': '/example/1/',
    }
    missing_groupreport = {
        'group_type': 'ACTIVE DIRECTORY',
        'description': 'standard_text',
        'parent_group': '/example/1/',
        'ldap_group_data': 'default',
        'members': 'default',
        'google_group_data': 'default',
        'name': 'standard_char',
        'parent': '/example/1/',
        'group_ids': '/example/1/',
    }

    modified_parent_group = {
        'group_type': 'ACTIVE DIRECTORY',
        'description': 'standard_text',
        'groupreport': '/example/1/',
        'parent_group': '/example/2/',
        'ldap_group_data': 'default',
        'members': 'default',
        'google_group_data': 'default',
        'name': 'standard_char',
        'parent': '/example/1/',
        'group_ids': '/example/1/',
    }
    missing_parent_group = {
        'group_type': 'ACTIVE DIRECTORY',
        'description': 'standard_text',
        'groupreport': '/example/1/',
        'ldap_group_data': 'default',
        'members': 'default',
        'google_group_data': 'default',
        'name': 'standard_char',
        'parent': '/example/1/',
        'group_ids': '/example/1/',
    }

    missing_ldap_group_data = {
        'group_type': 'ACTIVE DIRECTORY',
        'description': 'standard_text',
        'groupreport': '/example/1/',
        'parent_group': '/example/1/',
        'members': 'default',
        'google_group_data': 'default',
        'name': 'standard_char',
        'parent': '/example/1/',
        'group_ids': '/example/1/',
    }
    modified_ldap_group_data = {
        'group_type': 'ACTIVE DIRECTORY',
        'description': 'standard_text',
        'groupreport': '/example/1/',
        'parent_group': '/example/1/',
        'ldap_group_data': 'default',
        'members': 'default',
        'google_group_data': 'default',
        'name': 'standard_char',
        'parent': '/example/1/',
        'group_ids': '/example/1/',
    }

    missing_members = {
        'group_type': 'ACTIVE DIRECTORY',
        'description': 'standard_text',
        'groupreport': '/example/1/',
        'parent_group': '/example/1/',
        'ldap_group_data': 'default',
        'google_group_data': 'default',
        'name': 'standard_char',
        'parent': '/example/1/',
        'group_ids': '/example/1/',
    }
    modified_members = {
        'group_type': 'ACTIVE DIRECTORY',
        'description': 'standard_text',
        'groupreport': '/example/1/',
        'parent_group': '/example/1/',
        'ldap_group_data': 'default',
        'members': 'default',
        'google_group_data': 'default',
        'name': 'standard_char',
        'parent': '/example/1/',
        'group_ids': '/example/1/',
    }

    missing_google_group_data = {
        'group_type': 'ACTIVE DIRECTORY',
        'description': 'standard_text',
        'groupreport': '/example/1/',
        'parent_group': '/example/1/',
        'ldap_group_data': 'default',
        'members': 'default',
        'name': 'standard_char',
        'parent': '/example/1/',
        'group_ids': '/example/1/',
    }
    modified_google_group_data = {
        'group_type': 'ACTIVE DIRECTORY',
        'description': 'standard_text',
        'groupreport': '/example/1/',
        'parent_group': '/example/1/',
        'ldap_group_data': 'default',
        'members': 'default',
        'google_group_data': 'default',
        'name': 'standard_char',
        'parent': '/example/1/',
        'group_ids': '/example/1/',
    }

    modified_name = {
        'group_type': 'ACTIVE DIRECTORY',
        'description': 'standard_text',
        'groupreport': '/example/1/',
        'parent_group': '/example/1/',
        'ldap_group_data': 'default',
        'members': 'default',
        'google_group_data': 'default',
        'name': 'modified_char',
        'parent': '/example/1/',
        'group_ids': '/example/1/',
    }
    missing_name = {
        'group_type': 'ACTIVE DIRECTORY',
        'description': 'standard_text',
        'groupreport': '/example/1/',
        'parent_group': '/example/1/',
        'ldap_group_data': 'default',
        'members': 'default',
        'google_group_data': 'default',
        'parent': '/example/1/',
        'group_ids': '/example/1/',
    }

    missing_parent = {
        'group_type': 'ACTIVE DIRECTORY',
        'description': 'standard_text',
        'groupreport': '/example/1/',
        'parent_group': '/example/1/',
        'ldap_group_data': 'default',
        'members': 'default',
        'google_group_data': 'default',
        'name': 'standard_char',
        'group_ids': '/example/1/',
    }
    modified_parent = {
        'group_type': 'ACTIVE DIRECTORY',
        'description': 'standard_text',
        'groupreport': '/example/1/',
        'parent_group': '/example/1/',
        'ldap_group_data': 'default',
        'members': 'default',
        'google_group_data': 'default',
        'name': 'standard_char',
        'parent': '/example/2/',
        'group_ids': '/example/1/',
    }

    modified_group_ids = {
        'group_type': 'ACTIVE DIRECTORY',
        'description': 'standard_text',
        'groupreport': '/example/1/',
        'parent_group': '/example/1/',
        'ldap_group_data': 'default',
        'members': 'default',
        'google_group_data': 'default',
        'name': 'standard_char',
        'parent': '/example/1/',
        'group_ids': '/example/2/',
    }
    missing_group_ids = {
        'group_type': 'ACTIVE DIRECTORY',
        'description': 'standard_text',
        'groupreport': '/example/1/',
        'parent_group': '/example/1/',
        'ldap_group_data': 'default',
        'members': 'default',
        'google_group_data': 'default',
        'name': 'standard_char',
        'parent': '/example/1/',
    }



class PersonIdentifierReportTestData(AvaCoreTestData):
    """
    Test data for PersonIdentifierReport
    """

    @staticmethod
    def init_requirements():
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if PersonIdentifier.objects.count() == 0:
            PersonIdentifierTestData.init_requirements()
            model = PersonIdentifier.objects.create(**PersonIdentifierTestData.get_data('standard'))
            model.save()
            model = PersonIdentifier.objects.create(**PersonIdentifierTestData.get_data('unique'))
            model.save()

    # Store self information
    model = PersonIdentifierReport
    url = '/example'

    standard = {
        'description': 'standard_text',
        'identifier': '/example/1/',
        'is_resolved': True,
        'priority_type': 0,
        'reason_type': 0,
        'owner': '',
    }

    unique = {
        'description': 'unique_text',
        'identifier': '/example/2/',
        'is_resolved': False,
        'priority_type': 3,
        'reason_type': 3,
        'owner': '',
    }

    modified_description = {
        'description': 'modified_text',
        'identifier': '/example/1/',
        'is_resolved': True,
        'priority_type': 0,
        'reason_type': 0,
        'owner': '',
    }
    missing_description = {
        'identifier': '/example/1/',
        'is_resolved': True,
        'priority_type': 0,
        'reason_type': 0,
        'owner': '',
    }

    missing_identifier = {
        'description': 'standard_text',
        'is_resolved': True,
        'priority_type': 0,
        'reason_type': 0,
        'owner': '',
    }
    modified_identifier = {
        'description': 'standard_text',
        'identifier': '/example/2/',
        'is_resolved': True,
        'priority_type': 0,
        'reason_type': 0,
        'owner': '',
    }

    missing_is_resolved = {
        'description': 'standard_text',
        'identifier': '/example/1/',
        'priority_type': 0,
        'reason_type': 0,
        'owner': '',
    }
    modified_is_resolved = {
        'description': 'standard_text',
        'identifier': '/example/1/',
        'is_resolved': False,
        'priority_type': 0,
        'reason_type': 0,
        'owner': '',
    }

    modified_priority_type = {
        'description': 'standard_text',
        'identifier': '/example/1/',
        'is_resolved': True,
        'priority_type': 3,
        'reason_type': 0,
        'owner': '',
    }
    missing_priority_type = {
        'description': 'standard_text',
        'identifier': '/example/1/',
        'is_resolved': True,
        'reason_type': 0,
        'owner': '',
    }

    missing_reason_type = {
        'description': 'standard_text',
        'identifier': '/example/1/',
        'is_resolved': True,
        'priority_type': 0,
        'owner': '',
    }
    modified_reason_type = {
        'description': 'standard_text',
        'identifier': '/example/1/',
        'is_resolved': True,
        'priority_type': 0,
        'reason_type': 3,
        'owner': '',
    }

    modified_owner = {
        'description': 'standard_text',
        'identifier': '/example/1/',
        'is_resolved': True,
        'priority_type': 0,
        'reason_type': 0,
        'owner': '',
    }
    missing_owner = {
        'description': 'standard_text',
        'identifier': '/example/1/',
        'is_resolved': True,
        'priority_type': 0,
        'reason_type': 0,
    }



class GroupReportTestData(AvaCoreTestData):
    """
    Test data for GroupReport
    """

    @staticmethod
    def init_requirements():
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if Group.objects.count() == 0:
            GroupTestData.init_requirements()
            model = Group.objects.create(**GroupTestData.get_data('standard'))
            model.save()
            model = Group.objects.create(**GroupTestData.get_data('unique'))
            model.save()

    # Store self information
    model = GroupReport
    url = '/example'

    standard = {
        'group': '/example/1/',
        'description': 'standard_text',
        'is_resolved': True,
        'priority_type': 0,
        'reason_type': 0,
        'owner': '',
    }

    unique = {
        'group': '/example/2/',
        'description': 'unique_text',
        'is_resolved': False,
        'priority_type': 3,
        'reason_type': 0,
        'owner': '',
    }

    modified_group = {
        'group': '/example/2/',
        'description': 'standard_text',
        'is_resolved': True,
        'priority_type': 0,
        'reason_type': 0,
        'owner': '',
    }
    missing_group = {
        'description': 'standard_text',
        'is_resolved': True,
        'priority_type': 0,
        'reason_type': 0,
        'owner': '',
    }

    modified_description = {
        'group': '/example/1/',
        'description': 'modified_text',
        'is_resolved': True,
        'priority_type': 0,
        'reason_type': 0,
        'owner': '',
    }
    missing_description = {
        'group': '/example/1/',
        'is_resolved': True,
        'priority_type': 0,
        'reason_type': 0,
        'owner': '',
    }

    missing_is_resolved = {
        'group': '/example/1/',
        'description': 'standard_text',
        'priority_type': 0,
        'reason_type': 0,
        'owner': '',
    }
    modified_is_resolved = {
        'group': '/example/1/',
        'description': 'standard_text',
        'is_resolved': False,
        'priority_type': 0,
        'reason_type': 0,
        'owner': '',
    }

    modified_priority_type = {
        'group': '/example/1/',
        'description': 'standard_text',
        'is_resolved': True,
        'priority_type': 3,
        'reason_type': 0,
        'owner': '',
    }
    missing_priority_type = {
        'group': '/example/1/',
        'description': 'standard_text',
        'is_resolved': True,
        'reason_type': 0,
        'owner': '',
    }

    missing_reason_type = {
        'group': '/example/1/',
        'description': 'standard_text',
        'is_resolved': True,
        'priority_type': 0,
        'owner': '',
    }
    modified_reason_type = {
        'group': '/example/1/',
        'description': 'standard_text',
        'is_resolved': True,
        'priority_type': 0,
        'reason_type': 0,
        'owner': '',
    }

    modified_owner = {
        'group': '/example/1/',
        'description': 'standard_text',
        'is_resolved': True,
        'priority_type': 0,
        'reason_type': 0,
        'owner': '',
    }
    missing_owner = {
        'group': '/example/1/',
        'description': 'standard_text',
        'is_resolved': True,
        'priority_type': 0,
        'reason_type': 0,
    }



class GroupIdentifierTestData(AvaCoreTestData):
    """
    Test data for GroupIdentifier
    """

    @staticmethod
    def init_requirements():
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if GroupIdentifierAttribute.objects.count() == 0:
            GroupIdentifierAttributeTestData.init_requirements()
            model = GroupIdentifierAttribute.objects.create(**GroupIdentifierAttributeTestData.get_data('standard'))
            model.save()
            model = GroupIdentifierAttribute.objects.create(**GroupIdentifierAttributeTestData.get_data('unique'))
            model.save()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if Group.objects.count() == 0:
            GroupTestData.init_requirements()
            model = Group.objects.create(**GroupTestData.get_data('standard'))
            model.save()
            model = Group.objects.create(**GroupTestData.get_data('unique'))
            model.save()

    # Store self information
    model = GroupIdentifier
    url = '/example'

    standard = {
        'groupidentifierattribute': '/example/1/',
        'belongs_to': '/example/1/',
        'primary_identifier': True,
        'identifier_type': 'EMAIL',
        'identifier': 'standard_char',
    }

    unique = {
        'groupidentifierattribute': '/example/2/',
        'belongs_to': '/example/2/',
        'primary_identifier': False,
        'identifier_type': 'SID',
        'identifier': 'unique_char',
    }

    missing_groupidentifierattribute = {
        'belongs_to': '/example/1/',
        'primary_identifier': True,
        'identifier_type': 'EMAIL',
        'identifier': 'standard_char',
    }
    modified_groupidentifierattribute = {
        'groupidentifierattribute': '/example/2/',
        'belongs_to': '/example/1/',
        'primary_identifier': True,
        'identifier_type': 'EMAIL',
        'identifier': 'standard_char',
    }

    modified_belongs_to = {
        'groupidentifierattribute': '/example/1/',
        'belongs_to': '/example/2/',
        'primary_identifier': True,
        'identifier_type': 'EMAIL',
        'identifier': 'standard_char',
    }
    missing_belongs_to = {
        'groupidentifierattribute': '/example/1/',
        'primary_identifier': True,
        'identifier_type': 'EMAIL',
        'identifier': 'standard_char',
    }

    missing_primary_identifier = {
        'groupidentifierattribute': '/example/1/',
        'belongs_to': '/example/1/',
        'identifier_type': 'EMAIL',
        'identifier': 'standard_char',
    }
    modified_primary_identifier = {
        'groupidentifierattribute': '/example/1/',
        'belongs_to': '/example/1/',
        'primary_identifier': False,
        'identifier_type': 'EMAIL',
        'identifier': 'standard_char',
    }

    modified_identifier_type = {
        'groupidentifierattribute': '/example/1/',
        'belongs_to': '/example/1/',
        'primary_identifier': True,
        'identifier_type': 'SID',
        'identifier': 'standard_char',
    }
    missing_identifier_type = {
        'groupidentifierattribute': '/example/1/',
        'belongs_to': '/example/1/',
        'primary_identifier': True,
        'identifier': 'standard_char',
    }

    missing_identifier = {
        'groupidentifierattribute': '/example/1/',
        'belongs_to': '/example/1/',
        'primary_identifier': True,
        'identifier_type': 'EMAIL',
    }
    modified_identifier = {
        'groupidentifierattribute': '/example/1/',
        'belongs_to': '/example/1/',
        'primary_identifier': True,
        'identifier_type': 'EMAIL',
        'identifier': 'modified_char',
    }



class GroupIdentifierAttributeTestData(AvaCoreTestData):
    """
    Test data for GroupIdentifierAttribute
    """

    @staticmethod
    def init_requirements():
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if GroupIdentifier.objects.count() == 0:
            GroupIdentifierTestData.init_requirements()
            model = GroupIdentifier.objects.create(**GroupIdentifierTestData.get_data('standard'))
            model.save()
            model = GroupIdentifier.objects.create(**GroupIdentifierTestData.get_data('unique'))
            model.save()

    # Store self information
    model = GroupIdentifierAttribute
    url = '/example'

    standard = {
        'ignore_type': 0,
        'identifier': '/example/1/',
    }

    unique = {
        'ignore_type': 1,
        'identifier': '/example/2/',
    }

    modified_ignore_type = {
        'ignore_type': 1,
        'identifier': '/example/1/',
    }
    missing_ignore_type = {
        'identifier': '/example/1/',
    }

    missing_identifier = {
        'ignore_type': 0,
    }
    modified_identifier = {
        'ignore_type': 0,
        'identifier': '/example/2/',
    }



class PersonIdentifierAttributeTestData(AvaCoreTestData):
    """
    Test data for PersonIdentifierAttribute
    """

    @staticmethod
    def init_requirements():
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if PersonIdentifier.objects.count() == 0:
            PersonIdentifierTestData.init_requirements()
            model = PersonIdentifier.objects.create(**PersonIdentifierTestData.get_data('standard'))
            model.save()
            model = PersonIdentifier.objects.create(**PersonIdentifierTestData.get_data('unique'))
            model.save()

    # Store self information
    model = PersonIdentifierAttribute
    url = '/example'

    standard = {
        'ignore_type': 0,
        'identifier': '/example/1/',
    }

    unique = {
        'ignore_type': 2,
        'identifier': '/example/2/',
    }

    modified_ignore_type = {
        'ignore_type': 2,
        'identifier': '/example/1/',
    }
    missing_ignore_type = {
        'identifier': '/example/1/',
    }

    missing_identifier = {
        'ignore_type': 0,
    }
    modified_identifier = {
        'ignore_type': 0,
        'identifier': '/example/2/',
    }



class PersonTestData(AvaCoreTestData):
    """
    Test data for Person
    """

    @staticmethod
    def init_requirements():
        # Import the required model and data
        from ava_core.evaluate.models import EvaluateTest
        from ava_core.evaluate.test_data import EvaluateTestTestData
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if EvaluateTest.objects.count() == 0:
            EvaluateTestTestData.init_requirements()
            model = EvaluateTest.objects.create(**EvaluateTestTestData.get_data('standard'))
            model.save()
            model = EvaluateTest.objects.create(**EvaluateTestTestData.get_data('unique'))
            model.save()

        # Import the required model and data
        from ava_core.my.models import People
        from ava_core.my.test_data import PeopleTestData
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if People.objects.count() == 0:
            PeopleTestData.init_requirements()
            model = People.objects.create(**PeopleTestData.get_data('standard'))
            model.save()
            model = People.objects.create(**PeopleTestData.get_data('unique'))
            model.save()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if PersonAttribute.objects.count() == 0:
            PersonAttributeTestData.init_requirements()
            model = PersonAttribute.objects.create(**PersonAttributeTestData.get_data('standard'))
            model.save()
            model = PersonAttribute.objects.create(**PersonAttributeTestData.get_data('unique'))
            model.save()

        # Import the required model and data
        from ava_core.evaluate.models import EvaluateController
        from ava_core.evaluate.test_data import EvaluateControllerTestData
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if EvaluateController.objects.count() == 0:
            EvaluateControllerTestData.init_requirements()
            model = EvaluateController.objects.create(**EvaluateControllerTestData.get_data('standard'))
            model.save()
            model = EvaluateController.objects.create(**EvaluateControllerTestData.get_data('unique'))
            model.save()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if Group.objects.count() == 0:
            GroupTestData.init_requirements()
            model = Group.objects.create(**GroupTestData.get_data('standard'))
            model.save()
            model = Group.objects.create(**GroupTestData.get_data('unique'))
            model.save()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if PersonIdentifier.objects.count() == 0:
            PersonIdentifierTestData.init_requirements()
            model = PersonIdentifier.objects.create(**PersonIdentifierTestData.get_data('standard'))
            model.save()
            model = PersonIdentifier.objects.create(**PersonIdentifierTestData.get_data('unique'))
            model.save()

    # Store self information
    model = Person
    url = '/example'

    standard = {
        'surname': 'standard_char',
        'evaluatetest': '/example/1/',
        'google_identity_data': 'default',
        'ldap_identity_data': 'default',
        'people': '/example/1/',
        'personattribute': '/example/1/',
        'evaluatecontroller': 'default',
        'groups': 'default',
        'person_ids': '/example/1/',
        'first_name': 'standard_char',
    }

    unique = {
        'surname': 'unique_char',
        'evaluatetest': '/example/2/',
        'google_identity_data': 'default',
        'ldap_identity_data': 'default',
        'people': '/example/2/',
        'personattribute': '/example/2/',
        'evaluatecontroller': 'default',
        'groups': 'default',
        'person_ids': '/example/2/',
        'first_name': 'unique_char',
    }

    modified_surname = {
        'surname': 'modified_char',
        'evaluatetest': '/example/1/',
        'google_identity_data': 'default',
        'ldap_identity_data': 'default',
        'people': '/example/1/',
        'personattribute': '/example/1/',
        'evaluatecontroller': 'default',
        'groups': 'default',
        'person_ids': '/example/1/',
        'first_name': 'standard_char',
    }
    missing_surname = {
        'evaluatetest': '/example/1/',
        'google_identity_data': 'default',
        'ldap_identity_data': 'default',
        'people': '/example/1/',
        'personattribute': '/example/1/',
        'evaluatecontroller': 'default',
        'groups': 'default',
        'person_ids': '/example/1/',
        'first_name': 'standard_char',
    }

    modified_evaluatetest = {
        'surname': 'standard_char',
        'evaluatetest': '/example/2/',
        'google_identity_data': 'default',
        'ldap_identity_data': 'default',
        'people': '/example/1/',
        'personattribute': '/example/1/',
        'evaluatecontroller': 'default',
        'groups': 'default',
        'person_ids': '/example/1/',
        'first_name': 'standard_char',
    }
    missing_evaluatetest = {
        'surname': 'standard_char',
        'google_identity_data': 'default',
        'ldap_identity_data': 'default',
        'people': '/example/1/',
        'personattribute': '/example/1/',
        'evaluatecontroller': 'default',
        'groups': 'default',
        'person_ids': '/example/1/',
        'first_name': 'standard_char',
    }

    modified_google_identity_data = {
        'surname': 'standard_char',
        'evaluatetest': '/example/1/',
        'google_identity_data': 'default',
        'ldap_identity_data': 'default',
        'people': '/example/1/',
        'personattribute': '/example/1/',
        'evaluatecontroller': 'default',
        'groups': 'default',
        'person_ids': '/example/1/',
        'first_name': 'standard_char',
    }
    missing_google_identity_data = {
        'surname': 'standard_char',
        'evaluatetest': '/example/1/',
        'ldap_identity_data': 'default',
        'people': '/example/1/',
        'personattribute': '/example/1/',
        'evaluatecontroller': 'default',
        'groups': 'default',
        'person_ids': '/example/1/',
        'first_name': 'standard_char',
    }

    modified_ldap_identity_data = {
        'surname': 'standard_char',
        'evaluatetest': '/example/1/',
        'google_identity_data': 'default',
        'ldap_identity_data': 'default',
        'people': '/example/1/',
        'personattribute': '/example/1/',
        'evaluatecontroller': 'default',
        'groups': 'default',
        'person_ids': '/example/1/',
        'first_name': 'standard_char',
    }
    missing_ldap_identity_data = {
        'surname': 'standard_char',
        'evaluatetest': '/example/1/',
        'google_identity_data': 'default',
        'people': '/example/1/',
        'personattribute': '/example/1/',
        'evaluatecontroller': 'default',
        'groups': 'default',
        'person_ids': '/example/1/',
        'first_name': 'standard_char',
    }

    modified_people = {
        'surname': 'standard_char',
        'evaluatetest': '/example/1/',
        'google_identity_data': 'default',
        'ldap_identity_data': 'default',
        'people': '/example/2/',
        'personattribute': '/example/1/',
        'evaluatecontroller': 'default',
        'groups': 'default',
        'person_ids': '/example/1/',
        'first_name': 'standard_char',
    }
    missing_people = {
        'surname': 'standard_char',
        'evaluatetest': '/example/1/',
        'google_identity_data': 'default',
        'ldap_identity_data': 'default',
        'personattribute': '/example/1/',
        'evaluatecontroller': 'default',
        'groups': 'default',
        'person_ids': '/example/1/',
        'first_name': 'standard_char',
    }

    missing_personattribute = {
        'surname': 'standard_char',
        'evaluatetest': '/example/1/',
        'google_identity_data': 'default',
        'ldap_identity_data': 'default',
        'people': '/example/1/',
        'evaluatecontroller': 'default',
        'groups': 'default',
        'person_ids': '/example/1/',
        'first_name': 'standard_char',
    }
    modified_personattribute = {
        'surname': 'standard_char',
        'evaluatetest': '/example/1/',
        'google_identity_data': 'default',
        'ldap_identity_data': 'default',
        'people': '/example/1/',
        'personattribute': '/example/2/',
        'evaluatecontroller': 'default',
        'groups': 'default',
        'person_ids': '/example/1/',
        'first_name': 'standard_char',
    }

    modified_evaluatecontroller = {
        'surname': 'standard_char',
        'evaluatetest': '/example/1/',
        'google_identity_data': 'default',
        'ldap_identity_data': 'default',
        'people': '/example/1/',
        'personattribute': '/example/1/',
        'evaluatecontroller': 'default',
        'groups': 'default',
        'person_ids': '/example/1/',
        'first_name': 'standard_char',
    }
    missing_evaluatecontroller = {
        'surname': 'standard_char',
        'evaluatetest': '/example/1/',
        'google_identity_data': 'default',
        'ldap_identity_data': 'default',
        'people': '/example/1/',
        'personattribute': '/example/1/',
        'groups': 'default',
        'person_ids': '/example/1/',
        'first_name': 'standard_char',
    }

    missing_groups = {
        'surname': 'standard_char',
        'evaluatetest': '/example/1/',
        'google_identity_data': 'default',
        'ldap_identity_data': 'default',
        'people': '/example/1/',
        'personattribute': '/example/1/',
        'evaluatecontroller': 'default',
        'person_ids': '/example/1/',
        'first_name': 'standard_char',
    }
    modified_groups = {
        'surname': 'standard_char',
        'evaluatetest': '/example/1/',
        'google_identity_data': 'default',
        'ldap_identity_data': 'default',
        'people': '/example/1/',
        'personattribute': '/example/1/',
        'evaluatecontroller': 'default',
        'groups': 'default',
        'person_ids': '/example/1/',
        'first_name': 'standard_char',
    }

    missing_person_ids = {
        'surname': 'standard_char',
        'evaluatetest': '/example/1/',
        'google_identity_data': 'default',
        'ldap_identity_data': 'default',
        'people': '/example/1/',
        'personattribute': '/example/1/',
        'evaluatecontroller': 'default',
        'groups': 'default',
        'first_name': 'standard_char',
    }
    modified_person_ids = {
        'surname': 'standard_char',
        'evaluatetest': '/example/1/',
        'google_identity_data': 'default',
        'ldap_identity_data': 'default',
        'people': '/example/1/',
        'personattribute': '/example/1/',
        'evaluatecontroller': 'default',
        'groups': 'default',
        'person_ids': '/example/2/',
        'first_name': 'standard_char',
    }

    missing_first_name = {
        'surname': 'standard_char',
        'evaluatetest': '/example/1/',
        'google_identity_data': 'default',
        'ldap_identity_data': 'default',
        'people': '/example/1/',
        'personattribute': '/example/1/',
        'evaluatecontroller': 'default',
        'groups': 'default',
        'person_ids': '/example/1/',
    }
    modified_first_name = {
        'surname': 'standard_char',
        'evaluatetest': '/example/1/',
        'google_identity_data': 'default',
        'ldap_identity_data': 'default',
        'people': '/example/1/',
        'personattribute': '/example/1/',
        'evaluatecontroller': 'default',
        'groups': 'default',
        'person_ids': '/example/1/',
        'first_name': 'modified_char',
    }



class PersonAttributeTestData(AvaCoreTestData):
    """
    Test data for PersonAttribute
    """

    @staticmethod
    def init_requirements():
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if Person.objects.count() == 0:
            PersonTestData.init_requirements()
            model = Person.objects.create(**PersonTestData.get_data('standard'))
            model.save()
            model = Person.objects.create(**PersonTestData.get_data('unique'))
            model.save()

    # Store self information
    model = PersonAttribute
    url = '/example'

    standard = {
        'person': '/example/1/',
        'non_human': True,
    }

    unique = {
        'person': '/example/2/',
        'non_human': False,
    }

    missing_person = {
        'non_human': True,
    }
    modified_person = {
        'person': '/example/2/',
        'non_human': True,
    }

    missing_non_human = {
        'person': '/example/1/',
    }
    modified_non_human = {
        'person': '/example/1/',
        'non_human': False,
    }



class PersonIdentifierTestData(AvaCoreTestData):
    """
    Test data for PersonIdentifier
    """

    @staticmethod
    def init_requirements():
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
        if PersonIdentifierReport.objects.count() == 0:
            PersonIdentifierReportTestData.init_requirements()
            model = PersonIdentifierReport.objects.create(**PersonIdentifierReportTestData.get_data('standard'))
            model.save()
            model = PersonIdentifierReport.objects.create(**PersonIdentifierReportTestData.get_data('unique'))
            model.save()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if PersonIdentifierAttribute.objects.count() == 0:
            PersonIdentifierAttributeTestData.init_requirements()
            model = PersonIdentifierAttribute.objects.create(**PersonIdentifierAttributeTestData.get_data('standard'))
            model.save()
            model = PersonIdentifierAttribute.objects.create(**PersonIdentifierAttributeTestData.get_data('unique'))
            model.save()

    # Store self information
    model = PersonIdentifier
    url = '/example'

    standard = {
        'belongs_to': '/example/1/',
        'identifier': 'standard_char',
        'personidentifierreport': '/example/1/',
        'personidentifierattribute': '/example/1/',
        'identifier_type': 'EMAIL',
        'primary_identifier': True,
    }

    unique = {
        'belongs_to': '/example/2/',
        'identifier': 'unique_char',
        'personidentifierreport': '/example/2/',
        'personidentifierattribute': '/example/2/',
        'identifier_type': 'SID',
        'primary_identifier': False,
    }

    modified_belongs_to = {
        'belongs_to': '/example/2/',
        'identifier': 'standard_char',
        'personidentifierreport': '/example/1/',
        'personidentifierattribute': '/example/1/',
        'identifier_type': 'EMAIL',
        'primary_identifier': True,
    }
    missing_belongs_to = {
        'identifier': 'standard_char',
        'personidentifierreport': '/example/1/',
        'personidentifierattribute': '/example/1/',
        'identifier_type': 'EMAIL',
        'primary_identifier': True,
    }

    missing_identifier = {
        'belongs_to': '/example/1/',
        'personidentifierreport': '/example/1/',
        'personidentifierattribute': '/example/1/',
        'identifier_type': 'EMAIL',
        'primary_identifier': True,
    }
    modified_identifier = {
        'belongs_to': '/example/1/',
        'identifier': 'modified_char',
        'personidentifierreport': '/example/1/',
        'personidentifierattribute': '/example/1/',
        'identifier_type': 'EMAIL',
        'primary_identifier': True,
    }

    modified_personidentifierreport = {
        'belongs_to': '/example/1/',
        'identifier': 'standard_char',
        'personidentifierreport': '/example/2/',
        'personidentifierattribute': '/example/1/',
        'identifier_type': 'EMAIL',
        'primary_identifier': True,
    }
    missing_personidentifierreport = {
        'belongs_to': '/example/1/',
        'identifier': 'standard_char',
        'personidentifierattribute': '/example/1/',
        'identifier_type': 'EMAIL',
        'primary_identifier': True,
    }

    modified_personidentifierattribute = {
        'belongs_to': '/example/1/',
        'identifier': 'standard_char',
        'personidentifierreport': '/example/1/',
        'personidentifierattribute': '/example/2/',
        'identifier_type': 'EMAIL',
        'primary_identifier': True,
    }
    missing_personidentifierattribute = {
        'belongs_to': '/example/1/',
        'identifier': 'standard_char',
        'personidentifierreport': '/example/1/',
        'identifier_type': 'EMAIL',
        'primary_identifier': True,
    }

    modified_identifier_type = {
        'belongs_to': '/example/1/',
        'identifier': 'standard_char',
        'personidentifierreport': '/example/1/',
        'personidentifierattribute': '/example/1/',
        'identifier_type': 'SID',
        'primary_identifier': True,
    }
    missing_identifier_type = {
        'belongs_to': '/example/1/',
        'identifier': 'standard_char',
        'personidentifierreport': '/example/1/',
        'personidentifierattribute': '/example/1/',
        'primary_identifier': True,
    }

    missing_primary_identifier = {
        'belongs_to': '/example/1/',
        'identifier': 'standard_char',
        'personidentifierreport': '/example/1/',
        'personidentifierattribute': '/example/1/',
        'identifier_type': 'EMAIL',
    }
    modified_primary_identifier = {
        'belongs_to': '/example/1/',
        'identifier': 'standard_char',
        'personidentifierreport': '/example/1/',
        'personidentifierattribute': '/example/1/',
        'identifier_type': 'EMAIL',
        'primary_identifier': False,
    }




