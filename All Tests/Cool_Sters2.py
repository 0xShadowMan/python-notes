while True:
    n = int(input("Enter a number for the pattern: "))

    for i in range(1, n+1):
        print(" " * (n - i), end="")      # spaces before stars
        print("*" * (2 * i - 1), end="")  # stars
        print()                           # move to next line

    # Ask user if they want to run again
    choice = input("Do you want to run again? (y/n): ").lower()
    if choice != "y":
        print("Exiting program...")
        break
