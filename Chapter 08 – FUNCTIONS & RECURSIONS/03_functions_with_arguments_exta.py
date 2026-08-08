'''
like print function, we can use an extra things like print("text"). so that is an extra thing 
to use the function properly that is call Arguments.
'''



def goodDay(name, user_id):    # Define a function named goodDay that takes one parameter called name.
    print(f"Good Day! {name}")  # Print "Good Day!" followed by the valuable of name.
    print(f"Your id is {user_id}")
    print("You are an Senior Developer in section B")

a = input("Enter you name: ")  # Call the function and pass "Shadow" as the argument in name valuable.


b = int(input("Enter your ID: "))

goodDay(a , b)