from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import LDAPGatherHistoryAPI, LDAPImportAPI

router = DefaultRouter()
router.register(r'history', LDAPGatherHistoryAPI)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^import/(?P<pk>[0-9]+)/$', LDAPImportAPI.as_view()),
]
