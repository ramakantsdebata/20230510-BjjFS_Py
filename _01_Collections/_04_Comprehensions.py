def Test1():
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    newList = []
    for x in fruits:
        if 'a' in x:
            newList.append(x)
    print(newList)

def Test2():
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    newList = [x          for x in fruits if 'a' in x]
    newSet = {x          for x in fruits if 'a' in x}
    newDict = {hash(x):x          for x in fruits if 'a' in x}
    newGen = (x          for x in fruits if 'a' in x)
    print("Type(newGen) --> ", type(newGen))
    
    newTuple = tuple(x          for x in fruits if 'a' in x)
    print("Type(newTuple) --> ", type(newTuple))
    
    print(newList)

if __name__ == '__main__':
    Test2()  