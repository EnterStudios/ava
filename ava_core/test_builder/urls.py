from django.conf.urls import url
from .views import ProjectDataBuilder, ProjectTestBuilder

urlpatterns = [
    url(r'^data/$', ProjectDataBuilder.as_view()),
    url(r'^test/$', ProjectTestBuilder.as_view())
]
