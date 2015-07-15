# flake8: noqa

import httplib2
from apiclient import errors

from apiclient.discovery import build


class GoogleDirectoryHelper:

    def __init__(self):
        pass

    def import_google_directory(self, credential):
        http = httplib2.Http()
        http = credential.authorize(http)
        directory_service = build('admin', 'directory_v1', http=http)

        users = self.get_users(directory_service)
        groups = self.get_groups(directory_service)

        results = {
            'users': users,
            'groups': groups,
            'user_groups': self.get_user_groups(directory_service, users),
            'group_members': self.get_group_members(directory_service, groups),
        }

        return results

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
