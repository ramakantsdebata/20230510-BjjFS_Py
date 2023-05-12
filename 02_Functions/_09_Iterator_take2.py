x1 = [1, 2, 3, 4, 5]

def Iterate():
    it = iter(x1)

    try:
        while(1):
            print(it.__next__(), end='-')
    except StopIteration as e:
        print("End of data")
        print(type(e), e.__repr__())

def CheckIterable(obj):
    try:
        iter(obj)
        print("Iterable")
        return True
    except TypeError as e:
        print("Not an Iterable")
        return False
    
x = 10
y = [1, 2, 3]
z = "String"

def main():
    CheckIterable(x)
    CheckIterable(y)
    CheckIterable(z)

print("Module:", __name__)

if __name__ == '__main__':
    main()