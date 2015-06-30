import datetime

from haystack import indexes

from ava.core_identity.models import Person, Identifier


class PersonIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    created = indexes.DateTimeField(model_attr='created')
    modified = indexes.DateTimeField(model_attr='modified')

    def get_model(self):
        return Person

    def index_queryset(self):
        """Used when the entire index for model is modified."""
        return self.get_model().objects.filter(modified__lte=datetime.datetime.now())


class IdentifierIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    created = indexes.DateTimeField(model_attr='created')
    modified = indexes.DateTimeField(model_attr='modified')

    def get_model(self):
        return Identifier

    def index_queryset(self):
        """Used when the entire index for model is modified."""
        return self.get_model().objects.filter(modified__lte=datetime.datetime.now())
