class Programers:
    company = "Microsoft"

    def __init__(self, name, department, position):
        self.name = name
        self.department = department
        self.position = position

        print(f"Hi {self.name}, So you are working in {self.department}.\n \t As a {self.position} ")

a = input("Enter your name: ")
b = input("Enter your section: ")
c = input("Enter your position: ")

harry = Programers(a, b, c)
print(Programers.company)
        