censor_words = ["Donkey", "Silly", "Fool"]  # add whatever words you want censored

with open("pass.txt", "r") as file:
    content = file.read()

for word in censor_words:
    if word in content:
        content = content.replace(word, "#" * len(word))

with open("pass.txt", "w") as file:
    file.write(content)

print("Censoring complete!")