from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns(
    '',
    url('^$', views.Main.as_view(), name='google-auth-main'),
    url('^login-redirect/$', views.RedirectToGoogleLogin.as_view(), name='google-auth-login-redirect'),
    # This URL is configured at google's end in their 'developer console', so it needs to be
    # chosen carefully.
    url('^oauth2callback/$', views.GoogleOAuth2Callback.as_view(), name='google-auth-callback'),
    url('^retrieve-info/$', views.GoogleRetrieveInfo.as_view(), name='google-retrieve-info'),

)
