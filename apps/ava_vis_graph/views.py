from django.views import generic
from django.shortcuts import get_object_or_404

from apps.ava_core_ldap.models import QueryParameters, ExportLDAP


class LDAPGraphView(generic.DeleteView):
    template_name = 'graph/ldap.html'
    model = QueryParameters

    def get_context_data(self, **kwargs):
        context = super(LDAPGraphView, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        if pk:
            parameters = get_object_or_404(QueryParameters, pk=pk)
            exp = ExportLDAP()
            context['json'] = exp.generateGraph(parameters)
            context['link'] = "/graph/ldap/"+pk+"/hide/"
            context['link_message'] = "Hide Empty Groups"
        return context

#class LDAPGraphHideView(generic.DeleteView):
#    template_name = 'graph/ldap.html'
#    model = QueryParameters

#    def get_context_data(self, **kwargs):
#        context = super(LDAPGraphHideView, self).get_context_data(**kwargs)
#        pk = self.kwargs.get('pk')
#        if pk:
#            parameters = get_object_or_404(QueryParameters, pk=pk)
#            exp = ExportLDAP()
#            context['json'] = exp.generateGraph(parameters)
#            context['link'] = "/graph/ldap/"+pk+"/"
#            context['link_message'] = "Show Empty Groups"
#        return context

