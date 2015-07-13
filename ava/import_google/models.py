# flake8: noqa
import json

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.html import escape
from django.forms.models import model_to_dict

from django.contrib.auth.models import User
from django.contrib import admin

from ava.core.models import TimeStampedModel

from oauth2client.django_orm import FlowField, CredentialsField


class CredentialsModel(models.Model):
    id = models.OneToOneField(User, primary_key=True)
    credential = CredentialsField()



class CredentialsAdmin(admin.ModelAdmin):
    pass

class FlowModel(models.Model):
    id = models.OneToOneField(User, primary_key=True)
    flow = FlowField()

# TO DO - THESE FIELDS PROBABLY NEED SOME LOVE
# aliases": [ # List of aliases (Read-only)
#         "A String",
#       ],
# nonEditableAliases": [ # List of non editable aliases (Read-only)
#         "A String",
#       ],
#
# name": { # JSON template for name of a user in Directory API. # User's name
#         "fullName": "A String", # Full Name
#         "givenName": "A String", # First Name
#         "familyName": "A String", # Last Name

class GoogleDirectoryUser(TimeStampedModel):
    is_delegated_admin = models.BooleanField(default=False)
    suspended = models.BooleanField(default=False)
    google_id = models.CharField(max_length=300)
    deletion_time = models.CharField(max_length=300)
    suspension_reason = models.CharField(max_length=300)
    is_admin = models.BooleanField(default=False)
    etag = models.CharField(max_length=300)
    last_login_time = models.CharField(max_length=300)
    is_mailbox_setup = models.BooleanField(default=False)
    password = models.CharField(max_length=300)
    primary_email = models.EmailField()
    ip_whitelisted = models.BooleanField(default=False)
    hash_function = models.CharField(max_length=300)
    creation_time = models.CharField(max_length=300)
    change_password_at_next_login = models.BooleanField(default=False)
    groups = models.ManyToManyField('GoogleDirectoryGroup', related_name='users')
    google_configuration = models.ForeignKey('GoogleConfiguration')

    model_schema = {
        'is_delegated_admin': 'isDelegatedAdmin',
        'suspended': 'suspended',
        'google_id': 'id',
        'deletion_time': 'deletionTime',
        'suspension_reason': 'suspensionReason',
        'is_admin': 'isAdmin',
        'etag': 'etag',
        'last_login_time': 'lastLoginTime',
        'is_mailbox_setup': 'isMailboxSetup',
        'ip_whitelisted': 'ipWhitelisted',
        'password': 'password',
        'primary_email': 'primaryEmail',
        'hash_function': 'hashFunction',
        'creation_time': 'creationTime',
        'change_password_at_next_login': 'changePasswordAtNextLogin',

    }

    model_schema_reversed = {value: key for key, value in model_schema.items()}

    def model_field_to_google(self, fieldname):
        return self.model_schema.get(fieldname)

    def google_field_to_model(self, fieldname):
        return self.model_schema_reversed.get(fieldname)


    def __unicode__(self):
        return self.name or ''

    def get_absolute_url(self):
        return reverse('google-user-detail', kwargs={'pk': self.id})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in GoogleDirectoryUser._meta.fields]

    def import_from_json(self, google_configuration, users):
        for user in users:
            user_attributes = {}
            for key, value in user.items():
                # print("key : " + key + " value : " + str(value))
                if key in self.model_schema_reversed.keys():
                    user_attributes[self.google_field_to_model(key)] = value
            gd_user = GoogleDirectoryUser.objects.create(google_configuration=google_configuration, **user_attributes)
            gd_user.save()




class GoogleDirectoryGroup(TimeStampedModel):
    name = models.CharField(max_length=300, unique=True)
    google_id = models.CharField(max_length=300, unique=True)
    description = models.CharField(max_length=1000)
    direct_members_count = models.CharField(max_length=5)
    admin_created = models.BooleanField(default=False)
    email = models.EmailField()
    etag = models.CharField(max_length=300)
    google_configuration = models.ForeignKey('GoogleConfiguration')
    # group = models.ForeignKey('core_group.Group', null=True, blank=True)

    model_schema = {
        'google_id': 'id',
        'etag': 'etag',
        'email': 'email',
        'name': 'name',
        'direct_members_count': 'directMembersCount',
        'description': 'description',
        'admin_created': 'adminCreated',
    }

    model_schema_reversed = {value: key for key, value in model_schema.items()}

    def model_field_to_google(self, fieldname):
        return self.model_schema.get(fieldname)

    def google_field_to_model(self, fieldname):
        return self.model_schema_reversed.get(fieldname)


    def __unicode__(self):
        return self.name or ''

    def get_absolute_url(self):
        return reverse('google-group-detail', kwargs={'pk': self.id})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in GoogleDirectoryGroup._meta.fields]

    class Meta:
        ordering = ['name', 'google_id']
        
    def import_from_json(self, google_configuration, groups):
        for group in groups:
            group_attributes = {}
            for key, value in group.items():
                # print("key : " + key + " value : " + str(value))
                if key in self.model_schema_reversed.keys():
                    group_attributes[self.google_field_to_model(key)] = value
            gd_group = GoogleDirectoryGroup.objects.create(google_configuration=google_configuration, **group_attributes)
            gd_group.save()


class GoogleConfiguration(TimeStampedModel):
    domain = models.CharField(max_length=100, verbose_name='Primary Domain', unique=True)

    def __unicode__(self):
        return self.domain or ''

    def get_absolute_url(self):
        return reverse('google-configuration-detail', kwargs={'pk': self.id})


class ExportGoogle:
    def __init__(self):
        pass

    def generate_graph(self, parameters):
        node_results = self.nodes(parameters)
        return self.edges(node_results)

    def nodes(self, parameters):
        nodes = []
        elements = []
        google_users = GoogleDirectoryUser.objects.filter(google_configuration=parameters)
        user_fields = ['id', 'accountExpires', 'adminCount', 'name', 'isCriticalSystemObject', 'lastLogon',
                       'logonCount', 'pwdLastSet']
        for user in google_users:
            elements.append(user)
            current = model_to_dict(user, user_fields)
            current['name'] = escape(current['name'])
            current['node_type'] = 'user'
            nodes.append(current)

        google_groups = GoogleDirectoryGroup.objects.filter(google_configuration=parameters)
        group_fields = ['id', 'cn']
        for group in google_groups:
            current = model_to_dict(group, group_fields)
            current['node_type'] = 'group'
            if group.users.count() > 0:
                nodes.append(current)
                elements.append(group)

        results = {'nodes': nodes, 'elements': elements}

        return results

    def edges(self, node_data):
        elements = node_data['elements']
        nodes = node_data['nodes']

        edges = []
        for index, value in enumerate(elements):
            if isinstance(value, GoogleDirectoryGroup):
                users = value.users.all()
                for user in users:
                    current_edge = {}
                    user_index = elements.index(user)
                    current_edge['value'] = 'edge' + str(user_index) + "_" + str(index)
                    current_edge['source'] = user_index
                    current_edge['target'] = index
                    edges.append(current_edge)

        results = {'nodes': nodes, 'links': edges}

        return results
