from django.views import generic
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from apps.ava_core_ldap.models import LDAPConfiguration, ExportLDAP
from django.views.generic import ListView


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



class LDAPGraphIndex(ListView):
    template_name = 'graph/vis_ldap_graph_index.html'
    model = LDAPConfiguration
    context_object_name = 'ldap_configuration_list'

    def get_queryset(self):
        return LDAPConfiguration.objects.all()

