from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory


class QueryTestCase(TestCase):
    def test_get_executes(self):
        response = self.client.get('/api/query', format='json')
        self.assertEquals(response.status_code, 200)

