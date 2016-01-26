# Rest Imports
# Local Imports
from ava_core.abstract.test_data import AvaTestData
from ava_core.organize.models import PersonIdentifier, Person, PersonIdentifierAttribute, GroupIdentifierAttribute, Group, GroupIdentifier, PersonAttribute, PersonIdentifierReport, GroupReport


# Implementation
class PersonIdentifierTestData(AvaTestData):
    """
    Test data for PersonIdentifier
    """

    model = PersonIdentifier
    url = '/example'

    standard = {
        'primary_identifier': True,
        'personidentifierattribute': 'REQUIRES: ava_core.organize.models.PersonIdentifierAttribute',
        'identifier_type': 'EMAIL',
        'belongs_to': 'REQUIRES: ava_core.organize.models.Person',
        'personidentifierreport': 'REQUIRES: ava_core.organize.models.PersonIdentifierReport',
        'identifier': 'standard_char',
    }

    modified = {
        'primary_identifier': True,
        'personidentifierattribute': 'REQUIRES: ava_core.organize.models.PersonIdentifierAttribute',
        'identifier_type': 'EMAIL',
        'belongs_to': 'REQUIRES: ava_core.organize.models.Person',
        'personidentifierreport': 'REQUIRES: ava_core.organize.models.PersonIdentifierReport',
        'identifier': 'standard_char',
    }

    missing_primary_identifier = {
        'personidentifierattribute': 'REQUIRES: ava_core.organize.models.PersonIdentifierAttribute',
        'identifier_type': 'EMAIL',
        'belongs_to': 'REQUIRES: ava_core.organize.models.Person',
        'personidentifierreport': 'REQUIRES: ava_core.organize.models.PersonIdentifierReport',
        'identifier': 'standard_char',
    }

    modified_primary_identifier = {
        'primary_identifier': False,
        'personidentifierattribute': 'REQUIRES: ava_core.organize.models.PersonIdentifierAttribute',
        'identifier_type': 'EMAIL',
        'belongs_to': 'REQUIRES: ava_core.organize.models.Person',
        'personidentifierreport': 'REQUIRES: ava_core.organize.models.PersonIdentifierReport',
        'identifier': 'standard_char',
    }

    missing_personidentifierattribute = {
        'primary_identifier': True,
        'identifier_type': 'EMAIL',
        'belongs_to': 'REQUIRES: ava_core.organize.models.Person',
        'personidentifierreport': 'REQUIRES: ava_core.organize.models.PersonIdentifierReport',
        'identifier': 'standard_char',
    }

    modified_personidentifierattribute = {
        'primary_identifier': True,
        'personidentifierattribute': 'REQUIRES: ava_core.organize.models.PersonIdentifierAttribute',
        'identifier_type': 'EMAIL',
        'belongs_to': 'REQUIRES: ava_core.organize.models.Person',
        'personidentifierreport': 'REQUIRES: ava_core.organize.models.PersonIdentifierReport',
        'identifier': 'standard_char',
    }

    modified_identifier_type = {
        'primary_identifier': True,
        'personidentifierattribute': 'REQUIRES: ava_core.organize.models.PersonIdentifierAttribute',
        'identifier_type': 'SID',
        'belongs_to': 'REQUIRES: ava_core.organize.models.Person',
        'personidentifierreport': 'REQUIRES: ava_core.organize.models.PersonIdentifierReport',
        'identifier': 'standard_char',
    }

    missing_identifier_type = {
        'primary_identifier': True,
        'personidentifierattribute': 'REQUIRES: ava_core.organize.models.PersonIdentifierAttribute',
        'belongs_to': 'REQUIRES: ava_core.organize.models.Person',
        'personidentifierreport': 'REQUIRES: ava_core.organize.models.PersonIdentifierReport',
        'identifier': 'standard_char',
    }

    modified_belongs_to = {
        'primary_identifier': True,
        'personidentifierattribute': 'REQUIRES: ava_core.organize.models.PersonIdentifierAttribute',
        'identifier_type': 'EMAIL',
        'belongs_to': 'REQUIRES: ava_core.organize.models.Person',
        'personidentifierreport': 'REQUIRES: ava_core.organize.models.PersonIdentifierReport',
        'identifier': 'standard_char',
    }

    missing_belongs_to = {
        'primary_identifier': True,
        'personidentifierattribute': 'REQUIRES: ava_core.organize.models.PersonIdentifierAttribute',
        'identifier_type': 'EMAIL',
        'personidentifierreport': 'REQUIRES: ava_core.organize.models.PersonIdentifierReport',
        'identifier': 'standard_char',
    }

    missing_personidentifierreport = {
        'primary_identifier': True,
        'personidentifierattribute': 'REQUIRES: ava_core.organize.models.PersonIdentifierAttribute',
        'identifier_type': 'EMAIL',
        'belongs_to': 'REQUIRES: ava_core.organize.models.Person',
        'identifier': 'standard_char',
    }

    modified_personidentifierreport = {
        'primary_identifier': True,
        'personidentifierattribute': 'REQUIRES: ava_core.organize.models.PersonIdentifierAttribute',
        'identifier_type': 'EMAIL',
        'belongs_to': 'REQUIRES: ava_core.organize.models.Person',
        'personidentifierreport': 'REQUIRES: ava_core.organize.models.PersonIdentifierReport',
        'identifier': 'standard_char',
    }

    modified_identifier = {
        'primary_identifier': True,
        'personidentifierattribute': 'REQUIRES: ava_core.organize.models.PersonIdentifierAttribute',
        'identifier_type': 'EMAIL',
        'belongs_to': 'REQUIRES: ava_core.organize.models.Person',
        'personidentifierreport': 'REQUIRES: ava_core.organize.models.PersonIdentifierReport',
        'identifier': 'modified_char',
    }

    missing_identifier = {
        'primary_identifier': True,
        'personidentifierattribute': 'REQUIRES: ava_core.organize.models.PersonIdentifierAttribute',
        'identifier_type': 'EMAIL',
        'belongs_to': 'REQUIRES: ava_core.organize.models.Person',
        'personidentifierreport': 'REQUIRES: ava_core.organize.models.PersonIdentifierReport',
    }



