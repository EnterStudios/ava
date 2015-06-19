import datetime
import re
import sys

__author__ = 'ladynerd'
# import ldap, ldif, datetime, re
# from ldap import *
# from ldap.controls import *
# from ldap.cidict import cidict
from StringIO import StringIO

from ldap3 import *

class ActiveDirectoryHelper():

    PAGESIZE=1000

    # LDAP date/times in FILETIME format use this as their epoch
    FILETIME_EPOCH = datetime.datetime(1601, 1, 1, 0, 0, 0)
    # Upper bound on valid FILETIME values.
    FILETIME_MAX = (datetime.datetime.max - FILETIME_EPOCH).total_seconds() * 1000000
    # Regular expression to check for valid FILETIME values.
    TIME_FILETIME = re.compile(r'^\d+$')
    # Regular expression to check for valid date/time string values.
    TIME_DATESTRING = re.compile(r'^(?P<yr>\d{4})(?P<mon>0[1-9]|1[012])(?P<day>0[1-9]|[12][0-9]|3[01])(?P<hr>[01][0-9]|2[0-3])(?P<min>[0-5][0-9])(?P<sec>[0-5][0-9])(?:\.\d{1,3})?Z$')

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

        cookie = connection.result['controls']['1.2.840.113556.1.4.319']['value']['cookie']

        while cookie:
            connection.search(search_base = parameters.dump_dn, search_filter = filter, search_scope = SUBTREE,
                              attributes = attrs, paged_size = 5, paged_cookie = cookie)

            #print "loop iteration"

            cookie = connection.result['controls']['1.2.840.113556.1.4.319']['value']['cookie']
        return connection.response_to_json()

    def cleanhex(self,val):
        s = ['\\%02X' % ord(x) for x in val]
        return ''.join(s)

    def convert_date_time(self, dateValue):
        # Check if the data is a Windows FILETIME value.
        match = self.TIME_FILETIME.match(dateValue)
        if match:
            microseconds = long(dateValue) / 10
            if microseconds > 0:
                if microseconds > self.FILETIME_MAX:
                    return datetime.datetime.max
                delta = datetime.timedelta(microseconds=microseconds)
                return self.FILETIME_EPOCH + delta
            return None

        # Check if the data is a date string.
        match = self.TIME_DATESTRING.match(dateValue)
        if match:
            time_year = int(match.group('yr'))
            time_month = int(match.group('mon'))
            time_day = int(match.group('day'))
            time_hour = int(match.group('hr'))
            time_minute = int(match.group('min'))
            time_second = int(match.group('sec'))
            return datetime.datetime(time_year, time_month, time_day, time_hour, time_minute, time_second)

        # No value.
        return None




# class LDAPSearchResult:
#     dn = ''
#     attrs = {}
#     page_size = 10
#
#     def __init__(self, entry_tuple):
#         (dn, attrs) = entry_tuple
#         if dn:
#             self.dn = dn
#         else:
#             return
#
#         self.attrs = cidict(attrs)
#
#
#     def get_attributes(self):
#         return self.attrs
#
#
#     def set_attributes(self, attr_dict):
#         self.attrs = cidict(attr_dict)
#
#
#     def has_attribute(self, attr_name):
#         return self.attrs.has_key(attr_name)
#
#
#     def get_attr_values(self, key):
#         return self.attrs[key]
#
#
#     def get_attr_names(self):
#         return self.attrs.keys()
#
#
#     def get_dn(self):
#         return self.dn
#
#
#     def pretty_print(self):
#         str = "DN: " + self.dn + "\n"
#         for a, v_list in self.attrs.iteritems():
#             str = str + "Name: " + a + "\n"
#         for v in v_list:
#             str = str + " Value: " + v + "\n"
#             str = str + "========"
#         return str
#
#
#     def to_ldif(self):
#         out = StringIO()
#         ldif_out = ldif.LDIFWriter(out)
#         newdata = {}
#         if hasattr(self, 'attrs'):
#             newdata.update(self.attrs)
#         ldif_out.unparse(self.dn, newdata)
#         return out.getvalue()



