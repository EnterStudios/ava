from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from ava.import_google import views

urlpatterns = patterns(
    '',
    url(r'^import/$', login_required(views.GoogleDirectoryImport.as_view()),
        name='google-import'),
    url(r'^users/$', login_required(views.GoogleDirectoryUserIndex.as_view()),
        name='google-user-index'),
    url(r'^users/(?P<pk>\d+)/view/$', login_required(views.GoogleDirectoryUserDetail.as_view()),
        name='google-user-detail'),
    url(r'^users/(?P<pk>\d+)/delete/$', login_required(views.GoogleDirectoryUserDelete.as_view()),
        name='google-user-delete'),
)
