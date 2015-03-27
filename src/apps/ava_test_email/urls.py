from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from apps.ava_test.decorators import create_test_access_check
from apps.ava_test_email.decorators import email_test_access_check
from apps.ava_test_email import views
from apps.ava_core_project.models import ProjectAccess


urlpatterns = patterns('',
    url(r'^$', login_required(views.EmailTestIndex.as_view()), name='email-test-index'),
    url(r'^new/(?P<proj>\d+)/$', create_test_access_check('proj', ProjectAccess.RUN_TEST, views.EmailTestCreate.as_view()), name='email-test-create'),
    url(r'^(?P<pk>\d+)/$', email_test_access_check(ProjectAccess.VIEW, views.EmailTestDetail.as_view()), name="email-test-detail"),
    url(r'^(?P<pk>\d+)/update/$', email_test_access_check(ProjectAccess.RUN_TEST, views.EmailTestUpdate.as_view()),name='email-test-update'),
    url(r'^(?P<pk>\d+)/delete/$', email_test_access_check(ProjectAccess.RUN_TEST, views.EmailTestDelete.as_view()),name='email-test-delete'),
    url(r'^send/(?P<pk>\d+)/$', email_test_access_check(ProjectAccess.RUN_TEST, views.EmailSendEmail.as_view()), name='email-test-send'),
)
