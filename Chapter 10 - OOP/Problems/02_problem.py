class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        print("The square is:", self.number ** 2)

    def cube(self):
        print("The cube is:", self.number ** 3)

    def square_root(self):
       print("The square root is:", self.number ** 0.5)

num = int(input("Enter a number: "))

calc = Calculator(num)
calc.square()
calc.cube()
calc.square_root()

