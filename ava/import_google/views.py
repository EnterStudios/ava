# flake8: noqa

from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView

from ava.core_google_apps.models import *
from ava.core_google_apps.forms import GoogleConfigurationForm


class GoogleConfigurationIndex(ListView):
    template_name = 'google_apps/GoogleConfiguration_index.html'
    context_object_name = 'Google_configuration_list'

    def get_queryset(self):
        return GoogleConfiguration.objects.all()


class GoogleConfigurationDetail(DetailView):
    model = GoogleConfiguration
    context_object_name = 'Google_configuration'
    template_name = 'google_apps/GoogleConfiguration_detail.html'


class GoogleConfigurationCreate(CreateView):
    model = GoogleConfiguration
    template_name = 'google_apps/GoogleConfiguration.html'
    form_class = GoogleConfigurationForm


class GoogleConfigurationUpdate(UpdateView):
    model = GoogleConfiguration
    template_name = 'google_apps/GoogleConfiguration.html'
    form_class = GoogleConfigurationForm


class GoogleConfigurationDelete(DeleteView):
    model = GoogleConfiguration
    template_name = 'confirm_delete.html'
    success_url = '/Google/'


class GoogleDirectoryUserIndex(ListView):
    model = GoogleDirectoryUser
    template_name = 'google_apps/GoogleDirectoryUser_index.html'

    def get_context_data(self, **kwargs):
        context = super(GoogleDirectoryUserIndex, self).get_context_data(**kwargs)
        config_pk = self.kwargs.get('pk')
        if config_pk:
            instance = get_object_or_404(GoogleConfiguration, pk=config_pk)
            context['Google_user_list'] = GoogleDirectoryUser.objects.filter(Google_configuration=instance)
            context['Google_configuration'] = instance
        return context


class GoogleDirectoryUserDetail(DetailView):
    model = GoogleDirectoryUser
    context_object_name = 'activedirectoryuser'
    template_name = 'google_apps/GoogleDirectoryUser_detail.html'


class GoogleDirectoryUserCreate(CreateView):
    model = GoogleDirectoryUser
    template_name = 'google_apps/GoogleDirectoryUser.html'
    form_class = GoogleConfigurationForm


class GoogleDirectoryUserUpdate(UpdateView):
    model = GoogleDirectoryUser
    template_name = 'google_apps/GoogleDirectoryUser.html'
    form_class = GoogleConfigurationForm


class GoogleDirectoryUserDelete(DeleteView):
    model = GoogleDirectoryUser
    template_name = 'confirm_delete.html'
    success_url = '/Google/'


class GoogleDirectoryGroupIndex(ListView):
    model = GoogleDirectoryGroup
    template_name = 'google_apps/GoogleDirectoryGroup_index.html'

    def get_context_data(self, **kwargs):
        context = super(GoogleDirectoryGroupIndex, self).get_context_data(**kwargs)
        config_pk = self.kwargs.get('pk')
        if config_pk:
            instance = get_object_or_404(GoogleConfiguration, pk=config_pk)
            context['Google_group_list'] = GoogleDirectoryGroup.objects.filter(Google_configuration=instance)
            context['Google_configuration'] = instance
        return context


class GoogleDirectoryGroupDetail(DetailView):
    model = GoogleDirectoryGroup
    context_object_name = 'activedirectorygroup'
    template_name = 'google_apps/GoogleDirectoryGroup_detail.html'


class GoogleDirectoryGroupCreate(CreateView):
    model = GoogleDirectoryGroup
    template_name = 'google_apps/GoogleDirectoryGroup.html'
    form_class = GoogleConfigurationForm


class GoogleDirectoryGroupUpdate(UpdateView):
    model = GoogleDirectoryGroup
    template_name = 'google_apps/GoogleDirectoryGroup.html'
    form_class = GoogleConfigurationForm


class GoogleDirectoryGroupDelete(DeleteView):
    model = GoogleDirectoryGroup
    template_name = 'confirm_delete.html'
    success_url = '/Google/'


class GoogleConfigurationGetUsers(ListView):
    model = GoogleDirectoryUser
    context_object_name = 'activedirectoryuser_list'
    template_name = 'google_apps/GoogleDirectoryUser_index.html'

    def get_context_data(self, **kwargs):
        self.get_users()
        context = super(GoogleConfigurationGetUsers, self).get_context_data(**kwargs)
        config_pk = self.kwargs.get('pk')
        if config_pk:
            instance = get_object_or_404(GoogleConfiguration, pk=config_pk)
            context['activedirectoryuser_list'] = GoogleDirectoryUser.objects.filter(Google_configuration=instance)
        return context

    def get_users(self):
        config_pk = self.kwargs.get('pk')
        if config_pk:
            instance = get_object_or_404(GoogleConfiguration, pk=config_pk)
            adHelper = GoogleDirectoryHelper()
            adHelper.get_users(instance)

        return True


class GoogleConfigurationGetGroups(ListView):
    model = GoogleDirectoryGroup
    context_object_name = 'activedirectorygroup_list'
    template_name = 'google_apps/GoogleDirectoryGroup_index.html'

    def get_context_data(self, **kwargs):
        self.get_groups()
        context = super(GoogleConfigurationGetGroups, self).get_context_data(**kwargs)
        config_pk = self.kwargs.get('pk')
        if config_pk:
            instance = get_object_or_404(GoogleConfiguration, pk=config_pk)
            context['activedirectorygroup_list'] = GoogleDirectoryGroup.objects.filter(Google_configuration=instance)
        return context

    def get_groups(self):
        config_pk = self.kwargs.get('pk')
        if config_pk:
            instance = get_object_or_404(GoogleConfiguration, pk=config_pk)
            adHelper = GoogleDirectoryHelper()
            adHelper.get_groups(instance)
