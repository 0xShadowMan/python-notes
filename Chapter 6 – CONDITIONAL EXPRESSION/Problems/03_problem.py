# Spam messages filter on comments
spam1 = "Make a lot of money"
spam2 = "buy now"
spam3 = "subscribe this"
spam4 = "click this"

comment = input("Enter your comment: ").lower()

if (spam1 in comment) or (spam2 in comment) or (spam3 in comment) or (spam4 in comment):
    print("This is a spam comment.😡")
    print("Please avoid spam comments.🚫")

else:
    print("This is not a spam comment.😊")
    print("Thank you for your feedback.🙏")