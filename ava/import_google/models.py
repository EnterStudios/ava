# flake8: noqa

import ldap, ldif, datetime, re

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.html import escape
from io import StringIO

from ava.core.models import TimeStampedModel
from ava.core_identity.models import Identifier, Person, Identity
from ava.core_group.models import Group

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
    dn = models.CharField(max_length = 300)
    accountExpires = models.CharField(max_length = 300)
    adminCount = models.CharField(max_length = 300)
    badPasswordTime = models.CharField(max_length = 300)
    badPwdCount = models.CharField(max_length = 300)
    cn = models.CharField(max_length = 300)
    description = models.CharField(max_length = 300)
    displayName = models.CharField(max_length = 300)
    distinguishedName = models.CharField(max_length = 300)
    isCriticalSystemObject = models.CharField(max_length = 300)
    lastLogoff = models.CharField(max_length = 300)
    lastLogon = models.CharField(max_length = 300)
    lastLogonTimestamp = models.CharField(max_length = 300)
    logonCount = models.CharField(max_length = 300)
    groups = models.ManyToManyField('GoogleDirectoryGroup', related_name='users')
    google_configuration = models.ForeignKey('GoogleConfiguration')

    def __unicode__(self):
        return self.name or ''

    def get_absolute_url(self):
        return reverse('google-user-detail',kwargs={'pk': self.id})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in GoogleDirectoryUser._meta.fields]

    class Meta:
        unique_together = ('objectGUID','objectSid')
        ordering = ['cn','distinguishedName']
        
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
    name = models.CharField(max_length = 300, unique=True)
    id = models.CharField(max_length = 300, unique=True)
    description = models.CharField(max_length = 1000)
    adminCreated = models.BooleanField()
    email = models.EmailField()
    etag = models.CharField(max_length=300)
    google_configuration = models.ForeignKey('GoogleConfiguration')
    group = models.ForeignKey('core_group.Group', null=True, blank=True)

    def __unicode__(self):
        return self.name or ''

    def get_absolute_url(self):
        return reverse('google-group-detail',kwargs={'pk': self.id})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in GoogleDirectoryGroup._meta.fields]

    class Meta:
        ordering = ['name', 'id']


class GoogleConfiguration(TimeStampedModel):
    domain = models.CharField(max_length = 100, verbose_name='Primary Domain', unique=True)

    def __unicode__(self):
        return self.domain or ''

    def get_absolute_url(self):
        return reverse('google-configuration-detail',kwargs={'pk': self.id})


class GoogleDirectoryHelper():

    def getConnection(self, parameters):
        try:

            return google_conn

        except GoogleError as e:
            if type(e.message) == dict:
                for (k, v) in e.message.items():
                    sys.stderr.write("%s: %sn" % (k, v))
                    sys.stderr.write("\n")
            else:
                sys.stderr.write(e.message)
                sys.exit(1)

    def getGroups(self,parameters):
        pass


    def getUsers(self,parameters):
       pass


class ExportGoogle():
    def generateGraph(self,parameters):
        node_results = self.nodes(parameters)
        return self.edges(node_results)

    def nodes(self, parameters):
        nodes = []
        elements = []
        google_users = GoogleDirectoryUser.objects.filter(google_configuration=parameters)
        user_fields = ['id','accountExpires','adminCount','name','isCriticalSystemObject','lastLogon','logonCount','pwdLastSet']
        for user in google_users:
            elements.append(user)
            current = self.model_to_dict(user,user_fields)
            current['name']=escape(current['name'])
            current['node_type'] = 'user'
            nodes.append(current)

        google_groups = GoogleDirectoryGroup.objects.filter(google_configuration=parameters)
        group_fields = ['id','cn']
        for group in google_groups:
            current = self.model_to_dict(group,group_fields)
            current['node_type'] = 'group'
            if (group.users.count() > 0):
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
            if isinstance(value,GoogleDirectoryGroup):
                users = value.users.all()
                for user in users:
                    current_edge = {}
                    user_index = elements.index(user)
                    current_edge['value'] = 'edge'+str(user_index)+"_"+str(index)
                    current_edge['source'] = user_index
                    current_edge['target'] = index
                    edges.append(current_edge)

        results = {}
        results['nodes'] = nodes;
        results['links'] = edges;
        return results

    def model_to_dict(self,instance, fields=None, exclude=None):
        """
        Returns a dict containing the data in ``instance`` suitable for passing as
        a Form's ``initial`` keyword argument.
    
        ``fields`` is an optional list of field names. If provided, only the named
        fields will be included in the returned dict.


        ``exclude`` is an optional list of field names. If provided, the named
        fields will be excluded from the returned dict, even if they are listed in
        the ``fields`` argument.
        """
        # avoid a circular import
        from django.db.models.fields.related import ManyToManyField
        opts = instance._meta
        data = {}
        for f in opts.concrete_fields + opts.virtual_fields + opts.many_to_many:
            if not getattr(f, 'editable', False):
                continue
            if fields and f.name not in fields:
                continue
            if exclude and f.name in exclude:
                continue
            if isinstance(f, ManyToManyField):
                # If the object doesn't have a primary key yet, just use an empty
                # list for its m2m fields. Calling f.value_from_object will raise
                # an exception.
                if instance.pk is None:
                    data[f.name] = []
                else:
                    # MultipleChoiceWidget needs a list of pks, not object instances.
                    qs = f.value_from_object(instance)
                    if qs._result_cache is not None:
                        data[f.name] = [item.pk for item in qs]
                    else:
                        data[f.name] = list(qs.values_list('pk', flat=True))
            else:
                data[f.name] = f.value_from_object(instance)
        return data
