# Rest Imports
from rest_framework import status
# Local Imports
from ava_core.abstract.test_data import AvaCoreTestData
from ava_core.learn.models import Path, Module, Role


# Implementation
class PathTestData(AvaCoreTestData):
    """
    Test data for Path
    """

    @staticmethod
    def init_requirements(owner):
        # Grab data for object creation, with owner if required.
        data_model = ModuleTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = Module.objects.filter(owner=owner['email']) if 'email' in standard_data else Module.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            ModuleTestData.init_requirements(owner)
            model = Module.objects.create(**standard_data)
            model = Module.objects.create(**unique_data)

        # Grab data for object creation, with owner if required.
        data_model = RoleTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = Role.objects.filter(owner=owner['email']) if 'email' in standard_data else Role.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            RoleTestData.init_requirements(owner)
            model = Role.objects.create(**standard_data)
            model = Role.objects.create(**unique_data)

    # Store self information
    model = Path
    url = 'example/'

    standard = {
        'path_modules': 'default',
        'description': 'standard_text',
        'path_roles': 'default',
        'name': 'standard_char',
    }

    unique = {
        'path_modules': 'default',
        'description': 'unique_text',
        'path_roles': 'default',
        'name': 'unique_char',
    }

    modified_path_modules = {
        'path_modules': 'default',
        'description': 'standard_text',
        'path_roles': 'default',
        'name': 'standard_char',
    }
    missing_path_modules = {
        'description': 'standard_text',
        'path_roles': 'default',
        'name': 'standard_char',
    }

    missing_description = {
        'path_modules': 'default',
        'path_roles': 'default',
        'name': 'standard_char',
    }
    modified_description = {
        'path_modules': 'default',
        'description': 'modified_text',
        'path_roles': 'default',
        'name': 'standard_char',
    }

    missing_path_roles = {
        'path_modules': 'default',
        'description': 'standard_text',
        'name': 'standard_char',
    }
    modified_path_roles = {
        'path_modules': 'default',
        'description': 'standard_text',
        'path_roles': 'default',
        'name': 'standard_char',
    }

    modified_name = {
        'path_modules': 'default',
        'description': 'standard_text',
        'path_roles': 'default',
        'name': 'modified_char',
    }
    missing_name = {
        'path_modules': 'default',
        'description': 'standard_text',
        'path_roles': 'default',
    }



