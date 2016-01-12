from logging import getLogger

from django.apps import apps

log = getLogger(__name__)


def add_identifier(model_name, model_owner, identifier_type, identifier, is_primary=False):
    identifier_model = apps.get_model(model_name)
    model, created = identifier_model.objects.get_or_create(identifier=identifier,
                                                            identifier_type=identifier_type,
                                                            belongs_to=model_owner)
    model.primary_identifier = is_primary
    model.save()
