from typing import Generator


def gen_creator() -> Generator[int, None, None]:
    prime_nums = []
    ch = 2
    isprime = True
    while True:
        for i in prime_nums:
            if ch % i == 0:
                isprime = False
                break
        else:
            isprime = True

        if isprime:
            prime_nums.append(ch)
            yield ch

        ch += 1


gen = gen_creator()
while True:
    print(next(gen))