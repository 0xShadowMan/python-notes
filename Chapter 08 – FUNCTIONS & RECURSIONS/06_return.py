# -- Return --

def add(a, b):
    return a + b  
    # 'return' sends the value back, doesn't print or store it on its own

# add(3, 5)  
# runs, returns 8, but nothing catches it — value is lost.

result = add(3, 5)  
# now 8 is stored inside "result"

print(result)  
# prints what's inside result → 8

print(add(3, 5))  
# same idea, just shorter — no separate variable needed

