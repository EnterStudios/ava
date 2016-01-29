# Rest Imports
from rest_framework import status
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.organize.models import PersonIdentifierReport, PersonIdentifier, PersonIdentifierAttribute, Person, GroupIdentifierAttribute, GroupIdentifier, GroupReport, Group, PersonAttribute
from ava_core.evaluate.models import EvaluateController, EvaluateTest
from ava_core.evaluate.test_data import EvaluateControllerTestData, EvaluateTestTestData
from ava_core.my.models import People
from ava_core.my.test_data import PeopleTestData


# Implementation
class PersonIdentifierReportTestData(AvaCoreTestData):
    """
    Test data for PersonIdentifierReport
    """

    def __init__(self):
        # Store self information
        self.model = PersonIdentifierReport
        self.url = '/example'

        # Create any necessary required models.
        self.init_requirements()

    def init_requirements(self):
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if PersonIdentifier.objects.count() == 0:
            PersonIdentifierTestData.init_requirements()
            PersonIdentifier.objects.create(**PersonIdentifierTestData.get_data('standard'))
            PersonIdentifier.objects.create(**PersonIdentifierTestData.get_data('unique'))

    standard = {
        'description': 'standard_text',
        'reason_type': 0,
        'priority_type': 0,
        'is_resolved': True,
        'identifier': '/example/1/',
        'owner': '',
    }

    unique = {
        'description': 'unique_text',
        'reason_type': 3,
        'priority_type': 3,
        'is_resolved': False,
        'identifier': '/example/2/',
        'owner': '',
    }

    missing_description = {
        'reason_type': 0,
        'priority_type': 0,
        'is_resolved': True,
        'identifier': '/example/1/',
        'owner': '',
    }
    modified_description = {
        'description': 'modified_text',
        'reason_type': 0,
        'priority_type': 0,
        'is_resolved': True,
        'identifier': '/example/1/',
        'owner': '',
    }

    missing_reason_type = {
        'description': 'standard_text',
        'priority_type': 0,
        'is_resolved': True,
        'identifier': '/example/1/',
        'owner': '',
    }
    modified_reason_type = {
        'description': 'standard_text',
        'reason_type': 3,
        'priority_type': 0,
        'is_resolved': True,
        'identifier': '/example/1/',
        'owner': '',
    }

    missing_priority_type = {
        'description': 'standard_text',
        'reason_type': 0,
        'is_resolved': True,
        'identifier': '/example/1/',
        'owner': '',
    }
    modified_priority_type = {
        'description': 'standard_text',
        'reason_type': 0,
        'priority_type': 3,
        'is_resolved': True,
        'identifier': '/example/1/',
        'owner': '',
    }

    missing_is_resolved = {
        'description': 'standard_text',
        'reason_type': 0,
        'priority_type': 0,
        'identifier': '/example/1/',
        'owner': '',
    }
    modified_is_resolved = {
        'description': 'standard_text',
        'reason_type': 0,
        'priority_type': 0,
        'is_resolved': False,
        'identifier': '/example/1/',
        'owner': '',
    }

    modified_identifier = {
        'description': 'standard_text',
        'reason_type': 0,
        'priority_type': 0,
        'is_resolved': True,
        'identifier': '/example/2/',
        'owner': '',
    }
    missing_identifier = {
        'description': 'standard_text',
        'reason_type': 0,
        'priority_type': 0,
        'is_resolved': True,
        'owner': '',
    }

    modified_owner = {
        'description': 'standard_text',
        'reason_type': 0,
        'priority_type': 0,
        'is_resolved': True,
        'identifier': '/example/1/',
        'owner': '',
    }
    missing_owner = {
        'description': 'standard_text',
        'reason_type': 0,
        'priority_type': 0,
        'is_resolved': True,
        'identifier': '/example/1/',
    }



