from django.conf import settings

TEST_BUILDER_DIRECTORY = settings.MEDIA_ROOT + '/test_builder/'
TEST_BUILDER_IGNORED_APPS = ['ava_core.test_builder', 'ava_core.integration.integration_abstract', 'ava_core.abstract']
TEST_BUILDER_PREFIX = 'ava'