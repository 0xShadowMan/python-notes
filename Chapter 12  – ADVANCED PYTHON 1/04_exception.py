try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except ValueError as v:
    print("Heyyyy")
    print(v)
    
except Exception as e: # this will catch all the errors and exceptions
    print(e) 

print("Thank You")