from django.conf.urls import include, patterns, url
from django.contrib.auth.decorators import login_required

from apps.ava_test_email import views

urlpatterns = patterns('',
    
    url(r'^$', login_required(views.EmailTestIndexView.as_view()), name='emailtestindex'),
    url(r'^(?P<pk>\d+)/$', login_required(views.EmailTestIndexView.as_view()), name='emailtest'),
    url(r'^(?P<pk>\d+)/view/$', login_required(views.EmailTestDetailView.as_view()), name='emailtest_view'),
    url(r'^new/$',login_required(views.EmailTestCreate.as_view()),name='emailtest_new'),
    url(r'^(?P<pk>\d+)/update/$', login_required(views.EmailTestUpdateView.as_view()), name='emailtest_update'),
    url(r'^(?P<pk>\d+)/delete/$', login_required(views.EmailTestDeleteView.as_view()), name='emailtest_delete'),
    url(r'^send/$', login_required(views.EmailSendEmailView.as_view()), name='emailsend'),
)
