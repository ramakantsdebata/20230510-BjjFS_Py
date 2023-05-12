# def Test01():
#     from _01_Bytes_and_ByteArrays import *

#     lst = [1, 2, "Manish", "Abhijeet", Test1]

#     lst[4]()

#     print(id(lst))

#     lst.append(10)
#     print(id(lst))


def Test02():
    str1 = "Manish"
    str2 = str1
    str2 = "Abhijeet"

    print(str1)

def Test03():
    lst1 = [1, 2, 3, 4]
    lst2 = lst1[:]
    lst2.append(5)
    
    print(lst1)


Test03()