from .api_wrapper import ApiWrapper


class VkApiWrapper(ApiWrapper):
    def __init__(self, phone_number: str, password: str):
        self.vk_session = 1

    def make_query(self, parameters: str):
        return None

