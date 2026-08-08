# Write a python function to print multiplication table of a given number.

def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n*i}")

num = int(input("Enter a number: "))

multiplication_table(num)