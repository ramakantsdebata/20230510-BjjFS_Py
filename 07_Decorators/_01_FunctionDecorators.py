# Decorator function
def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)
    return wrap

# Using the decorator
def main():
    def Org1():
        return 'Bajaj©'

    @escape_unicode
    def Org2():
        return 'Bajaj©'

    print(Org1())
    print(Org2())

if __name__ == '__main__':
    main()