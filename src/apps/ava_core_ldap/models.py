import json
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.html import escape
from apps.ava_core.models import TimeStampedModel
from apps.ava_core_ldap.ldap_interface import ActiveDirectoryHelper
from apps.ava_core_identity.models import Identifier, Person, Identity
from apps.ava_core_group.models import Group


class ActiveDirectoryUser(TimeStampedModel):
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
    logonHours = models.CharField(max_length = 300)
    name = models.CharField(max_length = 300)
    objectGUID = models.CharField(max_length = 300)
    objectSid = models.CharField(max_length = 300)
    primaryGroupID = models.CharField(max_length = 300)
    pwdLastSet = models.CharField(max_length = 300)
    sAMAccountName = models.CharField(max_length = 300)
    sAMAccountType = models.CharField(max_length = 300)
    uSNChanged = models.CharField(max_length = 300)
    uSNCreated = models.CharField(max_length = 300)
    userAccountControl = models.CharField(max_length = 300)
    whenChanged = models.CharField(max_length = 300)
    whenCreated = models.CharField(max_length = 300)
    groups = models.ManyToManyField('ActiveDirectoryGroup', related_name='users')
    ldap_configuration = models.ForeignKey('LDAPConfiguration')
    #identity = models.ForeignKey('ava_core_identity.Identity',null=True,blank=True)

    def __unicode__(self):
        return self.name or u''

    def get_absolute_url(self):
        return reverse('ad-user-detail',kwargs={'pk': self.id})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in ActiveDirectoryUser._meta.fields]

    class Meta:
        unique_together = ('objectGUID','objectSid')
        ordering = ['cn','distinguishedName']

    def getUsers(self,parameters):
        filter = '(objectclass=user)'
        attrs = ['distinguishedName','objectGUID','objectSid','cn','accountExpires','adminCount','badPasswordTime','badPwdCount','description','displayName','isCriticalSystemObject','lastLogoff','lastLogon','lastLogonTimestamp','logonCount','logonHours','name','primaryGroupID','pwdLastSet','sAMAccountName','sAMAccountType','uSNChanged','uSNCreated','userAccountControl','whenChanged','whenCreated','memberOf','proxyAddresses']
        ad_help = ActiveDirectoryHelper()

        # return json object containing all user records
        results = ad_help.search(parameters,filter,attrs)

        #print results
        ldap_json = json.loads(results)

        for key, value in ldap_json.iteritems():
            print key

        attributes = ldap_json['entries']

        for key,value in attributes:
            print key

        #for v in attributes:
        #    print v

            # new_attrs = {}
            # groups = []
            # gen_groups = []
            # email_addresses = []
            # new_attrs.update(v.get_attributes())
            # for key, values in new_attrs.iteritems():
            #     if len(values) >  0:
            #         if key == 'memberOf':
            #             for cn in values:
            #                 qs = ActiveDirectoryGroup.objects.filter(ldap_configuration=parameters,distinguishedName=cn)
            #                 for q in qs:
            #                     groups.append(q)
            #                     if q.group:
            #                         gen_groups.append(q.group)
            #         elif key == 'proxyAddresses':
            #             for address in values:
            #                 if address[:5].lower() == 'smtp:':
            #                     email_addresses.append(address[5:])
            #         else:
            #             value = ' '.join(values)
            #
            #             try:
            #                 new_attrs[key] = value.decode('utf-8')
            #
            #                 if key in ('accountExpires','badPasswordTime','lastLogoff','lastLogon','lastLogonTimestamp','pwdLastSet','uSNChanged','uSNCreated','whenChanged','whenCreated'):
            #                     date = self.convert_date_time(new_attrs[key])
            #                     if date:
            #                         new_attrs[key] = date.isoformat()
            #             except UnicodeDecodeError:
            #                 new_attrs[key] = self.cleanhex(value)
            #
            # new_attrs.pop('memberOf',None)
            # new_attrs.pop('proxyAddresses',None)
            #
            # # Don't filter on everything. Start with the properties that are
            # # least likely to ever change, then work towards the more mutable
            # # properties.
            # filter_attrs = {}
            # if 'objectGUID' in new_attrs:
            #     filter_attrs['objectGUID'] = new_attrs['objectGUID']
            # elif 'objectSid' in new_attrs:
            #     filter_attrs['objectSid'] = new_attrs['objectSid']
            # elif 'distinguishedName' in new_attrs:
            #     filter_attrs['distinguishedName'] = new_attrs['distinguishedName']
            # else:
            #     continue
            #
            # # If no matching user currently exists then create one, otherwise
            # # update the existing user.
            # ad_user = None
            # ad_users = ActiveDirectoryUser.objects.filter(**filter_attrs)
            # if ad_users.count() == 0:
            #     ad_user = ActiveDirectoryUser.objects.create(ldap_configuration=parameters,**new_attrs)
            #     ad_user.save()
            # else:
            #     ad_users.update(**new_attrs)
            #     ad_user = ad_users.first()
            #
            # identity, created = Identity.objects.get_or_create(name=ad_user.displayName)
            # '''
            # TODO Do we need to create a person object for this identity??
            # '''
            # #Person.objects.get_or_create(firstname=firstname,surname=surname, identity=identity)
            #
            # Identifier.objects.get_or_create(identifier=ad_user.sAMAccountName, identifiertype=Identifier.UNAME,identity=identity)
            #
            # # Import the email addresses.
            # for email_address in email_addresses:
            #     Identifier.objects.get_or_create(identifier=email_address, identifiertype=Identifier.EMAIL, identity=identity)
            #
            # for group in groups:
            #     #print groups
            #     if ad_user.groups.filter(id=group.id).count() == 0:
            #         ad_user.groups.add(group)
            #
            # for gen_group in gen_groups:
            #     #print gen_group.id
            #     if identity.groups.filter(id=gen_group.id).count() == 0:
            #         identity.groups.add(gen_group)


