# flake8: noqa

from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView
from django.http import HttpResponseRedirect
from oauth2client.django_orm import Storage


from ava.import_google.google_apps_interface import GoogleAppsHelper
from ava.import_google.models import CredentialsModel, GoogleDirectoryUser, GoogleDirectoryGroup


class GoogleDirectoryUserIndex(ListView):
    model = GoogleDirectoryUser
    template_name = 'google_apps/GoogleDirectoryUser_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Google_user_list'] = GoogleDirectoryUser.objects.all()
        return context


class GoogleDirectoryUserDetail(DetailView):
    model = GoogleDirectoryUser
    context_object_name = 'activedirectoryuser'
    template_name = 'google_apps/GoogleDirectoryUser_detail.html'


class GoogleDirectoryUserDelete(DeleteView):
    model = GoogleDirectoryUser
    template_name = 'confirm_delete.html'
    success_url = '/Google/'


class GoogleDirectoryGroupIndex(ListView):
    model = GoogleDirectoryGroup
    template_name = 'google_apps/GoogleDirectoryGroup_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Google_group_list'] = GoogleDirectoryGroup.objects.all()
        return context


class GoogleDirectoryGroupDetail(DetailView):
    model = GoogleDirectoryGroup
    context_object_name = 'activedirectorygroup'
    template_name = 'google_apps/GoogleDirectoryGroup_detail.html'


class GoogleDirectoryGroupDelete(DeleteView):
    model = GoogleDirectoryGroup
    template_name = 'confirm_delete.html'
    success_url = '/Google/'


class GoogleDirectoryImport(ListView):
    template_name = 'google_apps/import.html'
    model = GoogleAppsHelper


def google_directory_authorize_import(request):
    gd_helper = GoogleAppsHelper()
    storage = Storage(CredentialsModel, 'id', request.user, 'credential')
    credential = storage.get()

    if credential is None or credential.invalid is True:
        authorize_url = gd_helper.get_auth_url()
        return HttpResponseRedirect(authorize_url)
    else:
        gd_helper.build_directory_service(credential)


    # def auth_return(self, request):
    #     credential = self.gd_helper.generate_credential(request.REQUEST['state'], request.user, request.REQUEST)
    #     if not credential:
    #         return HttpResponseBadRequest()
    #     storage = Storage(CredentialsModel, 'id', request.user, 'credential')
    #     storage.put(credential)
    #     return HttpResponseRedirect("/")