class PersonIdentifierTestData(AvaCoreTestData):
    """
    Test data for PersonIdentifier
    """

    def __init__(self):
        # Store self information
        self.model = PersonIdentifier
        self.url = '/example'

        # Create any necessary required models.
        self.init_requirements()

    def init_requirements(self):
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if PersonIdentifierAttribute.objects.count() == 0:
            PersonIdentifierAttributeTestData.init_requirements()
            PersonIdentifierAttribute.objects.create(**PersonIdentifierAttributeTestData.get_data('standard'))
            PersonIdentifierAttribute.objects.create(**PersonIdentifierAttributeTestData.get_data('unique'))
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if Person.objects.count() == 0:
            PersonTestData.init_requirements()
            Person.objects.create(**PersonTestData.get_data('standard'))
            Person.objects.create(**PersonTestData.get_data('unique'))
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if PersonIdentifierReport.objects.count() == 0:
            PersonIdentifierReportTestData.init_requirements()
            PersonIdentifierReport.objects.create(**PersonIdentifierReportTestData.get_data('standard'))
            PersonIdentifierReport.objects.create(**PersonIdentifierReportTestData.get_data('unique'))

    standard = {
        'identifier_type': 'EMAIL',
        'personidentifierattribute': '/example/1/',
        'belongs_to': '/example/1/',
        'primary_identifier': True,
        'identifier': 'standard_char',
        'personidentifierreport': '/example/1/',
    }

    unique = {
        'identifier_type': 'SID',
        'personidentifierattribute': '/example/2/',
        'belongs_to': '/example/2/',
        'primary_identifier': False,
        'identifier': 'unique_char',
        'personidentifierreport': '/example/2/',
    }

    modified_identifier_type = {
        'identifier_type': 'SID',
        'personidentifierattribute': '/example/1/',
        'belongs_to': '/example/1/',
        'primary_identifier': True,
        'identifier': 'standard_char',
        'personidentifierreport': '/example/1/',
    }
    missing_identifier_type = {
        'personidentifierattribute': '/example/1/',
        'belongs_to': '/example/1/',
        'primary_identifier': True,
        'identifier': 'standard_char',
        'personidentifierreport': '/example/1/',
    }

    missing_personidentifierattribute = {
        'identifier_type': 'EMAIL',
        'belongs_to': '/example/1/',
        'primary_identifier': True,
        'identifier': 'standard_char',
        'personidentifierreport': '/example/1/',
    }
    modified_personidentifierattribute = {
        'identifier_type': 'EMAIL',
        'personidentifierattribute': '/example/2/',
        'belongs_to': '/example/1/',
        'primary_identifier': True,
        'identifier': 'standard_char',
        'personidentifierreport': '/example/1/',
    }

    missing_belongs_to = {
        'identifier_type': 'EMAIL',
        'personidentifierattribute': '/example/1/',
        'primary_identifier': True,
        'identifier': 'standard_char',
        'personidentifierreport': '/example/1/',
    }
    modified_belongs_to = {
        'identifier_type': 'EMAIL',
        'personidentifierattribute': '/example/1/',
        'belongs_to': '/example/2/',
        'primary_identifier': True,
        'identifier': 'standard_char',
        'personidentifierreport': '/example/1/',
    }

    missing_primary_identifier = {
        'identifier_type': 'EMAIL',
        'personidentifierattribute': '/example/1/',
        'belongs_to': '/example/1/',
        'identifier': 'standard_char',
        'personidentifierreport': '/example/1/',
    }
    modified_primary_identifier = {
        'identifier_type': 'EMAIL',
        'personidentifierattribute': '/example/1/',
        'belongs_to': '/example/1/',
        'primary_identifier': False,
        'identifier': 'standard_char',
        'personidentifierreport': '/example/1/',
    }

    modified_identifier = {
        'identifier_type': 'EMAIL',
        'personidentifierattribute': '/example/1/',
        'belongs_to': '/example/1/',
        'primary_identifier': True,
        'identifier': 'modified_char',
        'personidentifierreport': '/example/1/',
    }
    missing_identifier = {
        'identifier_type': 'EMAIL',
        'personidentifierattribute': '/example/1/',
        'belongs_to': '/example/1/',
        'primary_identifier': True,
        'personidentifierreport': '/example/1/',
    }

    modified_personidentifierreport = {
        'identifier_type': 'EMAIL',
        'personidentifierattribute': '/example/1/',
        'belongs_to': '/example/1/',
        'primary_identifier': True,
        'identifier': 'standard_char',
        'personidentifierreport': '/example/2/',
    }
    missing_personidentifierreport = {
        'identifier_type': 'EMAIL',
        'personidentifierattribute': '/example/1/',
        'belongs_to': '/example/1/',
        'primary_identifier': True,
        'identifier': 'standard_char',
    }



class GroupIdentifierAttributeTestData(AvaCoreTestData):
    """
    Test data for GroupIdentifierAttribute
    """

    def __init__(self):
        # Store self information
        self.model = GroupIdentifierAttribute
        self.url = '/example'

        # Create any necessary required models.
        self.init_requirements()

    def init_requirements(self):
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if GroupIdentifier.objects.count() == 0:
            GroupIdentifierTestData.init_requirements()
            GroupIdentifier.objects.create(**GroupIdentifierTestData.get_data('standard'))
            GroupIdentifier.objects.create(**GroupIdentifierTestData.get_data('unique'))

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

    modified_identifier = {
        'ignore_type': 0,
        'identifier': '/example/2/',
    }
    missing_identifier = {
        'ignore_type': 0,
    }



