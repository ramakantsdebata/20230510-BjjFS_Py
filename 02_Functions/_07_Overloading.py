# ## Iteration 1 ##################################
# def Iteration1():
#     def Add(a, b):
#         result = a + b
#         return result

#     def Add(a, b, c):
#         result = a + b + c
#         return result

#     print(Add(1, 2))
#     print(Add(1, 2, 3))

# ## Iteration 2 #######################################

# # Not Efficient
# def Iteration2():
#     def Add(dataType, *args):
#         if dataType == 'int':
#             return AddIntegers(*args)
#         # elif dataType == 'str':
#         else:
#             return AddStrings(*args)
#         #else:
#         #   return None

#     def AddIntegers(*args):
#         result = 0
#         for x in args:
#             result += x
#         return result
    
#     def AddStrings(*args):
#         result = ''
#         for x in args:
#             result += x
#         return result
            

#     print(Add('int', 1, 2, 3))
#     print(Add('str', "1", "2", "3"))

# ## Iteration 3 #########################

# # Most inefficient
# def Iteration3():
#     def Add(a = None, b = None, c = None, d = None, e = None):
#         result = 0
#         # Before adding each element check for None
        
    
    
## Iteration 4 #############

def Iteration4():
    from multipledispatch import dispatch

    @dispatch(int, int)
    def Add(a, b):
        result = a + b
        return result

    @dispatch(int, int, int)
    def Add(a, b, c):
        result = a + b + c
        return result

    @dispatch(float, int, float)
    def Add(a, b, c):
        result = a + b + c
        return result

    print(Add(1, 2))
    print(Add(1, 2, 3))
        
        
    #print(Add('MyType', ob1, ob2, ob3))

Iteration4()