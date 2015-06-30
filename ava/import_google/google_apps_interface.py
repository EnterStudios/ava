__author__ = 'ladynerd'
import httplib2
from apiclient import errors
from apiclient.discovery import build
from oauth2client.client import OAuth2WebServerFlow


class GoogleAppsHelper:
    # Check https://developers.google.com/admin-sdk/directory/v1/guides/authorizing for all available scopes
    OAUTH_SCOPE = 'https://www.googleapis.com/auth/admin.directory.user.readonly '
                  'https://www.googleapis.com/auth/admin.directory.group.readonly https://www.googleapis.com/auth/admin.directory.group.member.readonly https://www.googleapis.com/auth/admin.directory.orgunit.readonly https://www.googleapis.com/auth/admin.directory.user.alias.readonly'

    # Redirect URI for installed apps
    REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'

    CLIENT_ID = ""

    CLIENT_SECRET = ""

    def get_connection(self):
        # Run through the OAuth flow and retrieve credentials
        flow = OAuth2WebServerFlow(self.CLIENT_ID, self.CLIENT_SECRET, self.OAUTH_SCOPE, self.REDIRECT_URI)
        authorize_url = flow.step1_get_authorize_url()
        print 'Go to the following link in your browser: ' + authorize_url
        code = raw_input('Enter verification code: ').strip()
        credentials = flow.step2_exchange(code)

        # Create an httplib2.Http object and authorize it with our credentials
        http = httplib2.Http()
        http = credentials.authorize(http)

        directory_service = build('admin', 'directory_v1', http=http)
        return directory_service

    def __init__(self):
        pass

    def get_users(self):
        directory_service = self.get_connection()
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
                print 'An error occurred: %s' % error
                break

        return all_users

    def get_groups(self):
        directory_service = self.get_connection()
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
                print 'An error occurred: %s' % error
                break

        return all_groups

    def get_user_groups(self, all_users):
        directory_service = self.get_connection()
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
                print 'An error occurred: %s' % error
                break

        return user_groups

    def get_group_members(self, all_groups):
        directory_service = self.get_connection()
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

                print current_page

                if 'members' in current_page:
                    curr_members.extend(current_page['members'])

                page_token = current_page.get('nextPageToken')
                if not page_token:
                    group_members[group['name']] = curr_members
                    break

            except errors.HttpError as error:
                print 'An error occurred: %s' % error
                break

        return group_members

    def to_string(self, dictionary):
        for key, value in dictionary:
            print key
            for item in value:
                print item
