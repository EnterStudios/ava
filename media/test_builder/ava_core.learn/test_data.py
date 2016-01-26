# Rest Imports
# Local Imports
from ava_core.abstract.test_data import AvaTestData
from ava_core.learn.models import Module, Path, Role


# Implementation
class ModuleTestData(AvaTestData):
    """
    Test data for Module
    """

    model = Module
    url = '/example'

    standard = {
        'parent_module': 'REQUIRES: ava_core.learn.models.Module',
        'queue_module': 'REQUIRES: ava_core.my.models.LearningQueue',
        'name': 'standard_char',
        'parent': 'REQUIRES: ava_core.learn.models.Module',
        'path': 'default',
        'module_url': 'standard_char',
        'description': 'standard_text',
        'history_module': 'REQUIRES: ava_core.my.models.LearningHistory',
    }

    modified = {
        'parent_module': 'REQUIRES: ava_core.learn.models.Module',
        'queue_module': 'REQUIRES: ava_core.my.models.LearningQueue',
        'name': 'standard_char',
        'parent': 'REQUIRES: ava_core.learn.models.Module',
        'path': 'default',
        'module_url': 'standard_char',
        'description': 'standard_text',
        'history_module': 'REQUIRES: ava_core.my.models.LearningHistory',
    }

    missing_parent_module = {
        'queue_module': 'REQUIRES: ava_core.my.models.LearningQueue',
        'name': 'standard_char',
        'parent': 'REQUIRES: ava_core.learn.models.Module',
        'path': 'default',
        'module_url': 'standard_char',
        'description': 'standard_text',
        'history_module': 'REQUIRES: ava_core.my.models.LearningHistory',
    }

    modified_parent_module = {
        'parent_module': 'REQUIRES: ava_core.learn.models.Module',
        'queue_module': 'REQUIRES: ava_core.my.models.LearningQueue',
        'name': 'standard_char',
        'parent': 'REQUIRES: ava_core.learn.models.Module',
        'path': 'default',
        'module_url': 'standard_char',
        'description': 'standard_text',
        'history_module': 'REQUIRES: ava_core.my.models.LearningHistory',
    }

    missing_queue_module = {
        'parent_module': 'REQUIRES: ava_core.learn.models.Module',
        'name': 'standard_char',
        'parent': 'REQUIRES: ava_core.learn.models.Module',
        'path': 'default',
        'module_url': 'standard_char',
        'description': 'standard_text',
        'history_module': 'REQUIRES: ava_core.my.models.LearningHistory',
    }

    modified_queue_module = {
        'parent_module': 'REQUIRES: ava_core.learn.models.Module',
        'queue_module': 'REQUIRES: ava_core.my.models.LearningQueue',
        'name': 'standard_char',
        'parent': 'REQUIRES: ava_core.learn.models.Module',
        'path': 'default',
        'module_url': 'standard_char',
        'description': 'standard_text',
        'history_module': 'REQUIRES: ava_core.my.models.LearningHistory',
    }

    modified_name = {
        'parent_module': 'REQUIRES: ava_core.learn.models.Module',
        'queue_module': 'REQUIRES: ava_core.my.models.LearningQueue',
        'name': 'modified_char',
        'parent': 'REQUIRES: ava_core.learn.models.Module',
        'path': 'default',
        'module_url': 'standard_char',
        'description': 'standard_text',
        'history_module': 'REQUIRES: ava_core.my.models.LearningHistory',
    }

    missing_name = {
        'parent_module': 'REQUIRES: ava_core.learn.models.Module',
        'queue_module': 'REQUIRES: ava_core.my.models.LearningQueue',
        'parent': 'REQUIRES: ava_core.learn.models.Module',
        'path': 'default',
        'module_url': 'standard_char',
        'description': 'standard_text',
        'history_module': 'REQUIRES: ava_core.my.models.LearningHistory',
    }

    modified_parent = {
        'parent_module': 'REQUIRES: ava_core.learn.models.Module',
        'queue_module': 'REQUIRES: ava_core.my.models.LearningQueue',
        'name': 'standard_char',
        'parent': 'REQUIRES: ava_core.learn.models.Module',
        'path': 'default',
        'module_url': 'standard_char',
        'description': 'standard_text',
        'history_module': 'REQUIRES: ava_core.my.models.LearningHistory',
    }

    missing_parent = {
        'parent_module': 'REQUIRES: ava_core.learn.models.Module',
        'queue_module': 'REQUIRES: ava_core.my.models.LearningQueue',
        'name': 'standard_char',
        'path': 'default',
        'module_url': 'standard_char',
        'description': 'standard_text',
        'history_module': 'REQUIRES: ava_core.my.models.LearningHistory',
    }

    modified_path = {
        'parent_module': 'REQUIRES: ava_core.learn.models.Module',
        'queue_module': 'REQUIRES: ava_core.my.models.LearningQueue',
        'name': 'standard_char',
        'parent': 'REQUIRES: ava_core.learn.models.Module',
        'path': 'default',
        'module_url': 'standard_char',
        'description': 'standard_text',
        'history_module': 'REQUIRES: ava_core.my.models.LearningHistory',
    }

    missing_path = {
        'parent_module': 'REQUIRES: ava_core.learn.models.Module',
        'queue_module': 'REQUIRES: ava_core.my.models.LearningQueue',
        'name': 'standard_char',
        'parent': 'REQUIRES: ava_core.learn.models.Module',
        'module_url': 'standard_char',
        'description': 'standard_text',
        'history_module': 'REQUIRES: ava_core.my.models.LearningHistory',
    }

    missing_module_url = {
        'parent_module': 'REQUIRES: ava_core.learn.models.Module',
        'queue_module': 'REQUIRES: ava_core.my.models.LearningQueue',
        'name': 'standard_char',
        'parent': 'REQUIRES: ava_core.learn.models.Module',
        'path': 'default',
        'description': 'standard_text',
        'history_module': 'REQUIRES: ava_core.my.models.LearningHistory',
    }

    modified_module_url = {
        'parent_module': 'REQUIRES: ava_core.learn.models.Module',
        'queue_module': 'REQUIRES: ava_core.my.models.LearningQueue',
        'name': 'standard_char',
        'parent': 'REQUIRES: ava_core.learn.models.Module',
        'path': 'default',
        'module_url': 'modified_char',
        'description': 'standard_text',
        'history_module': 'REQUIRES: ava_core.my.models.LearningHistory',
    }

    modified_description = {
        'parent_module': 'REQUIRES: ava_core.learn.models.Module',
        'queue_module': 'REQUIRES: ava_core.my.models.LearningQueue',
        'name': 'standard_char',
        'parent': 'REQUIRES: ava_core.learn.models.Module',
        'path': 'default',
        'module_url': 'standard_char',
        'description': 'modified_text',
        'history_module': 'REQUIRES: ava_core.my.models.LearningHistory',
    }

    missing_description = {
        'parent_module': 'REQUIRES: ava_core.learn.models.Module',
        'queue_module': 'REQUIRES: ava_core.my.models.LearningQueue',
        'name': 'standard_char',
        'parent': 'REQUIRES: ava_core.learn.models.Module',
        'path': 'default',
        'module_url': 'standard_char',
        'history_module': 'REQUIRES: ava_core.my.models.LearningHistory',
    }

    modified_history_module = {
        'parent_module': 'REQUIRES: ava_core.learn.models.Module',
        'queue_module': 'REQUIRES: ava_core.my.models.LearningQueue',
        'name': 'standard_char',
        'parent': 'REQUIRES: ava_core.learn.models.Module',
        'path': 'default',
        'module_url': 'standard_char',
        'description': 'standard_text',
        'history_module': 'REQUIRES: ava_core.my.models.LearningHistory',
    }

    missing_history_module = {
        'parent_module': 'REQUIRES: ava_core.learn.models.Module',
        'queue_module': 'REQUIRES: ava_core.my.models.LearningQueue',
        'name': 'standard_char',
        'parent': 'REQUIRES: ava_core.learn.models.Module',
        'path': 'default',
        'module_url': 'standard_char',
        'description': 'standard_text',
    }



