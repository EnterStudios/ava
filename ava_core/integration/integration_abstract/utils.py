import json
import logging

import oauth2client
from django.apps import apps

log = logging.getLogger(__name__)


def store_credential_in_session(request, credential):
    request.session['google_oauth2_credential'] = credential.to_json()


def retrieve_credential_from_session(request):
    credential_json = request.session.get('google_oauth2_credential')
    if credential_json is None:
        return None
    credential = oauth2client.client.OAuth2Credentials.from_json(credential_json)
    return credential


# store the credential in the database for the relevent adapter so that we can use it for updates
def store_credential_in_database(model_name, integration_id, credential):
    adapter = apps.get_model(model_name)
    oauth_adapter, created = adapter.objects.get_or_create(pk=integration_id)
    log.debug("Preparing to store credential " + str(credential))
    try:
        oauth_adapter.credential = credential.to_json()
    except Exception as e:
        oauth_adapter.credential = credential

    oauth_adapter.save()


# retrieve the credential from the database
def retrieve_credential_from_database(model_name, integration_id, integration_name):
    adapter = apps.get_model(model_name)
    if integration_name is 'google':
        oauth_adapter = adapter.objects.get(pk=integration_id)
        credential_json = oauth_adapter.credential
        if credential_json is None:
            return None
        credential = oauth2client.client.OAuth2Credentials.from_json(credential_json)
    else:
        integration_adapter = adapter.objects.get(pk=integration_id)
        log.debug("Credential from database = :: " + str(integration_adapter.credential))
        credential = json.dumps(obj=integration_adapter.credential)
        log.debug("Credential after dumps = :: " + str(credential))
    return credential

# retrieve the credential from the database
def retrieve_integration_from_database(model_name, integration_id):
    adapter = apps.get_model(model_name)
    return adapter.objects.get(pk=integration_id)



# store the credential in the database for the relevent adapter so that we can use it for updates
def store_temporary_flow_data_in_database(model_name, pk):
    adapter = apps.get_model(model_name)
    store, created = adapter.objects.get_or_create(integration_id=pk)
    store.save()


# store the credential in the database for the relevent adapter so that we can use it for updates
def retrieve_temporary_flow_data_from_database(model_name):
    adapter = apps.get_model(model_name)
    store = adapter.objects.first()
    return store.integration_id


# store the credential in the database for the relevent adapter so that we can use it for updates
def remove_temporary_flow_data_from_database(model_name, pk):
    adapter = apps.get_model(model_name)
    store, deleted = adapter.objects.filter(integration_id=pk).delete()
