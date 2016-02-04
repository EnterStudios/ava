# Rest Imports
from rest_framework import status
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.gather.gather_abstract.models import GatherHistory


# Implementation
class GatherHistoryTestData(AvaCoreTestData):
    """
    Test data for GatherHistory
    """

    @staticmethod
    def init_requirements():
        # Import the required model and data
        from ava_core.gather.gather_google.models import GoogleGatherHistory
        from ava_core.gather.gather_google.test_data import GoogleGatherHistoryTestData
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if GoogleGatherHistory.objects.count() == 0:
            GoogleGatherHistoryTestData.init_requirements()
            model = GoogleGatherHistory.objects.create(**GoogleGatherHistoryTestData.get_data('standard'))
            model.save()
            model = GoogleGatherHistory.objects.create(**GoogleGatherHistoryTestData.get_data('unique'))
            model.save()

        # Import the required model and data
        from ava_core.gather.gather_ldap.models import LDAPGatherHistory
        from ava_core.gather.gather_ldap.test_data import LDAPGatherHistoryTestData
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if LDAPGatherHistory.objects.count() == 0:
            LDAPGatherHistoryTestData.init_requirements()
            model = LDAPGatherHistory.objects.create(**LDAPGatherHistoryTestData.get_data('standard'))
            model.save()
            model = LDAPGatherHistory.objects.create(**LDAPGatherHistoryTestData.get_data('unique'))
            model.save()

        # Import the required model and data
        from ava_core.gather.gather_office365.models import Office365GatherHistory
        from ava_core.gather.gather_office365.test_data import Office365GatherHistoryTestData
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if Office365GatherHistory.objects.count() == 0:
            Office365GatherHistoryTestData.init_requirements()
            model = Office365GatherHistory.objects.create(**Office365GatherHistoryTestData.get_data('standard'))
            model.save()
            model = Office365GatherHistory.objects.create(**Office365GatherHistoryTestData.get_data('unique'))
            model.save()

    # Store self information
    model = GatherHistory
    url = '/example'

    standard = {
        'googlegatherhistory': 'default',
        'import_status': 0,
        'message': 'standard_char',
        'no_people': 12345,
        'ldapgatherhistory': 'default',
        'office365gatherhistory': 'default',
        'no_identifiers': 12345,
        'no_groups': 12345,
        'next_scheduled': 'default',
    }

    unique = {
        'googlegatherhistory': 'default',
        'import_status': 1,
        'message': 'unique_char',
        'no_people': 54321,
        'ldapgatherhistory': 'default',
        'office365gatherhistory': 'default',
        'no_identifiers': 54321,
        'no_groups': 54321,
        'next_scheduled': 'default',
    }

    missing_googlegatherhistory = {
        'import_status': 0,
        'message': 'standard_char',
        'no_people': 12345,
        'ldapgatherhistory': 'default',
        'office365gatherhistory': 'default',
        'no_identifiers': 12345,
        'no_groups': 12345,
        'next_scheduled': 'default',
    }
    modified_googlegatherhistory = {
        'googlegatherhistory': 'default',
        'import_status': 0,
        'message': 'standard_char',
        'no_people': 12345,
        'ldapgatherhistory': 'default',
        'office365gatherhistory': 'default',
        'no_identifiers': 12345,
        'no_groups': 12345,
        'next_scheduled': 'default',
    }

    modified_import_status = {
        'googlegatherhistory': 'default',
        'import_status': 1,
        'message': 'standard_char',
        'no_people': 12345,
        'ldapgatherhistory': 'default',
        'office365gatherhistory': 'default',
        'no_identifiers': 12345,
        'no_groups': 12345,
        'next_scheduled': 'default',
    }
    missing_import_status = {
        'googlegatherhistory': 'default',
        'message': 'standard_char',
        'no_people': 12345,
        'ldapgatherhistory': 'default',
        'office365gatherhistory': 'default',
        'no_identifiers': 12345,
        'no_groups': 12345,
        'next_scheduled': 'default',
    }

    missing_message = {
        'googlegatherhistory': 'default',
        'import_status': 0,
        'no_people': 12345,
        'ldapgatherhistory': 'default',
        'office365gatherhistory': 'default',
        'no_identifiers': 12345,
        'no_groups': 12345,
        'next_scheduled': 'default',
    }
    modified_message = {
        'googlegatherhistory': 'default',
        'import_status': 0,
        'message': 'modified_char',
        'no_people': 12345,
        'ldapgatherhistory': 'default',
        'office365gatherhistory': 'default',
        'no_identifiers': 12345,
        'no_groups': 12345,
        'next_scheduled': 'default',
    }

    missing_no_people = {
        'googlegatherhistory': 'default',
        'import_status': 0,
        'message': 'standard_char',
        'ldapgatherhistory': 'default',
        'office365gatherhistory': 'default',
        'no_identifiers': 12345,
        'no_groups': 12345,
        'next_scheduled': 'default',
    }
    modified_no_people = {
        'googlegatherhistory': 'default',
        'import_status': 0,
        'message': 'standard_char',
        'no_people': 54321,
        'ldapgatherhistory': 'default',
        'office365gatherhistory': 'default',
        'no_identifiers': 12345,
        'no_groups': 12345,
        'next_scheduled': 'default',
    }

    missing_ldapgatherhistory = {
        'googlegatherhistory': 'default',
        'import_status': 0,
        'message': 'standard_char',
        'no_people': 12345,
        'office365gatherhistory': 'default',
        'no_identifiers': 12345,
        'no_groups': 12345,
        'next_scheduled': 'default',
    }
    modified_ldapgatherhistory = {
        'googlegatherhistory': 'default',
        'import_status': 0,
        'message': 'standard_char',
        'no_people': 12345,
        'ldapgatherhistory': 'default',
        'office365gatherhistory': 'default',
        'no_identifiers': 12345,
        'no_groups': 12345,
        'next_scheduled': 'default',
    }

    missing_office365gatherhistory = {
        'googlegatherhistory': 'default',
        'import_status': 0,
        'message': 'standard_char',
        'no_people': 12345,
        'ldapgatherhistory': 'default',
        'no_identifiers': 12345,
        'no_groups': 12345,
        'next_scheduled': 'default',
    }
    modified_office365gatherhistory = {
        'googlegatherhistory': 'default',
        'import_status': 0,
        'message': 'standard_char',
        'no_people': 12345,
        'ldapgatherhistory': 'default',
        'office365gatherhistory': 'default',
        'no_identifiers': 12345,
        'no_groups': 12345,
        'next_scheduled': 'default',
    }

    missing_no_identifiers = {
        'googlegatherhistory': 'default',
        'import_status': 0,
        'message': 'standard_char',
        'no_people': 12345,
        'ldapgatherhistory': 'default',
        'office365gatherhistory': 'default',
        'no_groups': 12345,
        'next_scheduled': 'default',
    }
    modified_no_identifiers = {
        'googlegatherhistory': 'default',
        'import_status': 0,
        'message': 'standard_char',
        'no_people': 12345,
        'ldapgatherhistory': 'default',
        'office365gatherhistory': 'default',
        'no_identifiers': 54321,
        'no_groups': 12345,
        'next_scheduled': 'default',
    }

    modified_no_groups = {
        'googlegatherhistory': 'default',
        'import_status': 0,
        'message': 'standard_char',
        'no_people': 12345,
        'ldapgatherhistory': 'default',
        'office365gatherhistory': 'default',
        'no_identifiers': 12345,
        'no_groups': 54321,
        'next_scheduled': 'default',
    }
    missing_no_groups = {
        'googlegatherhistory': 'default',
        'import_status': 0,
        'message': 'standard_char',
        'no_people': 12345,
        'ldapgatherhistory': 'default',
        'office365gatherhistory': 'default',
        'no_identifiers': 12345,
        'next_scheduled': 'default',
    }

    missing_next_scheduled = {
        'googlegatherhistory': 'default',
        'import_status': 0,
        'message': 'standard_char',
        'no_people': 12345,
        'ldapgatherhistory': 'default',
        'office365gatherhistory': 'default',
        'no_identifiers': 12345,
        'no_groups': 12345,
    }
    modified_next_scheduled = {
        'googlegatherhistory': 'default',
        'import_status': 0,
        'message': 'standard_char',
        'no_people': 12345,
        'ldapgatherhistory': 'default',
        'office365gatherhistory': 'default',
        'no_identifiers': 12345,
        'no_groups': 12345,
        'next_scheduled': 'default',
    }




