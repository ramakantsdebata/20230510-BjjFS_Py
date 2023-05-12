x = [1, 2, 3, 4, 5]
s = "Hello"

for i in x:
    print(i, end = '-')
print("\n")

for c in s:
    print(c, end='-')

print("\n")
it = iter(x)

for n in range(len(x)):
    #print(it.__next__(), end='-')
    print(next(it), end='-')

next(it)
