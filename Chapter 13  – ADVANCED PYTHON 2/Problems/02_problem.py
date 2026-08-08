name = input("Enter your name: ")
phone_number = input("Enter your phone number: ")

try:
    marks = int(input("Enter your marks: "))
    print("hi {0}, \n\t Your marks are {1}\n and your phone number is {2}".format(name, marks, phone_number))

except ValueError as e:
    print("Error:", e)