class PersonTestData(AvaTestData):
    """
    Test data for Person
    """

    model = Person
    url = '/example'

    standard = {
        'evaluatetest': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
        'first_name': 'standard_char',
        'evaluatecontroller': 'default',
        'surname': 'standard_char',
        'person_ids': 'REQUIRES: ava_core.organize.models.PersonIdentifier',
        'google_identity_data': 'default',
        'groups': 'default',
        'people': 'REQUIRES: ava_core.my.models.People',
        'ldap_identity_data': 'default',
        'personattribute': 'REQUIRES: ava_core.organize.models.PersonAttribute',
    }

    modified = {
        'evaluatetest': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
        'first_name': 'standard_char',
        'evaluatecontroller': 'default',
        'surname': 'standard_char',
        'person_ids': 'REQUIRES: ava_core.organize.models.PersonIdentifier',
        'google_identity_data': 'default',
        'groups': 'default',
        'people': 'REQUIRES: ava_core.my.models.People',
        'ldap_identity_data': 'default',
        'personattribute': 'REQUIRES: ava_core.organize.models.PersonAttribute',
    }

    missing_evaluatetest = {
        'first_name': 'standard_char',
        'evaluatecontroller': 'default',
        'surname': 'standard_char',
        'person_ids': 'REQUIRES: ava_core.organize.models.PersonIdentifier',
        'google_identity_data': 'default',
        'groups': 'default',
        'people': 'REQUIRES: ava_core.my.models.People',
        'ldap_identity_data': 'default',
        'personattribute': 'REQUIRES: ava_core.organize.models.PersonAttribute',
    }

    modified_evaluatetest = {
        'evaluatetest': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
        'first_name': 'standard_char',
        'evaluatecontroller': 'default',
        'surname': 'standard_char',
        'person_ids': 'REQUIRES: ava_core.organize.models.PersonIdentifier',
        'google_identity_data': 'default',
        'groups': 'default',
        'people': 'REQUIRES: ava_core.my.models.People',
        'ldap_identity_data': 'default',
        'personattribute': 'REQUIRES: ava_core.organize.models.PersonAttribute',
    }

    modified_first_name = {
        'evaluatetest': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
        'first_name': 'modified_char',
        'evaluatecontroller': 'default',
        'surname': 'standard_char',
        'person_ids': 'REQUIRES: ava_core.organize.models.PersonIdentifier',
        'google_identity_data': 'default',
        'groups': 'default',
        'people': 'REQUIRES: ava_core.my.models.People',
        'ldap_identity_data': 'default',
        'personattribute': 'REQUIRES: ava_core.organize.models.PersonAttribute',
    }

    missing_first_name = {
        'evaluatetest': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
        'evaluatecontroller': 'default',
        'surname': 'standard_char',
        'person_ids': 'REQUIRES: ava_core.organize.models.PersonIdentifier',
        'google_identity_data': 'default',
        'groups': 'default',
        'people': 'REQUIRES: ava_core.my.models.People',
        'ldap_identity_data': 'default',
        'personattribute': 'REQUIRES: ava_core.organize.models.PersonAttribute',
    }

    missing_evaluatecontroller = {
        'evaluatetest': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
        'first_name': 'standard_char',
        'surname': 'standard_char',
        'person_ids': 'REQUIRES: ava_core.organize.models.PersonIdentifier',
        'google_identity_data': 'default',
        'groups': 'default',
        'people': 'REQUIRES: ava_core.my.models.People',
        'ldap_identity_data': 'default',
        'personattribute': 'REQUIRES: ava_core.organize.models.PersonAttribute',
    }

    modified_evaluatecontroller = {
        'evaluatetest': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
        'first_name': 'standard_char',
        'evaluatecontroller': 'default',
        'surname': 'standard_char',
        'person_ids': 'REQUIRES: ava_core.organize.models.PersonIdentifier',
        'google_identity_data': 'default',
        'groups': 'default',
        'people': 'REQUIRES: ava_core.my.models.People',
        'ldap_identity_data': 'default',
        'personattribute': 'REQUIRES: ava_core.organize.models.PersonAttribute',
    }

    missing_surname = {
        'evaluatetest': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
        'first_name': 'standard_char',
        'evaluatecontroller': 'default',
        'person_ids': 'REQUIRES: ava_core.organize.models.PersonIdentifier',
        'google_identity_data': 'default',
        'groups': 'default',
        'people': 'REQUIRES: ava_core.my.models.People',
        'ldap_identity_data': 'default',
        'personattribute': 'REQUIRES: ava_core.organize.models.PersonAttribute',
    }

    modified_surname = {
        'evaluatetest': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
        'first_name': 'standard_char',
        'evaluatecontroller': 'default',
        'surname': 'modified_char',
        'person_ids': 'REQUIRES: ava_core.organize.models.PersonIdentifier',
        'google_identity_data': 'default',
        'groups': 'default',
        'people': 'REQUIRES: ava_core.my.models.People',
        'ldap_identity_data': 'default',
        'personattribute': 'REQUIRES: ava_core.organize.models.PersonAttribute',
    }

    modified_person_ids = {
        'evaluatetest': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
        'first_name': 'standard_char',
        'evaluatecontroller': 'default',
        'surname': 'standard_char',
        'person_ids': 'REQUIRES: ava_core.organize.models.PersonIdentifier',
        'google_identity_data': 'default',
        'groups': 'default',
        'people': 'REQUIRES: ava_core.my.models.People',
        'ldap_identity_data': 'default',
        'personattribute': 'REQUIRES: ava_core.organize.models.PersonAttribute',
    }

    missing_person_ids = {
        'evaluatetest': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
        'first_name': 'standard_char',
        'evaluatecontroller': 'default',
        'surname': 'standard_char',
        'google_identity_data': 'default',
        'groups': 'default',
        'people': 'REQUIRES: ava_core.my.models.People',
        'ldap_identity_data': 'default',
        'personattribute': 'REQUIRES: ava_core.organize.models.PersonAttribute',
    }

    missing_google_identity_data = {
        'evaluatetest': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
        'first_name': 'standard_char',
        'evaluatecontroller': 'default',
        'surname': 'standard_char',
        'person_ids': 'REQUIRES: ava_core.organize.models.PersonIdentifier',
        'groups': 'default',
        'people': 'REQUIRES: ava_core.my.models.People',
        'ldap_identity_data': 'default',
        'personattribute': 'REQUIRES: ava_core.organize.models.PersonAttribute',
    }

    modified_google_identity_data = {
        'evaluatetest': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
        'first_name': 'standard_char',
        'evaluatecontroller': 'default',
        'surname': 'standard_char',
        'person_ids': 'REQUIRES: ava_core.organize.models.PersonIdentifier',
        'google_identity_data': 'default',
        'groups': 'default',
        'people': 'REQUIRES: ava_core.my.models.People',
        'ldap_identity_data': 'default',
        'personattribute': 'REQUIRES: ava_core.organize.models.PersonAttribute',
    }

    modified_groups = {
        'evaluatetest': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
        'first_name': 'standard_char',
        'evaluatecontroller': 'default',
        'surname': 'standard_char',
        'person_ids': 'REQUIRES: ava_core.organize.models.PersonIdentifier',
        'google_identity_data': 'default',
        'groups': 'default',
        'people': 'REQUIRES: ava_core.my.models.People',
        'ldap_identity_data': 'default',
        'personattribute': 'REQUIRES: ava_core.organize.models.PersonAttribute',
    }

    missing_groups = {
        'evaluatetest': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
        'first_name': 'standard_char',
        'evaluatecontroller': 'default',
        'surname': 'standard_char',
        'person_ids': 'REQUIRES: ava_core.organize.models.PersonIdentifier',
        'google_identity_data': 'default',
        'people': 'REQUIRES: ava_core.my.models.People',
        'ldap_identity_data': 'default',
        'personattribute': 'REQUIRES: ava_core.organize.models.PersonAttribute',
    }

    missing_people = {
        'evaluatetest': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
        'first_name': 'standard_char',
        'evaluatecontroller': 'default',
        'surname': 'standard_char',
        'person_ids': 'REQUIRES: ava_core.organize.models.PersonIdentifier',
        'google_identity_data': 'default',
        'groups': 'default',
        'ldap_identity_data': 'default',
        'personattribute': 'REQUIRES: ava_core.organize.models.PersonAttribute',
    }

    modified_people = {
        'evaluatetest': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
        'first_name': 'standard_char',
        'evaluatecontroller': 'default',
        'surname': 'standard_char',
        'person_ids': 'REQUIRES: ava_core.organize.models.PersonIdentifier',
        'google_identity_data': 'default',
        'groups': 'default',
        'people': 'REQUIRES: ava_core.my.models.People',
        'ldap_identity_data': 'default',
        'personattribute': 'REQUIRES: ava_core.organize.models.PersonAttribute',
    }

    modified_ldap_identity_data = {
        'evaluatetest': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
        'first_name': 'standard_char',
        'evaluatecontroller': 'default',
        'surname': 'standard_char',
        'person_ids': 'REQUIRES: ava_core.organize.models.PersonIdentifier',
        'google_identity_data': 'default',
        'groups': 'default',
        'people': 'REQUIRES: ava_core.my.models.People',
        'ldap_identity_data': 'default',
        'personattribute': 'REQUIRES: ava_core.organize.models.PersonAttribute',
    }

    missing_ldap_identity_data = {
        'evaluatetest': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
        'first_name': 'standard_char',
        'evaluatecontroller': 'default',
        'surname': 'standard_char',
        'person_ids': 'REQUIRES: ava_core.organize.models.PersonIdentifier',
        'google_identity_data': 'default',
        'groups': 'default',
        'people': 'REQUIRES: ava_core.my.models.People',
        'personattribute': 'REQUIRES: ava_core.organize.models.PersonAttribute',
    }

    modified_personattribute = {
        'evaluatetest': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
        'first_name': 'standard_char',
        'evaluatecontroller': 'default',
        'surname': 'standard_char',
        'person_ids': 'REQUIRES: ava_core.organize.models.PersonIdentifier',
        'google_identity_data': 'default',
        'groups': 'default',
        'people': 'REQUIRES: ava_core.my.models.People',
        'ldap_identity_data': 'default',
        'personattribute': 'REQUIRES: ava_core.organize.models.PersonAttribute',
    }

    missing_personattribute = {
        'evaluatetest': 'REQUIRES: ava_core.evaluate.models.EvaluateTest',
        'first_name': 'standard_char',
        'evaluatecontroller': 'default',
        'surname': 'standard_char',
        'person_ids': 'REQUIRES: ava_core.organize.models.PersonIdentifier',
        'google_identity_data': 'default',
        'groups': 'default',
        'people': 'REQUIRES: ava_core.my.models.People',
        'ldap_identity_data': 'default',
    }



