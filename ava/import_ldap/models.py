import json
import datetime
import re
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.html import escape
from django.forms.models import model_to_dict
from ava.core.models import TimeStampedModel
from ava.import_ldap.ldap_interface import ActiveDirectoryHelper
from ava.core_identity.models import Identifier, Identity
from ava.core_group.models import Group


class ActiveDirectoryUser(TimeStampedModel):
    dn = models.CharField(max_length=300)
    account_expires = models.CharField(max_length=300)
    admin_count = models.IntegerField(null=True, blank=True)
    bad_password_time = models.CharField(max_length=300)
    bad_pwd_count = models.IntegerField(null=True, blank=True)
    cn = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    display_name = models.CharField(max_length=300)
    distinguished_name = models.CharField(max_length=300)
    is_critical_system_object = models.CharField(max_length=300)
    last_logoff = models.CharField(max_length=300)
    last_logon = models.CharField(max_length=300)
    last_logon_timestamp = models.CharField(max_length=300)
    logon_count = models.IntegerField(null=True, blank=True)
    # logon_hours = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    object_guid = models.CharField(max_length=300)
    object_sid = models.CharField(max_length=300)
    primary_group_id = models.CharField(max_length=300)
    pwd_last_set = models.CharField(max_length=300)
    sam_account_name = models.CharField(max_length=300)
    sam_account_type = models.CharField(max_length=300)
    usn_changed = models.CharField(max_length=300)
    usn_created = models.CharField(max_length=300)
    user_account_control = models.CharField(max_length=300)
    when_changed = models.CharField(max_length=300)
    when_created = models.CharField(max_length=300)
    groups = models.ManyToManyField('ActiveDirectoryGroup', related_name='users')
    ldap_configuration = models.ForeignKey('LDAPConfiguration')

    def __str__(self):
        return self.name or ''

    def get_absolute_url(self):
        return reverse('ad-user-detail', kwargs={'pk': self.id})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in ActiveDirectoryUser._meta.fields]

    model_schema = {
        'dn': 'dn',
        'account_expires': 'accountExpires',
        'admin_count': 'adminCount',
        'bad_password_time': 'badPasswordTime',
        'bad_pwd_count': 'badPwdCount',
        'cn': 'cn',
        'description': 'description',
        'display_name': 'displayName',
        'distinguished_name': 'distinguishedName',
        'is_critical_system_object': 'isCriticalSystemObject',
        'last_logoff': 'lastLogoff',
        'last_logon': 'lastLogon',
        'last_logon_timestamp': 'lastLogonTimestamp',
        'logon_count': 'logonCount',
        # 'logon_hours': 'logonHours',
        'name': 'name',
        'object_guid': 'objectGUID',
        'object_sid': 'objectSid',
        'primary_group_id': 'primaryGroupID',
        'pwd_last_set': 'pwdLastSet',
        'sam_account_name': 'sAMAccountName',
        'sam_account_type': 'sAMAccountType',
        'usn_changed': 'uSNChanged',
        'usn_created': 'uSNCreated',
        'user_account_control': 'userAccountControl',
        'when_changed': 'whenChanged',
        'when_created': 'whenCreated',

    }

    model_schema_reversed = {value: key for key, value in model_schema.items()}

    def model_field_to_ldap(self, fieldname):
        return self.model_schema.get(fieldname)

    def ldap_field_to_model(self, fieldname):
        return self.model_schema_reversed.get(fieldname)

    class Meta:
        unique_together = ('object_guid', 'object_sid')
        ordering = ['cn', 'distinguished_name']

    def convert_date_time(self, date_value):

        # LDAP date/times in FILETIME format use this as their epoch
        filetime_epoch = datetime.datetime(1601, 1, 1, 0, 0, 0)
        # Upper bound on valid FILETIME values.
        filetime_max = (datetime.datetime.max - filetime_epoch).total_seconds() * 1000000
        # Regular expression to check for valid FILETIME values.
        time_filetime = re.compile(r'^\d+$')
        # Regular expression to check for valid date/time string values.
        time_datestring = re.compile(r'^(?P<yr>\d{4})(?P<mon>0[1-9]|1[012])(?P<day>0[1-9]|[12][0-9]|3[01])'
                                     r'(?P<hr>[01][0-9]|2[0-3])(?P<min>[0-5][0-9])(?P<sec>[0-5][0-9])(?:\.\d{1,3})?Z$')

        # Check if the data is a Windows FILETIME value.
        match = time_filetime.match(date_value)
        if match:
            microseconds = int(date_value) / 10
            if microseconds > 0:
                if microseconds > filetime_max:
                    return datetime.datetime.max
                delta = datetime.timedelta(microseconds=microseconds)
                return filetime_epoch + delta
            return None

        # Check if the data is a date string.
        match = time_datestring.match(date_value)
        if match:
            time_year = int(match.group('yr'))
            time_month = int(match.group('mon'))
            time_day = int(match.group('day'))
            time_hour = int(match.group('hr'))
            time_minute = int(match.group('min'))
            time_second = int(match.group('sec'))
            return datetime.datetime(time_year, time_month, time_day, time_hour, time_minute, time_second)

        # No value.
        return None

    def cleanhex(self, val):
        s = ['\\%02X' % ord(x) for x in val]
        return ''.join(s)

    def get_users(self, parameters):
        ad_help = ActiveDirectoryHelper()

        # return json object containing all user records
        results = ad_help.import_users(parameters)

        ldap_json = json.loads(results)

        entries = ldap_json['entries']

        for person in entries:
            attributes = person['attributes']
            model_attributes = {}

            groups = []
            gen_groups = []
            email_addresses = []

            for key, value in attributes.items():
                if len(value) > 0:
                    if key == 'memberOf':
                        for cn in value:
                            qs = ActiveDirectoryGroup.objects.filter(ldap_configuration=parameters,
                                                                     distinguished_name=cn)
                            for q in qs:
                                groups.append(q)
                                if q.group:
                                    gen_groups.append(q.group)
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
                                date = self.convert_date_time(value_string)
                                if date:
                                    value_string = date.isoformat()

                            if key in ('adminCount', 'badPwdCount', 'logonCount'):
                                # print("WTF IS HAPPENING HERE")
                                print(value_string)
                                if value_string is None or value_string is "":
                                    value_string = 0
                                else:
                                    value_string = int(value_string)

                            if not self.ldap_field_to_model(key) is None:
                                model_attributes[self.ldap_field_to_model(key)] = value_string

                        except UnicodeDecodeError:
                            model_attributes[self.ldap_field_to_model(key)] = self.cleanhex(value_string)

            attributes.pop('memberOf', None)
            attributes.pop('proxyAddresses', None)

            # Don't filter on everything. Start with the properties that are
            # least likely to ever change, then work towards the more mutable
            # properties.
            filter_attrs = {}
            if 'objectGUID' in attributes:
                filter_attrs['object_guid'] = model_attributes['object_guid']
            elif 'objectSid' in attributes:
                filter_attrs['object_sid'] = model_attributes['object_sid']
            elif 'distinguishedName' in attributes:
                filter_attrs['distinguished_name'] = model_attributes['distinguished_name']
            else:
                continue

            # If no matching user currently exists then create one, otherwise
            # update the existing user.
            ad_users = ActiveDirectoryUser.objects.filter(**filter_attrs)
            # print(model_attributes)
            if ad_users.count() == 0:
                ad_user = ActiveDirectoryUser.objects.create(ldap_configuration=parameters, **model_attributes)
                ad_user.save()
            else:
                ad_users.update(**model_attributes)
                ad_user = ad_users.first()

            identity, created = Identity.objects.get_or_create(name=ad_user.display_name)
            '''
            TODO Do we need to create a person object for this identity??
            '''

            Identifier.objects.get_or_create(identifier=ad_user.sam_account_name, identifier_type=Identifier.UNAME,
                                             identity=identity)

            # Import the email addresses.
            for email_address in email_addresses:
                Identifier.objects.get_or_create(identifier=email_address, identifier_type=Identifier.EMAIL,
                                                 identity=identity)

            for group in groups:
                # print(groups)
                if ad_user.groups.filter(id=group.id).count() == 0:
                    ad_user.groups.add(group)

            for gen_group in gen_groups:
                # print(gen_group.id)
                if identity.groups.filter(id=gen_group.id).count() == 0:
                    identity.groups.add(gen_group)


