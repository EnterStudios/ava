# flake8: noqa
import json
import os

import httplib2
from apiclient import errors

from apiclient.discovery import build


class GoogleDirectoryHelper:
    def __init__(self):
        pass

    MOCK_DATA_LOCATION = 'ava/testdata/'
    DATA_SOURCE = 'google'

    def import_google_directory(self, credential):

        # Feature and testing toggle to allow developers to test Google import without having
        # Google Apps at hand
        # Uses an environment variable to decide whether to test against local JSON file or actual
        # Google Apps instance
        # To test locally, ensure that the environment variable 'USE_MOCK_GOOGLE' is set

        import_files = {
            'users': 'user',
            'groups': 'group',
            # 'user_groups': 'user_group', Not currently used
            'group_members': 'group_member',
        }

        if os.environ.get('USE_MOCK_GOOGLE'):
            results = {}

            for key, prefix in import_files.items():
                print("Importing from " + key + "file")
                with open(self.MOCK_DATA_LOCATION + self.DATA_SOURCE+"_" + prefix + "_data.json", 'r') as infile:
                    results[key] = json.load(infile)
                infile.close()

            return results

        else:
            http = httplib2.Http()
            http = credential.authorize(http)
            directory_service = build('admin', 'directory_v1', http=http)

            users = self.get_users(directory_service)
            groups = self.get_groups(directory_service)

            results = {
                'users': users,
                'groups': groups,
                # 'user_groups': self.get_user_groups(directory_service, users), Not currently used
                'group_members': self.get_group_members(directory_service, groups),
            }

            # Feature and testing toggle to allow developers to test export new test data from Google Apps
            # Uses an environment variable to decide whether to dump the data to file or not
            # To toggle this feature on, ensure that the environment variable 'CREATE_MOCK_GOOGLE' is set
            if os.environ.get('CREATE_MOCK_GOOGLE'):
                for key, prefix in import_files.items():
                    with open(self.MOCK_DATA_LOCATION + self.DATA_SOURCE+"_" + prefix + "_data.json", 'w') as infile:
                        self.export_ldap_json(prefix, results[key])
                    infile.close()
            # end of toggled feature

        return results

    # Exports a JSON string to a file
    def export_ldap_json(self, prefix, results_json):
        filename = self.MOCK_DATA_LOCATION + self.DATA_SOURCE+"_" + prefix + '_data.json'

        with open(filename, 'w') as outfile:
            json.dump(results_json, outfile)
        outfile.close()

    @staticmethod
    def get_users(directory_service):
        page_token = None

        params = {'customer': 'my_customer'}
        all_users = []
        while True:
            try:
                if page_token:
                    params['pageToken'] = page_token
                current_page = directory_service.users().list(**params).execute()

                all_users.extend(current_page['users'])
                page_token = current_page.get('nextPageToken')
                if not page_token:
                    break

            except errors.HttpError as error:
                print('An error occurred: %s' % error)
                break

        return all_users

    @staticmethod
    def get_groups(directory_service):
        page_token = None
        params = {'customer': 'my_customer'}
        all_groups = []
        while True:
            try:
                if page_token:
                    params['pageToken'] = page_token
                current_page = directory_service.groups().list(**params).execute()

                all_groups.extend(current_page['groups'])
                page_token = current_page.get('nextPageToken')
                if not page_token:
                    break

            except errors.HttpError as error:
                print('An error occurred: %s' % error)
                break

        return all_groups

    @staticmethod
    def get_user_groups(directory_service, all_users):
        page_token = None
        params = {}
        user_groups = {}

        for user in all_users:
            user_groups[user['primaryEmail']] = []

            while True:
                try:
                    if page_token:
                        params['pageToken'] = page_token

                    params['userKey'] = user['id']
                    current_page = directory_service.groups().list(**params).execute()
                    curr_groups = []

                    if 'groups' in current_page:
                        curr_groups.extend(current_page['groups'])
                        # print current_page['groups']

                    page_token = current_page.get('nextPageToken')
                    if not page_token:
                        user_groups[user['primaryEmail']] = curr_groups
                        break

                except errors.HttpError as error:
                    print('An error occurred: %s' % error)
                    break

        return user_groups

    @staticmethod
    def get_group_members(directory_service, all_groups):
        page_token = None
        params = {}
        group_members = {}

        for group in all_groups:
            group_members[group['id']] = []

            while True:
                try:
                    if page_token:
                        params['pageToken'] = page_token

                    params['groupKey'] = group['id']
                    current_page = directory_service.members().list(**params).execute()
                    curr_members = []

                    if 'members' in current_page:
                        curr_members.extend(current_page['members'])

                    page_token = current_page.get('nextPageToken')
                    if not page_token:
                        group_members[group['id']] = curr_members
                        break

                except errors.HttpError as error:
                    print('An error occurred: %s' % error)
                    break

        return group_members

    @staticmethod
    def to_string(dictionary):
        for key, value in dictionary:
            print(key)
            for item in value:
                print(item)
