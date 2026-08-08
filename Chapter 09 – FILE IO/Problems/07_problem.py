with open("log.txt", "r") as file:
    lines = file.readlines()

found = False

for line_number, line in enumerate(lines, start=1):
    if "python" in line.lower():
        print(f"'python' found on line {line_number}: {line.strip()}")
        found = True

if not found:
    print("'python' was not found in the file.")