#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser
import json
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.sync import TelegramClient
from telethon import functions, types
import asyncio
import re


class TelegramApiWrapper:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read("config.ini")

        api_id = '1825907'
        api_hash = '55365009a01594f5263bef85e7fb5eb2'

        phone = '+79131173447'
        username = 'session_user'
        self.client = TelegramClient(username, api_id, api_hash)

    async def check_auth(self, user):
        if not await user.is_user_authorized():
            await user.send_code_request(self.phone)
            try:
                await user.sign_in(self.phone, input('Enter the code: '))
            except SessionPasswordNeededError:
                await user.sign_in(password=input('Password: '))

    async def async_search(self, search_query):
        await self.client.start()
        await self.check_auth(self.client)
        result = await self.client(functions.contacts.SearchRequest(
            q=search_query,
            limit=4
        ))
        channel_list = []
        for chat in result.chats:
            full_result = await self.client(functions.channels.GetFullChannelRequest(
                channel=chat.id
            ))
            result_dict = {"title": chat.title, "members": chat.participants_count, "link": "t.me/" + chat.username,
                           "channel_info": full_result.full_chat.about}
            result_str = result_dict['link']
            #self.send_messages("@hiddenSt1", result_str)
            # self.send_message(user.telegram_name, channel_list) когда будем получать имя пользователя в телеге
            channel_list.append(result_dict)
        self.send_messages("@hiddenSt1", channel_list)
        channels_json = json.dumps(channel_list, indent=4)
        return channels_json

    def send_messages(self, username, message):
            result = self.client(functions.messages.SendMessageRequest(
                peer=username,
                message=message
            ))

    def search_channels(self, search_query):
        with self.client:
            return self.client.loop.run_until_complete(self.async_search(search_query))
