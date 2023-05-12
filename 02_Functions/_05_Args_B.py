def PrintDetails(n1, n2, /, n3, *, n4,  **kwargs):

    print(type(kwargs))
    for key, value in kwargs.items():
        print("%s --> %s"%(key, value))

PrintDetails(1, 2,      3, n4 = 4, name = "Abhijeet", age = '17', standard = '5')
PrintDetails(1, 2, n3 = 3, n4 = 4, name = "Abhijeet", age = '17', standard = '5')