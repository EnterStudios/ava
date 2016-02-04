# Rest Imports
from rest_framework import status
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.learn.models import Module, Role, Path


# Implementation
class ModuleTestData(AvaCoreTestData):
    """
    Test data for Module
    """

    @staticmethod
    def init_requirements():
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if Path.objects.count() == 0:
            PathTestData.init_requirements()
            model = Path.objects.create(**PathTestData.get_data('standard'))
            model.save()
            model = Path.objects.create(**PathTestData.get_data('unique'))
            model.save()

        # Import the required model and data
        from ava_core.my.models import LearningHistory
        from ava_core.my.test_data import LearningHistoryTestData
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if LearningHistory.objects.count() == 0:
            LearningHistoryTestData.init_requirements()
            model = LearningHistory.objects.create(**LearningHistoryTestData.get_data('standard'))
            model.save()
            model = LearningHistory.objects.create(**LearningHistoryTestData.get_data('unique'))
            model.save()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if Module.objects.count() == 0:
            ModuleTestData.init_requirements()
            model = Module.objects.create(**ModuleTestData.get_data('standard'))
            model.save()
            model = Module.objects.create(**ModuleTestData.get_data('unique'))
            model.save()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if Module.objects.count() == 0:
            ModuleTestData.init_requirements()
            model = Module.objects.create(**ModuleTestData.get_data('standard'))
            model.save()
            model = Module.objects.create(**ModuleTestData.get_data('unique'))
            model.save()

        # Import the required model and data
        from ava_core.my.models import LearningQueue
        from ava_core.my.test_data import LearningQueueTestData
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if LearningQueue.objects.count() == 0:
            LearningQueueTestData.init_requirements()
            model = LearningQueue.objects.create(**LearningQueueTestData.get_data('standard'))
            model.save()
            model = LearningQueue.objects.create(**LearningQueueTestData.get_data('unique'))
            model.save()

    # Store self information
    model = Module
    url = '/example'

    standard = {
        'path': 'default',
        'history_module': '/example/1/',
        'parent_module': '/example/1/',
        'description': 'standard_text',
        'parent': '/example/1/',
        'queue_module': '/example/1/',
        'module_url': 'standard_char',
        'name': 'standard_char',
    }

    unique = {
        'path': 'default',
        'history_module': '/example/2/',
        'parent_module': '/example/2/',
        'description': 'unique_text',
        'parent': '/example/2/',
        'queue_module': '/example/2/',
        'module_url': 'unique_char',
        'name': 'unique_char',
    }

    modified_path = {
        'path': 'default',
        'history_module': '/example/1/',
        'parent_module': '/example/1/',
        'description': 'standard_text',
        'parent': '/example/1/',
        'queue_module': '/example/1/',
        'module_url': 'standard_char',
        'name': 'standard_char',
    }
    missing_path = {
        'history_module': '/example/1/',
        'parent_module': '/example/1/',
        'description': 'standard_text',
        'parent': '/example/1/',
        'queue_module': '/example/1/',
        'module_url': 'standard_char',
        'name': 'standard_char',
    }

    modified_history_module = {
        'path': 'default',
        'history_module': '/example/2/',
        'parent_module': '/example/1/',
        'description': 'standard_text',
        'parent': '/example/1/',
        'queue_module': '/example/1/',
        'module_url': 'standard_char',
        'name': 'standard_char',
    }
    missing_history_module = {
        'path': 'default',
        'parent_module': '/example/1/',
        'description': 'standard_text',
        'parent': '/example/1/',
        'queue_module': '/example/1/',
        'module_url': 'standard_char',
        'name': 'standard_char',
    }

    missing_parent_module = {
        'path': 'default',
        'history_module': '/example/1/',
        'description': 'standard_text',
        'parent': '/example/1/',
        'queue_module': '/example/1/',
        'module_url': 'standard_char',
        'name': 'standard_char',
    }
    modified_parent_module = {
        'path': 'default',
        'history_module': '/example/1/',
        'parent_module': '/example/2/',
        'description': 'standard_text',
        'parent': '/example/1/',
        'queue_module': '/example/1/',
        'module_url': 'standard_char',
        'name': 'standard_char',
    }

    modified_description = {
        'path': 'default',
        'history_module': '/example/1/',
        'parent_module': '/example/1/',
        'description': 'modified_text',
        'parent': '/example/1/',
        'queue_module': '/example/1/',
        'module_url': 'standard_char',
        'name': 'standard_char',
    }
    missing_description = {
        'path': 'default',
        'history_module': '/example/1/',
        'parent_module': '/example/1/',
        'parent': '/example/1/',
        'queue_module': '/example/1/',
        'module_url': 'standard_char',
        'name': 'standard_char',
    }

    missing_parent = {
        'path': 'default',
        'history_module': '/example/1/',
        'parent_module': '/example/1/',
        'description': 'standard_text',
        'queue_module': '/example/1/',
        'module_url': 'standard_char',
        'name': 'standard_char',
    }
    modified_parent = {
        'path': 'default',
        'history_module': '/example/1/',
        'parent_module': '/example/1/',
        'description': 'standard_text',
        'parent': '/example/2/',
        'queue_module': '/example/1/',
        'module_url': 'standard_char',
        'name': 'standard_char',
    }

    modified_queue_module = {
        'path': 'default',
        'history_module': '/example/1/',
        'parent_module': '/example/1/',
        'description': 'standard_text',
        'parent': '/example/1/',
        'queue_module': '/example/2/',
        'module_url': 'standard_char',
        'name': 'standard_char',
    }
    missing_queue_module = {
        'path': 'default',
        'history_module': '/example/1/',
        'parent_module': '/example/1/',
        'description': 'standard_text',
        'parent': '/example/1/',
        'module_url': 'standard_char',
        'name': 'standard_char',
    }

    missing_module_url = {
        'path': 'default',
        'history_module': '/example/1/',
        'parent_module': '/example/1/',
        'description': 'standard_text',
        'parent': '/example/1/',
        'queue_module': '/example/1/',
        'name': 'standard_char',
    }
    modified_module_url = {
        'path': 'default',
        'history_module': '/example/1/',
        'parent_module': '/example/1/',
        'description': 'standard_text',
        'parent': '/example/1/',
        'queue_module': '/example/1/',
        'module_url': 'modified_char',
        'name': 'standard_char',
    }

    modified_name = {
        'path': 'default',
        'history_module': '/example/1/',
        'parent_module': '/example/1/',
        'description': 'standard_text',
        'parent': '/example/1/',
        'queue_module': '/example/1/',
        'module_url': 'standard_char',
        'name': 'modified_char',
    }
    missing_name = {
        'path': 'default',
        'history_module': '/example/1/',
        'parent_module': '/example/1/',
        'description': 'standard_text',
        'parent': '/example/1/',
        'queue_module': '/example/1/',
        'module_url': 'standard_char',
    }



