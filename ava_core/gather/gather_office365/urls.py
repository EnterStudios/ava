from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import Office365ImportAPI,Office365GatherHistoryAPI

router = DefaultRouter()
router.register(r'history', Office365GatherHistoryAPI)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^import/(?P<pk>[0-9]+)/$', Office365ImportAPI.as_view()),
]
