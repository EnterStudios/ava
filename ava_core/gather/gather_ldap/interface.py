from django.conf import settings

from ava_core.gather.gather_abstract.interface import DirectoryHelper

__author__ = 'ladynerd'

from ldap3 import Server, Connection, LDAPExceptionError, SUBTREE
import sys
import logging
from ava_core.gather.gather_abstract.utils import load_local_test_data, create_local_test_data

log = logging.getLogger(__name__)


class ActiveDirectoryHelper(DirectoryHelper):
    def __init__(self):
        pass

    PAGESIZE = 1000

    DATA_SOURCE = 'ldap'

    def import_directory(self, credential):
        super(ActiveDirectoryHelper, self).import_directory(credential)
        # Feature and testing toggle to allow developers to test GATHER locally
        # Uses an environment variable to decide whether to test against local JSON file or not
        # To test locally, ensure that the gather.py variable 'GATHER_USE_LOCAL' is set

        if settings.GATHER_USE_LOCAL['ldap']:
            return load_local_test_data(self.DATA_SOURCE, self.DATA_IMPORT_FILES)

        else:

            self.setup(credential)

            results = {
                'users': self.get_users(),
                'groups': self.get_groups(),
            }

            # Feature and testing toggle to allow developers to test export new test data from gather
            # Uses a settings variable to decide whether to dump the data to file or not
            # To toggle this feature on, ensure that the gather.py variable 'CREATE_LOCAL_DATA' is set
            if settings.GATHER_CREATE_LOCAL['ldap']:
                create_local_test_data(self.DATA_SOURCE, results)

        return results
    
    def setup(self, credential):
        super(ActiveDirectoryHelper, self).setup(credential)
        self.CREDENTIAL = credential

    def get_connection(self):
        try:
            credential = self.CREDENTIAL
            log.debug("Called get_connection in ActiveDirectoryHelper with server : %s", credential.server)
            server = Server(credential.server)
            log.debug("Created server in ActiveDirectoryHelper with username : %s and password : %s",
                      credential.ldap_user, credential.ldap_password)
            ldap_conn = Connection(server, user=credential.ldap_user, password=credential.ldap_password,
                                   auto_bind=True)
            log.debug("Created connection in ActiveDirectoryHelper")
            return ldap_conn

        except LDAPExceptionError as e:
            print(e.message)
            print(e.args)
            sys.exit(1)

    def search(self, filterby, attrs):

        log.debug("Called search in ActiveDirectoryHelper")
        # bind to the LDAP server using the credentials provided
        connection = self.get_connection()

        log.debug("Created connection from ActiveDirectoryHelper:search")
        connection.search(search_base=self.CREDENTIAL.dump_dn, search_filter=filterby, search_scope=SUBTREE,
                          attributes=attrs, paged_size=5)

        log.debug("Called connection.search in ActiveDirectoryHelper:search")
        # store the search results
        results = connection.response

        # extract the cookie from the search result to allow for paged session continuation
        cookie = connection.result['controls']['1.2.840.113556.1.4.319']['value']['cookie']

        # while the results contain a cookie (ie. more records left to retrieve)
        while cookie:
            # search again using the cookie to continue paging
            connection.search(search_base=self.CREDENTIAL.dump_dn, search_filter=filterby, search_scope=SUBTREE,
                              attributes=attrs, paged_size=5, paged_cookie=cookie)

            # append the search results
            results += connection.response

            # get the cookie again
            cookie = connection.result['controls']['1.2.840.113556.1.4.319']['value']['cookie']

        # export the combined paged results to json format
        results_json = connection.response_to_json(search_result=results)

        return results_json

    # imports the users from an LDAP instance
    def get_users(self):
        super(ActiveDirectoryHelper, self).get_users()
        # specify that we only care about users
        filter_fields = '(objectclass=user)'

        # specify the fields to bring back for this user
        attributes = ['distinguishedName', 'objectGUID', 'objectSid', 'cn', 'accountExpires', 'adminCount',
                      'badPasswordTime', 'badPwdCount', 'description', 'displayName', 'isCriticalSystemObject',
                      'lastLogoff', 'lastLogon', 'lastLogonTimestamp', 'logonCount', 'lockoutTime', 'name',
                      'primaryGroupID', 'pwdLastSet', 'sAMAccountName', 'sAMAccountType', 'uSNChanged',
                      'uSNCreated', 'userAccountControl', 'whenChanged', 'whenCreated', 'memberOf',
                      'proxyAddresses']

        return self.search(filter_fields, attributes)

    # imports the groups from an LDAP instance
    def get_groups(self):
        super(ActiveDirectoryHelper, self).get_groups()

        # specify that we only care about groups
        filter_fields = '(objectclass=groups)'

        # specify the fields to bring back for this groups
        attributes = ['distinguishedName', 'objectGUID', 'objectSid', 'cn', 'name', 'objectCategory',
                      'sAMAccountName']

        # return a search result for these filter_fields and attributes in JSON format
        return self.search(filter_fields, attributes)
