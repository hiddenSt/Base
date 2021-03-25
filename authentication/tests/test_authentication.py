from rest_framework.test import APITestCase
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
)

class AuthenticationTest(APITestCase):
    def test_can_register_user(self):
        registration_content = {
            'email': 'simple@email.com',
            'name': 'David',
            'password': 'Pass1234',
            'password_confirmed': True,
        }

        response = self.client.post('/users', registration_content,
                                    content_type='application/json')
        self.assertEqual(response.status_code, HTTP_201_CREATED)

    def test_can_create_access_token(self):
        self.assertTrue(False)

    def test_can_refresh_tokens(self):
        self.assertTrue(False)

    def test_cant_register_user_with_invalid_email(self):
        registration_content = {
            'email': 'invalid_email',
            'password': 'Pass1234',
            'password_confirmed': True,
        }

        response = self.client.post('/users', registration_content,
                                    content_type='application/json')
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    def test_cant_register_user_with_invalid_password(self):
        registration_content = {
            'email': 'simple@email.com',
            'password': '',
            'password_confirmed': True,
        }

        response = self.client.post('/users', registration_content,
                                    content_type='application/json')
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    def test_cant_register_user_without_password_confirmation(self):
        registration_content = {
            'email': 'simple@email.com',
            'name': 'David',
            'password': 'Pass1234',
        }

        response = self.client.post('/users', registration_content,
                                    content_type='application/json')
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    def test_cant_register_user_with_invalid_name(self):
        registration_content = {
            'email': 'simple@email.com',
            'name': '',
            'password': 'Pass1234',
            'password_confirmed': True,
        }
        response = self.client.post('/users', registration_content,
                                    content_type='application/json')
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    def test_cant_refresh_tokens_with_invalid_refresh_tokens(self):
        self.assertTrue(False)

    def test_cant_create_access_token_with_invalid_email(self):
        self.assertTrue(False)

    def test_cant_create_access_token_with_invalid_password(self):
        self.assertTrue(False)
