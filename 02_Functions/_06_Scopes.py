# def f():
#     print("1:", globals()["s"])
#     s = "Local String"
#     print("2:", s)

# s = "Global string"

# f()
# print("3:", s)


# def myFunc():
#     a = 10
#     b = 20
#     print("Globals --> ", globals())
#     print("Locals --> ", locals())
#     globals()["c"] = 50

# c = 30
# d = 40

# myFunc()


def Outer():
    a = 200
    def Inner():
        # global a
        nonlocal a
        a = 300
        print("Inner:", a)
    Inner()
    print("Outer:", a)
    return Inner

a = 100
Outer()
print("Global:", a)

Outer()()