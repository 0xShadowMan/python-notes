class Employee:
    a = 1
    
    @classmethod # for this, the result will show class attribute.. 1
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = Employee()
e.a = 45 # for @classmethod, that can't change the class attribute value. 

e.show()