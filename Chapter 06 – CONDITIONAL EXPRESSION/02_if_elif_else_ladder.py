# If-elif-else ladder example: Age verification for website access

age = int(input("Enter your age: "))

if age >= 18 and age <= 100:
    print("You are allowed to enter the site. 😊")
    print("Welcome to the site!")

elif age < 0:
    print("Age cannot be negative. Please enter a valid age. 😡")

elif age == 0:
    print("You are just born! 😲")
    print("Please come back when you are a bit older.")

elif age > 100:
    print("Age seems unrealistic. Please enter a valid age. 😳")

else:
    print("You are not allowed to enter the site. 😕")
    print("Try again when you are 18 or older.")

print()
print("Thank you for visiting! 😊")