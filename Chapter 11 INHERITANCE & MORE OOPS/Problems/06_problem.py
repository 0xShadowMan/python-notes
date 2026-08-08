class Vector:
    def __init__(self, *components):
        self.components = components

    def __add__(self, other):
        return Vector(*(a + b for a, b in zip(self.components, other.components)))

    def __mul__(self, other):
        return sum(a * b for a, b in zip(self.components, other.components))

    def __str__(self):
        units = ['i', 'j', 'k']
        return " + ".join(f"{val}{unit}" for val, unit in zip(self.components, units))


v = Vector(7, 8, 10)
print(v)   # 7i + 8j + 10k