# flake8: noqa
import json
import logging

from rest_framework import permissions,status, viewsets
from rest_framework.response import Response

from ava_core.abstract.permissions import IsRetrieveOnly
from ava_core.gather.gather_abstract.views import GatherImportAPI
from ava_core.organize.models import Person, Identifier, Group, GroupIdentifier, PersonIdentifier
from ava_core.organize.tasks import task_run_intro_email
from ava_core.organize.utils import add_identifier
from ava_core.gather.gather_abstract.models import GatherHistory
from ava_core.integration.integration_abstract.utils import retrieve_integration_from_database
from .interface import Office365DirectoryHelper
from .models import Office365GatherHistory
from .serializers import Office365GatherHistorySerializer

log = logging.getLogger(__name__)


class Office365ImportAPI(GatherImportAPI):
    MODEL_NAME = 'integration_office365.Office365IntegrationAdapter'
    DIRECTORY_INTERFACE = Office365DirectoryHelper()
    INTEGRATION_NAME = 'office365'

    def get(self, request, **kwargs):
        super(Office365ImportAPI, self).get(request, **kwargs)
        log.debug("Office365ImportAPI::POST - Attempting group population")
        # self.populate_groups_from_json(self.IMPORT_DATA['group_members'])
        #
        # pk = self.kwargs.get('pk')
        #
        # integration = retrieve_integration_from_database(self.MODEL_NAME, pk)
        #
        # return_message = "Imported completed"
        # Office365GatherHistory.objects.create(integration=integration, message=return_message, import_status=GatherHistory.COMPLETED)

        return Response({'message': "Import complete"}, status=status.HTTP_200_OK)

    def import_users_from_json(self, users):
        super(Office365ImportAPI, self).import_users_from_json(users)

        # for user in users:
        #     # for key, value in user.items():
        #     #     log.debug("Office365ImportAPI::import_users_from_json -Key :: " + str(key) + " value :: " + str(value))
        #
        #     # check if we've already seen this person - assumes office365_id is unique
        #     if PersonIdentifier.objects.filter(identifier=user['id'],
        #                                        identifier_type=Identifier.OFFICE_ID).exists():
        #
        #         person = PersonIdentifier.objects.get(identifier=user['id'],
        #                                               identifier_type=Identifier.OFFICE_ID).belongs_to
        #     else:
        #         # create a person
        #         person, p_created = Person.objects.update_or_create(first_name=user['name']['givenName'],
        #                                                             surname=user['name']['familyName'],
        #                                                             office365_identity_data=json.dumps(user))
        #
        #     fullname = user['name']['fullName']
        #     add_identifier(self.PERSON_MODEL, person, Identifier.NAME, fullname)
        #
        #     if user.get('id'):
        #         add_identifier(self.PERSON_MODEL, person, Identifier.OFFICE_ID, user['id'])
        #
        #     # customer id is the id for the company - weird edge case so we need to handle this here
        #     office365_group, id_created = Group.objects.update_or_create(name=user['customerId'],
        #                                                               group_type=Group.OFFICE,
        #                                                               description="Office365 Customer Group - Organisation",
        #                                                               office365_group_data='')
        #     person.groups.add(office365_group)
        #
        #     if user.get('emails'):
        #         email_addresses = user['emails']
        #         for email_item in email_addresses:
        #             is_primary = 'primary' in email_item
        #             add_identifier(self.PERSON_MODEL, person, Identifier.EMAIL, email_item['address'], is_primary)
        #
        #     if user.get('aliases'):
        #         aliases = user['aliases']
        #         for alias in aliases:
        #             add_identifier(self.PERSON_MODEL, person, Identifier.EMAIL, alias)
        #
        #     if user.get('nonEditableAliases'):
        #         aliases = user['nonEditableAliases']
        #         for alias in aliases:
        #             add_identifier(self.PERSON_MODEL, person, Identifier.EMAIL, alias)
        #
        #     # Invite user to system
        #     task_run_intro_email.apply_async((person.id,), countdown=1)

    def import_groups_from_json(self, groups):
        super(Office365ImportAPI, self).import_groups_from_json(groups)
        #
        # for group in groups:
        #
        #     # check if we've already seen this group - assumes office365_id is unique
        #     if GroupIdentifier.objects.filter(identifier=group['id'],
        #                                       identifier_type=Identifier.OFFICE_ID).exists():
        #
        #         office365_group = GroupIdentifier.objects.get(identifier=group['id'],
        #                                                    identifier_type=Identifier.OFFICE_ID).belongs_to
        #     else:
        #         # create a group
        #         office365_group, id_created = Group.objects.update_or_create(name=group['name'],
        #                                                                   group_type=Group.OFFICE,
        #                                                                   description="Imported from Office365 Apps",
        #                                                                   office365_group_data=json.dumps(group))
        #
        #     add_identifier(self.GROUP_MODEL, office365_group, Identifier.OFFICE_ID, group['id'])
        #
        #     if group.get('aliases'):
        #         aliases = group['aliases']
        #         for alias in aliases:
        #             add_identifier(self.GROUP_MODEL, office365_group, Identifier.EMAIL, alias)
        #
        #     if group.get('nonEditableAliases'):
        #         aliases = group['nonEditableAliases']
        #         for alias in aliases:
        #             add_identifier(self.GROUP_MODEL, office365_group, Identifier.EMAIL, alias)

    def populate_groups_from_json(self, group_members):
        log.debug("Office365ImportAPI::populate_groups_from_json - ")
        # for key, value in group_members.items():
        #     log.debug("Office365ImportAPI::populate_groups_from_json - Searching for group id ::" + key)
        #     group = GroupIdentifier.objects.get(identifier=key, identifier_type=Identifier.OFFICE_ID).belongs_to
        #
        #     for user in value:
        #         log.debug("Office365ImportAPI::populate_groups_from_json - Searching for id ::" + user['id'])
        #
        #         for p in PersonIdentifier.objects.filter(identifier=user['id'], identifier_type=Identifier.OFFICE_ID):
        #             person = p.belongs_to
        #             person.groups.add(group)


class Office365GatherHistoryAPI(viewsets.ModelViewSet):
    queryset = Office365GatherHistory.objects.none()  # Required for DjangoModelPermissions
    serializer_class = Office365GatherHistorySerializer

    permission_classes = (permissions.IsAuthenticated,
                          permissions.IsAdminUser,
                          IsRetrieveOnly)

    def get_queryset(self):
        return Office365GatherHistory.objects.all()