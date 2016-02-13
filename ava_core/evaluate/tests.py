# Rest Imports
from rest_framework import status
from rest_framework.reverse import reverse
# Local Imports
from ava_core.abstract.test import AvaCoreTest
from ava_core.evaluate.test_data import EvaluateSenderTestData, EvaluateResultTestData, EvaluateTemplateTestData, \
    EvaluateControllerTestData, EvaluateTestTestData


class EvaluateSenderTest(AvaCoreTest):
    # step 2: replace evaluate and EvaluateSender
    model_name = 'evaluate.EvaluateSender'

    has_owner = False

    # step 3: populate this section to define what you expect the API permissions will be
    api_permissions = {
        'create': {'unauthenticated': False, 'standard': False, 'admin': True, 'owner': False},
        'retrieve': {'unauthenticated': False, 'standard': False, 'admin': True, 'owner': False},
        'update': {'unauthenticated': False, 'standard': False, 'admin': True, 'owner': False},
        'delete': {'unauthenticated': False, 'standard': False, 'admin': False, 'owner': False},
    }

    # step 4: update with the model name for apiviewset urls (for apiviews and custom api's this won't work
    api_urls = {
        'create': 'evaluatesender-list',
        'retrieve': 'evaluatesender-detail',
        'retrieve_all': 'evaluatesender-list',
        'update': 'evaluatesender-detail',
        'delete': 'evaluatesender-detail',
    }

    def setUp(self):
        # step 5: Update with Model Names
        super(EvaluateSenderTest, self).setUp()
        self.data = EvaluateSenderTestData()

    # step 7: replace evaluatesender globally with your model name in lowercase
    def test_evaluatesender_create_as_user(self):
        url = reverse(self.api_urls['create'])
        data = self.data.standard

        self.login_user(user='standard')

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['standard'])

    def test_evaluatesender_create_as_admin(self):
        url = reverse(self.api_urls['create'])
        data = self.data.standard

        self.login_user(user='admin')

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['admin'])

    def test_evaluatesender_create_as_unauthenticated(self):
        url = reverse(self.api_urls['create'])
        data = self.data.standard

        self.logout_user()

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['unauthenticated'])

    def test_evaluatesender_retrieve_single_as_user(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user='standard')

        url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['standard'])

    def test_evaluatesender_retrieve_all_as_user(self):
        self.create_object_via_api(data=self.data.standard)

        self.login_user(user='standard')

        url = reverse(self.api_urls['retrieve_all'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['standard'])

    def test_evaluatesender_retrieve_single_as_admin(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user='admin')

        url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['admin'])

    def test_evaluatesender_retrieve_all_as_admin(self):
        self.create_object_via_api(data=self.data.standard)

        self.login_user(user='admin')

        url = reverse(self.api_urls['retrieve_all'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['admin'])

    def test_evaluatesender_retrieve_single_as_unauthenticated(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['unauthenticated'])

    def test_evaluatesender_retrieve_all_as_unauthenticated(self):
        self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['retrieve_all'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['unauthenticated'])

    def test_evaluatesender_update_exists_as_user(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="standard")

        url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
        response = self.client.put(url, self.data.unique, format='json')
        # print("RES:: " +str(response.data))
        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_evaluatesender_update_does_not_exist_as_user(self):
        self.login_user(user="standard")

        url = reverse(self.api_urls['update'], kwargs={'pk': 1})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_evaluatesender_update_exists_as_admin(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="admin")

        url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['admin'])

    def test_evaluatesender_update_does_not_exist_as_admin(self):
        self.login_user(user="admin")

        url = reverse(self.api_urls['update'], kwargs={'pk': 1})
        response = self.client.put(url, self.data.unique, format='json')

        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_evaluatesender_update_exists_as_unauthenticated(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_evaluatesender_update_does_not_exist_as_unauthenticated(self):
        self.logout_user()

        url = reverse(self.api_urls['update'], kwargs={'pk': 1})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_evaluatesender_delete_does_not_exist_as_user(self):
        self.login_user(user="standard")

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['standard'])

    def test_evaluatesender_delete_exists_as_user(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="standard")

        url = reverse(self.api_urls['delete'], kwargs={'pk': object_id})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['standard'])

    def test_evaluatesender_delete_exists_as_admin(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="admin")

        url = reverse(self.api_urls['delete'], kwargs={'pk': object_id})
        response = self.client.delete(url)
        # print("RES:: " +str(response.data))
        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['admin'])

    def test_evaluatesender_delete_does_not_exist_as_admin(self):
        self.login_user(user="admin")

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['admin'])

    def test_evaluatesender_delete_exists_as_unauthenticated(self):
        self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['unauthenticated'])

    def test_evaluatesender_delete_does_not_exist_as_unauthenticated(self):
        self.logout_user()

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['unauthenticated'])


