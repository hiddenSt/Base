from rest_framework.test import APITestCase, URLPatternsTestCase
from rest_framework import status
from django.urls import include, path, reverse


class RegisterTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/', include('authentication.urls'))
    ]

    def test_returns_error_if_request_has_no_email(self):
        url = reverse('authentication:register')
        request = {'password': 'pass1234', 'username': 'user1214'}
        response = self.client.post(url, format='json', request=request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
