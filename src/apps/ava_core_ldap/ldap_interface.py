__author__ = 'ladynerd'

from ldap3 import Server, Connection, LDAPExceptionError, SUBTREE
import sys


class ActiveDirectoryHelper:
    PAGESIZE = 1000

    def get_connection(self, parameters):
        try:
            server = Server(parameters.server)
            ldap_conn = Connection(server, user=parameters.user_dn, password=parameters.user_pw,
                                   auto_bind=True)
            return ldap_conn

        except LDAPExceptionError, e:
            print e.message
            print e.args
            sys.exit(1)

    def search(self, parameters, filterby, attrs):

        connection = self.get_connection(parameters)

        connection.search(search_base=parameters.dump_dn, search_filter=filterby, search_scope=SUBTREE,
                          attributes=attrs, paged_size=5)

        results = connection.response

        cookie = connection.result['controls']['1.2.840.113556.1.4.319']['value']['cookie']

        while cookie:
            connection.search(search_base=parameters.dump_dn, search_filter=filterby, search_scope=SUBTREE,
                              attributes=attrs, paged_size=5, paged_cookie=cookie)

            results += connection.response

            cookie = connection.result['controls']['1.2.840.113556.1.4.319']['value']['cookie']

        results_json = connection.response_to_json(search_result=results)

        connection.close()

        return results_json
