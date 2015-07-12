from django.conf.urls import patterns, include, url
from django.contrib import admin
from dh5bp.urls import urlpatterns as dh5bp_urls
from django.contrib.auth.decorators import login_required
from ava.core.views import DashboardView

admin.autodiscover()

handler404 = 'dh5bp.views.page_not_found'
handler500 = 'dh5bp.views.server_error'

urlpatterns = patterns(
    '',
    url(r'^$', login_required(DashboardView.as_view()), name='index'),
    url(r'^ava/', include('ava.core.urls')),
    url(r'^project/', include('ava.core_project.urls')),
    url(r'^accounts/', include('ava.core_auth.urls')),
    url(r'^group/', include('ava.core_group.urls')),
    url(r'^ldap/', include('ava.import_ldap.urls')),
    url(r'^people/', include('ava.core_identity.urls')),
    url(r'^graph/', include('ava.vis_graph.urls')),
    url(r'^test/', include('ava.test.urls')),
    url(r'^test/email/', include('ava.test_email.urls')),
    url(r'^test/twitter/', include('ava.test_twitter.urls')),
    url(r'^go/', include('ava.test_tracking.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^welcome/', include('ava.welcome.urls')),
)
urlpatterns += dh5bp_urls
