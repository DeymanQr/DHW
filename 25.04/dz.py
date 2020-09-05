import requests


def get_translate(text):
    fromm = "ru"
    to = "en"
    url = f"https://api.mymemory.translated.net/get?q={text}&langpair={fromm}|{to}"
    resp = requests.get(url)
    translate = resp.json()
    answ = translate["responseData"]["translatedText"]
    return answ


def main():
    while True:
        text = input("\nВведите текст, который вы хотите перевести:\n")
        trans = get_translate(text)
        print(f"\nПеревод:\n{trans}")
        exit = input("\nХотите выйти?\n")
        if exit.lower() == "да":
            print("Пока-пока....")
            break


if __name__ == '__main__':
    main()