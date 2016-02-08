# Rest Imports
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.learn.models import Role, Module, Path


# Implementation
class RoleTestData(AvaCoreTestData):

    # Store self information
    model = Role
    url = 'learn/role/'

    standard = {
        'name': 'standard_char',
        'description': 'standard_text',
        'path': [],
    }

    unique = {
        'name': 'unique_char',
        'description': 'unique_text',
        'path': [],
    }


class ModuleTestData(AvaCoreTestData):
    # Store self information
    model = Module
    url = 'learn/module/'

    standard = {
        'name': 'standard_char',
        'module_url': 'http://www.example.com',
        'description': 'standard_text',
        'path': [],
    }

    unique = {
        'name': 'unique_char',
        'module_url': 'http://www.example2.com',
        'description': 'unique_text',
        'path': [],
    }


class PathTestData(AvaCoreTestData):

    # Store self information
    model = Path
    url = 'learn/path/'

    standard = {
        'name': 'standard_char',
        'description': 'standard_text',
        'path_roles': [],
        'path_modules': [],
    }

    unique = {
        'name': 'unique_char',
        'description': 'unique_text',
        'path_roles': [],
        'path_modules': [],
    }
