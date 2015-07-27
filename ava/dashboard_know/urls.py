from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from ava.dashboard_know import views

urlpatterns = patterns(
    '',
    url(r'^$', login_required(views.KnowDashboardView.as_view()), name='know-dashboard'),
)
