from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import redirect, callback, Office365AdapterAPI

router = DefaultRouter()
router.register(r'setup', Office365AdapterAPI)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^redirect/(?P<pk>[0-9]+)/$', redirect),
    url(r'^callback/$', callback),
    # url(r'^home/$', views.home, name='home'),
    url(r'^get_token/$', views.get_token, name='get_token'),
    # url(r'^main/$', views.main, name='main'),
    # url(r'^send_mail/$', views.send_mail, name='send_mail'),
    # url(r'^disconnect/$', views.disconnect, name='disconnect')
]
