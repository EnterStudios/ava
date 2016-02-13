# Django Imports
from django.apps import apps
from django.contrib.auth.models import User
# Rest Imports
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient


# Implementation
class AvaCoreTest(APITestCase):
    users = {
        'admin': {'username': 'admin@test.com', 'email': 'admin@test.com', 'password': 'test'},
        'standard': {'username': 'user@test.com', 'email': 'user@test.com', 'password': 'test'},
        'other': {'username': 'other@test.com', 'email': 'other@test.com', 'password': 'test'},
    }

    status_forbidden = {status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN}
    status_ok = {status.HTTP_200_OK, status.HTTP_201_CREATED, status.HTTP_204_NO_CONTENT}

    login_url = reverse("jwt_login")

    enforce_csrf = False

    def setUp(self):
        # Create required users
        for key, user in self.users.items():
            if key is 'admin':
                User.objects.create_superuser(username=user['email'], email=user['email'], password=user['password'])
                # user.is_staff = True
                # user.save()
            else:
                User.objects.create_user(username=user['email'], email=user['email'], password=user['password'])

        self.client = APIClient(enforce_csrf_checks=self.enforce_csrf)

    def create_user(self, user):
        User.objects.create_user(username=user['email'], email=user['email'], password=user['password'])

    def login_user(self, user):
        response = self.client.post(self.login_url, self.users[user], format='json')
        token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)

    def logout_user(self):
        self.client.credentials()

    def create_object_via_api(self, data, user='admin'):
        # step 6: you will need to write this method.... this template only works with single models
        # with no relationships
        url = reverse(self.api_urls['create'])

        if user:
            # must be admin to create
            self.login_user(user=user)
        else:
            self.logout_user()

        # must be admin to create
        self.login_user(user='admin')

        response = self.client.post(url, data, format='json')

        self.check_api_results(response=response, request_type='create', model_name=self.model_name,
                               permitted=self.api_permissions['create']['admin'])

        self.logout_user()

        # return the id of the model you are testing
        if 'id' in response.data:
            return response.data['id']

    def check_api_results(self, response, request_type, model_name, permitted=True):
        # model = apps.get_model(model_name)
        # print("CHECK API RESPONSE" + str(response.data))
        if permitted:
            self.assertIn(response.status_code, self.status_ok)
            # self.assertEqual(model.objects.count(), results_size[request_type]['permitted'])
        else:
            self.assertIn(response.status_code, self.status_forbidden)
            # self.assertEqual(model.objects.count(), results_size[request_type]['not-permitted'])