class ModuleTestData(AvaCoreTestData):
    """
    Test data for Module
    """

    @staticmethod
    def init_requirements(owner):
        # Grab data for object creation, with owner if required.
        data_model = ModuleTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = Module.objects.filter(owner=owner['email']) if 'email' in standard_data else Module.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            ModuleTestData.init_requirements(owner)
            model = Module.objects.create(**standard_data)
            model = Module.objects.create(**unique_data)

        # Import the required model and data
        from ava_core.my.models import LearningHistory
        from ava_core.my.test_data import LearningHistoryTestData
        # Grab data for object creation, with owner if required.
        data_model = LearningHistoryTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = LearningHistory.objects.filter(owner=owner['email']) if 'email' in standard_data else LearningHistory.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            LearningHistoryTestData.init_requirements(owner)
            model = LearningHistory.objects.create(**standard_data)
            model = LearningHistory.objects.create(**unique_data)

        # Import the required model and data
        from ava_core.my.models import LearningQueue
        from ava_core.my.test_data import LearningQueueTestData
        # Grab data for object creation, with owner if required.
        data_model = LearningQueueTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = LearningQueue.objects.filter(owner=owner['email']) if 'email' in standard_data else LearningQueue.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            LearningQueueTestData.init_requirements(owner)
            model = LearningQueue.objects.create(**standard_data)
            model = LearningQueue.objects.create(**unique_data)

        # Grab data for object creation, with owner if required.
        data_model = PathTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = Path.objects.filter(owner=owner['email']) if 'email' in standard_data else Path.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            PathTestData.init_requirements(owner)
            model = Path.objects.create(**standard_data)
            model = Path.objects.create(**unique_data)

        # Grab data for object creation, with owner if required.
        data_model = ModuleTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = Module.objects.filter(owner=owner['email']) if 'email' in standard_data else Module.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            ModuleTestData.init_requirements(owner)
            model = Module.objects.create(**standard_data)
            model = Module.objects.create(**unique_data)

    # Store self information
    model = Module
    url = 'example/'

    standard = {
        'module_url': 'standard_char',
        'parent_module': 'example//1/',
        'history_module': 'example//1/',
        'queue_module': 'example//1/',
        'description': 'standard_text',
        'path': 'default',
        'name': 'standard_char',
        'parent': 'example//1/',
    }

    unique = {
        'module_url': 'unique_char',
        'parent_module': 'example//2/',
        'history_module': 'example//2/',
        'queue_module': 'example//2/',
        'description': 'unique_text',
        'path': 'default',
        'name': 'unique_char',
        'parent': 'example//2/',
    }

    missing_module_url = {
        'parent_module': 'example//1/',
        'history_module': 'example//1/',
        'queue_module': 'example//1/',
        'description': 'standard_text',
        'path': 'default',
        'name': 'standard_char',
        'parent': 'example//1/',
    }
    modified_module_url = {
        'module_url': 'modified_char',
        'parent_module': 'example//1/',
        'history_module': 'example//1/',
        'queue_module': 'example//1/',
        'description': 'standard_text',
        'path': 'default',
        'name': 'standard_char',
        'parent': 'example//1/',
    }

    missing_parent_module = {
        'module_url': 'standard_char',
        'history_module': 'example//1/',
        'queue_module': 'example//1/',
        'description': 'standard_text',
        'path': 'default',
        'name': 'standard_char',
        'parent': 'example//1/',
    }
    modified_parent_module = {
        'module_url': 'standard_char',
        'parent_module': 'example//2/',
        'history_module': 'example//1/',
        'queue_module': 'example//1/',
        'description': 'standard_text',
        'path': 'default',
        'name': 'standard_char',
        'parent': 'example//1/',
    }

    missing_history_module = {
        'module_url': 'standard_char',
        'parent_module': 'example//1/',
        'queue_module': 'example//1/',
        'description': 'standard_text',
        'path': 'default',
        'name': 'standard_char',
        'parent': 'example//1/',
    }
    modified_history_module = {
        'module_url': 'standard_char',
        'parent_module': 'example//1/',
        'history_module': 'example//2/',
        'queue_module': 'example//1/',
        'description': 'standard_text',
        'path': 'default',
        'name': 'standard_char',
        'parent': 'example//1/',
    }

    modified_queue_module = {
        'module_url': 'standard_char',
        'parent_module': 'example//1/',
        'history_module': 'example//1/',
        'queue_module': 'example//2/',
        'description': 'standard_text',
        'path': 'default',
        'name': 'standard_char',
        'parent': 'example//1/',
    }
    missing_queue_module = {
        'module_url': 'standard_char',
        'parent_module': 'example//1/',
        'history_module': 'example//1/',
        'description': 'standard_text',
        'path': 'default',
        'name': 'standard_char',
        'parent': 'example//1/',
    }

    missing_description = {
        'module_url': 'standard_char',
        'parent_module': 'example//1/',
        'history_module': 'example//1/',
        'queue_module': 'example//1/',
        'path': 'default',
        'name': 'standard_char',
        'parent': 'example//1/',
    }
    modified_description = {
        'module_url': 'standard_char',
        'parent_module': 'example//1/',
        'history_module': 'example//1/',
        'queue_module': 'example//1/',
        'description': 'modified_text',
        'path': 'default',
        'name': 'standard_char',
        'parent': 'example//1/',
    }

    missing_path = {
        'module_url': 'standard_char',
        'parent_module': 'example//1/',
        'history_module': 'example//1/',
        'queue_module': 'example//1/',
        'description': 'standard_text',
        'name': 'standard_char',
        'parent': 'example//1/',
    }
    modified_path = {
        'module_url': 'standard_char',
        'parent_module': 'example//1/',
        'history_module': 'example//1/',
        'queue_module': 'example//1/',
        'description': 'standard_text',
        'path': 'default',
        'name': 'standard_char',
        'parent': 'example//1/',
    }

    modified_name = {
        'module_url': 'standard_char',
        'parent_module': 'example//1/',
        'history_module': 'example//1/',
        'queue_module': 'example//1/',
        'description': 'standard_text',
        'path': 'default',
        'name': 'modified_char',
        'parent': 'example//1/',
    }
    missing_name = {
        'module_url': 'standard_char',
        'parent_module': 'example//1/',
        'history_module': 'example//1/',
        'queue_module': 'example//1/',
        'description': 'standard_text',
        'path': 'default',
        'parent': 'example//1/',
    }

    modified_parent = {
        'module_url': 'standard_char',
        'parent_module': 'example//1/',
        'history_module': 'example//1/',
        'queue_module': 'example//1/',
        'description': 'standard_text',
        'path': 'default',
        'name': 'standard_char',
        'parent': 'example//2/',
    }
    missing_parent = {
        'module_url': 'standard_char',
        'parent_module': 'example//1/',
        'history_module': 'example//1/',
        'queue_module': 'example//1/',
        'description': 'standard_text',
        'path': 'default',
        'name': 'standard_char',
    }



