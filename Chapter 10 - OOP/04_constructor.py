class Employee: 

    def __init__(just, name, salary, language):# we create an arguments for getting infos efficiently 
        # name = "Harry"
        # salary = "10000"
        just.name = name # store the arguments values
        just.salary = salary
        just.language = language
        
    
    def getInfo(just):
        print(f"The language is {just.language}. The salary is {just.salary}")

    @staticmethod # here not need to use arguments 
    def greet():
        print("Good morning")


harry = Employee("Alex", "100000", "Python")

print(harry.name, harry.salary)

harry.greet()
 