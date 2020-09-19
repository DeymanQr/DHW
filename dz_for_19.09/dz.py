a = [i+1 for i in range(1000)]
a = [i ** 2 - 2 * len(str(i)) for i in a if sum([int(j) for j in str(i)]) >= i and i // 10 % 10 != 7]
print(a)