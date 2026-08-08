# Take marks input
sub1 = int(input("Enter marks of Subject 1: "))
sub2 = int(input("Enter marks of Subject 2: "))
sub3 = int(input("Enter marks of Subject 3: "))

# Calculate total and percentage
total = sub1 + sub2 + sub3
percentage = (total / 300) * 100   # assuming each subject is out of 100

print("\nYour Total Marks:", total)
print("Your Percentage:", percentage, "%")

# Check conditions
if (sub1 >= 33 and sub2 >= 33 and sub3 >= 33) and percentage >= 40:
    print("🎉 Congratulations! You Passed ✅")
else:
    print("❌ Sorry! You Failed.")
