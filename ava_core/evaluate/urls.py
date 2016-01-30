# Rest Imports
from rest_framework.routers import DefaultRouter
# Django Imports
from django.conf.urls import url, include
# Local Imports
from ava_core.evaluate import views


# Implementation
router = DefaultRouter()
router.register(r'controller', views.EvaluateControllerAPI)
router.register(r'sender', views.EvaluateSenderAPI)
router.register(r'test', views.EvaluateTestAPI)
router.register(r'result', views.EvaluateResultAPI)
router.register(r'template', views.EvaluateTemplateAPI)
router.register(r'return', views.EvaluateReturnAPI, base_name='evaluate_return')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^form/controller/$', views.EvaluateControllerFormDataAPI.as_view()),

]
