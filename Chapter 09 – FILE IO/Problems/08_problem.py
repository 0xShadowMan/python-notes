with open("this.txt", "r") as original:
    content = original.read()

with open("this_copy.txt", "w") as copy:
    copy.write(content)

print("File copied successfully!")