class GroupReportTestData(AvaCoreTestData):
    """
    Test data for GroupReport
    """

    def __init__(self):
        # Store self information
        self.model = GroupReport
        self.url = '/example'

        # Create any necessary required models.
        self.init_requirements()

    def init_requirements(self):
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if Group.objects.count() == 0:
            GroupTestData.init_requirements()
            Group.objects.create(**GroupTestData.get_data('standard'))
            Group.objects.create(**GroupTestData.get_data('unique'))

    standard = {
        'description': 'standard_text',
        'reason_type': 0,
        'priority_type': 0,
        'is_resolved': True,
        'group': '/example/1/',
        'owner': '',
    }

    unique = {
        'description': 'unique_text',
        'reason_type': 0,
        'priority_type': 3,
        'is_resolved': False,
        'group': '/example/2/',
        'owner': '',
    }

    missing_description = {
        'reason_type': 0,
        'priority_type': 0,
        'is_resolved': True,
        'group': '/example/1/',
        'owner': '',
    }
    modified_description = {
        'description': 'modified_text',
        'reason_type': 0,
        'priority_type': 0,
        'is_resolved': True,
        'group': '/example/1/',
        'owner': '',
    }

    missing_reason_type = {
        'description': 'standard_text',
        'priority_type': 0,
        'is_resolved': True,
        'group': '/example/1/',
        'owner': '',
    }
    modified_reason_type = {
        'description': 'standard_text',
        'reason_type': 0,
        'priority_type': 0,
        'is_resolved': True,
        'group': '/example/1/',
        'owner': '',
    }

    missing_priority_type = {
        'description': 'standard_text',
        'reason_type': 0,
        'is_resolved': True,
        'group': '/example/1/',
        'owner': '',
    }
    modified_priority_type = {
        'description': 'standard_text',
        'reason_type': 0,
        'priority_type': 3,
        'is_resolved': True,
        'group': '/example/1/',
        'owner': '',
    }

    missing_is_resolved = {
        'description': 'standard_text',
        'reason_type': 0,
        'priority_type': 0,
        'group': '/example/1/',
        'owner': '',
    }
    modified_is_resolved = {
        'description': 'standard_text',
        'reason_type': 0,
        'priority_type': 0,
        'is_resolved': False,
        'group': '/example/1/',
        'owner': '',
    }

    modified_group = {
        'description': 'standard_text',
        'reason_type': 0,
        'priority_type': 0,
        'is_resolved': True,
        'group': '/example/2/',
        'owner': '',
    }
    missing_group = {
        'description': 'standard_text',
        'reason_type': 0,
        'priority_type': 0,
        'is_resolved': True,
        'owner': '',
    }

    modified_owner = {
        'description': 'standard_text',
        'reason_type': 0,
        'priority_type': 0,
        'is_resolved': True,
        'group': '/example/1/',
        'owner': '',
    }
    missing_owner = {
        'description': 'standard_text',
        'reason_type': 0,
        'priority_type': 0,
        'is_resolved': True,
        'group': '/example/1/',
    }



class PersonIdentifierAttributeTestData(AvaCoreTestData):
    """
    Test data for PersonIdentifierAttribute
    """

    def __init__(self):
        # Store self information
        self.model = PersonIdentifierAttribute
        self.url = '/example'

        # Create any necessary required models.
        self.init_requirements()

    def init_requirements(self):
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if PersonIdentifier.objects.count() == 0:
            PersonIdentifierTestData.init_requirements()
            PersonIdentifier.objects.create(**PersonIdentifierTestData.get_data('standard'))
            PersonIdentifier.objects.create(**PersonIdentifierTestData.get_data('unique'))

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

    modified_identifier = {
        'ignore_type': 0,
        'identifier': '/example/2/',
    }
    missing_identifier = {
        'ignore_type': 0,
    }



