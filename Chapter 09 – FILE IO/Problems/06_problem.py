found = False
with open("log.txt", "r") as file:
    for line in file:
        if "python" in line.lower():
            found = True
            break

print("Yes, the log file contains 'python'." if found else "No, the log file does not contain 'python'.")