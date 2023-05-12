class Employee:
    _last_id = 0

    def __init__(self, first, last) -> None:
        self._last_id += 1
        self.id = self._last_id
        self._firstname = first
        self._lastname = last

    # def getName(self):
    #     return self._name
    
    # def setName(self, value):
    #     self._name = value

    @property
    def name(self):
        return self._firstname + " " + self._lastname
        # pass

    @name.setter
    def name(self, value):
        self._firstname = value

    def __str__(self):
        return f"{self.name}"

def Test1():
    e1 = Employee("Vishal", "Mane")
    print(e1._firstname + " " + e1._lastname)
    # print(e1.getName())
    # e1.setName("Abhijeet")
    # print(e1._name)
    

    e1.name = "Manish"
    print(e1.name)
    

Test1()