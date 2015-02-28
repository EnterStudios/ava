from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, DetailView
from django.shortcuts import get_object_or_404
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from apps.ava_core_ldap.models import ActiveDirectoryUser, ActiveDirectoryGroup, LDAPConfiguration, ActiveDirectoryHelper
from apps.ava_core_ldap.forms import  LDAPConfigurationForm
from apps.ava_core_identity.models import Identifier
from apps.ava_core_org.models import OrganisationGroup, GroupIdentifier


class LDAPConfigurationIndex(ListView):
    template_name = 'ldap/LDAPConfiguration_index.html'
    context_object_name = 'ldap_configuration_list'

    def get_queryset(self):
        """Return the last five created people."""
        return LDAPConfiguration.objects.all()

class LDAPConfigurationDetail(DetailView):
    model = LDAPConfiguration
    context_object_name = 'ldap_configuration'
    template_name = 'ldap/LDAPConfiguration_detail.html'

class LDAPConfigurationCreate(CreateView):
    model = LDAPConfiguration
    template_name = 'ldap/LDAPConfiguration.html'
    form_class = LDAPConfigurationForm

class LDAPConfigurationUpdate(UpdateView):
        model = LDAPConfiguration
        template_name = 'ldap/LDAPConfiguration.html'
        form_class = LDAPConfigurationForm

class LDAPConfigurationDelete(DeleteView):
        model = LDAPConfiguration
        template_name = 'confirm_delete.html'
        success_url = '/ldap/'



class ActiveDirectoryUserIndex(ListView):
    model = ActiveDirectoryUser
    template_name = 'ldap/itemindex.html'

    def get_context_data(self, **kwargs):
        context = super(ActiveDirectoryUserIndex, self).get_context_data(**kwargs)
        config_pk = self.kwargs.get('pk')
        if config_pk:
            instance = get_object_or_404(LDAPConfiguration, pk=config_pk)
            context['ldap_user_list'] = ActiveDirectoryUser.objects.filter(ldapConfiguration=instance)
        return context

class ActiveDirectoryUserDetail(DetailView):
    model = LDAPConfiguration
    context_object_name = 'activedirectoryuser'
    template_name = 'ldap/view.html'

class ActiveDirectoryUserCreate(CreateView):
    model = LDAPConfiguration
    template_name = 'ldap/ActiveDirectoryUser.html'
    form_class = LDAPConfigurationForm

class ActiveDirectoryUserUpdate(UpdateView):
        model = LDAPConfiguration
        template_name = 'ldap/ActiveDirectoryUser.html'
        form_class = LDAPConfigurationForm

class ActiveDirectoryUserDelete(DeleteView):
        model = LDAPConfiguration
        template_name = 'confirm_delete.html'
        success_url = '/ldap/'



class ActiveDirectoryGroupIndex(ListView):
    model = ActiveDirectoryGroup
    template_name = 'ldap/itemindex.html'

    def get_context_data(self, **kwargs):
        context = super(ActiveDirectoryGroupIndex, self).get_context_data(**kwargs)
        config_pk = self.kwargs.get('pk')
        if config_pk:
            instance = get_object_or_404(LDAPConfiguration, pk=config_pk)
            context['ldap_group_list'] = ActiveDirectoryGroup.objects.filter(ldapConfiguration=instance)
        return context

class ActiveDirectoryGroupDetail(DetailView):
    model = LDAPConfiguration
    context_object_name = 'activedirectorygroup'
    template_name = 'ldap/view.html'

class ActiveDirectoryGroupCreate(CreateView):
    model = LDAPConfiguration
    template_name = 'ldap/ActiveDirectoryGroup.html'
    form_class = LDAPConfigurationForm

class ActiveDirectoryGroupUpdate(UpdateView):
        model = LDAPConfiguration
        template_name = 'ldap/ActiveDirectoryGroup.html'
        form_class = LDAPConfigurationForm

class ActiveDirectoryGroupDelete(DeleteView):
        model = LDAPConfiguration
        template_name = 'confirm_delete.html'
        success_url = '/ldap/'








class LDAPConfigurationGetUsers(ListView):
    model = ActiveDirectoryUser
    template_name = 'ldap/items.html'

    def get_context_data(self, **kwargs):
        context = super(LDAPConfigurationGetUsers, self).get_context_data(**kwargs)
        config_pk = self.kwargs.get('pk')
        if config_pk:
            instance = get_object_or_404(LDAPConfiguration, pk=config_pk)
            adHelper = ActiveDirectoryHelper()
            adHelper.getUsers(instance)
             
        context['item_type'] = 'user'
        context['ldap_item_list'] = ActiveDirectoryUser.objects.filter(ldapConfiguration=instance)
        return context

class LDAPConfigurationGetAll(ListView):
    model = ActiveDirectoryUser
    template_name = 'ldap/items.html'

    def get_context_data(self, **kwargs):
        context = super(LDAPConfigurationGetAll, self).get_context_data(**kwargs)
        config_pk = self.kwargs.get('pk')
        if config_pk:
            instance = get_object_or_404(LDAPConfiguration, pk=config_pk)
            adHelper = ActiveDirectoryHelper()
            adHelper.getUsers(instance)
            adHelper.getGroups(instance)
            adHelper.getUsers(instance)
             
        context['item_type'] = 'user'
        ad_groups = ActiveDirectoryGroup.objects.filter(ldapConfiguration=instance)

        for adg in ad_groups:
            try:
                org_g = OrganisationGroup.objects.get(name=adg.cn)
                groups = adg.member.all()
                for g in groups:
                    try:
                        user = Identifier.objects.get(identifier=g.sAMAccountName,identifiertype=Identifier.UNAME)
                        GroupIdentifier.objects.get_or_create(identifier=user, group=org_g)
                        user1 = Identifier.objects.get(identifier=g.sAMAccountName+"@avasecure.com",identifiertype=Identifier.EMAIL)
                        GroupIdentifier.objects.get_or_create(identifier=user1, group=org_g)
                    except Identifier.DoesNotExist:
                        print " No such id :: " + g.sAMAccountName


            except OrganisationGroup.DoesNotExist:
                print "No such group :: " + adg.cn

        context['ldap_item_list'] = ActiveDirectoryUser.objects.filter(ldapConfiguration=instance)
        return context

class LDAPConfigurationGetGroups(ListView):
    model = ActiveDirectoryGroup
    template_name = 'ldap/items.html'

    def get_context_data(self, **kwargs):
        context = super(LDAPConfigurationGetGroups, self).get_context_data(**kwargs)
        config_pk = self.kwargs.get('pk')
        if config_pk:
            instance = get_object_or_404(LDAPConfiguration, pk=config_pk)
            adHelper = ActiveDirectoryHelper()
            adHelper.getGroups(instance)
        
        context['item_type'] = 'group'
        context['ldap_item_list'] = ActiveDirectoryGroup.objects.filter(ldapConfiguration=instance)
        return context



