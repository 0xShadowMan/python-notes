a = 89 # this is a global variable

def fun(): 
    global a # this will change the value of global variable a
    a = 3
    print(a)


fun()
print(a)