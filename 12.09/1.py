def fib(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def fib2(n: int) -> int:
    a_1 = 1
    a_2 = 1
    if n == 0 or n == 1:
        return a_2
    for _ in range(1, n):
        a_3 = a_1 + a_2
        a_1 = a_2
        a_2 = a_3
    return a_2


if __name__ == '__main__':
    print(fib(5))