from django.forms import ModelForm

from apps.ava_core_ldap.models import QueryParameters


class QueryParametersForm(ModelForm):
    class Meta:
        model = QueryParameters
        fields = ('user_dn','user_pw','dump_dn','server','organisation')
