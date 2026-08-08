# That is a example use of a function

# Function Definition


def about_me():
    print("I am a Programmer 👨‍💻")
    print("I practice Python programming 🐍")
    print("I am 14 years old 👦")
    print("I am a student of CSE Department🎓")


def avg():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = int(input("Enter a number: "))
    avg =(a + b + c) /3
    print(f"The average is: {avg}")




while True:
    print("\n===== Welcome to My Program =====")
    print("1. About me\n2. Average\n3. Exit")

    a = (int(input("Enter your Choice: ")))

    if (a == 1):
        about_me() # This is calling of functions

    elif (a == 2):
        avg()

    elif(a==3):
        print("Good Bye")

    else:
        print("Invalid choice")
