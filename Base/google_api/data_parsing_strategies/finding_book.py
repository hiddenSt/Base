import json
from google_api.data_parsing_strategies.base_strategy import \
    DataParsingStrategy


class FindingBookDataParsingStrategy(DataParsingStrategy):
    def parse_data(self, book_data):
        book_data = json.loads(book_data)
        all_books = []
        for item in book_data['items']:
            volume_info = item['volumeInfo']
            data = {'title': volume_info.get('title'), 'author':
                    volume_info.get('authors'), 'publisher': volume_info.get(
                    'publisher'), 'publishedDate': volume_info.get(
                    'publishedDate'), 'pageCount': volume_info.get('pageCount'),
                    'rating': volume_info.get('averageRating'), 'annotation':
                    volume_info.get('description')
                    }
            all_books.append(data)
        return json.dumps(all_books)
