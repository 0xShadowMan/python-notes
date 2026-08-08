# Let's Start ;-)

from pathlib import Path

def add_notes():
    install_note = input("Enter your note: ")

    if not Path("notes.txt").exists():
        file = open("notes.txt", "w+")
        file.write(install_note + "\n")
        file.seek(0)
        print("Note added successfully.")
        file.close()
    else:
        file = open("notes.txt", "a+")
        file.write(install_note + "\n")
        file.seek(0)
        print("Note added successfully.")
        file.close()

def show_notes():
    if not Path("notes.txt").exists():
        print("Notes not found — creating a new one...")
        add_notes()
    else:
        with open("notes.txt", "r") as file:
            show = file.read()
            print(("-" * 8), " Notes ", ("-" * 8))
            print(show)

def search_note():
    find_text = input("Enter word to search: ")

    if not Path("notes.txt").exists():
        print("Notes not found — creating a new one...")
        add_notes()
    else:
        with open("notes.txt", "r") as file:
            content = file.read()

        position = content.find(find_text)

        if position != -1:
            print(f"Found at position {position}")
        else:
            print("Not found")

def count_line():

    if not Path("notes.txt").exists():
        print("Notes not found — creating a new one...")
        add_notes()
    else:
        with open("notes.txt", "r") as file:
            lines = file.readlines()

        total_lines = len(lines)
        print(f"Total lines: {total_lines}")


while True:
    print(("="* 8), " Student Notes ", ("="* 8))
    print("")
    print("1. Add a Note")
    print("2. Show All Notes")
    print("3. Search a Note")
    print("4. Count Notes")
    print("5. Exit")
    user_choice = int(input("Enter your choice: "))

    if user_choice == 1:
        add_notes()
    elif(user_choice == 2):
        show_notes()
    elif(user_choice == 3):
        search_note()
    elif (user_choice == 4):
        count_line()
    elif(user_choice == 5):
        print("Thanks for using this program 😊")
        break