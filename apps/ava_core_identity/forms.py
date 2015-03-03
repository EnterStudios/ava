from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from apps.ava_core_identity.models import Identity, Person, Identifier


class IdentityForm(ModelForm):
    class Meta:
        model = Identity
        fields = ('name', 'description', 'member_of')
        labels = {
            'name':('Name'),
            'description':('Description'),
            'member_of' :('Member of'),
        }


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ('firstname', 'surname', 'identity')
        labels = {
            'firstname': ('First Name'),
            'surname': ('Surname/Family Name'),
            'identity': ('Identities'),
        }


class IdentifierForm(ModelForm):
    class Meta:
        model = Identifier
        fields = ('identifiertype', 'identifier')


IdentifierFormSet = inlineformset_factory(parent_model=Identity,
                                          model=Identifier,
                                          extra=0,
                                          min_num=1,
                                          fields=('identifier', 'identifiertype',)
                                          )
