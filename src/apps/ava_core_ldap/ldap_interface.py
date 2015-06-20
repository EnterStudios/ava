
from itertools import count
import sys
import json

__author__ = 'ladynerd'
# import ldap, ldif, datetime, re
# from ldap import *
# from ldap.controls import *
# from ldap.cidict import cidict
from StringIO import StringIO

from ldap3 import *

class ActiveDirectoryHelper():

    PAGESIZE=1000


    def getConnection(self, parameters):
        try:
            server = Server(parameters.server)
            ldap_conn = Connection(server, user=parameters.user_dn, password=parameters.user_pw,
                                   auto_bind=True)
            return ldap_conn

        except LDAPExceptionError, e:
            print e.message
            print e.args
            sys.exit(1)

    def search(self, parameters, filter, attrs, total_entries=None):

        connection = self.getConnection(parameters)

        connection.search(search_base=parameters.dump_dn, search_filter=filter, search_scope=SUBTREE,
                          attributes=attrs, paged_size=5)

        results = connection.response

        cookie = connection.result['controls']['1.2.840.113556.1.4.319']['value']['cookie']

        while cookie:
            connection.search(search_base = parameters.dump_dn, search_filter = filter, search_scope = SUBTREE,
                              attributes = attrs, paged_size = 5, paged_cookie = cookie)

            results += connection.response

            cookie = connection.result['controls']['1.2.840.113556.1.4.319']['value']['cookie']

        results_json = connection.response_to_json(search_result=results)

        return results_json

