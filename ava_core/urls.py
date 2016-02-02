from rest_framework_jwt.views import refresh_jwt_token, obtain_jwt_token, verify_jwt_token
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.authtoken import views as rest_views

urlpatterns = [


    url(r'^organize/', include('ava_core.organize.urls')),
    url(r'^my/', include('ava_core.my.urls')),
    url(r'^game/', include('ava_core.game.urls')),
    url(r'^learn/', include('ava_core.learn.urls')),
    url(r'^report/', include('ava_core.report.urls')),
    url(r'^evaluate/', include('ava_core.evaluate.urls')),
    # url(r'^notify/', include('ava_core.notify.urls')),
    url(r'^gather/google/', include('ava_core.gather.gather_google.urls')),
    url(r'^gather/ldap/', include('ava_core.gather.gather_ldap.urls')),
    url(r'^integration/google/', include('ava_core.integration.integration_google.urls')),
    url(r'^integration/ldap/', include('ava_core.integration.integration_ldap.urls')),
    url(r'^integration/office365/', include('ava_core.integration.integration_office365.urls')),

    url(r'^login/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
    url(r'^accounts/', include('ava_core.accounts.urls')),

    url(r'^tests/', include('ava_core.test_builder.urls')),


    # REMOVE OR COMMENT OUT BEFORE GOING INTO PRODUCTION ENVIRONMENTS
    url(r'^auth/', rest_views.obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),

]
