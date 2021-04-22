from rest_framework.test import APITestCase, URLPatternsTestCase
from rest_framework import status
from django.urls import include, path, reverse
from django.test import TransactionTestCase

class LoginTests(APITestCase, URLPatternsTestCase, TransactionTestCase):
    urlpatterns = [
        path('api/', include('authentication.urls'))
    ]

    def test_returns_400_bad_request_if_has_no_email(self):
        url = reverse('authentication:login')
        request = {'password': 'pass1234'}
        response = self.client.post(url, format='json', request=request)
        self.assertEqual(response.status_code,
                         status.HTTP_400_BAD_REQUEST)