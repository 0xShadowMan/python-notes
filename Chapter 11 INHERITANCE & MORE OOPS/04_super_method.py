class Employee:
    def __init__(self):
        print("Contractor of Employee") # Thats run only Employee class contactor 
    a = 1 

class Programmer(Employee):
    def __init__(self):
        print("Contractor of Programer ") # Thats run only Programer class contactor 
    b = 2 

class Manager(Programmer): 
    def __init__(self):
        super().__init__()
        print("Contractor of Manager") # Thats run only manager class contactor 
    c = 3

# o = Employee()
# print(o.a) 

# o = Programmer()
# print(o.a, o.b)


o = Manager()
print(o.a, o.b, o.c)
