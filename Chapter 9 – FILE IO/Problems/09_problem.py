with open("this.txt", "r") as file1:
    content1 = file1.read()

with open("this_copy.txt", "r") as file2:
    content2 = file2.read()

if content1 == content2:
    print("The files are identical.")
else:
    print("The files are different.")