# Rest Imports
from rest_framework import status
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

    modified_name = {
        'name': 'modified_char',
        'profile_role': 'example//1/',
        'description': 'standard_text',
        'path': 'default',
    }
    missing_name = {
        'profile_role': 'example//1/',
        'description': 'standard_text',
        'path': 'default',
    }

    missing_profile_role = {
        'name': 'standard_char',
        'description': 'standard_text',
        'path': 'default',
    }
    modified_profile_role = {
        'name': 'standard_char',
        'profile_role': 'example//2/',
        'description': 'standard_text',
        'path': 'default',
    }

    missing_description = {
        'name': 'standard_char',
        'profile_role': 'example//1/',
        'path': 'default',
    }
    modified_description = {
        'name': 'standard_char',
        'profile_role': 'example//1/',
        'description': 'modified_text',
        'path': 'default',
    }

    missing_path = {
        'name': 'standard_char',
        'profile_role': 'example//1/',
        'description': 'standard_text',
    }
    modified_path = {
        'name': 'standard_char',
        'profile_role': 'example//1/',
        'description': 'standard_text',
        'path': 'default',
    }



class ModuleTestData(AvaCoreTestData):
    """
    Test data for Module
    """

    @staticmethod
    def init_requirements(owner):
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

    modified_name = {
        'name': 'modified_char',
        'module_url': 'standard_char',
        'history_module': 'example//1/',
        'description': 'standard_text',
        'path': 'default',
        'parent': 'example//1/',
        'queue_module': 'example//1/',
        'parent_module': 'example//1/',
    }
    missing_name = {
        'module_url': 'standard_char',
        'history_module': 'example//1/',
        'description': 'standard_text',
        'path': 'default',
        'parent': 'example//1/',
        'queue_module': 'example//1/',
        'parent_module': 'example//1/',
    }

    missing_module_url = {
        'name': 'standard_char',
        'history_module': 'example//1/',
        'description': 'standard_text',
        'path': 'default',
        'parent': 'example//1/',
        'queue_module': 'example//1/',
        'parent_module': 'example//1/',
    }
    modified_module_url = {
        'name': 'standard_char',
        'module_url': 'modified_char',
        'history_module': 'example//1/',
        'description': 'standard_text',
        'path': 'default',
        'parent': 'example//1/',
        'queue_module': 'example//1/',
        'parent_module': 'example//1/',
    }

    missing_history_module = {
        'name': 'standard_char',
        'module_url': 'standard_char',
        'description': 'standard_text',
        'path': 'default',
        'parent': 'example//1/',
        'queue_module': 'example//1/',
        'parent_module': 'example//1/',
    }
    modified_history_module = {
        'name': 'standard_char',
        'module_url': 'standard_char',
        'history_module': 'example//2/',
        'description': 'standard_text',
        'path': 'default',
        'parent': 'example//1/',
        'queue_module': 'example//1/',
        'parent_module': 'example//1/',
    }

    missing_description = {
        'name': 'standard_char',
        'module_url': 'standard_char',
        'history_module': 'example//1/',
        'path': 'default',
        'parent': 'example//1/',
        'queue_module': 'example//1/',
        'parent_module': 'example//1/',
    }
    modified_description = {
        'name': 'standard_char',
        'module_url': 'standard_char',
        'history_module': 'example//1/',
        'description': 'modified_text',
        'path': 'default',
        'parent': 'example//1/',
        'queue_module': 'example//1/',
        'parent_module': 'example//1/',
    }

    missing_path = {
        'name': 'standard_char',
        'module_url': 'standard_char',
        'history_module': 'example//1/',
        'description': 'standard_text',
        'parent': 'example//1/',
        'queue_module': 'example//1/',
        'parent_module': 'example//1/',
    }
    modified_path = {
        'name': 'standard_char',
        'module_url': 'standard_char',
        'history_module': 'example//1/',
        'description': 'standard_text',
        'path': 'default',
        'parent': 'example//1/',
        'queue_module': 'example//1/',
        'parent_module': 'example//1/',
    }

    modified_parent = {
        'name': 'standard_char',
        'module_url': 'standard_char',
        'history_module': 'example//1/',
        'description': 'standard_text',
        'path': 'default',
        'parent': 'example//2/',
        'queue_module': 'example//1/',
        'parent_module': 'example//1/',
    }
    missing_parent = {
        'name': 'standard_char',
        'module_url': 'standard_char',
        'history_module': 'example//1/',
        'description': 'standard_text',
        'path': 'default',
        'queue_module': 'example//1/',
        'parent_module': 'example//1/',
    }

    modified_queue_module = {
        'name': 'standard_char',
        'module_url': 'standard_char',
        'history_module': 'example//1/',
        'description': 'standard_text',
        'path': 'default',
        'parent': 'example//1/',
        'queue_module': 'example//2/',
        'parent_module': 'example//1/',
    }
    missing_queue_module = {
        'name': 'standard_char',
        'module_url': 'standard_char',
        'history_module': 'example//1/',
        'description': 'standard_text',
        'path': 'default',
        'parent': 'example//1/',
        'parent_module': 'example//1/',
    }

    missing_parent_module = {
        'name': 'standard_char',
        'module_url': 'standard_char',
        'history_module': 'example//1/',
        'description': 'standard_text',
        'path': 'default',
        'parent': 'example//1/',
        'queue_module': 'example//1/',
    }
    modified_parent_module = {
        'name': 'standard_char',
        'module_url': 'standard_char',
        'history_module': 'example//1/',
        'description': 'standard_text',
        'path': 'default',
        'parent': 'example//1/',
        'queue_module': 'example//1/',
        'parent_module': 'example//2/',
    }



class PathTestData(AvaCoreTestData):
    """
    Test data for Path
    """

    @staticmethod
    def init_requirements(owner):
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

    missing_path_roles = {
        'name': 'standard_char',
        'description': 'standard_text',
        'path_modules': 'default',
    }
    modified_path_roles = {
        'path_roles': 'default',
        'name': 'standard_char',
        'description': 'standard_text',
        'path_modules': 'default',
    }

    modified_name = {
        'path_roles': 'default',
        'name': 'modified_char',
        'description': 'standard_text',
        'path_modules': 'default',
    }
    missing_name = {
        'path_roles': 'default',
        'description': 'standard_text',
        'path_modules': 'default',
    }

    missing_description = {
        'path_roles': 'default',
        'name': 'standard_char',
        'path_modules': 'default',
    }
    modified_description = {
        'path_roles': 'default',
        'name': 'standard_char',
        'description': 'modified_text',
        'path_modules': 'default',
    }

    missing_path_modules = {
        'path_roles': 'default',
        'name': 'standard_char',
        'description': 'standard_text',
    }
    modified_path_modules = {
        'path_roles': 'default',
        'name': 'standard_char',
        'description': 'standard_text',
        'path_modules': 'default',
    }




