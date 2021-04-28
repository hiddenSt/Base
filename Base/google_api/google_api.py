import requests


class GoogleBookApiWrapper:
    URL_PATTERNS = {'searching_url': 'https://www.googleapis.com/books/v1/'
                                     'volumes?q={0}&key={1}&maxResults={2}'}
    MAX_RESPONSES_NUMBER = 5

    def __init__(self, api_key):
        self.API_KEY = api_key

    def get_book_by_title(self, book_title, data_parsing_strategy):
        response = requests.get(
            url=GoogleBookApiWrapper.URL_PATTERNS['searching_url'].format(
                book_title, self.API_KEY, self.MAX_RESPONSES_NUMBER))
        return data_parsing_strategy.parse_data(response.content)