class PersonIdentifierAttributeTestData(AvaTestData):
    """
    Test data for PersonIdentifierAttribute
    """

    model = PersonIdentifierAttribute
    url = '/example'

    standard = {
        'ignore_type': 0,
        'identifier': 'REQUIRES: ava_core.organize.models.PersonIdentifier',
    }

    modified = {
        'ignore_type': 0,
        'identifier': 'REQUIRES: ava_core.organize.models.PersonIdentifier',
    }

    missing_ignore_type = {
        'identifier': 'REQUIRES: ava_core.organize.models.PersonIdentifier',
    }

    modified_ignore_type = {
        'ignore_type': 2,
        'identifier': 'REQUIRES: ava_core.organize.models.PersonIdentifier',
    }

    modified_identifier = {
        'ignore_type': 0,
        'identifier': 'REQUIRES: ava_core.organize.models.PersonIdentifier',
    }

    missing_identifier = {
        'ignore_type': 0,
    }



class GroupIdentifierAttributeTestData(AvaTestData):
    """
    Test data for GroupIdentifierAttribute
    """

    model = GroupIdentifierAttribute
    url = '/example'

    standard = {
        'ignore_type': 0,
        'identifier': 'REQUIRES: ava_core.organize.models.GroupIdentifier',
    }

    modified = {
        'ignore_type': 0,
        'identifier': 'REQUIRES: ava_core.organize.models.GroupIdentifier',
    }

    missing_ignore_type = {
        'identifier': 'REQUIRES: ava_core.organize.models.GroupIdentifier',
    }

    modified_ignore_type = {
        'ignore_type': 1,
        'identifier': 'REQUIRES: ava_core.organize.models.GroupIdentifier',
    }

    modified_identifier = {
        'ignore_type': 0,
        'identifier': 'REQUIRES: ava_core.organize.models.GroupIdentifier',
    }

    missing_identifier = {
        'ignore_type': 0,
    }



