from django.test import TestCase


class SimpleTestCase(TestCase):
    def test_is_failed(self):
        self.assertTrue(False)

    def test_is_passed(self):
        self.assertTrue(True)

