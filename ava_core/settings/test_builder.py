from django.conf import settings

TEST_BUILDER_PREFIX = 'ava'
TEST_BUILDER_DIRECTORY = '{}/test_builder/'.format(settings.MEDIA_ROOT)
TEST_BUILDER_ABSTRACT_DIRECTORY = '{}/{}/abstract/'.format(settings.BASE_DIR, TEST_BUILDER_PREFIX)
TEST_BUILDER_PROJECT_DATA_OUTPUT = 'output'
TEST_BUILDER_PROJECT_DATA_INPUT = 'output'
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