class GroupTestData(AvaCoreTestData):
    """
    Test data for Group
    """

    def __init__(self):
        # Store self information
        self.model = Group
        self.url = '/example'

        # Create any necessary required models.
        self.init_requirements()

    def init_requirements(self):
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if Group.objects.count() == 0:
            GroupTestData.init_requirements()
            Group.objects.create(**GroupTestData.get_data('standard'))
            Group.objects.create(**GroupTestData.get_data('unique'))
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if GroupIdentifier.objects.count() == 0:
            GroupIdentifierTestData.init_requirements()
            GroupIdentifier.objects.create(**GroupIdentifierTestData.get_data('standard'))
            GroupIdentifier.objects.create(**GroupIdentifierTestData.get_data('unique'))
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if Person.objects.count() == 0:
            PersonTestData.init_requirements()
            Person.objects.create(**PersonTestData.get_data('standard'))
            Person.objects.create(**PersonTestData.get_data('unique'))
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if GroupReport.objects.count() == 0:
            GroupReportTestData.init_requirements()
            GroupReport.objects.create(**GroupReportTestData.get_data('standard'))
            GroupReport.objects.create(**GroupReportTestData.get_data('unique'))
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if Group.objects.count() == 0:
            GroupTestData.init_requirements()
            Group.objects.create(**GroupTestData.get_data('standard'))
            Group.objects.create(**GroupTestData.get_data('unique'))

    standard = {
        'parent': '/example/1/',
        'google_group_data': 'default',
        'group_ids': '/example/1/',
        'description': 'standard_text',
        'members': 'default',
        'groupreport': '/example/1/',
        'ldap_group_data': 'default',
        'parent_group': '/example/1/',
        'group_type': 'ACTIVE DIRECTORY',
        'name': 'standard_char',
    }

    unique = {
        'parent': '/example/2/',
        'google_group_data': 'default',
        'group_ids': '/example/2/',
        'description': 'unique_text',
        'members': 'default',
        'groupreport': '/example/2/',
        'ldap_group_data': 'default',
        'parent_group': '/example/2/',
        'group_type': 'GOOGLE APPS',
        'name': 'unique_char',
    }

    missing_parent = {
        'google_group_data': 'default',
        'group_ids': '/example/1/',
        'description': 'standard_text',
        'members': 'default',
        'groupreport': '/example/1/',
        'ldap_group_data': 'default',
        'parent_group': '/example/1/',
        'group_type': 'ACTIVE DIRECTORY',
        'name': 'standard_char',
    }
    modified_parent = {
        'parent': '/example/2/',
        'google_group_data': 'default',
        'group_ids': '/example/1/',
        'description': 'standard_text',
        'members': 'default',
        'groupreport': '/example/1/',
        'ldap_group_data': 'default',
        'parent_group': '/example/1/',
        'group_type': 'ACTIVE DIRECTORY',
        'name': 'standard_char',
    }

    missing_google_group_data = {
        'parent': '/example/1/',
        'group_ids': '/example/1/',
        'description': 'standard_text',
        'members': 'default',
        'groupreport': '/example/1/',
        'ldap_group_data': 'default',
        'parent_group': '/example/1/',
        'group_type': 'ACTIVE DIRECTORY',
        'name': 'standard_char',
    }
    modified_google_group_data = {
        'parent': '/example/1/',
        'google_group_data': 'default',
        'group_ids': '/example/1/',
        'description': 'standard_text',
        'members': 'default',
        'groupreport': '/example/1/',
        'ldap_group_data': 'default',
        'parent_group': '/example/1/',
        'group_type': 'ACTIVE DIRECTORY',
        'name': 'standard_char',
    }

    missing_group_ids = {
        'parent': '/example/1/',
        'google_group_data': 'default',
        'description': 'standard_text',
        'members': 'default',
        'groupreport': '/example/1/',
        'ldap_group_data': 'default',
        'parent_group': '/example/1/',
        'group_type': 'ACTIVE DIRECTORY',
        'name': 'standard_char',
    }
    modified_group_ids = {
        'parent': '/example/1/',
        'google_group_data': 'default',
        'group_ids': '/example/2/',
        'description': 'standard_text',
        'members': 'default',
        'groupreport': '/example/1/',
        'ldap_group_data': 'default',
        'parent_group': '/example/1/',
        'group_type': 'ACTIVE DIRECTORY',
        'name': 'standard_char',
    }

    missing_description = {
        'parent': '/example/1/',
        'google_group_data': 'default',
        'group_ids': '/example/1/',
        'members': 'default',
        'groupreport': '/example/1/',
        'ldap_group_data': 'default',
        'parent_group': '/example/1/',
        'group_type': 'ACTIVE DIRECTORY',
        'name': 'standard_char',
    }
    modified_description = {
        'parent': '/example/1/',
        'google_group_data': 'default',
        'group_ids': '/example/1/',
        'description': 'modified_text',
        'members': 'default',
        'groupreport': '/example/1/',
        'ldap_group_data': 'default',
        'parent_group': '/example/1/',
        'group_type': 'ACTIVE DIRECTORY',
        'name': 'standard_char',
    }

    missing_members = {
        'parent': '/example/1/',
        'google_group_data': 'default',
        'group_ids': '/example/1/',
        'description': 'standard_text',
        'groupreport': '/example/1/',
        'ldap_group_data': 'default',
        'parent_group': '/example/1/',
        'group_type': 'ACTIVE DIRECTORY',
        'name': 'standard_char',
    }
    modified_members = {
        'parent': '/example/1/',
        'google_group_data': 'default',
        'group_ids': '/example/1/',
        'description': 'standard_text',
        'members': 'default',
        'groupreport': '/example/1/',
        'ldap_group_data': 'default',
        'parent_group': '/example/1/',
        'group_type': 'ACTIVE DIRECTORY',
        'name': 'standard_char',
    }

    modified_groupreport = {
        'parent': '/example/1/',
        'google_group_data': 'default',
        'group_ids': '/example/1/',
        'description': 'standard_text',
        'members': 'default',
        'groupreport': '/example/2/',
        'ldap_group_data': 'default',
        'parent_group': '/example/1/',
        'group_type': 'ACTIVE DIRECTORY',
        'name': 'standard_char',
    }
    missing_groupreport = {
        'parent': '/example/1/',
        'google_group_data': 'default',
        'group_ids': '/example/1/',
        'description': 'standard_text',
        'members': 'default',
        'ldap_group_data': 'default',
        'parent_group': '/example/1/',
        'group_type': 'ACTIVE DIRECTORY',
        'name': 'standard_char',
    }

    modified_ldap_group_data = {
        'parent': '/example/1/',
        'google_group_data': 'default',
        'group_ids': '/example/1/',
        'description': 'standard_text',
        'members': 'default',
        'groupreport': '/example/1/',
        'ldap_group_data': 'default',
        'parent_group': '/example/1/',
        'group_type': 'ACTIVE DIRECTORY',
        'name': 'standard_char',
    }
    missing_ldap_group_data = {
        'parent': '/example/1/',
        'google_group_data': 'default',
        'group_ids': '/example/1/',
        'description': 'standard_text',
        'members': 'default',
        'groupreport': '/example/1/',
        'parent_group': '/example/1/',
        'group_type': 'ACTIVE DIRECTORY',
        'name': 'standard_char',
    }

    modified_parent_group = {
        'parent': '/example/1/',
        'google_group_data': 'default',
        'group_ids': '/example/1/',
        'description': 'standard_text',
        'members': 'default',
        'groupreport': '/example/1/',
        'ldap_group_data': 'default',
        'parent_group': '/example/2/',
        'group_type': 'ACTIVE DIRECTORY',
        'name': 'standard_char',
    }
    missing_parent_group = {
        'parent': '/example/1/',
        'google_group_data': 'default',
        'group_ids': '/example/1/',
        'description': 'standard_text',
        'members': 'default',
        'groupreport': '/example/1/',
        'ldap_group_data': 'default',
        'group_type': 'ACTIVE DIRECTORY',
        'name': 'standard_char',
    }

    missing_group_type = {
        'parent': '/example/1/',
        'google_group_data': 'default',
        'group_ids': '/example/1/',
        'description': 'standard_text',
        'members': 'default',
        'groupreport': '/example/1/',
        'ldap_group_data': 'default',
        'parent_group': '/example/1/',
        'name': 'standard_char',
    }
    modified_group_type = {
        'parent': '/example/1/',
        'google_group_data': 'default',
        'group_ids': '/example/1/',
        'description': 'standard_text',
        'members': 'default',
        'groupreport': '/example/1/',
        'ldap_group_data': 'default',
        'parent_group': '/example/1/',
        'group_type': 'GOOGLE APPS',
        'name': 'standard_char',
    }

    modified_name = {
        'parent': '/example/1/',
        'google_group_data': 'default',
        'group_ids': '/example/1/',
        'description': 'standard_text',
        'members': 'default',
        'groupreport': '/example/1/',
        'ldap_group_data': 'default',
        'parent_group': '/example/1/',
        'group_type': 'ACTIVE DIRECTORY',
        'name': 'modified_char',
    }
    missing_name = {
        'parent': '/example/1/',
        'google_group_data': 'default',
        'group_ids': '/example/1/',
        'description': 'standard_text',
        'members': 'default',
        'groupreport': '/example/1/',
        'ldap_group_data': 'default',
        'parent_group': '/example/1/',
        'group_type': 'ACTIVE DIRECTORY',
    }



