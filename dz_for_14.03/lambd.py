func1 = lambda i: True if isinstance(i, int) and i % 2 == 0 else False

spis = ['kek', 1, 4, 2, 13]
spis2 = []
for i in spis:
    if func1(i):
        spis2.append(i)

print(spis2)