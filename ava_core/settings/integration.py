# GOOGLE OAUTH2 ADAPTER CONFIGURATION SETTINGS
# Sets the variables needed for authentication and authorisation against Google
import os

GOOGLE_OAUTH2_CLIENT_ID = os.environ.get('GOOGLE_OAUTH2_CLIENT_ID', None)
GOOGLE_OAUTH2_CLIENT_SECRET = os.environ.get('GOOGLE_OAUTH2_CLIENT_SECRET', None)

GOOGLE_OAUTH2_SCOPE = ['https://www.googleapis.com/auth/admin.directory.user.readonly',
                       'https://www.googleapis.com/auth/admin.directory.group.readonly',
                       'https://www.googleapis.com/auth/admin.directory.group.member.readonly',
                       'https://www.googleapis.com/auth/admin.directory.orgunit.readonly',
                       'https://www.googleapis.com/auth/admin.directory.user.alias.readonly']

GOOGLE_OAUTH2_REDIRECT_URL = 'http://avasecure.com:8888/integration/google/callback/'

GOOGLE_OAUTH2_USE_LOCAL = False

OFFICE365_OAUTH2_CLIENT_ID = os.environ.get('OFFICE365_OAUTH2_CLIENT_ID', None)
OFFICE365_OAUTH2_CLIENT_SECRET = os.environ.get('OFFICE365_OAUTH2_CLIENT_SECRET', None)

OFFICE365_OAUTH2_REDIRECT_URL = 'http://avasecure.com:9000/integration/office365/callback/'

OFFICE365_OAUTH2_USE_LOCAL = False