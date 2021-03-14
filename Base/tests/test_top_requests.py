from django.test import TestCase

from django.contrib.auth.models import User

from Base.models.request_model import RequestModel
from Base.services.top_requests import get_top


class TopRequestsTest(TestCase):
    def setUp(self):
        self.userInstance = User.objects.create(username='zxc')

    def test_top_requests_logic(self):
        request_dict = {}
        RequestModel.objects.create(user=self.userInstance, text='123')
        request_dict.setdefault('123', 1)
        for i in range(2):
            RequestModel.objects.create(user=self.userInstance, text='12345')
        request_dict.setdefault('12345', 2)
        for i in range(5):
            RequestModel.objects.create(user=self.userInstance,
                                        text='123456789')
        request_dict.setdefault('123456789', 5)
        print(get_top(), request_dict)
        self.assertEqual(get_top(), request_dict)
