import tkinter as tk
import time

word = input()

class Klava:
    def __init__(self):
        self.tk = tk.Tk()
        self.tk.attributes("-topmost", True)
        self.c = tk.Canvas(self.tk, width=669, height=249)
        self.klava = ['1234567890-=', 'qwertyuiop[]\\', 'asdfghjkl;\'', 'zxcvbnm,./']
        self.letters_on_c = {' ': self.c.create_rectangle(121, 201, 571, 251), 'shift': self.c.create_rectangle(2, 151, 71, 201), '`': self.c.create_rectangle(21, 1, 71, 51)}
        self.c.create_text(45, 25, text='`', font='Arial 20')
        self.c.create_text(37, 176, text='Shift', font='Arial 20')
        for i, j in enumerate(self.klava):
            for k, l in enumerate(j):
                self.letters_on_c[l] = self.c.create_rectangle(50*k+71, 50*i+1, 50*k+121, 50*i+51)
                self.c.create_text(50*k+95, 50*i+25, text=l, font='Arial 20')
        self.shift_letters = {'~': '`', '!': '1', '@': '2', '#': '3', '$': '4', '%': '5', '^': '6', '&': '7', '*': '8', '(': '9', ')': '0', '_': '-', '+': '=', 'Q': 'q', 'W': 'w', 'E': 'e', 'R': 'r', 'T': 't', 'Y': 'y', 'U': 'u', 'I': 'i', 'O': 'o', 'P': 'p', '{': '[', '}': ']', '|': '\\', 'Z': 'z', 'X': 'x', 'C': 'c', 'V': 'v', 'B': 'b', 'N': 'n', 'M': 'm', '<': ',', '>': '.', '?': '/', 'A': 'a', 'S': 's', 'D': 'd', 'F': 'f', 'G': 'g', 'H': 'h', 'J': 'j', 'K': 'k', 'L': 'l', ':': ';', '"': "'"}
        self.c.pack()

    def blink(self, key):
        if key in self.shift_letters.keys():
            self.c.itemconfig(self.letters_on_c['shift'], fill='red')
            self.c.update()
            time.sleep(0.2)
            self.c.itemconfig(self.letters_on_c[self.shift_letters[key]], fill='red')
            self.c.update()
            time.sleep(0.3)
            self.c.itemconfig(self.letters_on_c[self.shift_letters[key]], fill='')
            self.c.update()
            time.sleep(0.3)
            self.c.itemconfig(self.letters_on_c['shift'], fill='')
            self.c.update()
            time.sleep(0.2)
        else:
            self.c.itemconfig(self.letters_on_c[key], fill='red')
            self.c.update()
            time.sleep(0.3)
            self.c.itemconfig(self.letters_on_c[key], fill='')
            self.c.update()
            time.sleep(0.3)


a = Klava()
a.c.update()
time.sleep(1)
try:
    for i in word:
        a.blink(i)
except KeyError:
    print('You are invalid!')