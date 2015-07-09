# flake8: noqa

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.html import escape
from django.forms.models import model_to_dict


from ava.core.models import TimeStampedModel


# { # JSON template for User object in Directory API.
#      "addresses": "",
#      "phones": "",
#      "isDelegatedAdmin": True or False, # Boolean indicating if the user is delegated admin (Read-only)
#      "thumbnailPhotoEtag": "A String", # ETag of the user's photo (Read-only)
#      "suspended": True or False, # Indicates if user is suspended
#      "id": "A String", # Unique identifier of User (Read-only)
#      "aliases": [ # List of aliases (Read-only)
#        "A String",
#      ],
#      "nonEditableAliases": [ # List of non editable aliases (Read-only)
#        "A String",
#      ],
#      "customSchemas": { # Custom fields of the user.
#        "a_key": { # JSON template for a set of custom properties (i.e. all fields in a particular schema)
#          "a_key": "",
#        },
#      },
#      "deletionTime": "A String",
#      "suspensionReason": "A String", # Suspension reason if user is suspended (Read-only)
#      "thumbnailPhotoUrl": "A String", # Photo Url of the user (Read-only)
#      "isAdmin": True or False, # Boolean indicating if the user is admin (Read-only)
#      "relations": "",
#      "includeInGlobalAddressList": True or False, # Boolean indicating if user is included in Global Address List
#      "etag": "A String", # ETag of the resource.
#      "lastLoginTime": "A String", # User's last login time. (Read-only)
#      "orgUnitPath": "A String", # OrgUnit of User
#      "agreedToTerms": True or False, # Indicates if user has agreed to terms (Read-only)
#      "externalIds": "",
#      "ipWhitelisted": True or False, # Boolean indicating if ip is whitelisted
#      "kind": "admin#directory#user", # Kind of resource this is.
#      "isMailboxSetup": True or False, # Is mailbox setup (Read-only)
#      "password": "A String", # User's password
#      "emails": "",
#      "organizations": "",
#      "primaryEmail": "A String", # username of User
#      "hashFunction": "A String", # Hash function name for password. Supported are MD5, SHA-1 and crypt
#      "name": { # JSON template for name of a user in Directory API. # User's name
#        "fullName": "A String", # Full Name
#        "givenName": "A String", # First Name
#        "familyName": "A String", # Last Name
#      },
#      "notes": "",
#      "creationTime": "A String", # User's Google account creation time. (Read-only)
#      "websites": "",
#      "changePasswordAtNextLogin": True or False, # Boolean indicating if the user should change password in next login
#      "ims": "",
#      "customerId": "A String", # CustomerId of User (Read-only)
#    }
class GoogleDirectoryUser(TimeStampedModel):
    dn = models.CharField(max_length=300)
    account_expires = models.CharField(max_length=300)
    admin_count = models.CharField(max_length=300)
    bad_passwordTime = models.CharField(max_length=300)
    badPwdCount = models.CharField(max_length=300)
    cn = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    displayName = models.CharField(max_length=300)
    distinguishedName = models.CharField(max_length=300)
    isCriticalSystemObject = models.CharField(max_length=300)
    lastLogoff = models.CharField(max_length=300)
    lastLogon = models.CharField(max_length=300)
    lastLogonTimestamp = models.CharField(max_length=300)
    logonCount = models.CharField(max_length=300)
    groups = models.ManyToManyField('GoogleDirectoryGroup', related_name='users')
    google_configuration = models.ForeignKey('GoogleConfiguration')

    def __unicode__(self):
        return self.name or ''

    def get_absolute_url(self):
        return reverse('google-user-detail', kwargs={'pk': self.id})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in GoogleDirectoryUser._meta.fields]

    class Meta:
        unique_together = ('objectGUID', 'objectSid')
        ordering = ['cn', 'distinguishedName']


# 
# { # JSON template for Group resource in Directory API.
#       "nonEditableAliases": [ # List of non editable aliases (Read-only)
#         "A String",
#       ],
#       "kind": "admin#directory#group", # Kind of resource this is.
#       "description": "A String", # Description of the group
#       "adminCreated": True or False, # Is the group created by admin (Read-only) *
#       "directMembersCount": "A String", # Group direct members count
#       "email": "A String", # Email of Group
#       "etag": "A String", # ETag of the resource.
#       "aliases": [ # List of aliases (Read-only)
#         "A String",
#       ],
#       "id": "A String", # Unique identifier of Group (Read-only)
#       "name": "A String", # Group name
#     }
class GoogleDirectoryGroup(TimeStampedModel):
    name = models.CharField(max_length=300, unique=True)
    id = models.CharField(max_length=300, unique=True)
    description = models.CharField(max_length=1000)
    adminCreated = models.BooleanField()
    email = models.EmailField()
    etag = models.CharField(max_length=300)
    google_configuration = models.ForeignKey('GoogleConfiguration')
    group = models.ForeignKey('core_group.Group', null=True, blank=True)

    def __unicode__(self):
        return self.name or ''

    def get_absolute_url(self):
        return reverse('google-group-detail', kwargs={'pk': self.id})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in GoogleDirectoryGroup._meta.fields]

    class Meta:
        ordering = ['name', 'id']


class GoogleConfiguration(TimeStampedModel):
    domain = models.CharField(max_length=100, verbose_name='Primary Domain', unique=True)

    def __unicode__(self):
        return self.domain or ''

    def get_absolute_url(self):
        return reverse('google-configuration-detail', kwargs={'pk': self.id})


class GoogleDirectoryHelper:

    def __init__(self):
        pass

    def get_connection(self):
        # try:
        #
        #     return google_conn
        #
        # except GoogleError as e:
        #     if type(e.message) == dict:
        #         for (k, v) in e.message.items():
        #             sys.stderr.write("%s: %sn" % (k, v))
        #             sys.stderr.write("\n")
        #     else:
        #         sys.stderr.write(e.message)
        #         sys.exit(1)1

    def get_groups(self, parameters):
        pass

    def get_users(self, parameters):
        pass


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
