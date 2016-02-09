import json
import logging

from rest_framework import status, viewsets, permissions
from rest_framework.response import Response

from ava_core.abstract.permissions import IsRetrieveOnly, IsCreateOrRetrieveOnly
from ava_core.organize.models import Group, Person, Identifier
from ava_core.organize.tasks import task_run_intro_email
from ava_core.organize.utils import add_identifier
from ava_core.gather.gather_abstract.views import GatherImportAPI
from ava_core.gather.gather_abstract.models import GatherHistory

from .interface import ActiveDirectoryHelper
from .serializers import LDAPGatherHistorySerializer
from .models import LDAPGatherHistory
from .utils import clean_hex, convert_date_time, ldap_field_to_group_model, ldap_field_to_user_model
from ava_core.integration.integration_abstract.utils import retrieve_integration_from_database


log = logging.getLogger(__name__)


class LDAPImportAPI(GatherImportAPI):
    MODEL_NAME = 'integration_ldap.LDAPIntegrationAdapter'
    DIRECTORY_INTERFACE = ActiveDirectoryHelper()


    def get(self, request, **kwargs):
        super(LDAPImportAPI, self).get(request, **kwargs)

        pk = self.kwargs.get('pk')

        integration = retrieve_integration_from_database(self.MODEL_NAME, pk)

        return_message = "Imported completed"
        LDAPGatherHistory.objects.create(integration=integration,message=return_message, import_status=GatherHistory.COMPLETED)



        return Response({'message': "Import complete"}, status=status.HTTP_200_OK)

    def import_users_from_json(self, users):
        super(LDAPImportAPI, self).import_users_from_json(users)

        ldap_json = json.loads(users)

        entries = ldap_json['entries']

        for person in entries:
            log.debug("Handling groups '%s'", person.get('objectGUID'))
            attributes = person['attributes']

            model_attributes = {}

            groups = []
            gen_groups = []
            email_addresses = []

            for key, value in attributes.items():
                # log.debug("Handling attributes for person key = %s, value = %s", key, value)
                if len(value) > 0:
                    if key == 'memberOf':
                        for cn in value:
                            qs = Group.objects.filter(name=cn)
                            for q in qs:
                                groups.append(q)
                                if q.groups:
                                    gen_groups.append(q.groups)
                    elif key == 'proxyAddresses':
                        for address in value:
                            email_addresses.append(address[5:])
                    else:
                        value_string = ""
                        try:
                            if isinstance(value, str):
                                value_string = value
                                value_string = value_string.decode('utf-8')
                            else:
                                for e in value:
                                    if isinstance(e, str):
                                        value_string = ''.join(e)
                                    else:
                                        value_string = e['encoded']

                            if key in ('accountExpires', 'badPasswordTime', 'lastLogoff', 'lastLogon',
                                       'lastLogonTimestamp', 'pwdLastSet', 'uSNChanged', 'uSNCreated',
                                       'whenChanged', 'whenCreated'):
                                date = convert_date_time(self, value_string)
                                if date:
                                    value_string = date.isoformat()

                            if key in ('adminCount', 'badPwdCount', 'logonCount'):
                                # print("WTF IS HAPPENING HERE")
                                # print(value_string)
                                if value_string is None or value_string is "":
                                    value_string = 0
                                else:
                                    value_string = int(value_string)

                                log.debug("Adding to mode;_attributes for person key = %s, value = %s",
                                          ldap_field_to_user_model(self, key), value_string)

                            model_attributes[ldap_field_to_user_model(self, key)] = value_string

                        except UnicodeDecodeError:
                            log.debug("Adding to mode;_attributes for person key = %s, value = %s",
                                      ldap_field_to_user_model(self, key), clean_hex(self, value_string))
                            model_attributes[ldap_field_to_user_model(self, key)] = clean_hex(self, value_string)

            attributes.pop('memberOf', None)
            attributes.pop('proxyAddresses', None)

            name = model_attributes['cn'];
            firstname = ''
            surname = name

            if " " in name:
                name_parts = name.split(" ")
                if len(name_parts) > 1:
                    firstname = name_parts[0]
                    surname = name_parts[1]

            curr_person, p_created = Person.objects.get_or_create(first_name=firstname,
                                                                  surname=surname,
                                                                  ldap_identity_data=json.dumps(model_attributes))

            if 'object_guid' in model_attributes:
                add_identifier(self.PERSON_MODEL, curr_person, Identifier.GUID, model_attributes['object_guid'])

            if 'object_sid' in model_attributes:
                add_identifier(self.PERSON_MODEL, curr_person, Identifier.SID, model_attributes['object_sid'])

            if 'distinguished_name' in model_attributes:
                add_identifier(self.PERSON_MODEL, curr_person, Identifier.NAME, model_attributes['distinguished_name'])

            if 'sam_account_name' in attributes:
                add_identifier(self.PERSON_MODEL, curr_person, Identifier.NAME, model_attributes['sam_account_name'])

            if 'cn' in model_attributes:
                add_identifier(self.PERSON_MODEL, curr_person, Identifier.NAME, model_attributes['cn'])

        # Import the email addresses.
        for email_address in email_addresses:
            add_identifier(self.PERSON_MODEL, curr_person, Identifier.EMAIL, email_address)

        for group in groups:
            if curr_person.groups.filter(id=group.id).count() == 0:
                curr_person.groups.add(group)

        # Invite user to system
        task_run_intro_email.apply_async((curr_person.id,), countdown=1)

    def import_groups_from_json(self, groups):
        super(LDAPImportAPI, self).import_groups_from_json(groups)

        ldap_json = json.loads(groups)

        entries = ldap_json['entries']

        for group in entries:
            log.debug("Handling groups '%s'", group.get('dn'))

            attributes = group['attributes']
            model_attributes = {}

            log.debug("Cleaning and processing attributes for group")
            for key, value in attributes.items():

                if len(value) > 0:
                    value_string = ""
                    try:
                        if isinstance(value, str):
                            value_string = value
                            value_string = value_string.decode('utf-8')
                        else:
                            for e in value:
                                if isinstance(e, str):
                                    value_string = ''.join(e)
                                    # value_string = value_string.decode('utf-8')
                                else:
                                    value_string = e['encoded']

                        model_attributes[ldap_field_to_group_model(self, key)] = value_string

                    except UnicodeDecodeError:
                        model_attributes[ldap_field_to_group_model(self, key)] = clean_hex(self, value_string)

            # # If no matching groups currently exists then create one, otherwise
            # # update the existing groups.
            groups = Group.objects.filter(name=model_attributes['cn'])

            if groups.count() == 0:

                # log.debug("Attempting to create new Group object")
                # for k, v in model_attributes.items():
                # log.debug("Model Attributes : %s = %s", k, v)

                gen_group, group_created = Group.objects.get_or_create(name=model_attributes['cn'], group_type=Group.AD,
                                                                       description="Imported group from LDAP")

                if 'object_guid' in model_attributes:
                    log.debug("Adding group identifier (%s) as type guid to %s", model_attributes['object_guid'],
                              gen_group.name)
                    add_identifier(self.GROUP_MODEL, gen_group, Identifier.GUID, model_attributes['object_guid'])

                if 'object_sid' in model_attributes:
                    log.debug("Adding group identifier (%s) as type sid to %s", model_attributes['object_sid'],
                              gen_group.name)
                    add_identifier(self.GROUP_MODEL, gen_group, Identifier.SID, model_attributes['object_sid'])

                if 'distinguished_name' in model_attributes:
                    log.debug("Adding group identifier (%s) as type dist name to %s",
                              model_attributes['distinguished_name'], gen_group.name)
                    add_identifier(self.GROUP_MODEL, gen_group, Identifier.NAME, model_attributes['distinguished_name'])

                if 'sam_account_name' in model_attributes:
                    log.debug("Adding group identifier (%s) as type sam account name to %s",
                              model_attributes['sam_account_name'], gen_group.name)
                    add_identifier(self.GROUP_MODEL, gen_group, Identifier.NAME, model_attributes['sam_account_name'])


class LDAPGatherHistoryAPI(viewsets.ModelViewSet):
    queryset = LDAPGatherHistory.objects.none()  # Required for DjangoModelPermissions
    serializer_class = LDAPGatherHistorySerializer

    permission_classes = (permissions.IsAuthenticated,
                          permissions.IsAdminUser, IsCreateOrRetrieveOnly)

    def get_queryset(self):
        return LDAPGatherHistory.objects.all()



