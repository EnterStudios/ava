from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from apps.ava_vis_graph import views


urlpatterns = patterns('',
    
    url(r'^ldap/(?P<pk>\d+)/$', login_required(views.LDAPGraph.as_view()), name='vis-ldap-graph-view'),
    url(r'^ldap/(?P<pk>\d+)/data/$', login_required(views.graph_data), name='vis-ldap-graph-data'),
    #url(r'^ldap/(?P<pk>\d+)/hide/$', login_required(views.LDAPGraphHideView.as_view()), name='ldap_graph_view'),
)
