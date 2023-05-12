
class SimpleList:
    
    _no_of_lists = 0
    _my_type = "SimpleList"

    @staticmethod
    def getSq(lst):
        return list(map(lambda x : x**2, lst))

    @classmethod
    def getClassData(cls):
        print(cls._no_of_lists)
        print(cls._my_type)
        
    def __init__(self, data):
        self.lst = list(data)
        SimpleList._no_of_lists += 1

    def add(self, val):
        self.lst.append(val)

    def getAt(self, idx):
        print("SimpleList")
        return self.lst[idx]
    
    def __getitem__(self, index):
        return self.lst[index]

    def __len__(self):
        return len(self.lst)
    
    def __repr__(self) -> str:
        return f"{type(self).__name__}: The data in my list is of length {len(self.lst)} ||{self.lst}"

    def __str__(self) -> str:
        return f"{self.lst}"

    def sort(self):
        self.lst.sort()

class SortedList(SimpleList):

    my_type = "SortedList"

    def __init__(self, data):
        super().__init__(data)      # Reference to base clas / immediate parent
        print("SortedList")

    def getAt(self, index):
        print("SortedList")
        return super().getAt(index)

    

class IntList(SimpleList):
    def __init__(self, data):
        super().__init__(data)
        print("IntList")

    def getAt(self, index):
        print("IntList")
        return super().getAt(index)

class SortedIntList(SortedList, IntList):
    def __init__(self, data):
        super().__init__(data)
        print("SortedIntList")

    def getAt(self, index):
        print("SortedIntList")
        return super().getAt(index)



def Test1():
    s1 = SimpleList([1, 2, 3, 4])
    s2 = SimpleList([73, 32, 98, 13, 26])
    print(s2[2])
    print(s2.getAt(2))
    print(len(s1))
    print("Str -->", s1.__str__())
    print("Repr -->", s1.__repr__())
    s2.sort()
    print(s2)
# lst1 = []
# lst1.__len__()
# len(lst1)

    si1 = SortedIntList([1, 2, 3])
    print(si1)


def Test2():
    si1 = SortedIntList([1, 2, 3])
    ss1 = SortedList([1, 2, 3])
    ss1.getClassData()
    print(SimpleList._no_of_lists)


def Test3():
    s1 = SortedIntList([34, 23, 15, 45])
    print("\n\n")
    print(s1.getAt(2))
    print("\n\n")
    print(SortedIntList.__mro__)



# Test1()
# Test2()

Test3()
