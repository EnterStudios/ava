from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, DetailView
from django.shortcuts import get_object_or_404
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from apps.ava_core_ldap.models import ActiveDirectoryUser, ActiveDirectoryGroup, QueryParameters, ActiveDirectoryHelper
from apps.ava_core_ldap.forms import  QueryParametersForm
from apps.ava_core_identity.models import Identifier
from apps.ava_core_org.models import GroupIdentifier, OrganisationGroup


class ConfigurationIndexView(ListView):
    template_name = 'ldap/index.html'
    context_object_name = 'ldap_config_list'

    def get_queryset(self):
        """Return the last five created people."""
        return QueryParameters.objects.filter(user=self.request.user)

class ConfigurationUserView(ListView):
    model = ActiveDirectoryUser
    template_name = 'ldap/itemindex.html'

    def get_context_data(self, **kwargs):
        context = super(ConfigurationUserView, self).get_context_data(**kwargs)
        config_pk = self.kwargs.get('pk')
        if config_pk:
            instance = get_object_or_404(QueryParameters, pk=config_pk)
            context['ldap_user_list'] = ActiveDirectoryUser.objects.filter(queryParameters=instance,user=self.request.user)
        return context

class ConfigurationGroupView(ListView):
    model = ActiveDirectoryGroup
    template_name = 'ldap/itemindex.html'

    def get_context_data(self, **kwargs):
        context = super(ConfigurationGroupView, self).get_context_data(**kwargs)
        config_pk = self.kwargs.get('pk')
        if config_pk:
            instance = get_object_or_404(QueryParameters, pk=config_pk)
            context['ldap_group_list'] = ActiveDirectoryGroup.objects.filter(queryParameters=instance,user=self.request.user)
        return context

class ConfigurationItemView(ListView):
    model = ActiveDirectoryUser
    template_name = 'ldap/itemindex.html'

    def get_context_data(self, **kwargs):
        context = super(ConfigurationItemView, self).get_context_data(**kwargs)
        config_pk = self.kwargs.get('pk')
        if config_pk:
            instance = get_object_or_404(QueryParameters, pk=config_pk)
            context['ldap_user_list'] = ActiveDirectoryUser.objects.filter(queryParameters=instance,user=self.request.user)
            context['ldap_group_list'] = ActiveDirectoryGroup.objects.filter(queryParameters=instance,user=self.request.user)

        return context

class ConfigurationDetailView(DetailView):
    model = QueryParameters
    context_object_name = 'ldap_config'
    template_name = 'ldap/view.html'

class ConfigurationUpdateView(UpdateView):
        model = QueryParameters
        template_name = 'ldap/configuration.html'
        form_class = QueryParametersForm
        success_url = '/ldap/'

class ConfigurationGetUsers(ListView):
    model = ActiveDirectoryUser
    template_name = 'ldap/items.html'

    def get_context_data(self, **kwargs):
        context = super(ConfigurationGetUsers, self).get_context_data(**kwargs)
        config_pk = self.kwargs.get('pk')
        if config_pk:
            instance = get_object_or_404(QueryParameters, pk=config_pk)
            adHelper = ActiveDirectoryHelper()
            adHelper.getUsers(instance,self.request.user,instance.organisation)
             
        context['item_type'] = 'user'
        context['ldap_item_list'] = ActiveDirectoryUser.objects.filter(queryParameters=instance,user=self.request.user)
        return context

class ConfigurationGetAll(ListView):
    model = ActiveDirectoryUser
    template_name = 'ldap/items.html'

    def get_context_data(self, **kwargs):
        context = super(ConfigurationGetAll, self).get_context_data(**kwargs)
        config_pk = self.kwargs.get('pk')
        if config_pk:
            instance = get_object_or_404(QueryParameters, pk=config_pk)
            adHelper = ActiveDirectoryHelper()
            adHelper.getUsers(instance,self.request.user,instance.organisation)
            adHelper.getGroups(instance,self.request.user,instance.organisation)
            adHelper.getUsers(instance,self.request.user,instance.organisation)
             
        context['item_type'] = 'user'
        ad_groups = ActiveDirectoryGroup.objects.filter(queryParameters=instance, user=self.request.user)

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

        context['ldap_item_list'] = ActiveDirectoryUser.objects.filter(queryParameters=instance,user=self.request.user)
        return context

class ConfigurationGetGroups(ListView):
    model = ActiveDirectoryGroup
    template_name = 'ldap/items.html'

    def get_context_data(self, **kwargs):
        context = super(ConfigurationGetGroups, self).get_context_data(**kwargs)
        config_pk = self.kwargs.get('pk')
        if config_pk:
            instance = get_object_or_404(QueryParameters, pk=config_pk)
            adHelper = ActiveDirectoryHelper()
            adHelper.getGroups(instance,self.request.user,instance.organisation)
        
        context['item_type'] = 'group'
        context['ldap_item_list'] = ActiveDirectoryGroup.objects.filter(queryParameters=instance,user=self.request.user)
        return context

class ConfigurationDeleteGroup(DeleteView):
        model = ActiveDirectoryGroup
        template_name = 'confirm_delete.html'
        success_url = '/ldap/'

class ConfigurationDeleteUser(DeleteView):
        model = ActiveDirectoryUser
        template_name = 'confirm_delete.html'
        success_url = '/ldap/'

class ConfigurationDeleteView(DeleteView):
        model = QueryParameters
        template_name = 'confirm_delete.html'
        success_url = '/ldap/'

class ConfigurationCreateView(CreateView):
    model = QueryParameters
    template_name = 'ldap/configuration.html'
    form_class = QueryParametersForm
    page_title = 'create'
    button_value = 'Add Configuration'

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(
            self.get_context_data(form=form,
                                  page_title=self.page_title,button_value=self.button_value))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        dependancyList = form.save(commit=False)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        """
        Called if all forms are valid. Creates an instance along with
        associated items and then redirects to a
        success page.
        """
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  page_title=self.page_title,button_value=self.button_value))
