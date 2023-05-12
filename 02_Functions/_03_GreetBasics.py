def greet():
    '''Says Hello to just about anyone'''
    print("Hello World!")
    return "!!!"

def greetPerson(name):
    '''Says Hello to just about anyone'''
    city = "Pune"
    print("Hello {1} from {0}. Regards {1}".format(city, name))
    # print("Hello {} from {}".format(city, name))

    print("Hello", name)
    print(f"Hello {name}")
    print(f"Hello %s"%(name))

    return "!!!"

print(greet.__doc__)
greetPerson("Rakesh")