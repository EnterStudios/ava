from django.conf.urls import patterns, url

from ava.utils import require_ava_superuser
from . import views


urlpatterns = patterns(
    '',
    url('^first-user/$', views.CreateFirstUser.as_view(), name='welcome-first-user'),
    url('^import-selection/$', require_ava_superuser(views.ImportSelection.as_view()), name='welcome-import-selection'),
    url('^import-ldap/$', require_ava_superuser(views.ImportLDAP.as_view()), name='welcome-import-ldap'),
    url('^import-google/$', require_ava_superuser(views.ImportGoogle.as_view()), name='welcome-import-google'),
    url('^import-progress/$', require_ava_superuser(views.ImportProgress.as_view()), name='welcome-import-progress'),
)
