from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import QuestionAPI, SuspiciousAPI, ReportResponseAPI, ReportFormDataAPI

router = DefaultRouter()
router.register(r'question', QuestionAPI)
router.register(r'suspicious', SuspiciousAPI)
router.register(r'response', ReportResponseAPI)

urlpatterns = [
    url(r'^', include(router.urls)),
        url(r'^form/$', ReportFormDataAPI.as_view()),
]
