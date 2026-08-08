# Example of using functions in Python
# 1. Define functions
# 2. Call functions through a menu system

# 1st function
def about_me():
    print("\n--- About Me ---")
    print("I am a Programmer 👨‍💻")
    print("I practice Python programming 🐍")
    print("I am 14 years old 👦")
    print("I am a student of CSE Department 🎓")
    print("-----------------\n")

# 2nd function
def avg():
    print("\n--- Average Calculator ---")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    result = (a + b + c) / 3
    print("Average is", result, "\n")

# 3rd function
def ster():
    print("\n--- Star Pattern ---")
    n = int(input("Enter number of rows: "))

    for i in range(1, n+1):
        print(" " * (n - i), end="")      # spaces before stars
        print("*" * (2 * i - 1))          # stars

    print("----------------------\n")

# 4th function
def exit_program():
    print("\nExiting program... Goodbye! 👋\n")

# main program loop
while True:
    print("Welcome to my program :)")
    print("1. About me\n2. Average\n3. Star Pattern\n4. Exit") 

    choice = int(input("Enter your choice: "))

    # use the function in condition
    if choice == 1:
        about_me()
    elif choice == 2:
        avg()
    elif choice == 3:
        ster()
    elif choice == 4:
        exit_program()
        break
    else:
        print("Invalid choice! Please try again.\n")
