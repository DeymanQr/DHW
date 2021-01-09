import requests
import json
from typing import Union, List, Type, Optional


class MetaEngine:
    pass


class MetaParser:
    pass


class Engine(MetaEngine):
    @classmethod
    def get(cls, link) -> requests.Response:
        resp = requests.get(link)
        return resp

    @classmethod
    def post(cls, link: str, data: dict = None) -> requests.Response:
        if data is None:
            resp = requests.post(link)
        else:
            resp = requests.post(link, json=data)
        return resp


class NumbersAPICrawler:
    def __init__(self, numbers: List[Union[int]]):
        self._numbers = numbers
        self._engine = self.__set_engine()
        self._parser = self.__set_parser()

    @staticmethod
    def __set_engine() -> Type[MetaEngine]:
        return Engine

    @staticmethod
    def __set_parser() -> Type[MetaParser]:
        return NumbersAPIParser

    @classmethod
    def domain(cls) -> str:
        return 'numbersapi.com'

    @classmethod
    def create_search_url(cls, numbers: List[int]) -> str:
        numbers_str = ','.join([str(x) for x in numbers])
        return f'http://{cls.domain()}/{numbers_str}'

    def get_number_by_index(self, index: int) -> Optional[int]:
        try:
            return self._numbers[index]
        except IndexError:
            return None

    def change_number_by_index(self, new_number: int, index: int) -> None:
        if len(self._numbers) > index:
            self._numbers[index] = new_number
            return
        raise IndexError('Index is out of range. We can not set new value')

    def crawl(self):
        url = self.create_search_url(self._numbers)
        response = self._engine.get(url)
        return self._parser.parse(response)


class NumbersAPIParser(MetaParser):
    @classmethod
    def parse(cls, response: requests.Response) -> Union[dict, str]:
        try:
            return response.json()
        except json.decoder.JSONDecodeError:
            return response.text


crawler = NumbersAPICrawler([42, 123])
print(crawler.crawl())