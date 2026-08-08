'''4. A file contains a word “Donkey” multiple times. You need to write a program
which replace this word with ##### by updating the same file. '''

word = "Donkey"

with open("pass.txt", "r") as file:
    content = file.read()

if word in content:
    content = content.replace(word, "#" * len(word))

    with open("pass.txt", "w") as file:
        file.write(content)

    print("Updated the file...")