class GroupTestData(AvaTestData):
    """
    Test data for Group
    """

    model = Group
    url = '/example'

    standard = {
        'ldap_group_data': 'default',
        'group_ids': 'REQUIRES: ava_core.organize.models.GroupIdentifier',
        'members': 'default',
        'parent_group': 'REQUIRES: ava_core.organize.models.Group',
        'name': 'standard_char',
        'google_group_data': 'default',
        'description': 'standard_text',
        'parent': 'REQUIRES: ava_core.organize.models.Group',
        'groupreport': 'REQUIRES: ava_core.organize.models.GroupReport',
        'group_type': 'ACTIVE DIRECTORY',
    }

    modified = {
        'ldap_group_data': 'default',
        'group_ids': 'REQUIRES: ava_core.organize.models.GroupIdentifier',
        'members': 'default',
        'parent_group': 'REQUIRES: ava_core.organize.models.Group',
        'name': 'standard_char',
        'google_group_data': 'default',
        'description': 'standard_text',
        'parent': 'REQUIRES: ava_core.organize.models.Group',
        'groupreport': 'REQUIRES: ava_core.organize.models.GroupReport',
        'group_type': 'ACTIVE DIRECTORY',
    }

    missing_ldap_group_data = {
        'group_ids': 'REQUIRES: ava_core.organize.models.GroupIdentifier',
        'members': 'default',
        'parent_group': 'REQUIRES: ava_core.organize.models.Group',
        'name': 'standard_char',
        'google_group_data': 'default',
        'description': 'standard_text',
        'parent': 'REQUIRES: ava_core.organize.models.Group',
        'groupreport': 'REQUIRES: ava_core.organize.models.GroupReport',
        'group_type': 'ACTIVE DIRECTORY',
    }

    modified_ldap_group_data = {
        'ldap_group_data': 'default',
        'group_ids': 'REQUIRES: ava_core.organize.models.GroupIdentifier',
        'members': 'default',
        'parent_group': 'REQUIRES: ava_core.organize.models.Group',
        'name': 'standard_char',
        'google_group_data': 'default',
        'description': 'standard_text',
        'parent': 'REQUIRES: ava_core.organize.models.Group',
        'groupreport': 'REQUIRES: ava_core.organize.models.GroupReport',
        'group_type': 'ACTIVE DIRECTORY',
    }

    missing_group_ids = {
        'ldap_group_data': 'default',
        'members': 'default',
        'parent_group': 'REQUIRES: ava_core.organize.models.Group',
        'name': 'standard_char',
        'google_group_data': 'default',
        'description': 'standard_text',
        'parent': 'REQUIRES: ava_core.organize.models.Group',
        'groupreport': 'REQUIRES: ava_core.organize.models.GroupReport',
        'group_type': 'ACTIVE DIRECTORY',
    }

    modified_group_ids = {
        'ldap_group_data': 'default',
        'group_ids': 'REQUIRES: ava_core.organize.models.GroupIdentifier',
        'members': 'default',
        'parent_group': 'REQUIRES: ava_core.organize.models.Group',
        'name': 'standard_char',
        'google_group_data': 'default',
        'description': 'standard_text',
        'parent': 'REQUIRES: ava_core.organize.models.Group',
        'groupreport': 'REQUIRES: ava_core.organize.models.GroupReport',
        'group_type': 'ACTIVE DIRECTORY',
    }

    modified_members = {
        'ldap_group_data': 'default',
        'group_ids': 'REQUIRES: ava_core.organize.models.GroupIdentifier',
        'members': 'default',
        'parent_group': 'REQUIRES: ava_core.organize.models.Group',
        'name': 'standard_char',
        'google_group_data': 'default',
        'description': 'standard_text',
        'parent': 'REQUIRES: ava_core.organize.models.Group',
        'groupreport': 'REQUIRES: ava_core.organize.models.GroupReport',
        'group_type': 'ACTIVE DIRECTORY',
    }

    missing_members = {
        'ldap_group_data': 'default',
        'group_ids': 'REQUIRES: ava_core.organize.models.GroupIdentifier',
        'parent_group': 'REQUIRES: ava_core.organize.models.Group',
        'name': 'standard_char',
        'google_group_data': 'default',
        'description': 'standard_text',
        'parent': 'REQUIRES: ava_core.organize.models.Group',
        'groupreport': 'REQUIRES: ava_core.organize.models.GroupReport',
        'group_type': 'ACTIVE DIRECTORY',
    }

    missing_parent_group = {
        'ldap_group_data': 'default',
        'group_ids': 'REQUIRES: ava_core.organize.models.GroupIdentifier',
        'members': 'default',
        'name': 'standard_char',
        'google_group_data': 'default',
        'description': 'standard_text',
        'parent': 'REQUIRES: ava_core.organize.models.Group',
        'groupreport': 'REQUIRES: ava_core.organize.models.GroupReport',
        'group_type': 'ACTIVE DIRECTORY',
    }

    modified_parent_group = {
        'ldap_group_data': 'default',
        'group_ids': 'REQUIRES: ava_core.organize.models.GroupIdentifier',
        'members': 'default',
        'parent_group': 'REQUIRES: ava_core.organize.models.Group',
        'name': 'standard_char',
        'google_group_data': 'default',
        'description': 'standard_text',
        'parent': 'REQUIRES: ava_core.organize.models.Group',
        'groupreport': 'REQUIRES: ava_core.organize.models.GroupReport',
        'group_type': 'ACTIVE DIRECTORY',
    }

    modified_name = {
        'ldap_group_data': 'default',
        'group_ids': 'REQUIRES: ava_core.organize.models.GroupIdentifier',
        'members': 'default',
        'parent_group': 'REQUIRES: ava_core.organize.models.Group',
        'name': 'modified_char',
        'google_group_data': 'default',
        'description': 'standard_text',
        'parent': 'REQUIRES: ava_core.organize.models.Group',
        'groupreport': 'REQUIRES: ava_core.organize.models.GroupReport',
        'group_type': 'ACTIVE DIRECTORY',
    }

    missing_name = {
        'ldap_group_data': 'default',
        'group_ids': 'REQUIRES: ava_core.organize.models.GroupIdentifier',
        'members': 'default',
        'parent_group': 'REQUIRES: ava_core.organize.models.Group',
        'google_group_data': 'default',
        'description': 'standard_text',
        'parent': 'REQUIRES: ava_core.organize.models.Group',
        'groupreport': 'REQUIRES: ava_core.organize.models.GroupReport',
        'group_type': 'ACTIVE DIRECTORY',
    }

    modified_google_group_data = {
        'ldap_group_data': 'default',
        'group_ids': 'REQUIRES: ava_core.organize.models.GroupIdentifier',
        'members': 'default',
        'parent_group': 'REQUIRES: ava_core.organize.models.Group',
        'name': 'standard_char',
        'google_group_data': 'default',
        'description': 'standard_text',
        'parent': 'REQUIRES: ava_core.organize.models.Group',
        'groupreport': 'REQUIRES: ava_core.organize.models.GroupReport',
        'group_type': 'ACTIVE DIRECTORY',
    }

    missing_google_group_data = {
        'ldap_group_data': 'default',
        'group_ids': 'REQUIRES: ava_core.organize.models.GroupIdentifier',
        'members': 'default',
        'parent_group': 'REQUIRES: ava_core.organize.models.Group',
        'name': 'standard_char',
        'description': 'standard_text',
        'parent': 'REQUIRES: ava_core.organize.models.Group',
        'groupreport': 'REQUIRES: ava_core.organize.models.GroupReport',
        'group_type': 'ACTIVE DIRECTORY',
    }

    modified_description = {
        'ldap_group_data': 'default',
        'group_ids': 'REQUIRES: ava_core.organize.models.GroupIdentifier',
        'members': 'default',
        'parent_group': 'REQUIRES: ava_core.organize.models.Group',
        'name': 'standard_char',
        'google_group_data': 'default',
        'description': 'modified_text',
        'parent': 'REQUIRES: ava_core.organize.models.Group',
        'groupreport': 'REQUIRES: ava_core.organize.models.GroupReport',
        'group_type': 'ACTIVE DIRECTORY',
    }

    missing_description = {
        'ldap_group_data': 'default',
        'group_ids': 'REQUIRES: ava_core.organize.models.GroupIdentifier',
        'members': 'default',
        'parent_group': 'REQUIRES: ava_core.organize.models.Group',
        'name': 'standard_char',
        'google_group_data': 'default',
        'parent': 'REQUIRES: ava_core.organize.models.Group',
        'groupreport': 'REQUIRES: ava_core.organize.models.GroupReport',
        'group_type': 'ACTIVE DIRECTORY',
    }

    modified_parent = {
        'ldap_group_data': 'default',
        'group_ids': 'REQUIRES: ava_core.organize.models.GroupIdentifier',
        'members': 'default',
        'parent_group': 'REQUIRES: ava_core.organize.models.Group',
        'name': 'standard_char',
        'google_group_data': 'default',
        'description': 'standard_text',
        'parent': 'REQUIRES: ava_core.organize.models.Group',
        'groupreport': 'REQUIRES: ava_core.organize.models.GroupReport',
        'group_type': 'ACTIVE DIRECTORY',
    }

    missing_parent = {
        'ldap_group_data': 'default',
        'group_ids': 'REQUIRES: ava_core.organize.models.GroupIdentifier',
        'members': 'default',
        'parent_group': 'REQUIRES: ava_core.organize.models.Group',
        'name': 'standard_char',
        'google_group_data': 'default',
        'description': 'standard_text',
        'groupreport': 'REQUIRES: ava_core.organize.models.GroupReport',
        'group_type': 'ACTIVE DIRECTORY',
    }

    missing_groupreport = {
        'ldap_group_data': 'default',
        'group_ids': 'REQUIRES: ava_core.organize.models.GroupIdentifier',
        'members': 'default',
        'parent_group': 'REQUIRES: ava_core.organize.models.Group',
        'name': 'standard_char',
        'google_group_data': 'default',
        'description': 'standard_text',
        'parent': 'REQUIRES: ava_core.organize.models.Group',
        'group_type': 'ACTIVE DIRECTORY',
    }

    modified_groupreport = {
        'ldap_group_data': 'default',
        'group_ids': 'REQUIRES: ava_core.organize.models.GroupIdentifier',
        'members': 'default',
        'parent_group': 'REQUIRES: ava_core.organize.models.Group',
        'name': 'standard_char',
        'google_group_data': 'default',
        'description': 'standard_text',
        'parent': 'REQUIRES: ava_core.organize.models.Group',
        'groupreport': 'REQUIRES: ava_core.organize.models.GroupReport',
        'group_type': 'ACTIVE DIRECTORY',
    }

    modified_group_type = {
        'ldap_group_data': 'default',
        'group_ids': 'REQUIRES: ava_core.organize.models.GroupIdentifier',
        'members': 'default',
        'parent_group': 'REQUIRES: ava_core.organize.models.Group',
        'name': 'standard_char',
        'google_group_data': 'default',
        'description': 'standard_text',
        'parent': 'REQUIRES: ava_core.organize.models.Group',
        'groupreport': 'REQUIRES: ava_core.organize.models.GroupReport',
        'group_type': 'GOOGLE APPS',
    }

    missing_group_type = {
        'ldap_group_data': 'default',
        'group_ids': 'REQUIRES: ava_core.organize.models.GroupIdentifier',
        'members': 'default',
        'parent_group': 'REQUIRES: ava_core.organize.models.Group',
        'name': 'standard_char',
        'google_group_data': 'default',
        'description': 'standard_text',
        'parent': 'REQUIRES: ava_core.organize.models.Group',
        'groupreport': 'REQUIRES: ava_core.organize.models.GroupReport',
    }



