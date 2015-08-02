# flake8: noqa
import operator

__author__ = 'ladynerd'

from ava.import_google.models import GoogleDirectoryUser

class GoogleStatistics():
    GOOGLE_CONFIG = None

    def get_all_stats(self):
        all_users = GoogleDirectoryUser.objects.filter()
        results = {
            'never_expires': self.get_never_expires(all_users),
            'admin_accounts': self.get_admin_accounts(all_users),
            'delegated_admin_accounts': self.get_delegated_admin_accounts(all_users),
            'never_logged_in': self.get_never_logged_in(all_users),
            'connection_size': self.get_connection_size(all_users),
        }

        return results

    def get_stats(self, google_config):
        self.GOOGLE_CONFIG = google_config
        all_users = GoogleDirectoryUser.objects.filter(google_configuration=self.GOOGLE_CONFIG)
        results = {
            'never_expires': self.get_never_expires(all_users),
            'admin_accounts': self.get_admin_accounts(all_users),
            'delegated_admin_accounts': self.get_delegated_admin_accounts(all_users),
            'never_logged_in': self.get_never_logged_in(all_users),
            'connection_size': self.get_connection_size(all_users),
        }

        return results

    @staticmethod
    def get_admin_accounts(users):
        results = []

        for user in users:
            if user.is_admin is True:
                results.append(user)

        return results

    @staticmethod
    def get_delegated_admin_accounts(users):
        results = []

        for user in users:
            if user.is_delegated_admin is True:
                results.append(user)

        return results

    @staticmethod
    def get_never_logged_in(users):
        results = []

        for user in users:
            if user.last_logon_time is None:
                results.append(user)

        return results

    def get_connection_size(self, users):
        results = {}

        for user in users:
            results[user] = user.groups.len()

        sorted_results = sorted(results.items(), key=operator.itemgetter(1))
        return sorted_results
