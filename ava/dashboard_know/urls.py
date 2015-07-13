from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from ava.test import views


urlpatterns = patterns(
    '',
    url(r'^$', login_required(views.KnowDashboardView.as_view()), name='know-dashboard'),
)
