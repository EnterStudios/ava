from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import NotificationEmailAPI

router = DefaultRouter()


urlpatterns = [
    url(r'^', include(router.urls)),
]
