# a = input("Enter your 1st marks:")

# b = input("Enter your 2d marks:")

# This will concatenate the inputs as strings so this is wrong
# print("Your total marks is:", a + b) 

# So we need to convert them to integers so do tow ways


# Way 1: Use the int() in the input itself
a = int(input("Enter your 1st marks: "))
b = int(input("Enter your 2d marks: "))

print("Your total marks is:", a + b)


# --------------------------------------------------
# Way 2: Convert while using
# print("Your total marks is:", int(a) + int(b))

# Also we can convert to float, boll, etc if needed 
# print("Your total marks is:", float(a) + float(b))
# print("Your total marks is:", bool(a) + bool(b))
# --------------------------------------------------

# ---------------------------
# Way 3:  Convert while taking input
# a = int(a)
# b = int(b)

# print("Your total marks is:", a + b) 

# ---------------------------
