list_of_name = ["Alice", "Bob", "Charlie", "David", "Eve"]

username = input("Enter your username: ").capitalize()

if " " in username:
    print("Username cannot contain spaces. 😡")
    print("Please enter a username without spaces. 🚫")

elif len(username) >= 10:
    print("Username is invalid. 😡")
    print("Please enter a username with less than 10 characters. 🚫")

elif username in list_of_name:
    print("Username is not available. 😡")

else:
    print("Username is valid. 😊")