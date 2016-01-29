from django.conf import settings

TEST_BUILDER_INPUT_APP_PREFIX = 'ava_core'
TEST_BUILDER_OUTPUT_APP_PREFIX = 'ava_core'
TEST_BUILDER_DIRECTORY = '{}/test_builder/'.format(settings.MEDIA_ROOT)
TEST_BUILDER_ABSTRACT_DIRECTORY = '{}/abstract/'.format(TEST_BUILDER_OUTPUT_APP_PREFIX)
TEST_BUILDER_PROJECT_DATA_OUTPUT = 'output'
TEST_BUILDER_PROJECT_DATA_INPUT = 'output'
TEST_BUILDER_FORCE_NO_ARCHIVE = True  # TODO:	Comment this out when running local to a project
TEST_BUILDER_STORE_TEMP = False  # TODO:	Comment this out when running local to a project
TEST_BUILDER_IGNORED_APPS = [
    'ava_core.test_builder',
    'ava_core.integration.integration_abstract',
    'ava_core.abstract'
]
TEST_BUILDER_IGNORED_MODELS = [

]
TEST_BUILDER_IGNORED_FIELDS = [
    'id',
    'created',
    'modified'
]
