from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from apps.ava_test_email import views


urlpatterns = patterns('',
    url(r'^$', login_required(views.EmailTestIndex.as_view()), name='email-test-index'),
    url(r'^new/$', login_required(views.EmailTestCreate.as_view()), name='email-test-new'),
    url(r'^(?P<pk>\d+)/$', login_required(views.EmailTestDetail.as_view()), name="email-test-detail"),
    url(r'^(?P<pk>\d+)/update/$', login_required(views.EmailTestUpdate.as_view()),name='email-test-update'),
    url(r'^(?P<pk>\d+)/delete/$', login_required(views.EmailTestDelete.as_view()),name='email-test-delete'),
    url(r'^send/(?P<pk>\d+)/$', login_required(views.EmailSendEmail.as_view()), name='email-test-send'),
)