# class EvaluateResultTest(AvaCoreTest):
#     # step 2: replace evaluate and EvaluateResult
#     model_name = 'evaluate.EvaluateResult'
#
#     has_owner = False
#
#     # step 3: populate this section to define what you expect the API permissions will be
#     api_permissions = {
#         'create': {'unauthenticated': False, 'standard': False, 'admin': True, 'owner': False},
#         'retrieve': {'unauthenticated': False, 'standard': True, 'admin': True, 'owner': False},
#         'update': {'unauthenticated': False, 'standard': False, 'admin': True, 'owner': False},
#         'delete': {'unauthenticated': False, 'standard': False, 'admin': True, 'owner': False},
#     }
#
#     # step 4: update with the model name for apiviewset urls (for apiviews and custom api's this won't work
#     api_urls = {
#         'create': 'evaluateresult-list',
#         'retrieve': 'evaluateresult-detail',
#         'retrieve_all': 'evaluateresult-list',
#         'update': 'evaluateresult-detail',
#         'delete': 'evaluateresult-detail',
#     }
#
#     def setUp(self):
#         # step 5: Update with Model Names
#         super(EvaluateResultTest, self).setUp()
#         self.data = EvaluateResultTestData()
#
#      def create_object_via_api(self, data, user='admin'):
        # step 6: you will need to write this method.... this template only works with single models
        # with no relationships
        # url = reverse(self.api_urls['create'])
        #
        # if user:
        #     # must be admin to create
        #     self.login_user(user=user)
        # else:
        #     self.logout_user()
        #
        # # must be admin to create
        # self.login_user(user='admin')
        #
        # response = self.client.post(url, data, format='json')
        #
        # self.check_api_results(response=response, request_type='create', model_name=self.model_name,
        #                        permitted=self.api_permissions['create']['admin'])
        #
        # self.logout_user()
        #
        # # return the id of the model you are testing
        # if 'id' in response.data:
        #     return response.data['id']
