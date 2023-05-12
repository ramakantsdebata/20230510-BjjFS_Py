def SumNums(n1, n2, n3 = 0):
    sum = n1 + n2 + n3
    return sum

def SumNumsNew(n1, n2, /, n3, n4, n5, n6, n7):
    sum = n1 + n2 + n3 + n4 + n5 + n6 + n7
    return sum


# print(SumNums(1, 2, 3))
# print(SumNums(1, 2))
# print(SumNums(n2=10, n1=20))
print(SumNumsNew(1, 2, 3, 4, 5, 6, 7))

data = [1, 2, 3, 4, 5, 6, 7]
print(SumNumsNew(*data))


def SumFlex1(*data):
    print(type(data), end="  ")
    sum = 0
    for ele in data:
        sum += ele
    return sum

def SumFlex2(n1, *data):
    print(type(data), end="  ")
    sum = n1
    for ele in data:
        sum += ele
    return sum

def SumFlex3(n1, n2, *data):
    print(type(data), end="  ")
    sum = n1 + n2
    for ele in data:
        sum += ele
    return sum


# print(SumFlex3(1))
# print(SumFlex3(1, 2))
# print(SumFlex3(1, 2, 3))
# print(SumFlex3(1, 2, 3, 4))
my_data = [1, 2, 3, 4, 5, 6, 7]
print(SumFlex1(*data))
print(SumFlex3(*data))