class RoleTestData(AvaCoreTestData):
    """
    Test data for Role
    """

    @staticmethod
    def init_requirements():
        # Import the required model and data
        from ava_core.my.models import LearningProfile
        from ava_core.my.test_data import LearningProfileTestData
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if LearningProfile.objects.count() == 0:
            LearningProfileTestData.init_requirements()
            model = LearningProfile.objects.create(**LearningProfileTestData.get_data('standard'))
            model.save()
            model = LearningProfile.objects.create(**LearningProfileTestData.get_data('unique'))
            model.save()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if Path.objects.count() == 0:
            PathTestData.init_requirements()
            model = Path.objects.create(**PathTestData.get_data('standard'))
            model.save()
            model = Path.objects.create(**PathTestData.get_data('unique'))
            model.save()

    # Store self information
    model = Role
    url = '/example'

    standard = {
        'profile_role': '/example/1/',
        'path': 'default',
        'description': 'standard_text',
        'name': 'standard_char',
    }

    unique = {
        'profile_role': '/example/2/',
        'path': 'default',
        'description': 'unique_text',
        'name': 'unique_char',
    }

    modified_profile_role = {
        'profile_role': '/example/2/',
        'path': 'default',
        'description': 'standard_text',
        'name': 'standard_char',
    }
    missing_profile_role = {
        'path': 'default',
        'description': 'standard_text',
        'name': 'standard_char',
    }

    modified_path = {
        'profile_role': '/example/1/',
        'path': 'default',
        'description': 'standard_text',
        'name': 'standard_char',
    }
    missing_path = {
        'profile_role': '/example/1/',
        'description': 'standard_text',
        'name': 'standard_char',
    }

    modified_description = {
        'profile_role': '/example/1/',
        'path': 'default',
        'description': 'modified_text',
        'name': 'standard_char',
    }
    missing_description = {
        'profile_role': '/example/1/',
        'path': 'default',
        'name': 'standard_char',
    }

    modified_name = {
        'profile_role': '/example/1/',
        'path': 'default',
        'description': 'standard_text',
        'name': 'modified_char',
    }
    missing_name = {
        'profile_role': '/example/1/',
        'path': 'default',
        'description': 'standard_text',
    }



class PathTestData(AvaCoreTestData):
    """
    Test data for Path
    """

    @staticmethod
    def init_requirements():
        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if Role.objects.count() == 0:
            RoleTestData.init_requirements()
            model = Role.objects.create(**RoleTestData.get_data('standard'))
            model.save()
            model = Role.objects.create(**RoleTestData.get_data('unique'))
            model.save()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if Module.objects.count() == 0:
            ModuleTestData.init_requirements()
            model = Module.objects.create(**ModuleTestData.get_data('standard'))
            model.save()
            model = Module.objects.create(**ModuleTestData.get_data('unique'))
            model.save()

    # Store self information
    model = Path
    url = '/example'

    standard = {
        'path_roles': 'default',
        'description': 'standard_text',
        'path_modules': 'default',
        'name': 'standard_char',
    }

    unique = {
        'path_roles': 'default',
        'description': 'unique_text',
        'path_modules': 'default',
        'name': 'unique_char',
    }

    missing_path_roles = {
        'description': 'standard_text',
        'path_modules': 'default',
        'name': 'standard_char',
    }
    modified_path_roles = {
        'path_roles': 'default',
        'description': 'standard_text',
        'path_modules': 'default',
        'name': 'standard_char',
    }

    modified_description = {
        'path_roles': 'default',
        'description': 'modified_text',
        'path_modules': 'default',
        'name': 'standard_char',
    }
    missing_description = {
        'path_roles': 'default',
        'path_modules': 'default',
        'name': 'standard_char',
    }

    missing_path_modules = {
        'path_roles': 'default',
        'description': 'standard_text',
        'name': 'standard_char',
    }
    modified_path_modules = {
        'path_roles': 'default',
        'description': 'standard_text',
        'path_modules': 'default',
        'name': 'standard_char',
    }

    modified_name = {
        'path_roles': 'default',
        'description': 'standard_text',
        'path_modules': 'default',
        'name': 'modified_char',
    }
    missing_name = {
        'path_roles': 'default',
        'description': 'standard_text',
        'path_modules': 'default',
    }




