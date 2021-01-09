from random import randint
from tkinter import *
from time import sleep

WIDTH = 300
HEIGHT = 300


root = Tk()

c = Canvas(root, width=WIDTH, height=HEIGHT)
c.pack()

dots = []
height_of_dot = HEIGHT/2

while True:
    center_dot = c.create_oval(WIDTH, height_of_dot, WIDTH+3, height_of_dot-3, fill="black")
    dots.append(center_dot)
    for i in dots[:]:
        c.move(i, -3, 0)
        if c.coords(i)[0] <= 0:
            c.move(i, WIDTH*10, HEIGHT*10)
            dots.remove(i)
    a = randint(1, 5)
    if a == 1 or a == 2:
        height_of_dot -= 3
    elif a == 3 or a == 4:
        height_of_dot += 3
    if c.coords(dots[-1])[1] >= HEIGHT:
        print("Bitcoin has been dead :(")
        break
    elif c.coords(dots[-1])[-1] <= 0:
        print("Bitcoin is kek ;)")
        break
    c.update()
    sleep(0.05)

root.mainloop()