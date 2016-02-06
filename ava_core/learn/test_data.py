# Rest Imports
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.learn.models import Role, Module, Path


# Implementation
class RoleTestData(AvaCoreTestData):
    """
    Test data for Role
    """

    @staticmethod
    def init_requirements(owner):
        pass

    # Store self information
    model = Role
    url = 'example/'

    standard = {
        'name': 'standard_char',
        'profile_role': 'example//1/',
        'description': 'standard_text',
        'path': 'default',
    }

    unique = {
        'name': 'unique_char',
        'profile_role': 'example//2/',
        'description': 'unique_text',
        'path': 'default',
    }


class ModuleTestData(AvaCoreTestData):
    """
    Test data for Module
    """

    @staticmethod
    def init_requirements(owner):
        pass

    # Store self information
    model = Module
    url = 'example/'

    standard = {
        'name': 'standard_char',
        'module_url': 'standard_char',
        'history_module': 'example//1/',
        'description': 'standard_text',
        'path': 'default',
        'parent': 'example//1/',
        'queue_module': 'example//1/',
        'parent_module': 'example//1/',
    }

    unique = {
        'name': 'unique_char',
        'module_url': 'unique_char',
        'history_module': 'example//2/',
        'description': 'unique_text',
        'path': 'default',
        'parent': 'example//2/',
        'queue_module': 'example//2/',
        'parent_module': 'example//2/',
    }


class PathTestData(AvaCoreTestData):
    """
    Test data for Path
    """

    @staticmethod
    def init_requirements(owner):
        pass

    # Store self information
    model = Path
    url = 'example/'

    standard = {
        'path_roles': 'default',
        'name': 'standard_char',
        'description': 'standard_text',
        'path_modules': 'default',
    }

    unique = {
        'path_roles': 'default',
        'name': 'unique_char',
        'description': 'unique_text',
        'path_modules': 'default',
    }
