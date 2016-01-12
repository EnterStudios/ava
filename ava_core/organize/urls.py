from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import PersonAPI, GroupAPI, PersonAttributeAPI, PersonIdentifierAttributeAPI, GroupIdentifierAttributeAPI, \
    PersonIdentifierReportAPI, GroupReportAPI

router = DefaultRouter()
router.register(r'person', PersonAPI)
router.register(r'group', GroupAPI)
router.register(r'person_attribute', PersonAttributeAPI)
router.register(r'person_identifier_attribute', PersonIdentifierAttributeAPI)
router.register(r'group_identifier_attribute', GroupIdentifierAttributeAPI)
router.register(r'person_identifier_report', PersonIdentifierReportAPI)
router.register(r'group_report', GroupReportAPI)

urlpatterns = [
    url(r'^', include(router.urls)),
]
