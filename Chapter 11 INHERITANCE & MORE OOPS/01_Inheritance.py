class Employee:
    company = "ITC"
    def show(self):
        print(f"The name {self.name} and his salary is {self.salary}")

'''
class Programer:
    company = "ITC Infotech"

    def show(self):
        print(f"The name {self.name} and his salary is {self.salary}")
    def language(self):
        print(f"his language is: {self.language}")'''

# The better way we can do this

class Programer(Employee):
    company = "ITC Infotech"
    def language(self):
            print(f"his language is: {self.language}")


a = Employee()
b = Programer()

a.company()
b.company()

    

