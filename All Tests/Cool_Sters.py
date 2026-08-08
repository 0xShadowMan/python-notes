while True:
    # Input number of rows
    n = int(input("Enter a number: "))

    # Print pyramid pattern
    for i in range(1, n+1):
        print(" " * (n - i), end="")      # spaces before stars
        print("*" * (2 * i - 1), end="")  # stars
        print()                           # move to next line

    # Ask user what to do next
    f = input("\n1. Run again\n2. Exit the program\nChoose 1 or 2: ")

    if (f == "1"):  # if user chooses anything other than 1, exit
        print("Exiting program...")
        break