class GroupIdentifierTestData(AvaCoreTestData):
    """
    Test data for GroupIdentifier
    """

    def __init__(self):
        # Store self information
        self.model = GroupIdentifier
        self.url = '/example'

        # Create any necessary required models.
        self.init_requirements()

    def init_requirements(self):
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if Group.objects.count() == 0:
            GroupTestData.init_requirements()
            Group.objects.create(**GroupTestData.get_data('standard'))
            Group.objects.create(**GroupTestData.get_data('unique'))
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if GroupIdentifierAttribute.objects.count() == 0:
            GroupIdentifierAttributeTestData.init_requirements()
            GroupIdentifierAttribute.objects.create(**GroupIdentifierAttributeTestData.get_data('standard'))
            GroupIdentifierAttribute.objects.create(**GroupIdentifierAttributeTestData.get_data('unique'))

    standard = {
        'belongs_to': '/example/1/',
        'identifier_type': 'EMAIL',
        'primary_identifier': True,
        'groupidentifierattribute': '/example/1/',
        'identifier': 'standard_char',
    }

    unique = {
        'belongs_to': '/example/2/',
        'identifier_type': 'SID',
        'primary_identifier': False,
        'groupidentifierattribute': '/example/2/',
        'identifier': 'unique_char',
    }

    missing_belongs_to = {
        'identifier_type': 'EMAIL',
        'primary_identifier': True,
        'groupidentifierattribute': '/example/1/',
        'identifier': 'standard_char',
    }
    modified_belongs_to = {
        'belongs_to': '/example/2/',
        'identifier_type': 'EMAIL',
        'primary_identifier': True,
        'groupidentifierattribute': '/example/1/',
        'identifier': 'standard_char',
    }

    modified_identifier_type = {
        'belongs_to': '/example/1/',
        'identifier_type': 'SID',
        'primary_identifier': True,
        'groupidentifierattribute': '/example/1/',
        'identifier': 'standard_char',
    }
    missing_identifier_type = {
        'belongs_to': '/example/1/',
        'primary_identifier': True,
        'groupidentifierattribute': '/example/1/',
        'identifier': 'standard_char',
    }

    missing_primary_identifier = {
        'belongs_to': '/example/1/',
        'identifier_type': 'EMAIL',
        'groupidentifierattribute': '/example/1/',
        'identifier': 'standard_char',
    }
    modified_primary_identifier = {
        'belongs_to': '/example/1/',
        'identifier_type': 'EMAIL',
        'primary_identifier': False,
        'groupidentifierattribute': '/example/1/',
        'identifier': 'standard_char',
    }

    missing_groupidentifierattribute = {
        'belongs_to': '/example/1/',
        'identifier_type': 'EMAIL',
        'primary_identifier': True,
        'identifier': 'standard_char',
    }
    modified_groupidentifierattribute = {
        'belongs_to': '/example/1/',
        'identifier_type': 'EMAIL',
        'primary_identifier': True,
        'groupidentifierattribute': '/example/2/',
        'identifier': 'standard_char',
    }

    modified_identifier = {
        'belongs_to': '/example/1/',
        'identifier_type': 'EMAIL',
        'primary_identifier': True,
        'groupidentifierattribute': '/example/1/',
        'identifier': 'modified_char',
    }
    missing_identifier = {
        'belongs_to': '/example/1/',
        'identifier_type': 'EMAIL',
        'primary_identifier': True,
        'groupidentifierattribute': '/example/1/',
    }



