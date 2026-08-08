from pathlib import Path

# Folder where all the table files will be saved
folder_name = "Multiplication_Tables"

# Create the folder if it doesn't already exist
Path(folder_name).mkdir(exist_ok=True)

# Generate tables from 2 to 20
for number in range(2, 21):
    filename = f"{folder_name}/table_of_{number}.txt"

    with open(filename, "w") as file:
        file.write(f"Multiplication Table of {number}\n")
        file.write("=" * 30 + "\n")

        for i in range(1, 11):
            result = number * i
            file.write(f"{number} x {i:2} = {result}\n")

    print(f"✅ Created: {filename}")

print("\nAll multiplication tables have been generated!")