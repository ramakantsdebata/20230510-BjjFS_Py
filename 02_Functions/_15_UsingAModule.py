def Test1():
    from _09_Iterator_take2 import CheckIterable

    x = 2
    CheckIterable(x)

    print("MyProg: ", __name__)

def Test2():
    import sys
    #print(sys.path)
    sys.path.append(r"C:\RSD\Trainings Conducted\GitCode_Bajaj_Python\20230510-BjjFS_Py\01_Collections")
    #print(sys.path)
    # from _01_Collections._04_Comprehensions import Test2 as SomeCode
    from _04_Comprehensions import Test2 as SomeCode
    SomeCode()

Test2()