class PathTestData(AvaTestData):
    """
    Test data for Path
    """

    model = Path
    url = '/example'

    standard = {
        'name': 'standard_char',
        'path_roles': 'default',
        'path_modules': 'default',
        'description': 'standard_text',
    }

    modified = {
        'name': 'standard_char',
        'path_roles': 'default',
        'path_modules': 'default',
        'description': 'standard_text',
    }

    modified_name = {
        'name': 'modified_char',
        'path_roles': 'default',
        'path_modules': 'default',
        'description': 'standard_text',
    }

    missing_name = {
        'path_roles': 'default',
        'path_modules': 'default',
        'description': 'standard_text',
    }

    modified_path_roles = {
        'name': 'standard_char',
        'path_roles': 'default',
        'path_modules': 'default',
        'description': 'standard_text',
    }

    missing_path_roles = {
        'name': 'standard_char',
        'path_modules': 'default',
        'description': 'standard_text',
    }

    modified_path_modules = {
        'name': 'standard_char',
        'path_roles': 'default',
        'path_modules': 'default',
        'description': 'standard_text',
    }

    missing_path_modules = {
        'name': 'standard_char',
        'path_roles': 'default',
        'description': 'standard_text',
    }

    modified_description = {
        'name': 'standard_char',
        'path_roles': 'default',
        'path_modules': 'default',
        'description': 'modified_text',
    }

    missing_description = {
        'name': 'standard_char',
        'path_roles': 'default',
        'path_modules': 'default',
    }



class RoleTestData(AvaTestData):
    """
    Test data for Role
    """

    model = Role
    url = '/example'

    standard = {
        'profile_role': 'REQUIRES: ava_core.my.models.LearningProfile',
        'path': 'default',
        'name': 'standard_char',
        'description': 'standard_text',
    }

    modified = {
        'profile_role': 'REQUIRES: ava_core.my.models.LearningProfile',
        'path': 'default',
        'name': 'standard_char',
        'description': 'standard_text',
    }

    modified_profile_role = {
        'profile_role': 'REQUIRES: ava_core.my.models.LearningProfile',
        'path': 'default',
        'name': 'standard_char',
        'description': 'standard_text',
    }

    missing_profile_role = {
        'path': 'default',
        'name': 'standard_char',
        'description': 'standard_text',
    }

    modified_path = {
        'profile_role': 'REQUIRES: ava_core.my.models.LearningProfile',
        'path': 'default',
        'name': 'standard_char',
        'description': 'standard_text',
    }

    missing_path = {
        'profile_role': 'REQUIRES: ava_core.my.models.LearningProfile',
        'name': 'standard_char',
        'description': 'standard_text',
    }

    modified_name = {
        'profile_role': 'REQUIRES: ava_core.my.models.LearningProfile',
        'path': 'default',
        'name': 'modified_char',
        'description': 'standard_text',
    }

    missing_name = {
        'profile_role': 'REQUIRES: ava_core.my.models.LearningProfile',
        'path': 'default',
        'description': 'standard_text',
    }

    modified_description = {
        'profile_role': 'REQUIRES: ava_core.my.models.LearningProfile',
        'path': 'default',
        'name': 'standard_char',
        'description': 'modified_text',
    }

    missing_description = {
        'profile_role': 'REQUIRES: ava_core.my.models.LearningProfile',
        'path': 'default',
        'name': 'standard_char',
    }




