from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import RoleAPI, PathAPI, ModuleAPI, PathFormDataAPI

router = DefaultRouter()
router.register(r'role', RoleAPI)
router.register(r'path', PathAPI)
router.register(r'module', ModuleAPI)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^form/$', PathFormDataAPI.as_view()),
]
