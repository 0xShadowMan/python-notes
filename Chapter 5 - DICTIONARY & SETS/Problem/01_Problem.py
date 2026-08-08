# Bangla (written in English letters) to English Dictionary
dictionary = {
    "boi": "Book",
    "kolom": "Pen",
    "kagoj": "Paper",
    "school": "School",
    "shikkhok": "Teacher",
    "chhatro": "Student"
}

print("Welcome to the Bangla-English Dictionary!")
print("Available words:", list(dictionary.keys()))

# user input
word = input("Enter a Bangla word (in English letters): ").lower()

print(dictionary[word])

# Use this to avoid error if word not found
print("The English translation is:", dictionary.get(word, "Word not found in dictionary."))
