from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from .views import LDAPAdapterAPI

router = DefaultRouter()

router.register(r'setup', LDAPAdapterAPI, "ldap-setup")

urlpatterns = [
    url(r'^', include(router.urls)),
]
