from django.conf.urls import patterns, include, url
from django.contrib import admin
from dh5bp.urls import urlpatterns as dh5bp_urls
from django.contrib.auth.decorators import login_required
from apps.ava_core_identity.views import IdentityIndex

admin.autodiscover()

handler404 = 'dh5bp.views.page_not_found'
handler500 = 'dh5bp.views.server_error'

urlpatterns = patterns('',
    url(r'^$', login_required(IdentityIndex.as_view()), name='index'),
    url(r'^ava/', include('apps.ava_core.urls')),
    url(r'^project/', include('apps.ava_core_project.urls')),
    url(r'^accounts/', include('apps.ava_core_auth.urls')),
    url(r'^ldap/', include('apps.ava_core_ldap.urls')),
    url(r'^people/', include('apps.ava_core_identity.urls')),
    url(r'^org/', include('apps.ava_core_org.urls')),
    url(r'^graph/', include('apps.ava_vis_graph.urls')),
    url(r'^test/', include('apps.ava_test.urls')),
    url(r'^test/email/', include('apps.ava_test_email.urls')),
    url(r'^test/twitter/', include('apps.ava_test_twitter.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += dh5bp_urls