#
#     # step 7: replace evaluateresult globally with your model name in lowercase
#     def test_evaluateresult_create_as_user(self):
#         url = reverse(self.api_urls['create'])
#         data = self.data.standard
#
#         self.login_user(user='standard')
#
#         response = self.client.post(url, data, format='json')
#
#         self.check_api_results(response=response, request_type='create', model_name=self.model_name,
#                                permitted=self.api_permissions['create']['standard'])
#
#     def test_evaluateresult_create_as_admin(self):
#         url = reverse(self.api_urls['create'])
#         data = self.data.standard
#
#         self.login_user(user='admin')
#
#         response = self.client.post(url, data, format='json')
#
#         self.check_api_results(response=response, request_type='create', model_name=self.model_name,
#                                permitted=self.api_permissions['create']['admin'])
#
#     def test_evaluateresult_create_as_unauthenticated(self):
#         url = reverse(self.api_urls['create'])
#         data = self.data.standard
#
#         self.logout_user()
#
#         response = self.client.post(url, data, format='json')
#
#         self.check_api_results(response=response, request_type='create', model_name=self.model_name,
#                                permitted=self.api_permissions['create']['unauthenticated'])
#
#     def test_evaluateresult_retrieve_single_as_user(self):
#         object_id = self.create_object_via_api(data=self.data.standard)
#
#         self.login_user(user='standard')
#
#         url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
#         response = self.client.get(url)
#
#         self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
#                                permitted=self.api_permissions['retrieve']['standard'])
#
#     def test_evaluateresult_retrieve_all_as_user(self):
#         self.create_object_via_api(data=self.data.standard)
#
#         self.login_user(user='standard')
#
#         url = reverse(self.api_urls['retrieve_all'])
#         response = self.client.get(url)
#
#         self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
#                                permitted=self.api_permissions['retrieve']['standard'])
#
#     def test_evaluateresult_retrieve_single_as_admin(self):
#         object_id = self.create_object_via_api(data=self.data.standard)
#
#         self.login_user(user='admin')
#
#         url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
#         response = self.client.get(url)
#
#         self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
#                                permitted=self.api_permissions['retrieve']['admin'])
#
#     def test_evaluateresult_retrieve_all_as_admin(self):
#         self.create_object_via_api(data=self.data.standard)
#
#         self.login_user(user='admin')
#
#         url = reverse(self.api_urls['retrieve_all'])
#         response = self.client.get(url)
#
#         self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
#                                permitted=self.api_permissions['retrieve']['admin'])
#
#     def test_evaluateresult_retrieve_single_as_unauthenticated(self):
#         object_id = self.create_object_via_api(data=self.data.standard)
#
#         self.logout_user()
#
#         url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
#         response = self.client.get(url)
#
#         self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
#                                permitted=self.api_permissions['retrieve']['unauthenticated'])
#
#     def test_evaluateresult_retrieve_all_as_unauthenticated(self):
#         self.create_object_via_api(data=self.data.standard)
#
#         self.logout_user()
#
#         url = reverse(self.api_urls['retrieve_all'])
#         response = self.client.get(url)
#
#         self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
#                                permitted=self.api_permissions['retrieve']['unauthenticated'])
#
#     def test_evaluateresult_update_exists_as_user(self):
#         object_id = self.create_object_via_api(data=self.data.standard)
#
#         self.login_user(user="standard")
#
#         url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
#         response = self.client.put(url, self.data.unique, format='json')
#
#         self.check_api_results(response=response, request_type='update', model_name=self.model_name,
#                                permitted=self.api_permissions['update']['standard'])
#
#     def test_evaluateresult_update_does_not_exist_as_user(self):
#         self.login_user(user="standard")
#
#         url = reverse(self.api_urls['update'], kwargs={'pk': 1})
#         response = self.client.put(url, self.data.unique, format='json')
#
#         self.check_api_results(response=response, request_type='update', model_name=self.model_name,
#                                permitted=self.api_permissions['update']['standard'])
#
#     def test_evaluateresult_update_exists_as_admin(self):
#         object_id = self.create_object_via_api(data=self.data.standard)
#
#         self.login_user(user="admin")
#
#         url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
#         response = self.client.put(url, self.data.unique, format='json')
#
#         self.check_api_results(response=response, request_type='update', model_name=self.model_name,
#                                permitted=self.api_permissions['update']['admin'])
#
#     def test_evaluateresult_update_does_not_exist_as_admin(self):
#         self.login_user(user="admin")
#
#         url = reverse(self.api_urls['update'], kwargs={'pk': 1})
#         response = self.client.put(url, self.data.unique, format='json')
#
#         self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)
#
#     def test_evaluateresult_update_exists_as_unauthenticated(self):
#         object_id = self.create_object_via_api(data=self.data.standard)
#
#         self.logout_user()
#
#         url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
#         response = self.client.put(url, self.data.unique, format='json')
#
#         self.check_api_results(response=response, request_type='update', model_name=self.model_name,
#                                permitted=self.api_permissions['update']['standard'])
#
#     def test_evaluateresult_update_does_not_exist_as_unauthenticated(self):
#         self.logout_user()
#
#         url = reverse(self.api_urls['update'], kwargs={'pk': 1})
#         response = self.client.put(url, self.data.unique, format='json')
#
#         self.check_api_results(response=response, request_type='update', model_name=self.model_name,
#                                permitted=self.api_permissions['update']['standard'])
#
#     def test_evaluateresult_delete_does_not_exist_as_user(self):
#         self.login_user(user="standard")
#
#         url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
#         response = self.client.delete(url)
#
#         self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
#                                permitted=self.api_permissions['delete']['standard'])
#
#     def test_evaluateresult_delete_exists_as_user(self):
#         object_id = self.create_object_via_api(data=self.data.standard)
#
#         self.login_user(user="standard")
#
#         url = reverse(self.api_urls['delete'], kwargs={'pk': object_id})
#         response = self.client.delete(url)
#
#         self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
#                                permitted=self.api_permissions['delete']['standard'])
#
#     def test_evaluateresult_delete_exists_as_admin(self):
#         object_id = self.create_object_via_api(data=self.data.standard)
#
#         self.login_user(user="admin")
#
#         url = reverse(self.api_urls['delete'], kwargs={'pk': object_id})
#         response = self.client.delete(url)
#
#         self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
#                                permitted=self.api_permissions['delete']['admin'])
#
#     def test_evaluateresult_delete_does_not_exist_as_admin(self):
#         self.login_user(user="admin")
#
#         url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
#         response = self.client.delete(url)
#
#         self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)
#
#     def test_evaluateresult_delete_exists_as_unauthenticated(self):
#         self.create_object_via_api(data=self.data.standard)
#
#         self.logout_user()
#
#         url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
#         response = self.client.delete(url)
#
#         self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
#                                permitted=self.api_permissions['delete']['unauthenticated'])
#
#     def test_evaluateresult_delete_does_not_exist_as_unauthenticated(self):
#         self.logout_user()
#
#         url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
#         response = self.client.delete(url)
#
#         self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
#                                permitted=self.api_permissions['delete']['unauthenticated'])
#
#
class EvaluateTemplateTest(AvaCoreTest):
    # step 2: replace evaluate and EvaluateTemplate
    model_name = 'evaluate.EvaluateTemplate'

    has_owner = False

    # step 3: populate this section to define what you expect the API permissions will be
    api_permissions = {
        'create': {'unauthenticated': False, 'standard': False, 'admin': True, 'owner': False},
        'retrieve': {'unauthenticated': False, 'standard': False, 'admin': True, 'owner': False},
        'update': {'unauthenticated': False, 'standard': False, 'admin': True, 'owner': False},
        'delete': {'unauthenticated': False, 'standard': False, 'admin': False, 'owner': False},
    }

    # step 4: update with the model name for apiviewset urls (for apiviews and custom api's this won't work
    api_urls = {
        'create': 'evaluatetemplate-list',
        'retrieve': 'evaluatetemplate-detail',
        'retrieve_all': 'evaluatetemplate-list',
        'update': 'evaluatetemplate-detail',
        'delete': 'evaluatetemplate-detail',
    }

    def setUp(self):
        # step 5: Update with Model Names
        super(EvaluateTemplateTest, self).setUp()
        self.data = EvaluateTemplateTestData()

    # step 7: replace evaluatetemplate globally with your model name in lowercase
    def test_evaluatetemplate_create_as_user(self):
        url = reverse(self.api_urls['create'])
        data = self.data.standard

        self.login_user(user='standard')

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['standard'])

    def test_evaluatetemplate_create_as_admin(self):
        url = reverse(self.api_urls['create'])
        data = self.data.standard

        self.login_user(user='admin')

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['admin'])

    def test_evaluatetemplate_create_as_unauthenticated(self):
        url = reverse(self.api_urls['create'])
        data = self.data.standard

        self.logout_user()

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['unauthenticated'])

    def test_evaluatetemplate_retrieve_single_as_user(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user='standard')

        url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['standard'])

    def test_evaluatetemplate_retrieve_all_as_user(self):
        self.create_object_via_api(data=self.data.standard)

        self.login_user(user='standard')

        url = reverse(self.api_urls['retrieve_all'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['standard'])

    def test_evaluatetemplate_retrieve_single_as_admin(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user='admin')

        url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['admin'])

    def test_evaluatetemplate_retrieve_all_as_admin(self):
        self.create_object_via_api(data=self.data.standard)

        self.login_user(user='admin')

        url = reverse(self.api_urls['retrieve_all'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['admin'])

    def test_evaluatetemplate_retrieve_single_as_unauthenticated(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['unauthenticated'])

    def test_evaluatetemplate_retrieve_all_as_unauthenticated(self):
        self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['retrieve_all'])
        response = self.client.get(url)

        self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
                               permitted=self.api_permissions['retrieve']['unauthenticated'])

    def test_evaluatetemplate_update_exists_as_user(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="standard")

        url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_evaluatetemplate_update_does_not_exist_as_user(self):
        self.login_user(user="standard")

        url = reverse(self.api_urls['update'], kwargs={'pk': 1})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_evaluatetemplate_update_exists_as_admin(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="admin")

        url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['admin'])

    def test_evaluatetemplate_update_does_not_exist_as_admin(self):
        self.login_user(user="admin")

        url = reverse(self.api_urls['update'], kwargs={'pk': 1})
        response = self.client.put(url, self.data.unique, format='json')

        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_evaluatetemplate_update_exists_as_unauthenticated(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_evaluatetemplate_update_does_not_exist_as_unauthenticated(self):
        self.logout_user()

        url = reverse(self.api_urls['update'], kwargs={'pk': 1})
        response = self.client.put(url, self.data.unique, format='json')

        self.check_api_results(response=response, request_type='update', model_name=self.model_name,
                               permitted=self.api_permissions['update']['standard'])

    def test_evaluatetemplate_delete_does_not_exist_as_user(self):
        self.login_user(user="standard")

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['standard'])

    def test_evaluatetemplate_delete_exists_as_user(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="standard")

        url = reverse(self.api_urls['delete'], kwargs={'pk': object_id})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['standard'])

    def test_evaluatetemplate_delete_exists_as_admin(self):
        object_id = self.create_object_via_api(data=self.data.standard)

        self.login_user(user="admin")

        url = reverse(self.api_urls['delete'], kwargs={'pk': object_id})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['admin'])

    def test_evaluatetemplate_delete_does_not_exist_as_admin(self):
        self.login_user(user="admin")

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['admin'])

    def test_evaluatetemplate_delete_exists_as_unauthenticated(self):
        self.create_object_via_api(data=self.data.standard)

        self.logout_user()

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['unauthenticated'])

    def test_evaluatetemplate_delete_does_not_exist_as_unauthenticated(self):
        self.logout_user()

        url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
        response = self.client.delete(url)

        self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
                               permitted=self.api_permissions['delete']['unauthenticated'])