class ActiveDirectoryGroup(TimeStampedModel):

    cn = models.CharField(max_length=300)
    distinguished_name = models.CharField(max_length=300, unique=True)
    name = models.CharField(max_length=100)
    object_category = models.CharField(max_length=300)
    sam_account_name = models.CharField(max_length=300)
    object_guid = models.CharField(max_length=300)
    object_sid = models.CharField(max_length=300)
    ldap_configuration = models.ForeignKey('LDAPConfiguration')
    group = models.ForeignKey('core_group.Group', null=True, blank=True)

    def __str__(self):
        return self.cn or ''

    def get_absolute_url(self):
        return reverse('ad-group-detail', kwargs={'pk': self.id})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in ActiveDirectoryGroup._meta.fields]

    model_schema = {
        'cn': 'cn',
        'distinguished_name': 'distinguishedName',
        'name': 'name',
        'object_category': 'objectCategory',
        'sam_account_name': 'sAMAccountName',
        'object_guid': 'objectGUID',
        'object_sid': 'objectSid',

    }

    model_schema_reversed = {value: key for key, value in model_schema.items()}

    def model_field_to_ldap(self, fieldname):
        return self.model_schema.get(fieldname)

    def ldap_field_to_model(self, fieldname):
        return self.model_schema_reversed.get(fieldname)

    def get_groups(self, parameters):
        ad_help = ActiveDirectoryHelper()
        results = ad_help.import_groups(parameters)

        ldap_json = json.loads(results)

        entries = ldap_json['entries']

        for group in entries:
            attributes = group['attributes']
            model_attributes = {}

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

                        model_attributes[self.ldap_field_to_model(key)] = value_string

                    except UnicodeDecodeError:
                        model_attributes[self.ldap_field_to_model(key)] = self.cleanhex(value_string)

            """
            Don't filter on everything. Start with the properties that are
            least likely to ever change, then work towards the more mutable
            properties.
            """
            filter_attrs = {}
            if 'objectGUID' in attributes:
                filter_attrs['object_guid'] = model_attributes['object_guid']
            elif 'objectSid' in attributes:
                filter_attrs['object_sid'] = model_attributes['object_sid']
            elif 'distinguishedName' in attributes:
                filter_attrs['distinguished_name'] = model_attributes['distinguished_name']
            else:
                continue

            # If no matching group currently exists then create one, otherwise
            # update the existing group.
            ad_groups = ActiveDirectoryGroup.objects.filter(**filter_attrs)
            if ad_groups.count() == 0:

                ad_group = ActiveDirectoryGroup.objects.create(ldap_configuration=parameters, **model_attributes)

                gen_group = Group.objects.create(name=ad_group.cn, group_type=Group.AD,
                                                 description="Imported group from LDAP")
                gen_group.save()

                ad_group.group = gen_group
                ad_group.save()
            else:
                # print("existing group")
                ad_groups.update(**model_attributes)
                ad_group = ad_groups.first()

                gen_group = ad_group.group
                if gen_group:
                    gen_group.name = ad_group.cn
                    gen_group.save()

    class Meta:
        unique_together = ('object_guid', 'object_sid')
        ordering = ['cn', 'distinguished_name']


