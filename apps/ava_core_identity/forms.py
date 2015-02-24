from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from apps.ava_core_identity.models import Identity, Person, Identifier


class IdentityForm(ModelForm):
    class Meta:
        model = Identity
        fields = ('name', 'description')


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ('firstname',  'surname')
        #labels = {
        #    'firstname': ('Firstname'),
        #    'surname': ('Surname/Family Name'),
        #}

IdentifierFormSet = inlineformset_factory(Identity,  Identifier, extra=0, min_num=1, fields=('identifier', 'identifiertype',))
