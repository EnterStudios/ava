from django.conf.urls import patterns, url, include


urlpatterns = patterns('',
                       url(
                           '^login/',
                           'django.contrib.auth.views.login',
                           {'template_name': 'auth/login.html'},
                           name='login'
                       ),
                       url(
                           '^logout/',
                           'django.contrib.auth.views.logout',
                           {'template_name': 'auth/logout.html'},
                           name='logout'
                       ),
                       url(
                           '^password_change/',
                           'django.contrib.auth.views.password_change',
                           {'template_name': 'auth/password-change.html'},
                           name='password_change'
                       ),

                       url(
                           '^password_change/done/',
                           'django.contrib.auth.views.password_change_done',
                           {'template_name': 'auth/password-change-done.html'},
                           name='password_change_done'
                       ),
                       url(
                           '^password_reset/$',
                           'django.contrib.auth.views.password_reset',
                           {'template_name': 'auth/password-reset.html'},
                           name='password_reset'
                       ),
                       url(
                           '^password_reset/done/$',
                           'django.contrib.auth.views.password_reset_done',
                           {'template_name': 'auth/password-reset-done.html', 'post_reset_redirect': '/'},
                           name='password_reset_done'
                       ),
                       url(
                           '^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
                           'django.contrib.auth.views.password_reset_confirm',
                           {'template_name': 'auth/password-reset-confirm.html'},
                           name='password_reset_confirm'
                       ),
                       url(
                           '^reset/done/',
                           'django.contrib.auth.views.password_reset_complete',
                           {'template_name': 'auth/password-reset-complete.html'},
                           name='password_reset_complete'
                       ),
)
