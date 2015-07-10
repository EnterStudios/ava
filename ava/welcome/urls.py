from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns(
    '',
    url('^first-user/$', views.CreateFirstUser.as_view(), name='welcome-first-user'),
    url('^import-selection/$', views.ImportSelection.as_view(), name='welcome-import-selection'),
    url('^import-ldap/$', views.ImportLDAP.as_view(), name='welcome-import-ldap'),
    url('^import-progress/$', views.ImportProgress.as_view(), name='welcome-import-progress'),
)
