# Django Imports
from django.core.validators import ValidationError
from django.utils.deconstruct import deconstructible


# Implementation
class GenericValidator(object):
    def __init__(self, queryset, query_field, query='_iexact', message='Duplicate found.'):
        self.queryset = queryset
        self.query_field = query_field
        self.query = query
        self.message = message

    def __call__(self, value):
        kwargs = {
            # Formats filter e.g. 'name', '_iexact' becomes name__iexact and 'tech', 'id' becomes tech_id
            '{0}_{1}'.format(self.query_field, self.query): value
        }

        if self.queryset.filter(**kwargs).exists():
            raise ValidationError(self.message)


class GenericTogetherValidator(object):
    def __init__(self, queryset, query_fields, message='Duplicate found.'):
        self.queryset = queryset
        self.query_fields = query_fields
        self.message = message

    def __call__(self, value):
        kwargs = {}

        for key in self.query_fields:
            kwargs.update({
                # Formats filter e.g. 'name', '_iexact' becomes name__iexact and 'tech', 'id' becomes tech_id
                '{0}_{1}'.format(key, self.query_fields[key]): value[key]
            })

        if self.queryset.filter(**kwargs).exists():
            raise ValidationError(self.message)
