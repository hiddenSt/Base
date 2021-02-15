from django.test import TestCase


class BaseTestCase(TestCase):
    def simple_test(self):
        self.assertTrue(True)