class GroupIdentifierTestData(AvaTestData):
    """
    Test data for GroupIdentifier
    """

    model = GroupIdentifier
    url = '/example'

    standard = {
        'identifier_type': 'EMAIL',
        'belongs_to': 'REQUIRES: ava_core.organize.models.Group',
        'groupidentifierattribute': 'REQUIRES: ava_core.organize.models.GroupIdentifierAttribute',
        'primary_identifier': True,
        'identifier': 'standard_char',
    }

    modified = {
        'identifier_type': 'EMAIL',
        'belongs_to': 'REQUIRES: ava_core.organize.models.Group',
        'groupidentifierattribute': 'REQUIRES: ava_core.organize.models.GroupIdentifierAttribute',
        'primary_identifier': True,
        'identifier': 'standard_char',
    }

    modified_identifier_type = {
        'identifier_type': 'SID',
        'belongs_to': 'REQUIRES: ava_core.organize.models.Group',
        'groupidentifierattribute': 'REQUIRES: ava_core.organize.models.GroupIdentifierAttribute',
        'primary_identifier': True,
        'identifier': 'standard_char',
    }

    missing_identifier_type = {
        'belongs_to': 'REQUIRES: ava_core.organize.models.Group',
        'groupidentifierattribute': 'REQUIRES: ava_core.organize.models.GroupIdentifierAttribute',
        'primary_identifier': True,
        'identifier': 'standard_char',
    }

    modified_belongs_to = {
        'identifier_type': 'EMAIL',
        'belongs_to': 'REQUIRES: ava_core.organize.models.Group',
        'groupidentifierattribute': 'REQUIRES: ava_core.organize.models.GroupIdentifierAttribute',
        'primary_identifier': True,
        'identifier': 'standard_char',
    }

    missing_belongs_to = {
        'identifier_type': 'EMAIL',
        'groupidentifierattribute': 'REQUIRES: ava_core.organize.models.GroupIdentifierAttribute',
        'primary_identifier': True,
        'identifier': 'standard_char',
    }

    modified_groupidentifierattribute = {
        'identifier_type': 'EMAIL',
        'belongs_to': 'REQUIRES: ava_core.organize.models.Group',
        'groupidentifierattribute': 'REQUIRES: ava_core.organize.models.GroupIdentifierAttribute',
        'primary_identifier': True,
        'identifier': 'standard_char',
    }

    missing_groupidentifierattribute = {
        'identifier_type': 'EMAIL',
        'belongs_to': 'REQUIRES: ava_core.organize.models.Group',
        'primary_identifier': True,
        'identifier': 'standard_char',
    }

    missing_primary_identifier = {
        'identifier_type': 'EMAIL',
        'belongs_to': 'REQUIRES: ava_core.organize.models.Group',
        'groupidentifierattribute': 'REQUIRES: ava_core.organize.models.GroupIdentifierAttribute',
        'identifier': 'standard_char',
    }

    modified_primary_identifier = {
        'identifier_type': 'EMAIL',
        'belongs_to': 'REQUIRES: ava_core.organize.models.Group',
        'groupidentifierattribute': 'REQUIRES: ava_core.organize.models.GroupIdentifierAttribute',
        'primary_identifier': False,
        'identifier': 'standard_char',
    }

    modified_identifier = {
        'identifier_type': 'EMAIL',
        'belongs_to': 'REQUIRES: ava_core.organize.models.Group',
        'groupidentifierattribute': 'REQUIRES: ava_core.organize.models.GroupIdentifierAttribute',
        'primary_identifier': True,
        'identifier': 'modified_char',
    }

    missing_identifier = {
        'identifier_type': 'EMAIL',
        'belongs_to': 'REQUIRES: ava_core.organize.models.Group',
        'groupidentifierattribute': 'REQUIRES: ava_core.organize.models.GroupIdentifierAttribute',
        'primary_identifier': True,
    }



