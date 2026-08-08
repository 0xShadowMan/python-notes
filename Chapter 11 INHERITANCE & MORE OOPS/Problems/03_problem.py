
class Employee:
    def __init__(self, salary, increment):
        self.salary = salary
        self.increment = increment

    @property
    def salaryAfterIncrement(self):
        return self.salary + (self.salary * self.increment)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_increment):
        self.increment = new_increment

e = Employee(10000, 0.2)
print(e.salaryAfterIncrement)
