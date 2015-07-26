from django.shortcuts import get_object_or_404
from django.views import generic
from ava.import_ldap.models import LDAPConfiguration
from ava.import_ldap.stats_interface import LDAPStatistics


class KnowDashboardView(generic.ListView):
    template_name = 'know/dashboard.html'
    model = LDAPConfiguration
    context_object_name = 'list'

    def get_context_data(self, **kwargs):
        context = super(KnowDashboardView, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        if pk:
            ldap_config = get_object_or_404(LDAPConfiguration, pk=pk)
            context['ldap'] = LDAPStatistics(ldap_config)
        return context