class ActiveDirectoryGroup(TimeStampedModel):
    cn = models.CharField(max_length = 300)
    distinguishedName = models.CharField(max_length = 300, unique=True)
    name = models.CharField(max_length = 100)
    objectCategory = models.CharField(max_length = 300)
    sAMAccountName = models.CharField(max_length = 300)
    objectGUID = models.CharField(max_length = 300)
    objectSid = models.CharField(max_length = 300)
    ldap_configuration = models.ForeignKey('LDAPConfiguration')
    group = models.ForeignKey('ava_core_group.Group', null=True, blank=True)

    def __unicode__(self):
        return self.cn or u''

    def get_absolute_url(self):
        return reverse('ad-group-detail',kwargs={'pk': self.id})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in ActiveDirectoryGroup._meta.fields]

    def getGroups(self,parameters):
        filter = '(objectclass=group)'
        attrs = ['distinguishedName','objectGUID','objectSid','cn','name','objectCategory','sAMAccountName']
        ad_help = ActiveDirectoryHelper()
        results = ad_help.search(parameters,filter,attrs)
        for  v in results:
            new_attrs = {}
            new_attrs.update(v.get_attributes())
            for key, value in new_attrs.iteritems():
                if len(value) >  0:
                    value = ' '.join(value)

                    try:
                        new_attrs[key] = value.decode('utf-8')
                    except UnicodeDecodeError:
                        new_attrs[key] = self.cleanhex(value)

            # Don't filter on everything. Start with the properties that are
            # least likely to ever change, then work towards the more mutable
            # properties.
            filter_attrs = {}
            if 'objectGUID' in new_attrs:
                filter_attrs['objectGUID'] = new_attrs['objectGUID']
            elif 'objectSid' in new_attrs:
                filter_attrs['objectSid'] = new_attrs['objectSid']
            elif 'distinguishedName' in new_attrs:
                filter_attrs['distinguishedName'] = new_attrs['distinguishedName']
            else:
                continue

            # If no matching group currently exists then create one, otherwise
            # update the existing group.
            ad_groups = ActiveDirectoryGroup.objects.filter(**filter_attrs)
            if ad_groups.count() == 0:
                ad_group = ActiveDirectoryGroup.objects.create(ldap_configuration=parameters, **new_attrs)

                gen_group = Group.objects.create(name=ad_group.cn, group_type=Group.AD, description="Imported group from LDAP")
                gen_group.save()

                ad_group.group = gen_group
                ad_group.save()
            else:
                ad_groups.update(**new_attrs)
                ad_group = ad_groups.first()

                gen_group = ad_group.group
                if gen_group:
                    gen_group.name = ad_group.cn
                    gen_group.save()

    class Meta:
        unique_together = ('objectGUID','objectSid')
        ordering = ['cn', 'distinguishedName']


class LDAPConfiguration(TimeStampedModel):
    #user_dn = "cn=Administrator,cn=Users,dc=ava,dc=test,dc=domain"
    #user_pw = "Password1"
    #dump_dn = "dc=ava,dc=test,dc=domain"
    #server = 'ldap://dc.ava.test.domain'
    user_dn = models.CharField(max_length = 100, verbose_name='User')
    user_pw = models.CharField(max_length = 100, verbose_name='Password')
    dump_dn = models.CharField(max_length = 100, verbose_name='Domain')
    server = models.CharField(max_length = 100, verbose_name='Server')

    def __unicode__(self):
        return self.server or u''

    class Meta:
        unique_together=('server','user_dn')

    def get_absolute_url(self):
        return reverse('ldap-configuration-detail',kwargs={'pk': self.id})


class ExportLDAP():
    def generateGraph(self,parameters):
        node_results = self.nodes(parameters)
        return self.edges(node_results)

    def nodes(self, parameters):
        nodes = []
        elements = []
        ldap_users = ActiveDirectoryUser.objects.filter(ldap_configuration=parameters)
        user_fields = ['id','accountExpires','adminCount','name','isCriticalSystemObject','lastLogon','logonCount','pwdLastSet']
        for user in ldap_users:
            elements.append(user)
            current = self.model_to_dict(user,user_fields)
            current['name']=escape(current['name'])
            current['node_type'] = 'user'
            nodes.append(current)

        ldap_groups = ActiveDirectoryGroup.objects.filter(ldap_configuration=parameters)
        group_fields = ['id','cn']
        for group in ldap_groups:
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
            if isinstance(value,ActiveDirectoryGroup):
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
