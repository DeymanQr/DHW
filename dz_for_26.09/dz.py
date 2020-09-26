print(len(set(input().split())))

a = (1, 2, 3, 2, 2, 3, 3)
b = max({i: a.count(i) for i in set(a)}.items(), key=lambda x: x[1])[0]
print(b)