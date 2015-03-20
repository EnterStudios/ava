from django.views import generic
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from apps.ava_core_ldap.models import LDAPConfiguration, ExportLDAP


class LDAPGraph(generic.TemplateView):
    template_name = 'graph/vis_ldap_graph_view.html'
    
    def get(self, request, *args, **kwargs):
        # Make sure that this is a valid LDAP config before the page is shown.
        pk = kwargs['pk']
        get_object_or_404(LDAPConfiguration, pk=pk)
        return super(LDAPGraph, self).get(request, *args, **kwargs)


def graph_data(request, pk):
    '''
    Generates a JSON object containing the nodes to display on a D3 graph.
    :param request: The current HTTP request.
    :param pk: The identifier of the LDAP configuration to be graphed.
    '''
    parameters = get_object_or_404(LDAPConfiguration, pk=pk)
    exp = ExportLDAP()
    json_data = exp.generateGraph(parameters)
    return JsonResponse(json_data)


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