class PersonTestData(AvaCoreTestData):
    """
    Test data for Person
    """

    def __init__(self):
        # Store self information
        self.model = Person
        self.url = '/example'

        # Create any necessary required models.
        self.init_requirements()

    def init_requirements(self):
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if PersonAttribute.objects.count() == 0:
            PersonAttributeTestData.init_requirements()
            PersonAttribute.objects.create(**PersonAttributeTestData.get_data('standard'))
            PersonAttribute.objects.create(**PersonAttributeTestData.get_data('unique'))
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if PersonIdentifier.objects.count() == 0:
            PersonIdentifierTestData.init_requirements()
            PersonIdentifier.objects.create(**PersonIdentifierTestData.get_data('standard'))
            PersonIdentifier.objects.create(**PersonIdentifierTestData.get_data('unique'))
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if People.objects.count() == 0:
            PeopleTestData.init_requirements()
            People.objects.create(**PeopleTestData.get_data('standard'))
            People.objects.create(**PeopleTestData.get_data('unique'))
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if EvaluateController.objects.count() == 0:
            EvaluateControllerTestData.init_requirements()
            EvaluateController.objects.create(**EvaluateControllerTestData.get_data('standard'))
            EvaluateController.objects.create(**EvaluateControllerTestData.get_data('unique'))
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if Group.objects.count() == 0:
            GroupTestData.init_requirements()
            Group.objects.create(**GroupTestData.get_data('standard'))
            Group.objects.create(**GroupTestData.get_data('unique'))
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if EvaluateTest.objects.count() == 0:
            EvaluateTestTestData.init_requirements()
            EvaluateTest.objects.create(**EvaluateTestTestData.get_data('standard'))
            EvaluateTest.objects.create(**EvaluateTestTestData.get_data('unique'))

    standard = {
        'google_identity_data': 'default',
        'ldap_identity_data': 'default',
        'personattribute': '/example/1/',
        'person_ids': '/example/1/',
        'people': '/example/1/',
        'first_name': 'standard_char',
        'evaluatecontroller': 'default',
        'groups': 'default',
        'evaluatetest': '/example/1/',
        'surname': 'standard_char',
    }

    unique = {
        'google_identity_data': 'default',
        'ldap_identity_data': 'default',
        'personattribute': '/example/2/',
        'person_ids': '/example/2/',
        'people': '/example/2/',
        'first_name': 'unique_char',
        'evaluatecontroller': 'default',
        'groups': 'default',
        'evaluatetest': '/example/2/',
        'surname': 'unique_char',
    }

    missing_google_identity_data = {
        'ldap_identity_data': 'default',
        'personattribute': '/example/1/',
        'person_ids': '/example/1/',
        'people': '/example/1/',
        'first_name': 'standard_char',
        'evaluatecontroller': 'default',
        'groups': 'default',
        'evaluatetest': '/example/1/',
        'surname': 'standard_char',
    }
    modified_google_identity_data = {
        'google_identity_data': 'default',
        'ldap_identity_data': 'default',
        'personattribute': '/example/1/',
        'person_ids': '/example/1/',
        'people': '/example/1/',
        'first_name': 'standard_char',
        'evaluatecontroller': 'default',
        'groups': 'default',
        'evaluatetest': '/example/1/',
        'surname': 'standard_char',
    }

    modified_ldap_identity_data = {
        'google_identity_data': 'default',
        'ldap_identity_data': 'default',
        'personattribute': '/example/1/',
        'person_ids': '/example/1/',
        'people': '/example/1/',
        'first_name': 'standard_char',
        'evaluatecontroller': 'default',
        'groups': 'default',
        'evaluatetest': '/example/1/',
        'surname': 'standard_char',
    }
    missing_ldap_identity_data = {
        'google_identity_data': 'default',
        'personattribute': '/example/1/',
        'person_ids': '/example/1/',
        'people': '/example/1/',
        'first_name': 'standard_char',
        'evaluatecontroller': 'default',
        'groups': 'default',
        'evaluatetest': '/example/1/',
        'surname': 'standard_char',
    }

    missing_personattribute = {
        'google_identity_data': 'default',
        'ldap_identity_data': 'default',
        'person_ids': '/example/1/',
        'people': '/example/1/',
        'first_name': 'standard_char',
        'evaluatecontroller': 'default',
        'groups': 'default',
        'evaluatetest': '/example/1/',
        'surname': 'standard_char',
    }
    modified_personattribute = {
        'google_identity_data': 'default',
        'ldap_identity_data': 'default',
        'personattribute': '/example/2/',
        'person_ids': '/example/1/',
        'people': '/example/1/',
        'first_name': 'standard_char',
        'evaluatecontroller': 'default',
        'groups': 'default',
        'evaluatetest': '/example/1/',
        'surname': 'standard_char',
    }

    modified_person_ids = {
        'google_identity_data': 'default',
        'ldap_identity_data': 'default',
        'personattribute': '/example/1/',
        'person_ids': '/example/2/',
        'people': '/example/1/',
        'first_name': 'standard_char',
        'evaluatecontroller': 'default',
        'groups': 'default',
        'evaluatetest': '/example/1/',
        'surname': 'standard_char',
    }
    missing_person_ids = {
        'google_identity_data': 'default',
        'ldap_identity_data': 'default',
        'personattribute': '/example/1/',
        'people': '/example/1/',
        'first_name': 'standard_char',
        'evaluatecontroller': 'default',
        'groups': 'default',
        'evaluatetest': '/example/1/',
        'surname': 'standard_char',
    }

    modified_people = {
        'google_identity_data': 'default',
        'ldap_identity_data': 'default',
        'personattribute': '/example/1/',
        'person_ids': '/example/1/',
        'people': '/example/2/',
        'first_name': 'standard_char',
        'evaluatecontroller': 'default',
        'groups': 'default',
        'evaluatetest': '/example/1/',
        'surname': 'standard_char',
    }
    missing_people = {
        'google_identity_data': 'default',
        'ldap_identity_data': 'default',
        'personattribute': '/example/1/',
        'person_ids': '/example/1/',
        'first_name': 'standard_char',
        'evaluatecontroller': 'default',
        'groups': 'default',
        'evaluatetest': '/example/1/',
        'surname': 'standard_char',
    }

    modified_first_name = {
        'google_identity_data': 'default',
        'ldap_identity_data': 'default',
        'personattribute': '/example/1/',
        'person_ids': '/example/1/',
        'people': '/example/1/',
        'first_name': 'modified_char',
        'evaluatecontroller': 'default',
        'groups': 'default',
        'evaluatetest': '/example/1/',
        'surname': 'standard_char',
    }
    missing_first_name = {
        'google_identity_data': 'default',
        'ldap_identity_data': 'default',
        'personattribute': '/example/1/',
        'person_ids': '/example/1/',
        'people': '/example/1/',
        'evaluatecontroller': 'default',
        'groups': 'default',
        'evaluatetest': '/example/1/',
        'surname': 'standard_char',
    }

    missing_evaluatecontroller = {
        'google_identity_data': 'default',
        'ldap_identity_data': 'default',
        'personattribute': '/example/1/',
        'person_ids': '/example/1/',
        'people': '/example/1/',
        'first_name': 'standard_char',
        'groups': 'default',
        'evaluatetest': '/example/1/',
        'surname': 'standard_char',
    }
    modified_evaluatecontroller = {
        'google_identity_data': 'default',
        'ldap_identity_data': 'default',
        'personattribute': '/example/1/',
        'person_ids': '/example/1/',
        'people': '/example/1/',
        'first_name': 'standard_char',
        'evaluatecontroller': 'default',
        'groups': 'default',
        'evaluatetest': '/example/1/',
        'surname': 'standard_char',
    }

    modified_groups = {
        'google_identity_data': 'default',
        'ldap_identity_data': 'default',
        'personattribute': '/example/1/',
        'person_ids': '/example/1/',
        'people': '/example/1/',
        'first_name': 'standard_char',
        'evaluatecontroller': 'default',
        'groups': 'default',
        'evaluatetest': '/example/1/',
        'surname': 'standard_char',
    }
    missing_groups = {
        'google_identity_data': 'default',
        'ldap_identity_data': 'default',
        'personattribute': '/example/1/',
        'person_ids': '/example/1/',
        'people': '/example/1/',
        'first_name': 'standard_char',
        'evaluatecontroller': 'default',
        'evaluatetest': '/example/1/',
        'surname': 'standard_char',
    }

    missing_evaluatetest = {
        'google_identity_data': 'default',
        'ldap_identity_data': 'default',
        'personattribute': '/example/1/',
        'person_ids': '/example/1/',
        'people': '/example/1/',
        'first_name': 'standard_char',
        'evaluatecontroller': 'default',
        'groups': 'default',
        'surname': 'standard_char',
    }
    modified_evaluatetest = {
        'google_identity_data': 'default',
        'ldap_identity_data': 'default',
        'personattribute': '/example/1/',
        'person_ids': '/example/1/',
        'people': '/example/1/',
        'first_name': 'standard_char',
        'evaluatecontroller': 'default',
        'groups': 'default',
        'evaluatetest': '/example/2/',
        'surname': 'standard_char',
    }

    modified_surname = {
        'google_identity_data': 'default',
        'ldap_identity_data': 'default',
        'personattribute': '/example/1/',
        'person_ids': '/example/1/',
        'people': '/example/1/',
        'first_name': 'standard_char',
        'evaluatecontroller': 'default',
        'groups': 'default',
        'evaluatetest': '/example/1/',
        'surname': 'modified_char',
    }
    missing_surname = {
        'google_identity_data': 'default',
        'ldap_identity_data': 'default',
        'personattribute': '/example/1/',
        'person_ids': '/example/1/',
        'people': '/example/1/',
        'first_name': 'standard_char',
        'evaluatecontroller': 'default',
        'groups': 'default',
        'evaluatetest': '/example/1/',
    }



class PersonAttributeTestData(AvaCoreTestData):
    """
    Test data for PersonAttribute
    """

    def __init__(self):
        # Store self information
        self.model = PersonAttribute
        self.url = '/example'

        # Create any necessary required models.
        self.init_requirements()

    def init_requirements(self):
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if Person.objects.count() == 0:
            PersonTestData.init_requirements()
            Person.objects.create(**PersonTestData.get_data('standard'))
            Person.objects.create(**PersonTestData.get_data('unique'))

    standard = {
        'person': '/example/1/',
        'non_human': True,
    }

    unique = {
        'person': '/example/2/',
        'non_human': False,
    }

    modified_person = {
        'person': '/example/2/',
        'non_human': True,
    }
    missing_person = {
        'non_human': True,
    }

    missing_non_human = {
        'person': '/example/1/',
    }
    modified_non_human = {
        'person': '/example/1/',
        'non_human': False,
    }




