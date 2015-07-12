# flake8: noqa

from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView
from django.http import HttpResponseRedirect, HttpResponseBadRequest, JsonResponse
from oauth2client.django_orm import Storage

from ava.import_google.google_apps_interface import GoogleAppsHelper
from ava.import_google.models import CredentialsModel, GoogleDirectoryUser, GoogleDirectoryGroup, FlowModel


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
    model = GoogleDirectoryUser


def google_directory_authorize_import(request):
    user = request.user
    gd_helper = GoogleAppsHelper()
    storage = Storage(CredentialsModel, 'id', user, 'credential')
    credential = storage.get()

    oauth_flow = gd_helper.get_flow()
    if credential is None or credential.invalid is True:
        # oauth_flow.params['state'] = gd_helper.generate_xsrf_token(user)
        authorize_url = oauth_flow.step1_get_authorize_url()
        f = FlowModel(id=user, flow=oauth_flow)
        f.save()
        return HttpResponseRedirect(authorize_url)
    else:
        directory_service = gd_helper.build_directory_service(credential)
        results = gd_helper.import_google_directory(directory_service)
        return JsonResponse(results)


def google_directory_auth_return(request):
    user = request.user
    gd_helper = GoogleAppsHelper()
    # if not gd_helper.validate_xsrf_token(request):
    #     return HttpResponseBadRequest()
    oauth_flow = FlowModel.objects.get(id=user).flow
    print(oauth_flow)
    credential = oauth_flow.step2_exchange(request.REQUEST)
    storage = Storage(CredentialsModel, 'id', user, 'credential')
    storage.put(credential)
    return HttpResponseRedirect("/google/auth/")
