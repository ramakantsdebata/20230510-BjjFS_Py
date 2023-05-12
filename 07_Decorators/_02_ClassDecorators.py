# Decorator

class CallCount:
    def __init__(self, f):
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.f(*args, **kwargs)
    

# Using the decorator
def main():
    @CallCount
    def Hello(name):
        print('Hello, {}!'.format(name))

    Hello('Ramakant')
    Hello('Manish')
    Hello('Abhijeet')
    print(Hello.count)

if __name__ == '__main__':
    main()