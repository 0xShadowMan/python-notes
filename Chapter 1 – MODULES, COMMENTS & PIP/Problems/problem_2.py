import os

file_content = "This is a test file. And i am the shadow king"

listdir = os.listdir()

create_file = open("test.txt", "w")

create_file.write(file_content)

create_file.close()



print(listdir)
