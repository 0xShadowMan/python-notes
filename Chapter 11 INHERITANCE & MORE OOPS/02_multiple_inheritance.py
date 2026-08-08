class Employee:
    company = "ITC"
    name = "Default Name"
    salary = 1444
    def show(self):
        print(f"The name {self.name} and his salary is {self.salary}")

class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"This is the language for all of you: {self.language}")

class Programer(Employee, Coder): # Here is the multiple inheritance Employee and Coder 
    company = "ITC Infotech"
    def show_language(self):
        print(f"his language is: {self.language}")


b = Programer()
b.show()
b.printLanguage()
b.show_language()