class PersonAttributeTestData(AvaTestData):
    """
    Test data for PersonAttribute
    """

    model = PersonAttribute
    url = '/example'

    standard = {
        'non_human': True,
        'person': 'REQUIRES: ava_core.organize.models.Person',
    }

    modified = {
        'non_human': True,
        'person': 'REQUIRES: ava_core.organize.models.Person',
    }

    modified_non_human = {
        'non_human': False,
        'person': 'REQUIRES: ava_core.organize.models.Person',
    }

    missing_non_human = {
        'person': 'REQUIRES: ava_core.organize.models.Person',
    }

    modified_person = {
        'non_human': True,
        'person': 'REQUIRES: ava_core.organize.models.Person',
    }

    missing_person = {
        'non_human': True,
    }



class PersonIdentifierReportTestData(AvaTestData):
    """
    Test data for PersonIdentifierReport
    """

    model = PersonIdentifierReport
    url = '/example'

    standard = {
        'is_resolved': True,
        'reason_type': 0,
        'description': 'standard_text',
        'identifier': 'REQUIRES: ava_core.organize.models.PersonIdentifier',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'priority_type': 0,
    }

    modified = {
        'is_resolved': True,
        'reason_type': 0,
        'description': 'standard_text',
        'identifier': 'REQUIRES: ava_core.organize.models.PersonIdentifier',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'priority_type': 0,
    }

    modified_is_resolved = {
        'is_resolved': False,
        'reason_type': 0,
        'description': 'standard_text',
        'identifier': 'REQUIRES: ava_core.organize.models.PersonIdentifier',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'priority_type': 0,
    }

    missing_is_resolved = {
        'reason_type': 0,
        'description': 'standard_text',
        'identifier': 'REQUIRES: ava_core.organize.models.PersonIdentifier',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'priority_type': 0,
    }

    modified_reason_type = {
        'is_resolved': True,
        'reason_type': 3,
        'description': 'standard_text',
        'identifier': 'REQUIRES: ava_core.organize.models.PersonIdentifier',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'priority_type': 0,
    }

    missing_reason_type = {
        'is_resolved': True,
        'description': 'standard_text',
        'identifier': 'REQUIRES: ava_core.organize.models.PersonIdentifier',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'priority_type': 0,
    }

    modified_description = {
        'is_resolved': True,
        'reason_type': 0,
        'description': 'modified_text',
        'identifier': 'REQUIRES: ava_core.organize.models.PersonIdentifier',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'priority_type': 0,
    }

    missing_description = {
        'is_resolved': True,
        'reason_type': 0,
        'identifier': 'REQUIRES: ava_core.organize.models.PersonIdentifier',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'priority_type': 0,
    }

    modified_identifier = {
        'is_resolved': True,
        'reason_type': 0,
        'description': 'standard_text',
        'identifier': 'REQUIRES: ava_core.organize.models.PersonIdentifier',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'priority_type': 0,
    }

    missing_identifier = {
        'is_resolved': True,
        'reason_type': 0,
        'description': 'standard_text',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'priority_type': 0,
    }

    missing_owner = {
        'is_resolved': True,
        'reason_type': 0,
        'description': 'standard_text',
        'identifier': 'REQUIRES: ava_core.organize.models.PersonIdentifier',
        'priority_type': 0,
    }

    modified_owner = {
        'is_resolved': True,
        'reason_type': 0,
        'description': 'standard_text',
        'identifier': 'REQUIRES: ava_core.organize.models.PersonIdentifier',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'priority_type': 0,
    }

    missing_priority_type = {
        'is_resolved': True,
        'reason_type': 0,
        'description': 'standard_text',
        'identifier': 'REQUIRES: ava_core.organize.models.PersonIdentifier',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
    }

    modified_priority_type = {
        'is_resolved': True,
        'reason_type': 0,
        'description': 'standard_text',
        'identifier': 'REQUIRES: ava_core.organize.models.PersonIdentifier',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'priority_type': 3,
    }