#
#
# class EvaluateControllerTest(AvaCoreTest):
#     # step 2: replace evaluate and EvaluateController
#     model_name = 'evaluate.EvaluateController'
#
#     has_owner = False
#
#     # step 3: populate this section to define what you expect the API permissions will be
#     api_permissions = {
#         'create': {'unauthenticated': False, 'standard': False, 'admin': True, 'owner': False},
#         'retrieve': {'unauthenticated': False, 'standard': True, 'admin': True, 'owner': False},
#         'update': {'unauthenticated': False, 'standard': False, 'admin': True, 'owner': False},
#         'delete': {'unauthenticated': False, 'standard': False, 'admin': True, 'owner': False},
#     }
#
#     # step 4: update with the model name for apiviewset urls (for apiviews and custom api's this won't work
#     api_urls = {
#         'create': 'evaluatecontroller-list',
#         'retrieve': 'evaluatecontroller-detail',
#         'retrieve_all': 'evaluatecontroller-list',
#         'update': 'evaluatecontroller-detail',
#         'delete': 'evaluatecontroller-detail',
#     }
#
#     def setUp(self):
#         # step 5: Update with Model Names
#         super(EvaluateControllerTest, self).setUp()
#         self.data = EvaluateControllerTestData()
#
#      def create_object_via_api(self, data, user='admin'):
        # step 6: you will need to write this method.... this template only works with single models
        # with no relationships
        # url = reverse(self.api_urls['create'])
        #
        # if user:
        #     # must be admin to create
        #     self.login_user(user=user)
        # else:
        #     self.logout_user()
        #
        # # must be admin to create
        # self.login_user(user='admin')
        #
        # response = self.client.post(url, data, format='json')
        #
        # self.check_api_results(response=response, request_type='create', model_name=self.model_name,
        #                        permitted=self.api_permissions['create']['admin'])
        #
        # self.logout_user()
        #
        # # return the id of the model you are testing
        # if 'id' in response.data:
        #     return response.data['id']
