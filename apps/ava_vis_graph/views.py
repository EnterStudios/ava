from django.views import generic
from django.shortcuts import get_object_or_404

from apps.ava_core_ldap.models import LDAPConfiguration, ExportLDAP


class LDAPGraph(generic.DeleteView):
    template_name = 'graph/vis_ldap_graph_view.html'
    model = LDAPConfiguration

    def get_context_data(self, **kwargs):
        context = super(LDAPGraph, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        if pk:
            parameters = get_object_or_404(LDAPConfiguration, pk=pk)
            exp = ExportLDAP()
            context['json'] = exp.generateGraph(parameters)

        return context

#class LDAPGraphHideView(generic.DeleteView):
#    template_name = 'graph/ldap.html'
#    model = LDAPConfiguration

#    def get_context_data(self, **kwargs):
#        context = super(LDAPGraphHideView, self).get_context_data(**kwargs)
#        pk = self.kwargs.get('pk')
#        if pk:
#            parameters = get_object_or_404(LDAPConfiguration, pk=pk)
#            exp = ExportLDAP()
#            context['json'] = exp.generateGraph(parameters)
#            context['link'] = "/graph/ldap/"+pk+"/"
#            context['link_message'] = "Show Empty Groups"
#        return context

