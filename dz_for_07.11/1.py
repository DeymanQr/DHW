import requests
from abc import ABC, abstractmethod
from typing import Type, Dict, Optional
from pprint import pprint as pp


class AbstractEngine(ABC):
    @classmethod
    @abstractmethod
    def get(cls, link: str) -> requests.Response:
        pass


class AbstractParser(ABC):
    @classmethod
    @abstractmethod
    def parse(cls, response: requests.Response) -> Dict:
        pass


class AbstractCrawler(ABC):
    @classmethod
    @abstractmethod
    def _set_engine(cls) -> Type[AbstractEngine]:
        pass

    @classmethod
    @abstractmethod
    def _set_parser(cls) -> Type[AbstractParser]:
        pass

    @abstractmethod
    def crawl(self, type: str) -> Dict:
        pass


class Engine(AbstractEngine):
    @classmethod
    def get(cls, link: str) -> requests.Response:
        resp = requests.get(link)
        return resp

    @classmethod
    def post(cls, link: str, data: Optional[Dict] = None) -> requests.Response:
        if data is None:
            resp = requests.post(link)
        else:
            resp = requests.post(link, json=data)
        return resp


class OpenWeatherAPICrawler(AbstractCrawler):
    def __init__(self, city: str):
        self._city = city
        self._engine = self._set_engine()
        self._parser = self._set_parser()

    @classmethod
    def _set_engine(cls) -> Type[AbstractEngine]:
        return Engine

    @classmethod
    def _set_parser(cls) -> Type[AbstractParser]:
        return OpenWeatherAPIParser

    @classmethod
    def domain(cls) -> str:
        return "api.openweathermap.org"

    @classmethod
    def api_key(cls) -> str:
        return "95eb789aee367126d308f60f914b26e8"

    @classmethod
    def create_search_url(cls, type: str) -> str:
        if type == "WN": # Weather Now
            return f"https://{cls.domain()}/data/2.5/weather"
        elif type == "MAMT": # Max And Min Temperature
            return f"https://{cls.domain()}/data/2.5/onecall"

    def get_lon_lat(self) -> Dict:
        data = {
            "q": self._city,
            "appid": self.api_key(),
        }
        url = self.create_search_url("WN") + "?" + "&".join([f"{i[0]}={i[1]}" for i in data.items()])
        response = self._engine.get(url)
        return self._parser.parse_lon_lat(response)

    def crawl(self, type: str) -> Dict:
        lon_lat_data = self.get_lon_lat()
        data = {
            "lon": lon_lat_data["lon"],
            "lat": lon_lat_data["lat"],
            "exclude": "minutely,hourly",
            "appid": self.api_key(),
            "units": "metric",
            "lang": "ru",
        }
        url = self.create_search_url("MAMT") + "?" + "&".join([f"{i[0]}={i[1]}" for i in data.items()])
        response = self._engine.get(url)
        if type == "WN": # Weather Now
            return self._parser.parse(response)["current"]
        elif type == "MAMT": # Max And Min Temperature
            resp = self._parser.parse(response)["daily"][:5]
            temps = {
                "max temperature": resp[0]["temp"]["max"],
                "min temperature": resp[0]["temp"]["min"],
            }
            for i in resp:
                if temps["max temperature"] < i["temp"]["max"]:
                    temps["max temperature"] = i["temp"]["max"]
                if temps["min temperature"] > i["temp"]["min"]:
                    temps["min temperature"] = i["temp"]["min"]
            return temps



class OpenWeatherAPIParser(AbstractParser):
    @classmethod
    def parse(cls, response: requests.Response) -> Dict:
        try:
            json_data = response.json()
            if json_data.get("name") is None:
                return response.json()
            else:
                return {
                    "main": json_data["main"],
                    "weather": json_data["weather"],
                }
        except KeyError:
            return {}

    @classmethod
    def parse_lon_lat(cls, response: requests.Response) -> Dict:
        try:
            return response.json()["coord"]
        except KeyError:
            return {}


crawler = OpenWeatherAPICrawler("Kyiv")
pp(crawler.crawl("MAMT"))