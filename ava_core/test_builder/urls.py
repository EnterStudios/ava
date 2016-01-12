from django.conf.urls import url

from .views import TestDataBuilder

urlpatterns = [
    url(r'^build/data/$', TestDataBuilder.as_view()),
    # url(r'^build/$', TestBuilder.as_view()),
]
