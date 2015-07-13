__author__ = 'ladynerd'

from ava.import_ldap.models import LDAPConfiguration

class LDAPStatistics(ldap_configuration):

    LDAP_CONFIG = None

    def __init__(self):
        LDAP_CONFIG = ldap_configuration

