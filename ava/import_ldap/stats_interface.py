# flake8: noqa

__author__ = 'ladynerd'

from ava.import_ldap.models import LDAPConfiguration, ActiveDirectoryUser
<<<<<<< HEAD
=======

>>>>>>> origin/fix_know_dashboard

class LDAPStatistics():
    LDAP_CONFIG = None
    DESC = '-'
    ASC = ''

    def get_stats(self, ldap_config):
        self.LDAP_CONFIG = ldap_config
        all_users = ActiveDirectoryUser.objects.filter(ldap_configuration=self.LDAP_CONFIG)
        results = {
            'never_expires': self.get_never_expires(all_users),
            'admin_accounts': self.get_admin_accounts(all_users),
            'never_logged_in': self.get_never_logged_in(all_users),
            'logon_count': self.get_logon_count(self.DESC),
            'password_last_set': self.get_password_last_set(self.DESC),
            'connection_size': self.get_connection_size(self.DESC),
        }

        return results

    # Checks the current active directory users for this ldap configuration and returns all users that do not expire
    @staticmethod
    def get_never_expires(users):
        results = []

        for user in users:
            if str.startswith(str(user.account_expires), "9999"):
                # print("found one : " + user.name + " = " + user.account_expires)
                results.append(user)

        # print(len(results))
        return results

    @staticmethod
    def get_admin_accounts(users):
        results = []

        for user in users:
            if user.admin_count == 1:
                results.append(user)

        return results

    @staticmethod
    def get_never_logged_in(users):
        results = []

        for user in users:
            if user.logon_count is None:
                results.append(user)

        return results

    def get_logon_count(self, direction):
        if direction is self.DESC:
            return ActiveDirectoryUser.objects.filter(ldap_configuration=self.LDAP_CONFIG).order_by('-logon_count')
        else:
            return ActiveDirectoryUser.objects.filter(ldap_configuration=self.LDAP_CONFIG).order_by('logon_count')

<<<<<<< HEAD
    def get_password_last_set(self, direction):
        if direction is self.DESC:
            return ActiveDirectoryUser.objects.filter(ldap_configuration=self.LDAP_CONFIG).order_by('-pwd_last_set')
        else:
            return ActiveDirectoryUser.objects.filter(ldap_configuration=self.LDAP_CONFIG).order_by('pwd_last_set')

=======
    DESC = '-'
    ASC = ''

    def get_stats(self, ldap_config):
        self.LDAP_CONFIG = ldap_config
        all_users = ActiveDirectoryUser.objects.filter(ldap_configuration=self.LDAP_CONFIG)
        results = {
            'never_expires': self.get_never_expires(all_users),
            'admin_accounts': self.get_admin_accounts(all_users),
            'never_logged_in': self.get_never_logged_in(all_users),
            'logon_count': self.get_logon_count(self.DESC),
            'password_last_set': self.get_password_last_set(self.DESC),
            'connection_size': self.get_connection_size(self.DESC),
        }

        return results

    # Checks the current active directory users for this ldap configuration and returns all users that do not expire
    @staticmethod
    def get_never_expires(users):
        results = []

        for user in users:
            if str.startswith(str(user.account_expires), "9999"):
                # print("found one : " + user.name + " = " + user.account_expires)
                results.append(user)

        # print(len(results))
        return results

    @staticmethod
    def get_admin_accounts(users):
        results = []

        for user in users:
            if user.admin_count == 1:
                results.append(user)

        return results

    @staticmethod
    def get_never_logged_in(users):
        results = []

        for user in users:
            if user.logon_count is None:
                results.append(user)

        return results

    def get_logon_count(self, direction):
        if direction is self.DESC:
            return ActiveDirectoryUser.objects.filter(ldap_configuration=self.LDAP_CONFIG).order_by('-logon_count')
        else:
            return ActiveDirectoryUser.objects.filter(ldap_configuration=self.LDAP_CONFIG).order_by('logon_count')

    def get_password_last_set(self, direction):
        if direction is self.DESC:
            return ActiveDirectoryUser.objects.filter(ldap_configuration=self.LDAP_CONFIG).order_by('-pwd_last_set')
        else:
            return ActiveDirectoryUser.objects.filter(ldap_configuration=self.LDAP_CONFIG).order_by('pwd_last_set')

>>>>>>> origin/fix_know_dashboard
    def get_connection_size(self, direction):
        pass
