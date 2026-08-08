''' 1. Write a program to read the text from a given file poems.txt and find out
 whether it contains the word twinkle.'''

found = False
with open("poems.txt", "r") as file:
    f = file.read()
    if("twinkle" in f):
        print("Found! twinkle")
    else:
        "Not found."

