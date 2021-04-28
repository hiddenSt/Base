from django.test import TestCase
from TelegramApiWrapper.telegram_api_wrapper import TelegramApiWrapper


class Channel():
    def __init__(self):
        self.title = "title"
        self.participants_count = "90000"
        self.username = "username"
        self.channel_info = "about"


class WrapperTestCase(TestCase):
    def setUp(self):
        self.telegram = TelegramApiWrapper()

    def test_search_channels(self):
        result = self.telegram.search_channels("python")
        result_b = False
        if result[0]['title'].find("python"):
            result_b = True
        self.assertTrue(result_b)

    def test_create_dict(self):
        correct_dict = {'title': "title",
                        'members': "90000",
                        'link': "t.me/username",
                        'channel_info': "about"
                        }
        channel = Channel()
        result_dict = self.telegram.create_dict(channel, channel.channel_info)
        self.assertEqual(result_dict, correct_dict)
