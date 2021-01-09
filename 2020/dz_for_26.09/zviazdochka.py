import pytube
import os
import datetime

main_link = "https://www.youtube.com/watch?v=BBGEG21CGo0"
link = "https://www.youtube.com/watch?v=v2ztT1T_qUw"

time = input("Введите время (пример: 11 00 00):")

print(f"Запуск произойдет в {time}")


def wait():
    while datetime.datetime.now().strftime("%H %M %S") < time:
        pass


path = os.getcwd()
filename = 'lol'

try:
    with open('lol.mp4', 'r'):
        print('Файл уже на компе!')
except FileNotFoundError:
    yt = pytube.YouTube(link)

    streams = yt.streams

    video = streams.get_by_itag(22)

    video.download(output_path=path, filename=filename)

    print('Файл установлен')

wait()

print("Запуск файла...")

os.startfile(f"{path}\\{filename}.mp4")
