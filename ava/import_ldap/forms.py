from django.forms import ModelForm

from ava.import_ldap.models import LDAPConfiguration


class LDAPConfigurationForm(ModelForm):

    class Meta:
        model = LDAPConfiguration
        fields = ('user_dn', 'user_pw', 'dump_dn', 'server')
