a = [i+1 for i in range(-1000, -1)]
a = [i ** 2 - 2 * len(str(i)) for i in a if sum([int(j) for j in str(i)[1:]]) >= abs(i) and i // 10 % 10 != -7]
print(a)