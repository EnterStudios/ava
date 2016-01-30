# Rest Imports
from rest_framework import status
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.learn.models import Path, Module, Role
from ava_core.my.models import LearningProfile, LearningHistory, LearningQueue
from ava_core.my.test_data import LearningProfileTestData, LearningHistoryTestData, LearningQueueTestData


# Implementation
class PathTestData(AvaCoreTestData):
    """
    Test data for Path
    """

    def __init__(self):
        # Store self information
        self.model = Path
        self.url = '/example'

        # Create any necessary required models.
        self.init_requirements()

    def init_requirements(self):
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if Module.objects.count() == 0:
            ModuleTestData.init_requirements()
            Module.objects.create(**ModuleTestData.get_data('standard'))
            Module.objects.create(**ModuleTestData.get_data('unique'))
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if Role.objects.count() == 0:
            RoleTestData.init_requirements()
            Role.objects.create(**RoleTestData.get_data('standard'))
            Role.objects.create(**RoleTestData.get_data('unique'))

    standard = {
        'name': 'standard_char',
        'description': 'standard_text',
        'path_modules': 'default',
        'path_roles': 'default',
    }

    unique = {
        'name': 'unique_char',
        'description': 'unique_text',
        'path_modules': 'default',
        'path_roles': 'default',
    }

    modified_name = {
        'name': 'modified_char',
        'description': 'standard_text',
        'path_modules': 'default',
        'path_roles': 'default',
    }
    missing_name = {
        'description': 'standard_text',
        'path_modules': 'default',
        'path_roles': 'default',
    }

    missing_description = {
        'name': 'standard_char',
        'path_modules': 'default',
        'path_roles': 'default',
    }
    modified_description = {
        'name': 'standard_char',
        'description': 'modified_text',
        'path_modules': 'default',
        'path_roles': 'default',
    }

    missing_path_modules = {
        'name': 'standard_char',
        'description': 'standard_text',
        'path_roles': 'default',
    }
    modified_path_modules = {
        'name': 'standard_char',
        'description': 'standard_text',
        'path_modules': 'default',
        'path_roles': 'default',
    }

    modified_path_roles = {
        'name': 'standard_char',
        'description': 'standard_text',
        'path_modules': 'default',
        'path_roles': 'default',
    }
    missing_path_roles = {
        'name': 'standard_char',
        'description': 'standard_text',
        'path_modules': 'default',
    }



class RoleTestData(AvaCoreTestData):
    """
    Test data for Role
    """

    def __init__(self):
        # Store self information
        self.model = Role
        self.url = '/example'

        # Create any necessary required models.
        self.init_requirements()

    def init_requirements(self):
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if LearningProfile.objects.count() == 0:
            LearningProfileTestData.init_requirements()
            LearningProfile.objects.create(**LearningProfileTestData.get_data('standard'))
            LearningProfile.objects.create(**LearningProfileTestData.get_data('unique'))
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if Path.objects.count() == 0:
            PathTestData.init_requirements()
            Path.objects.create(**PathTestData.get_data('standard'))
            Path.objects.create(**PathTestData.get_data('unique'))

    standard = {
        'profile_role': '/example/1/',
        'name': 'standard_char',
        'description': 'standard_text',
        'path': 'default',
    }

    unique = {
        'profile_role': '/example/2/',
        'name': 'unique_char',
        'description': 'unique_text',
        'path': 'default',
    }

    missing_profile_role = {
        'name': 'standard_char',
        'description': 'standard_text',
        'path': 'default',
    }
    modified_profile_role = {
        'profile_role': '/example/2/',
        'name': 'standard_char',
        'description': 'standard_text',
        'path': 'default',
    }

    modified_name = {
        'profile_role': '/example/1/',
        'name': 'modified_char',
        'description': 'standard_text',
        'path': 'default',
    }
    missing_name = {
        'profile_role': '/example/1/',
        'description': 'standard_text',
        'path': 'default',
    }

    missing_description = {
        'profile_role': '/example/1/',
        'name': 'standard_char',
        'path': 'default',
    }
    modified_description = {
        'profile_role': '/example/1/',
        'name': 'standard_char',
        'description': 'modified_text',
        'path': 'default',
    }

    missing_path = {
        'profile_role': '/example/1/',
        'name': 'standard_char',
        'description': 'standard_text',
    }
    modified_path = {
        'profile_role': '/example/1/',
        'name': 'standard_char',
        'description': 'standard_text',
        'path': 'default',
    }



