'''
Like the print() function, we can pass extra values inside the parentheses,
such as print("Hello").

These extra values are called Arguments.
Arguments provide information to a function so it can do its job.
'''

Developers = ["Harry", "Shadow", "Alex", "TheMan", "Bob"]
Ids = [122, 112, 22, 11, 5554]


def goodDay(name, user_id):
    # name and user_id are Parameters
    print(f"Good Day! {name}")
    print(f"Your ID is {user_id}")
    print("You are a Senior Developer in Section B")

while True:
    # Get input from the user
    a = input("Enter your name: ").capitalize()
    b = int(input("Enter your ID: "))

    # Check if the name and ID belong to the same person
    if a in Developers:
        index = Developers.index(a)      # Find the position of the name

        if Ids[index] == b:
            goodDay(a, b)                # Pass arguments to the function
        else:
            print("❌ Wrong ID!")
    else:
        print("❌ Name not found!")
