from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from ava.core_identity.models import Identity, Person, Identifier


class IdentityForm(ModelForm):

    class Meta:
        model = Identity
        fields = ('name', 'description', 'groups')
        labels = {
            'name': 'Name',
            'description': 'Description',
            'groups': 'Member of',
        }


class PersonForm(ModelForm):

    class Meta:
        model = Person
        fields = ('first_name', 'surname', 'identity')
        labels = {
            'first_name': 'First Name',
            'surname': 'Surname/Family Name',
            'identity': 'Identities',
        }


class IdentifierForm(ModelForm):

    class Meta:
        model = Identifier
        fields = ('identifier_type', 'identifier')


IdentifierFormSet = inlineformset_factory(parent_model=Identity,
                                          model=Identifier,
                                          extra=0,
                                          min_num=1,
                                          fields=('identifier', 'identifier_type',)
                                          )
