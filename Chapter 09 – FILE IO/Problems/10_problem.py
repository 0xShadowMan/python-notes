with open("this.txt", "w") as file:
    pass  # opening in "w" mode alone already erases the content
    file.write("") # also this way we can do that

print("File content wiped out!")