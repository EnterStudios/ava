from django.conf.urls import patterns, url

from apps.ava_core_auth import views


urlpatterns = patterns('',
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^register/$', views.user_register, name='register'),
)
