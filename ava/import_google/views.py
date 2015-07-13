# flake8: noqa
from django.core.urlresolvers import reverse

from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView

from ava.google_auth.views import retrieve_credential_from_session, django
from ava.import_google.google_apps_interface import GoogleDirectoryHelper
from ava.import_google.models import GoogleDirectoryUser, GoogleDirectoryGroup, GoogleConfiguration



class GoogleDirectoryUserIndex(ListView):
    model = GoogleDirectoryUser
    template_name = 'google_apps/GoogleDirectoryUser_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['google_user_list'] = GoogleDirectoryUser.objects.all()
        return context


class GoogleDirectoryUserDetail(DetailView):
    model = GoogleDirectoryUser
    context_object_name = 'googledirectoryuser'
    template_name = 'google_apps/GoogleDirectoryUser_detail.html'


class GoogleDirectoryUserDelete(DeleteView):
    model = GoogleDirectoryUser
    template_name = 'confirm_delete.html'
    success_url = reverse('google-user-index')


class GoogleDirectoryGroupIndex(ListView):
    model = GoogleDirectoryGroup
    template_name = 'google_apps/GoogleDirectoryGroup_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['google_group_list'] = GoogleDirectoryGroup.objects.all()
        return context


class GoogleDirectoryGroupDetail(DetailView):
    model = GoogleDirectoryGroup
    context_object_name = 'googledirectorygroup'
    template_name = 'google_apps/GoogleDirectoryGroup_detail.html'


class GoogleDirectoryGroupDelete(DeleteView):
    model = GoogleDirectoryGroup
    template_name = 'confirm_delete.html'
    success_url = reverse('google-group-index')


class GoogleDirectoryImport(django.views.generic.View):

    def get(self, request):
        credential = retrieve_credential_from_session(request)
        gd_helper = GoogleDirectoryHelper()

        # this is a mess. figure out whether we actually need multiple google domains/configs
        google_config = GoogleConfiguration()
        google_config.domain="test"
        google_config.save()

        # import the directory information from google
        import_data = gd_helper.import_google_directory(credential)

        # parse and store the users
        gd_user = GoogleDirectoryUser()
        gd_user.import_from_json(google_config, import_data['users'])

        # parse and store the groups
        gd_group = GoogleDirectoryGroup()
        gd_group.import_from_json(google_config, import_data['groups'])

        return django.http.HttpResponseRedirect(reverse('google-user-index'))

