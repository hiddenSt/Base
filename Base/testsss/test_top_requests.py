from django.test import TestCase

from django.contrib.auth.models import User

from Base.models.request_model import RequestModel
from Base.top_requests.top_requests import get_top


class TopRequestsTest(TestCase):
    def setUp(self):
        self.userInstance = User.objects.create(username='zxc')

    def test_top_requests_logic(self):
        TEXT_1 = '123'
        TEXT_2 = '12345'
        TEXT_3 = '123456789'
        request_dict = {}
        RequestModel.objects.create(user=self.userInstance, text=TEXT_1)
        request_dict.setdefault(TEXT_1, 1)
        for i in range(2):
            RequestModel.objects.create(user=self.userInstance, text=TEXT_2)
        request_dict.setdefault(TEXT_2, 2)
        for i in range(5):
            RequestModel.objects.create(user=self.userInstance, text=TEXT_3)
        request_dict.setdefault(TEXT_3, 5)
        self.assertEqual(get_top(), request_dict)
