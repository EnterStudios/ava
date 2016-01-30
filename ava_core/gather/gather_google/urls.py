from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import GoogleImportAPI,GoogleGatherHistoryAPI

router = DefaultRouter()
router.register(r'history', GoogleGatherHistoryAPI)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^import/(?P<pk>[0-9]+)/$', GoogleImportAPI.as_view()),
]
