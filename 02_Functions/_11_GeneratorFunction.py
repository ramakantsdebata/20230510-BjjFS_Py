def SimpleGeneratorFunc():
    yield 1
    yield 2
    yield 3

def Test1():
    for value in SimpleGeneratorFunc():
        print(value, end=' ')
    SimpleGeneratorFunc()
    SimpleGeneratorFunc()

# Test1()




def FibGen(n):
    '''Generateds a sequence of 'n' fibonacci numbers'''
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a+b

def Test2():
    it = FibGen(10)
    try:
        while True:
            print(next(it), end=", ")
    except StopIteration:
        print("\nDone")

Test2()