# flake8: noqa
import logging

log = logging.getLogger(__name__)


class DirectoryHelper:
    def __init__(self):
        pass

    DATA_SOURCE = ''

    DATA_IMPORT_FILES = {
        'users': 'users',
        'groups': 'groups',
    }

    CREDENTIAL = None

    def import_directory(self, credential):
        pass

    def setup(self, credential):
        self.CREDENTIAL = credential

    def get_users(self):
        return None

    def get_groups(self):
        return None
