from random import randint


def generator():
    while True:
        yield randint(1, 10000)


def ispalindrom(numb=0):
    if numb != numb[::-1]:
        raise TypeError("strange things")


answ = 0
ch = 0
gen = generator()
while ch < 100:
    num = next(gen)
    try:
        ispalindrom(numb=num)
    except TypeError:
        continue
    answ += num
    ch += 1
print(answ)