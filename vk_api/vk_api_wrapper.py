import vk_api


class VkApiWrapper:
    def __init__(self, phone_number: str, password: str):
        self.vk_session = vk_api.VkApi(phone_number, password)
        self.vk = self.vk_session.get_api()
        try:
            self.vk_session.auth(token_only=True)
        except vk_api.AuthError as error_msg:
            print(error_msg)
            return

    def search(self, params: str):
        result = self.vk.search.getHints(q=params)
        result_list = []
        for item in result['items']:
            if item['type'] == 'group':
                group_item = item['group']
                result_dict = {'title': group_item['name'],
                               'subs_count': item['description'],
                               'logo': group_item['photo_100']}
                result_list.append(result_dict)
        return result_list