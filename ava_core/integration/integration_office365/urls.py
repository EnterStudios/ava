from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import redirect, callback, Office365AdapterAPI

router = DefaultRouter()
router.register(r'setup', Office365AdapterAPI, "office365-setup")

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^redirect/(?P<pk>[0-9]+)/$', redirect),
    url(r'^callback/$', callback),

]
