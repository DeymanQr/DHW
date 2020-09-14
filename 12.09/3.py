def years():
    ch = 2000
    is_even = True
    while True:
        data = yield ch
        if data == "odd" and is_even:
            ch -= 1
            is_even = False
        elif data == "even" and not is_even:
            ch -= 1
            is_even = True
        ch += 2


if __name__ == '__main__':
    gen = years()
    print(next(gen))
    print(gen.send("odd"))
    print(next(gen))
    print(next(gen))
    print(gen.send("even"))
    print(next(gen))
    print(gen.send("odd"))