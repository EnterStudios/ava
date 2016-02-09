from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import redirect, callback, GoogleAdapterAPI

router = DefaultRouter()
router.register(r'setup', GoogleAdapterAPI,"google-setup")

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^redirect/(?P<pk>[0-9]+)/$', redirect),
    url(r'^callback/$', callback),
]
