#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser
import json
from telethon.errors import SessionPasswordNeededError
from telethon.sync import TelegramClient
from telethon import functions


class TelegramApiWrapper:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read("config.ini")

        api_id = '1825907'
        api_hash = '55365009a01594f5263bef85e7fb5eb2'

        self.phone = '+79131173447'
        username = 'session_user'
        self.client = TelegramClient(username, api_id, api_hash)

    def check_auth(self, user):
        if not user.is_user_authorized():
            user.send_code_request(self.phone)
            try:
                user.sign_in(self.phone, input('Enter the code: '))
            except SessionPasswordNeededError:
                user.sign_in(password=input('Password: '))

    def search_channels(self, search_query):
        self.client.start()
        self.check_auth(self.client)
        result = self.client(functions.contacts.SearchRequest(
            q=search_query,
            limit=4
        ))
        channel_list = []
        for chat in result.chats:
            full_result = self.client(functions.channels.GetFullChannelRequest(
                channel=chat.id
            ))
            result_dict = {"title": chat.title,
                           "members": chat.participants_count,
                           "link": "t.me/" + chat.username,
                           "channel_info": full_result.full_chat.about}
            result_str = result_dict['link']
            self.send_messages("@hiddenSt1", result_str)  # временная помойка
            # self.send_message(user.telegram_name, result_str)
            # когда будем получать имя пользователя в телеге
            channel_list.append(result_dict)
        channels_json = json.dumps(channel_list, indent=4)
        return channels_json

    def send_messages(self, username, message):
        self.client(functions.messages.SendMessageRequest(
            peer=username,
            message=message
        ))
