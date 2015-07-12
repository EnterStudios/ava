# flake8: noqa
import os
import sys

import httplib2
from apiclient import errors
from apiclient.discovery import build
from oauth2client import xsrfutil
from oauth2client.client import OAuth2WebServerFlow, flow_from_clientsecrets


class GoogleAppsHelper:
    # Define the specific access we would like to request from the user
    # Check https://developers.google.com/admin-sdk/directory/v1/guides/authorizing for all available scopes
    OAUTH_SCOPE = 'https://www.googleapis.com/auth/admin.directory.user.readonly ' \
                  'https://www.googleapis.com/auth/admin.directory.group.readonly ' \
                  'https://www.googleapis.com/auth/admin.directory.group.member.readonly ' \
                  'https://www.googleapis.com/auth/admin.directory.orgunit.readonly ' \
                  'https://www.googleapis.com/auth/admin.directory.user.alias.readonly'

    # Redirect URI for installed apps
    REDIRECT_URI = 'http://avasecure.com:8000/google/auth/return/'

    # these are pulled from environment variables. do not hard code these
    CLIENT_ID = ""

    # these are pulled from environment variables. do not hard code these
    CLIENT_SECRET = ""

    FLOW = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE, REDIRECT_URI)
    
    DIRECTORY_SERVICE = None


    def __init__(self):
        try:
            # Pull the client_id and client_secret from environment variables. If these variables do not exist. Log and
            # exit as this will not work

            self.CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID')
            self.CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET')
            self.FLOW = OAuth2WebServerFlow(self.CLIENT_ID, self.CLIENT_SECRET, self.OAUTH_SCOPE, self.REDIRECT_URI)
        except OSError as e:
            print(e.message)
            print(e.args)
            sys.exit(1)

    def generate_xsrf_token(self,user):
        return xsrfutil.generate_token(self.CLIENT_SECRET, user)

    def validate_xsrf_token(self, request):
        print(request.REQUEST['state'])
        return xsrfutil.validate_token(self.CLIENT_SECRET, request.REQUEST['state'], request.user)

    def get_flow(self):
        #return flow_from_clientsecrets(self.CLIENT_SECRET, self.OAUTH_SCOPE, self.REDIRECT_URI)
        return OAuth2WebServerFlow(self.CLIENT_ID, self.CLIENT_SECRET, self.OAUTH_SCOPE, self.REDIRECT_URI)

    def get_auth_url(self, flow):

        return self.FLOW.step1_get_authorize_url()

    def build_directory_service(self, credential):
        http = httplib2.Http()
        http = credential.authorize(http)
        self.DIRECTORY_SERVICE= build("admin", "directory_v1", http=http)

    def generate_credential(self, request):
        # if not xsrfutil.validate_token(self.CLIENT_SECRET, request_state, request_user):
        #    return False
        return self.FLOW.step2_exchange(request)

    def import_google_directory(self):
        users = GoogleAppsHelper.get_users(self.DIRECTORY_SERVICE)
        groups = GoogleAppsHelper.get_groups(self.DIRECTORY_SERVICE)

        results = {
            'users': users,
            'groups': groups,
            'user_groups': GoogleAppsHelper.get_users(self.DIRECTORY_SERVICE, users),
            'group_members': GoogleAppsHelper.get_users(self.DIRECTORY_SERVICE, groups),
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
                print ('An error occurred: %s' % error)
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
                print ('An error occurred: %s' % error)
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
                print ('An error occurred: %s' % error)
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

                print (current_page)

                if 'members' in current_page:
                    curr_members.extend(current_page['members'])

                page_token = current_page.get('nextPageToken')
                if not page_token:
                    group_members[group['name']] = curr_members
                    break

            except errors.HttpError as error:
                print ('An error occurred: %s' % error)
                break

        return group_members

    @staticmethod
    def to_string(dictionary):
        for key, value in dictionary:
            print (key)
            for item in value:
                print (item)
