import os

with open("old.txt", "r") as original:
    content = original.read()

with open("renamed_by_python.txt", "w") as new_file:
    new_file.write(content)

os.remove("old.txt")

print("File renamed successfully! (old.txt removed)")