#
#     # step 7: replace evaluatecontroller globally with your model name in lowercase
#     def test_evaluatecontroller_create_as_user(self):
#         url = reverse(self.api_urls['create'])
#         data = self.data.standard
#
#         self.login_user(user='standard')
#
#         response = self.client.post(url, data, format='json')
#
#         self.check_api_results(response=response, request_type='create', model_name=self.model_name,
#                                permitted=self.api_permissions['create']['standard'])
#
#     def test_evaluatecontroller_create_as_admin(self):
#         url = reverse(self.api_urls['create'])
#         data = self.data.standard
#
#         self.login_user(user='admin')
#
#         response = self.client.post(url, data, format='json')
#
#         self.check_api_results(response=response, request_type='create', model_name=self.model_name,
#                                permitted=self.api_permissions['create']['admin'])
#
#     def test_evaluatecontroller_create_as_unauthenticated(self):
#         url = reverse(self.api_urls['create'])
#         data = self.data.standard
#
#         self.logout_user()
#
#         response = self.client.post(url, data, format='json')
#
#         self.check_api_results(response=response, request_type='create', model_name=self.model_name,
#                                permitted=self.api_permissions['create']['unauthenticated'])
#
#     def test_evaluatecontroller_retrieve_single_as_user(self):
#         object_id = self.create_object_via_api(data=self.data.standard)
#
#         self.login_user(user='standard')
#
#         url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
#         response = self.client.get(url)
#
#         self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
#                                permitted=self.api_permissions['retrieve']['standard'])
#
#     def test_evaluatecontroller_retrieve_all_as_user(self):
#         self.create_object_via_api(data=self.data.standard)
#
#         self.login_user(user='standard')
#
#         url = reverse(self.api_urls['retrieve_all'])
#         response = self.client.get(url)
#
#         self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
#                                permitted=self.api_permissions['retrieve']['standard'])
#
#     def test_evaluatecontroller_retrieve_single_as_admin(self):
#         object_id = self.create_object_via_api(data=self.data.standard)
#
#         self.login_user(user='admin')
#
#         url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
#         response = self.client.get(url)
#
#         self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
#                                permitted=self.api_permissions['retrieve']['admin'])
#
#     def test_evaluatecontroller_retrieve_all_as_admin(self):
#         self.create_object_via_api(data=self.data.standard)
#
#         self.login_user(user='admin')
#
#         url = reverse(self.api_urls['retrieve_all'])
#         response = self.client.get(url)
#
#         self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
#                                permitted=self.api_permissions['retrieve']['admin'])
#
#     def test_evaluatecontroller_retrieve_single_as_unauthenticated(self):
#         object_id = self.create_object_via_api(data=self.data.standard)
#
#         self.logout_user()
#
#         url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
#         response = self.client.get(url)
#
#         self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
#                                permitted=self.api_permissions['retrieve']['unauthenticated'])
#
#     def test_evaluatecontroller_retrieve_all_as_unauthenticated(self):
#         self.create_object_via_api(data=self.data.standard)
#
#         self.logout_user()
#
#         url = reverse(self.api_urls['retrieve_all'])
#         response = self.client.get(url)
#
#         self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
#                                permitted=self.api_permissions['retrieve']['unauthenticated'])
#
#     def test_evaluatecontroller_update_exists_as_user(self):
#         object_id = self.create_object_via_api(data=self.data.standard)
#
#         self.login_user(user="standard")
#
#         url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
#         response = self.client.put(url, self.data.unique, format='json')
#
#         self.check_api_results(response=response, request_type='update', model_name=self.model_name,
#                                permitted=self.api_permissions['update']['standard'])
#
#     def test_evaluatecontroller_update_does_not_exist_as_user(self):
#         self.login_user(user="standard")
#
#         url = reverse(self.api_urls['update'], kwargs={'pk': 1})
#         response = self.client.put(url, self.data.unique, format='json')
#
#         self.check_api_results(response=response, request_type='update', model_name=self.model_name,
#                                permitted=self.api_permissions['update']['standard'])
#
#     def test_evaluatecontroller_update_exists_as_admin(self):
#         object_id = self.create_object_via_api(data=self.data.standard)
#
#         self.login_user(user="admin")
#
#         url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
#         response = self.client.put(url, self.data.unique, format='json')
#
#         self.check_api_results(response=response, request_type='update', model_name=self.model_name,
#                                permitted=self.api_permissions['update']['admin'])
#
#     def test_evaluatecontroller_update_does_not_exist_as_admin(self):
#         self.login_user(user="admin")
#
#         url = reverse(self.api_urls['update'], kwargs={'pk': 1})
#         response = self.client.put(url, self.data.unique, format='json')
#
#         self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)
#
#     def test_evaluatecontroller_update_exists_as_unauthenticated(self):
#         object_id = self.create_object_via_api(data=self.data.standard)
#
#         self.logout_user()
#
#         url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
#         response = self.client.put(url, self.data.unique, format='json')
#
#         self.check_api_results(response=response, request_type='update', model_name=self.model_name,
#                                permitted=self.api_permissions['update']['standard'])
#
#     def test_evaluatecontroller_update_does_not_exist_as_unauthenticated(self):
#         self.logout_user()
#
#         url = reverse(self.api_urls['update'], kwargs={'pk': 1})
#         response = self.client.put(url, self.data.unique, format='json')
#
#         self.check_api_results(response=response, request_type='update', model_name=self.model_name,
#                                permitted=self.api_permissions['update']['standard'])
#
#     def test_evaluatecontroller_delete_does_not_exist_as_user(self):
#         self.login_user(user="standard")
#
#         url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
#         response = self.client.delete(url)
#
#         self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
#                                permitted=self.api_permissions['delete']['standard'])
#
#     def test_evaluatecontroller_delete_exists_as_user(self):
#         object_id = self.create_object_via_api(data=self.data.standard)
#
#         self.login_user(user="standard")
#
#         url = reverse(self.api_urls['delete'], kwargs={'pk': object_id})
#         response = self.client.delete(url)
#
#         self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
#                                permitted=self.api_permissions['delete']['standard'])
#
#     def test_evaluatecontroller_delete_exists_as_admin(self):
#         object_id = self.create_object_via_api(data=self.data.standard)
#
#         self.login_user(user="admin")
#
#         url = reverse(self.api_urls['delete'], kwargs={'pk': object_id})
#         response = self.client.delete(url)
#
#         self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
#                                permitted=self.api_permissions['delete']['admin'])
#
#     def test_evaluatecontroller_delete_does_not_exist_as_admin(self):
#         self.login_user(user="admin")
#
#         url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
#         response = self.client.delete(url)
#
#         self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)
#
#     def test_evaluatecontroller_delete_exists_as_unauthenticated(self):
#         self.create_object_via_api(data=self.data.standard)
#
#         self.logout_user()
#
#         url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
#         response = self.client.delete(url)
#
#         self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
#                                permitted=self.api_permissions['delete']['unauthenticated'])
#
#     def test_evaluatecontroller_delete_does_not_exist_as_unauthenticated(self):
#         self.logout_user()
#
#         url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
#         response = self.client.delete(url)
#
#         self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
#                                permitted=self.api_permissions['delete']['unauthenticated'])
#
#
# class EvaluateTestTest(AvaCoreTest):
#     # step 2: replace evaluate and EvaluateTest
#     model_name = 'evaluate.EvaluateTest'
#
#     has_owner = False
#
#     # step 3: populate this section to define what you expect the API permissions will be
#     api_permissions = {
#         'create': {'unauthenticated': False, 'standard': False, 'admin': True, 'owner': False},
#         'retrieve': {'unauthenticated': False, 'standard': True, 'admin': True, 'owner': False},
#         'update': {'unauthenticated': False, 'standard': False, 'admin': True, 'owner': False},
#         'delete': {'unauthenticated': False, 'standard': False, 'admin': True, 'owner': False},
#     }
#
#     # step 4: update with the model name for apiviewset urls (for apiviews and custom api's this won't work
#     api_urls = {
#         'create': 'evaluatetest-list',
#         'retrieve': 'evaluatetest-detail',
#         'retrieve_all': 'evaluatetest-list',
#         'update': 'evaluatetest-detail',
#         'delete': 'evaluatetest-detail',
#     }
#
#     def setUp(self):
#         # step 5: Update with Model Names
#         super(EvaluateTestTest, self).setUp()
#         self.data = EvaluateTestTestData()
#
#      def create_object_via_api(self, data, user='admin'):
        # step 6: you will need to write this method.... this template only works with single models
        # with no relationships
        # url = reverse(self.api_urls['create'])
        #
        # if user:
        #     # must be admin to create
        #     self.login_user(user=user)
        # else:
        #     self.logout_user()
        #
        # # must be admin to create
        # self.login_user(user='admin')
        #
        # response = self.client.post(url, data, format='json')
        #
        # self.check_api_results(response=response, request_type='create', model_name=self.model_name,
        #                        permitted=self.api_permissions['create']['admin'])
        #
        # self.logout_user()
        #
        # # return the id of the model you are testing
        # if 'id' in response.data:
        #     return response.data['id']
