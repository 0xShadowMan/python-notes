class player:
    language = "python" # this are the class attribute 
    salary = 120000

harry = player()
harry.name = "Harry"
print(harry.name, harry.language, harry.salary)

Alex = player()
Alex.name = "Alex" # an # this are the instance attribute 
print(Alex.name, Alex.language, Alex.salary)