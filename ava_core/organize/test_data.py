# Rest Imports
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.organize.models import GroupIdentifierAttribute, PersonIdentifierAttribute, GroupReport, \
    PersonIdentifierReport, Person, PersonAttribute, Group, GroupIdentifier, PersonIdentifier


# Implementation
class GroupIdentifierAttributeTestData(AvaCoreTestData):
    """
    Test data for GroupIdentifierAttribute
    """

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


class PersonIdentifierAttributeTestData(AvaCoreTestData):
    """
    Test data for PersonIdentifierAttribute
    """

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


class GroupReportTestData(AvaCoreTestData):
    """
    Test data for GroupReport
    """

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


class PersonIdentifierReportTestData(AvaCoreTestData):
    """
    Test data for PersonIdentifierReport
    """

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


class PersonTestData(AvaCoreTestData):
    """
    Test data for Person
    """

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


class PersonAttributeTestData(AvaCoreTestData):
    """
    Test data for PersonAttribute
    """

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


class GroupTestData(AvaCoreTestData):
    """
    Test data for Group
    """

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


class GroupIdentifierTestData(AvaCoreTestData):
    """
    Test data for GroupIdentifier
    """

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
    
class PersonIdentifierTestData(AvaCoreTestData):
    """
    Test data for PersonIdentifier
    """

    # Store self information
    model = PersonIdentifier
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


class PersonIdentifierTestData(AvaCoreTestData):
    """
    Test data for PersonIdentifier
    """

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
