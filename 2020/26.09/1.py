a = input().split()

'''for i in set(a):
    print(f"{i}: {a.count(i)}")'''

b = iter(set(a))
while True:
    try:
        i = next(b)
        print(f"{i}: {a.count(i)}")
    except StopIteration:
        break
