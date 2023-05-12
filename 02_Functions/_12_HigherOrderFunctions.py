def Print1(n):
    print(f"n\t{n}\n")

def Print2(n):
    print(f"n:\t{n}\n")

def Print3(n):
    print(f"n is\t{n}\n")

def JobMgr(fn, n):
    fn(n)

def Test1():
    JobMgr(Print1, 10)
    JobMgr(Print2, 10)
    JobMgr(Print3, 10)