class ModuleTestData(AvaCoreTestData):
    """
    Test data for Module
    """

    def __init__(self):
        # Store self information
        self.model = Module
        self.url = '/example'

        # Create any necessary required models.
        self.init_requirements()

    def init_requirements(self):
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if Module.objects.count() == 0:
            ModuleTestData.init_requirements()
            Module.objects.create(**ModuleTestData.get_data('standard'))
            Module.objects.create(**ModuleTestData.get_data('unique'))
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if LearningHistory.objects.count() == 0:
            LearningHistoryTestData.init_requirements()
            LearningHistory.objects.create(**LearningHistoryTestData.get_data('standard'))
            LearningHistory.objects.create(**LearningHistoryTestData.get_data('unique'))
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if Path.objects.count() == 0:
            PathTestData.init_requirements()
            Path.objects.create(**PathTestData.get_data('standard'))
            Path.objects.create(**PathTestData.get_data('unique'))
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if Module.objects.count() == 0:
            ModuleTestData.init_requirements()
            Module.objects.create(**ModuleTestData.get_data('standard'))
            Module.objects.create(**ModuleTestData.get_data('unique'))
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if LearningQueue.objects.count() == 0:
            LearningQueueTestData.init_requirements()
            LearningQueue.objects.create(**LearningQueueTestData.get_data('standard'))
            LearningQueue.objects.create(**LearningQueueTestData.get_data('unique'))

    standard = {
        'parent_module': '/example/1/',
        'history_module': '/example/1/',
        'description': 'standard_text',
        'module_url': 'standard_char',
        'name': 'standard_char',
        'path': 'default',
        'parent': '/example/1/',
        'queue_module': '/example/1/',
    }

    unique = {
        'parent_module': '/example/2/',
        'history_module': '/example/2/',
        'description': 'unique_text',
        'module_url': 'unique_char',
        'name': 'unique_char',
        'path': 'default',
        'parent': '/example/2/',
        'queue_module': '/example/2/',
    }

    modified_parent_module = {
        'parent_module': '/example/2/',
        'history_module': '/example/1/',
        'description': 'standard_text',
        'module_url': 'standard_char',
        'name': 'standard_char',
        'path': 'default',
        'parent': '/example/1/',
        'queue_module': '/example/1/',
    }
    missing_parent_module = {
        'history_module': '/example/1/',
        'description': 'standard_text',
        'module_url': 'standard_char',
        'name': 'standard_char',
        'path': 'default',
        'parent': '/example/1/',
        'queue_module': '/example/1/',
    }

    missing_history_module = {
        'parent_module': '/example/1/',
        'description': 'standard_text',
        'module_url': 'standard_char',
        'name': 'standard_char',
        'path': 'default',
        'parent': '/example/1/',
        'queue_module': '/example/1/',
    }
    modified_history_module = {
        'parent_module': '/example/1/',
        'history_module': '/example/2/',
        'description': 'standard_text',
        'module_url': 'standard_char',
        'name': 'standard_char',
        'path': 'default',
        'parent': '/example/1/',
        'queue_module': '/example/1/',
    }

    missing_description = {
        'parent_module': '/example/1/',
        'history_module': '/example/1/',
        'module_url': 'standard_char',
        'name': 'standard_char',
        'path': 'default',
        'parent': '/example/1/',
        'queue_module': '/example/1/',
    }
    modified_description = {
        'parent_module': '/example/1/',
        'history_module': '/example/1/',
        'description': 'modified_text',
        'module_url': 'standard_char',
        'name': 'standard_char',
        'path': 'default',
        'parent': '/example/1/',
        'queue_module': '/example/1/',
    }

    modified_module_url = {
        'parent_module': '/example/1/',
        'history_module': '/example/1/',
        'description': 'standard_text',
        'module_url': 'modified_char',
        'name': 'standard_char',
        'path': 'default',
        'parent': '/example/1/',
        'queue_module': '/example/1/',
    }
    missing_module_url = {
        'parent_module': '/example/1/',
        'history_module': '/example/1/',
        'description': 'standard_text',
        'name': 'standard_char',
        'path': 'default',
        'parent': '/example/1/',
        'queue_module': '/example/1/',
    }

    modified_name = {
        'parent_module': '/example/1/',
        'history_module': '/example/1/',
        'description': 'standard_text',
        'module_url': 'standard_char',
        'name': 'modified_char',
        'path': 'default',
        'parent': '/example/1/',
        'queue_module': '/example/1/',
    }
    missing_name = {
        'parent_module': '/example/1/',
        'history_module': '/example/1/',
        'description': 'standard_text',
        'module_url': 'standard_char',
        'path': 'default',
        'parent': '/example/1/',
        'queue_module': '/example/1/',
    }

    missing_path = {
        'parent_module': '/example/1/',
        'history_module': '/example/1/',
        'description': 'standard_text',
        'module_url': 'standard_char',
        'name': 'standard_char',
        'parent': '/example/1/',
        'queue_module': '/example/1/',
    }
    modified_path = {
        'parent_module': '/example/1/',
        'history_module': '/example/1/',
        'description': 'standard_text',
        'module_url': 'standard_char',
        'name': 'standard_char',
        'path': 'default',
        'parent': '/example/1/',
        'queue_module': '/example/1/',
    }

    missing_parent = {
        'parent_module': '/example/1/',
        'history_module': '/example/1/',
        'description': 'standard_text',
        'module_url': 'standard_char',
        'name': 'standard_char',
        'path': 'default',
        'queue_module': '/example/1/',
    }
    modified_parent = {
        'parent_module': '/example/1/',
        'history_module': '/example/1/',
        'description': 'standard_text',
        'module_url': 'standard_char',
        'name': 'standard_char',
        'path': 'default',
        'parent': '/example/2/',
        'queue_module': '/example/1/',
    }

    modified_queue_module = {
        'parent_module': '/example/1/',
        'history_module': '/example/1/',
        'description': 'standard_text',
        'module_url': 'standard_char',
        'name': 'standard_char',
        'path': 'default',
        'parent': '/example/1/',
        'queue_module': '/example/2/',
    }
    missing_queue_module = {
        'parent_module': '/example/1/',
        'history_module': '/example/1/',
        'description': 'standard_text',
        'module_url': 'standard_char',
        'name': 'standard_char',
        'path': 'default',
        'parent': '/example/1/',
    }