class GroupReportTestData(AvaTestData):
    """
    Test data for GroupReport
    """

    model = GroupReport
    url = '/example'

    standard = {
        'is_resolved': True,
        'group': 'REQUIRES: ava_core.organize.models.Group',
        'description': 'standard_text',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'priority_type': 0,
        'reason_type': 0,
    }

    modified = {
        'is_resolved': True,
        'group': 'REQUIRES: ava_core.organize.models.Group',
        'description': 'standard_text',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'priority_type': 0,
        'reason_type': 0,
    }

    modified_is_resolved = {
        'is_resolved': False,
        'group': 'REQUIRES: ava_core.organize.models.Group',
        'description': 'standard_text',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'priority_type': 0,
        'reason_type': 0,
    }

    missing_is_resolved = {
        'group': 'REQUIRES: ava_core.organize.models.Group',
        'description': 'standard_text',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'priority_type': 0,
        'reason_type': 0,
    }

    missing_group = {
        'is_resolved': True,
        'description': 'standard_text',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'priority_type': 0,
        'reason_type': 0,
    }

    modified_group = {
        'is_resolved': True,
        'group': 'REQUIRES: ava_core.organize.models.Group',
        'description': 'standard_text',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'priority_type': 0,
        'reason_type': 0,
    }

    modified_description = {
        'is_resolved': True,
        'group': 'REQUIRES: ava_core.organize.models.Group',
        'description': 'modified_text',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'priority_type': 0,
        'reason_type': 0,
    }

    missing_description = {
        'is_resolved': True,
        'group': 'REQUIRES: ava_core.organize.models.Group',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'priority_type': 0,
        'reason_type': 0,
    }

    missing_owner = {
        'is_resolved': True,
        'group': 'REQUIRES: ava_core.organize.models.Group',
        'description': 'standard_text',
        'priority_type': 0,
        'reason_type': 0,
    }

    modified_owner = {
        'is_resolved': True,
        'group': 'REQUIRES: ava_core.organize.models.Group',
        'description': 'standard_text',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'priority_type': 0,
        'reason_type': 0,
    }

    missing_priority_type = {
        'is_resolved': True,
        'group': 'REQUIRES: ava_core.organize.models.Group',
        'description': 'standard_text',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'reason_type': 0,
    }

    modified_priority_type = {
        'is_resolved': True,
        'group': 'REQUIRES: ava_core.organize.models.Group',
        'description': 'standard_text',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'priority_type': 3,
        'reason_type': 0,
    }

    modified_reason_type = {
        'is_resolved': True,
        'group': 'REQUIRES: ava_core.organize.models.Group',
        'description': 'standard_text',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'priority_type': 0,
        'reason_type': 0,
    }

    missing_reason_type = {
        'is_resolved': True,
        'group': 'REQUIRES: ava_core.organize.models.Group',
        'description': 'standard_text',
        'owner': 'REQUIRES: django.contrib.auth.models.User',
        'priority_type': 0,
    }




