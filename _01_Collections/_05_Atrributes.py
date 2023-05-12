MethodsAndAttribs = [method for method in dir(int) if method.startswith("_") is False]
print(MethodsAndAttribs)

onlyMethods = [method for method in dir(int) if callable(getattr(int, method)) is True and method.startswith("_") is False]
print(onlyMethods)