class RoleTestData(AvaCoreTestData):
    """
    Test data for Role
    """

    @staticmethod
    def init_requirements(owner):
        # Import the required model and data
        from ava_core.my.models import LearningProfile
        from ava_core.my.test_data import LearningProfileTestData
        # Grab data for object creation, with owner if required.
        data_model = LearningProfileTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = LearningProfile.objects.filter(owner=owner['email']) if 'email' in standard_data else LearningProfile.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            LearningProfileTestData.init_requirements(owner)
            model = LearningProfile.objects.create(**standard_data)
            model = LearningProfile.objects.create(**unique_data)

        # Grab data for object creation, with owner if required.
        data_model = PathTestData()
        standard_data = data_model.get_data_with_owner(owner=owner, name='standard')
        unique_data = data_model.get_data_with_owner(owner=owner, name='unique')

        # Grab the required data set depending on if an owner is required.
        query_set = Path.objects.filter(owner=owner['email']) if 'email' in standard_data else Path.objects.all()

        # Check that requirements haven't already been created.
        # True - Create necessary requirements.
        if query_set.count() == 0:
            PathTestData.init_requirements(owner)
            model = Path.objects.create(**standard_data)
            model = Path.objects.create(**unique_data)

    # Store self information
    model = Role
    url = 'example/'

    standard = {
        'profile_role': 'example//1/',
        'description': 'standard_text',
        'path': 'default',
        'name': 'standard_char',
    }

    unique = {
        'profile_role': 'example//2/',
        'description': 'unique_text',
        'path': 'default',
        'name': 'unique_char',
    }

    modified_profile_role = {
        'profile_role': 'example//2/',
        'description': 'standard_text',
        'path': 'default',
        'name': 'standard_char',
    }
    missing_profile_role = {
        'description': 'standard_text',
        'path': 'default',
        'name': 'standard_char',
    }

    missing_description = {
        'profile_role': 'example//1/',
        'path': 'default',
        'name': 'standard_char',
    }
    modified_description = {
        'profile_role': 'example//1/',
        'description': 'modified_text',
        'path': 'default',
        'name': 'standard_char',
    }

    missing_path = {
        'profile_role': 'example//1/',
        'description': 'standard_text',
        'name': 'standard_char',
    }
    modified_path = {
        'profile_role': 'example//1/',
        'description': 'standard_text',
        'path': 'default',
        'name': 'standard_char',
    }

    modified_name = {
        'profile_role': 'example//1/',
        'description': 'standard_text',
        'path': 'default',
        'name': 'modified_char',
    }
    missing_name = {
        'profile_role': 'example//1/',
        'description': 'standard_text',
        'path': 'default',
    }




