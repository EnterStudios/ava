from django.conf.urls import url

from .views import RegisterView, get_user_from_token, PasswordResetView, PasswordResetConfirmView, \
    PasswordChangeView

urlpatterns = [
    # URLs that do not require a session or valid token
    url(r'^password/reset/$', PasswordResetView.as_view(),
        name='rest_password_reset'),

    # TODO added for email link verification stuff but couldn't test it - test this
    url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),

    # URLs that require a user to be logged in with a valid session / token.

    url(r'^password/change/$', PasswordChangeView.as_view(),
        name='rest_password_change'),

    url(r'^register/$', RegisterView.as_view(), name='rest_register'),

    url(r'^verify-email/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        PasswordResetConfirmView.as_view(), name='account_confirm_email'),

    url(r'^user/token/$', get_user_from_token),
]
