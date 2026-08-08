def find_greatest():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    num3 = int(input("Enter a number: "))

    if num1 > num2 and num1 > num3:
        print(f"num1 is the Greatest Number {num1}")
    elif num2 > num1 and num2 > num3:
        print(f"num2 is the Greatest Number {num2}")
    elif num3 > num1 and num3 > num2:
        print(f"num3 is the Greatest Number {num3}")
    else:
        print("You entered same number multiple times")

find_greatest()