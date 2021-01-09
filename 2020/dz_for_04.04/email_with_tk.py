from tkinter import *
from time import sleep

width = 155
height = 400

root = Tk()
root.title("Lolkek")
root.geometry(f"{width}x{height}")


def get_info(email_input="None", username_input="None"):
    if email_input != "None" and username_input != "None":
        email = email_input.get()
        username = username_input.get()
        print(email + username)


Label(root, text="Введите свой ник:").grid(row=0)
name = Entry(width="25")
name.grid(row=1)
Label(root, text="Введите свой email:").grid(row=2)
email_input = Entry(width="25")
email_input.grid(row=3)
Label(root, text="\n").grid(row=4)
Button(root, text="Отправить заявку", command=lambda: get_info(email_input=email_input, username_input=name)).grid(row=5)

root.mainloop()