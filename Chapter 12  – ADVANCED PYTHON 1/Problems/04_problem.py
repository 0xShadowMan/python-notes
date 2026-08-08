try:
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    c = a/b
    print("Result:", c)
except Exception as e:
    print("Error:", e)

print("Program continues...")