#
#     # step 7: replace evaluatetest globally with your model name in lowercase
#     def test_evaluatetest_create_as_user(self):
#         url = reverse(self.api_urls['create'])
#         data = self.data.standard
#
#         self.login_user(user='standard')
#
#         response = self.client.post(url, data, format='json')
#
#         self.check_api_results(response=response, request_type='create', model_name=self.model_name,
#                                permitted=self.api_permissions['create']['standard'])
#
#     def test_evaluatetest_create_as_admin(self):
#         url = reverse(self.api_urls['create'])
#         data = self.data.standard
#
#         self.login_user(user='admin')
#
#         response = self.client.post(url, data, format='json')
#
#         self.check_api_results(response=response, request_type='create', model_name=self.model_name,
#                                permitted=self.api_permissions['create']['admin'])
#
#     def test_evaluatetest_create_as_unauthenticated(self):
#         url = reverse(self.api_urls['create'])
#         data = self.data.standard
#
#         self.logout_user()
#
#         response = self.client.post(url, data, format='json')
#
#         self.check_api_results(response=response, request_type='create', model_name=self.model_name,
#                                permitted=self.api_permissions['create']['unauthenticated'])
#
#     def test_evaluatetest_retrieve_single_as_user(self):
#         object_id = self.create_object_via_api(data=self.data.standard)
#
#         self.login_user(user='standard')
#
#         url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
#         response = self.client.get(url)
#
#         self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
#                                permitted=self.api_permissions['retrieve']['standard'])
#
#     def test_evaluatetest_retrieve_all_as_user(self):
#         self.create_object_via_api(data=self.data.standard)
#
#         self.login_user(user='standard')
#
#         url = reverse(self.api_urls['retrieve_all'])
#         response = self.client.get(url)
#
#         self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
#                                permitted=self.api_permissions['retrieve']['standard'])
#
#     def test_evaluatetest_retrieve_single_as_admin(self):
#         object_id = self.create_object_via_api(data=self.data.standard)
#
#         self.login_user(user='admin')
#
#         url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
#         response = self.client.get(url)
#
#         self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
#                                permitted=self.api_permissions['retrieve']['admin'])
#
#     def test_evaluatetest_retrieve_all_as_admin(self):
#         self.create_object_via_api(data=self.data.standard)
#
#         self.login_user(user='admin')
#
#         url = reverse(self.api_urls['retrieve_all'])
#         response = self.client.get(url)
#
#         self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
#                                permitted=self.api_permissions['retrieve']['admin'])
#
#     def test_evaluatetest_retrieve_single_as_unauthenticated(self):
#         object_id = self.create_object_via_api(data=self.data.standard)
#
#         self.logout_user()
#
#         url = reverse(self.api_urls['retrieve'], kwargs={'pk': object_id})
#         response = self.client.get(url)
#
#         self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
#                                permitted=self.api_permissions['retrieve']['unauthenticated'])
#
#     def test_evaluatetest_retrieve_all_as_unauthenticated(self):
#         self.create_object_via_api(data=self.data.standard)
#
#         self.logout_user()
#
#         url = reverse(self.api_urls['retrieve_all'])
#         response = self.client.get(url)
#
#         self.check_api_results(response=response, request_type='retrieve', model_name=self.model_name,
#                                permitted=self.api_permissions['retrieve']['unauthenticated'])
#
#     def test_evaluatetest_update_exists_as_user(self):
#         object_id = self.create_object_via_api(data=self.data.standard)
#
#         self.login_user(user="standard")
#
#         url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
#         response = self.client.put(url, self.data.unique, format='json')
#
#         self.check_api_results(response=response, request_type='update', model_name=self.model_name,
#                                permitted=self.api_permissions['update']['standard'])
#
#     def test_evaluatetest_update_does_not_exist_as_user(self):
#         self.login_user(user="standard")
#
#         url = reverse(self.api_urls['update'], kwargs={'pk': 1})
#         response = self.client.put(url, self.data.unique, format='json')
#
#         self.check_api_results(response=response, request_type='update', model_name=self.model_name,
#                                permitted=self.api_permissions['update']['standard'])
#
#     def test_evaluatetest_update_exists_as_admin(self):
#         object_id = self.create_object_via_api(data=self.data.standard)
#
#         self.login_user(user="admin")
#
#         url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
#         response = self.client.put(url, self.data.unique, format='json')
#
#         self.check_api_results(response=response, request_type='update', model_name=self.model_name,
#                                permitted=self.api_permissions['update']['admin'])
#
#     def test_evaluatetest_update_does_not_exist_as_admin(self):
#         self.login_user(user="admin")
#
#         url = reverse(self.api_urls['update'], kwargs={'pk': 1})
#         response = self.client.put(url, self.data.unique, format='json')
#
#         self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)
#
#     def test_evaluatetest_update_exists_as_unauthenticated(self):
#         object_id = self.create_object_via_api(data=self.data.standard)
#
#         self.logout_user()
#
#         url = reverse(self.api_urls['update'], kwargs={'pk': object_id})
#         response = self.client.put(url, self.data.unique, format='json')
#
#         self.check_api_results(response=response, request_type='update', model_name=self.model_name,
#                                permitted=self.api_permissions['update']['standard'])
#
#     def test_evaluatetest_update_does_not_exist_as_unauthenticated(self):
#         self.logout_user()
#
#         url = reverse(self.api_urls['update'], kwargs={'pk': 1})
#         response = self.client.put(url, self.data.unique, format='json')
#
#         self.check_api_results(response=response, request_type='update', model_name=self.model_name,
#                                permitted=self.api_permissions['update']['standard'])
#
#     def test_evaluatetest_delete_does_not_exist_as_user(self):
#         self.login_user(user="standard")
#
#         url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
#         response = self.client.delete(url)
#
#         self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
#                                permitted=self.api_permissions['delete']['standard'])
#
#     def test_evaluatetest_delete_exists_as_user(self):
#         object_id = self.create_object_via_api(data=self.data.standard)
#
#         self.login_user(user="standard")
#
#         url = reverse(self.api_urls['delete'], kwargs={'pk': object_id})
#         response = self.client.delete(url)
#
#         self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
#                                permitted=self.api_permissions['delete']['standard'])
#
#     def test_evaluatetest_delete_exists_as_admin(self):
#         object_id = self.create_object_via_api(data=self.data.standard)
#
#         self.login_user(user="admin")
#
#         url = reverse(self.api_urls['delete'], kwargs={'pk': object_id})
#         response = self.client.delete(url)
#
#         self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
#                                permitted=self.api_permissions['delete']['admin'])
#
#     def test_evaluatetest_delete_does_not_exist_as_admin(self):
#         self.login_user(user="admin")
#
#         url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
#         response = self.client.delete(url)
#
#         self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)
#
#     def test_evaluatetest_delete_exists_as_unauthenticated(self):
#         self.create_object_via_api(data=self.data.standard)
#
#         self.logout_user()
#
#         url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
#         response = self.client.delete(url)
#
#         self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
#                                permitted=self.api_permissions['delete']['unauthenticated'])
#
#     def test_evaluatetest_delete_does_not_exist_as_unauthenticated(self):
#         self.logout_user()
#
#         url = reverse(self.api_urls['delete'], kwargs={'pk': 1})
#         response = self.client.delete(url)
#
#         self.check_api_results(response=response, request_type='delete', model_name=self.model_name,
#                                permitted=self.api_permissions['delete']['unauthenticated'])
