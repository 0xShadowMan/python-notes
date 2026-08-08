list = ["Alice", "Bob", "Charlie", "David"]

name = input("Enter your name: ").capitalize()

if (name in list):
    print(f"Hello, {name} ! Welcome back.")
else:
    print(f"Sorry, {name} you are not registered.")