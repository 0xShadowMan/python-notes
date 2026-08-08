class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"


c1 = Complex(2, 3)
c2 = Complex(1, 4)

print(c1 + c2)   # 3 + 7i
print(c1 * c2)   # -10 + 11i