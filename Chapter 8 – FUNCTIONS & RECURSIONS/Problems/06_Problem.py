# Write a python function which converts inches to cms. 

def inches_to_cms(inches):
    return inches * 2.54

n = int(input("Enter a number: "))
print(f"{n} inches is equal to {inches_to_cms(n)} cms")