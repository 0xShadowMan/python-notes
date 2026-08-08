# Basic usage of operators in Python

# Arithmetic Operators
a = 10
b = 3
c = (a + b) 
# print(c)

print("Addition:", a + b)        # 13
print("Subtraction:", a - b)     # 7
print("Multiplication:", a * b)  # 30
print("Division:", a / b)        # 3.333...
print("Floor Division:", a // b) # 3
print("Modulus:", a % b)         # 1
print("Exponent:", a ** b)       # 1000

# Comparison Operators
print("Equal:", a == b)          # False
print("Not Equal:", a != b)      # True
print("Greater Than:", a > b)    # True
print("Less Than:", a < b)       # False
print("Greater or Equal:", a >= b) # True
print("Less or Equal:", a <= b)    # False

# Logical Operators
x = True
y = False

print("AND:", x and y)           # False
print("OR:", x or y)             # True
print("NOT:", not x)             # False

# Assignment Operators
c = 5
c += 2   # c = c + 2
print("c after += 2:", c)        # 7
c *= 3   # c = c * 3
print("c after *= 3:", c)        # 21

# Bitwise Operators
d = 6    # 0b110
e = 2    # 0b010

print("Bitwise AND:", d & e)     # 2
print("Bitwise OR:", d | e)      # 6
print("Bitwise XOR:", d ^ e)     # 4
print("Bitwise NOT:", ~d)        # -7
print("Left Shift:", d << 1)     # 12
print("Right Shift:", d >> 1)    # 3