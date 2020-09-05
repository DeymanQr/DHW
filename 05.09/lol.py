import requests
from bs4 import BeautifulSoup

strin = "+".join(input().replace("+", "%2B").replace("/", "%2F").split())
url = f"https://www.google.com/search?q={strin}"
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'lxml')
answ = soup.find("div", {"class": "BNeawe iBp4i AP7Wnd"}).text
print(answ)