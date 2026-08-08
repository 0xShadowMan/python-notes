class Demo:
    a = 4 # Class attribute shared by all objects unless an object creates its own copy.

o = Demo()
print(o.a)
o.a = 0
print(o.a)