a = input().split()
print(a)
maximum = 0
el = None
for i in a:
    if a.count(i) > maximum:
        maximum = a.count(i)
        el = i

print(el)