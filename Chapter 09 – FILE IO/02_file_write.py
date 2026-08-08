def write_file():
    st = "Alex is a progmer"
    file = open("Chapter 9/myfile.txt", "w")
    file.write(st)
    file.close()


write_file()