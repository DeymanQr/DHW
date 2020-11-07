import requests


class Crawler:
    def __init__(self, *args, **kwargs):
        self.__numb = int(input("Write some number:\t"))

    def get_number(self):
        return self.__numb

    def change_number(self, new_numb: int, *args, **kwargs):
        try:
            self.__numb = new_numb
            return True
        except Exception:
            return False


class Engine:
    def __init__(self, domain: str, *args, **kwargs):
        self.domain = domain

    def get(self, numb_crawler: Crawler, *args, **kwargs):
        resp = requests.get("http://" + self.domain + "/" + str(numb_crawler.get_number()))
        return resp

    def post(self, numb_crawler: Crawler, data: list, *args, **kwargs):
        resp = requests.get("http://" + self.domain + "/" + str(numb_crawler.get_number()))



class Parser:
    def __init__(self, resp: requests.Response, *args, **kwargs):
        self.response = resp

    def get_useful_data(self, *args, **kwargs):
        return {
            "number": int(self.response.url.split("/")[-1]),
            "text": self.response.text,
        }

    def print_useful_data(self, *args, **kwargs):
        data = {
            "number": int(self.response.url.split("/")[-1]),
            "text": self.response.text,
        }
        if "is a boring number." in data["text"] or "is an unremarkable number." in data["text"] or\
                "is a number for which we're missing a fact (submit one to numbersapi at google mail!)." in data["text"] or\
                "is an uninteresting number." in data["text"]:
            print("We don't find any interesting facts about number", data["number"])
        else:
            print("Interesting fact about number", data["number"], ":", data["text"])


craw = Crawler()
eng = Engine("numbersapi.com")

response = eng.get(craw)

pars = Parser(response)

pars.print_useful_data()