class LDAPConfiguration(TimeStampedModel):
    """
    dump_dn = "dc=ava,dc=test,dc=domain"
    server = 'ldap://dc.ava.test.domain'
    """
    dump_dn = models.CharField(max_length=100, verbose_name='Domain')
    server = models.CharField(max_length=100, verbose_name='Server')

    def __str__(self):
        return self.server or ''

    class Meta:
        unique_together = ('server', 'dump_dn')

    def get_absolute_url(self):
        return reverse('ldap-configuration-detail', kwargs={'pk': self.id})

    def import_all(self, user_dn, user_pw):
        ad_group = ActiveDirectoryGroup()
        ad_group.get_groups(self)
        ad_user = ActiveDirectoryUser()
        ad_user.get_users(self)


class ExportLDAP:

    def __init__(self):
        pass

    def generate_graph(self, parameters):
        node_results = self.nodes(parameters)
        return self.edges(node_results)

    def nodes(self, parameters):
        nodes = []
        elements = []
        ldap_users = ActiveDirectoryUser.objects.filter(ldap_configuration=parameters)
        user_fields = ['id', 'accountExpires', 'adminCount', 'name', 'isCriticalSystemObject', 'lastLogon',
                       'logonCount', 'pwdLastSet']
        for user in ldap_users:
            elements.append(user)
            current = model_to_dict(user, user_fields)
            current['name'] = escape(current['name'])
            current['node_type'] = 'user'
            nodes.append(current)

        ldap_groups = ActiveDirectoryGroup.objects.filter(ldap_configuration=parameters)
        group_fields = ['id', 'cn']
        for group in ldap_groups:
            current = model_to_dict(group, group_fields)
            current['node_type'] = 'group'
            if group.users.count() > 0:
                nodes.append(current)
                elements.append(group)

        results = {}
        results['elements'] = elements
        results['nodes'] = nodes
        return results

    def edges(self, node_data):
        elements = node_data['elements']
        nodes = node_data['nodes']

        edges = []
        for index, value in enumerate(elements):
            if isinstance(value, ActiveDirectoryGroup):
                users = value.users.all()
                for user in users:
                    current_edge = {}
                    user_index = elements.index(user)
                    current_edge['value'] = 'edge' + str(user_index) + "_" + str(index)
                    current_edge['source'] = user_index
                    current_edge['target'] = index
                    edges.append(current_edge)

        results = {}
        results['nodes'] = nodes
        results['links'] = edges
        return results
