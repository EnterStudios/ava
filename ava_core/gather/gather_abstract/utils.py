import json
from logging import getLogger

from django import apps
from django.conf import settings

from ava_core.settings.base import MEDIA_ROOT
from ava_core.gather.gather_abstract.models import GatherHistory

log = getLogger(__name__)
MOCK_DATA_LOCATION = MEDIA_ROOT + settings.GATHER_LOCAL_DATA_LOCATION


def load_local_test_data(data_source, import_dict):
    results = {}
    log.debug("load_local_test_data:: attempting to load local test data")
    for key, prefix in import_dict.items():
        filename = MOCK_DATA_LOCATION + "/" + data_source + "/" + data_source + "_" + key + "_data.json"
        log.debug("Importing from " + filename)
        with open(filename, 'r') as infile:
            results[key] = json.load(infile)
        infile.close()

    return results


def create_local_test_data(data_source, results_dict):
    # Feature and testing toggle to allow developers to test export new test data from gather
    # Uses a settings variable to decide whether to dump the data to file or not
    # To toggle this feature on, ensure that the gather.py variable 'CREATE_LOCAL_DATA' is set
    for key, prefix in results_dict.items():
        filename = MOCK_DATA_LOCATION + "/" + data_source + "/" + data_source + "_" + key + "_data.json"
        with open(filename, 'w') as outfile:
            json.dump(results_dict[key], outfile)
        outfile.close()
        # end of toggled feature


def to_string(dictionary):
    for key, value in dictionary:
        print(key)
        for item in value:
            print(item)


def log_gather_history(model_name, message, no_people, no_groups, no_identifiers, status=GatherHistory.COMPLETED):
    history = apps.get_model(model_name)

    store, created = history.objects.create(message=message, no_groups=no_groups, no_people=no_people,
                                            no_identifiers=no_identifiers, import_status=status)
    store.save()
