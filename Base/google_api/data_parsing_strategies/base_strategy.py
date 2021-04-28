from abc import ABC, abstractmethod


class DataParsingStrategy(ABC):
    @abstractmethod
    def parse_data(self, data):
        pass
