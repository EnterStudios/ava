# flake8: noqa
import json
import logging
import uuid

import httplib2
import requests
from apiclient import errors
from apiclient.discovery import build
from django.conf import settings

from ava_core.gather.gather_abstract.interface import DirectoryHelper
from ava_core.gather.gather_abstract.utils import load_local_test_data, create_local_test_data

log = logging.getLogger(__name__)


class Office365DirectoryHelper(DirectoryHelper):
    def __init__(self):
        pass

    DATA_SOURCE = 'office365'

    DIRECTORY_SERVICE = None

    DATA_IMPORT_FILES = {
        'users': 'users',
        'groups': 'groups',
        'group_members': 'group_members',
    }

    # The base URL for the Microsoft Graph API.
    graph_api_endpoint = 'https://graph.microsoft.com/v1.0{0}'

    request_urls = {'users': 'https://graph.microsoft.com/v1.0/users',
                    'groups': 'https://graph.microsoft.com/v1.0/groups'}

    def import_directory(self, credential):
        # Feature and testing toggle to allow developers to test GATHER locally
        # Uses an environment variable to decide whether to test against local JSON file or not
        # To test locally, ensure that the gather.py variable 'GATHER_USE_LOCAL' is set

        if settings.GATHER_USE_LOCAL['office365']:
            return load_local_test_data(self.DATA_SOURCE, self.DATA_IMPORT_FILES)

        else:

            self.setup(credential)

            groups = self.get_groups()

            results = {
                'users': self.get_users(),
                'groups': groups,
                # 'group_members': self.get_group_members(groups),
            }

            # Feature and testing toggle to allow developers to test export new test data from gather
            # Uses a settings variable to decide whether to dump the data to file or not
            # To toggle this feature on, ensure that the gather.py variable 'CREATE_LOCAL_DATA' is set
            if settings.GATHER_CREATE_LOCAL['office365']:
                create_local_test_data(self.DATA_SOURCE, results)

        return results

    def setup(self, credential):
        self.access_token = credential['access_token']

    def get_data(self, access_token, request_url):
        # Set request headers.
        headers = {
            'User-Agent': 'ava_gather_office365/1.0',
            'Authorization': 'Bearer {0}'.format(access_token),
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

        # Use these headers to instrument calls. Makes it easier
        # to correlate requests and responses in case of problems
        # and is a recommended best practice.
        request_id = str(uuid.uuid4())
        instrumentation = {
            'client-request-id': request_id,
            'return-client-request-id': 'true'
        }
        headers.update(instrumentation)

        response = requests.get(url=request_url, headers=headers, params=None)

        # Check if the response is 202 (success) or not (failure).
        if response.status_code is 200:
            return response
        else:
            log.error("{0}: {1}".format(response.status_code, response.text))
            return "{0}: {1}".format(response.status_code, response.text)

    def get_users(self):
        try:
            response = self.get_data(access_token=self.access_token, request_url=self.request_urls['users'])
            # log.debug("get_users :: status code :: " + str(response.status_code))
            # log.debug("get_users :: content :: " + str(response.text))
            # log.debug("type " + str(type(response.text)))
            if type(response.text) is str:
                json_results = json.loads(s=response.text)
                if 'value' in json_results:
                    return json_results['value']
            return False
        except Exception as e:
            log.error("Exception thrown :: " + str(e))

    def get_groups(self):
        try:
            response = self.get_data(access_token=self.access_token, request_url=self.request_urls['groups'])
            # log.debug("get_groups :: status code :: " + str(response.status_code))
            # log.debug("get_groups :: content :: " + str(response.text))
            if type(response.text) is str:
                json_results = json.loads(s=response.text)
                if 'value' in json_results:
                    return json_results['value']
            return False
        except Exception as e:
            log.error("Exception thrown :: " + str(e))


