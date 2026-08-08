# Spam messages filter on comments 

# List of spam keywords
spam_keywords = [
    "make a lot of money",
    "buy now",
    "subscribe this",
    "click this",
    "watch this video",
    "free gift",
    "visit my profile",
    "earn money fast",
    "limited offer",
    "win a prize",
    "check this out",
    "get rich quick",
    "exclusive deal",
    "follow me",
    "cheap price"
]

# Take user comment (convert to lowercase for case-insensitive check)
comment = input("Enter your comment: ").lower()

# Collect all matched spam words
found_spam = [spam for spam in spam_keywords if spam in comment]

# Check if any spam keyword is in the comment
if found_spam:
    print("⚠️ This is a spam comment.🚫")
    print("Detected spam keywords:", ", ".join(found_spam))
else:
    print("✅ This is not a spam comment.😊")
    print("Thank you for your feedback.🙏")

input("Press... Enter to exit")