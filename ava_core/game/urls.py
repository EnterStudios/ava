from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import AchievementAPI

router = DefaultRouter()
router.register(r'achievement', AchievementAPI)


urlpatterns = [
    url(r'^', include(router.urls)),
]
