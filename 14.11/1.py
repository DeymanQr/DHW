import requests


class NumbersAPI:
    def __getattr__(self, item):
        if item[0:2] == "_n" and item[2:].isdigit():
            resp = requests.get(f"http://numbersapi.com/{item[2:]}")
            self.__dict__[item] = resp.text
            return resp.text
        raise AttributeError("Unknown attribute")


lolkek = NumbersAPI()
print(lolkek._n12)
print(lolkek._n12)
