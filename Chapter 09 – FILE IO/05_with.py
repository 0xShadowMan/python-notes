'''
theNote = open("note.txt")

file= theNote.read()
print(file)
theNote.close()
'''
# the same thing can done by with statement

with open("note.txt") as f:
    print(f.read())

# you don't need to close this 

