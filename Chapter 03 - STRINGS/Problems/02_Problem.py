name = input("Enter your name: ")

letter = f"Dear {name.capitalize()},\n You are selected! Congratulations!\nin Date: 20/29/2843 "

print(letter)


# Other way to do this is by using replace() 

lr = '''
        Dear <|Name|>,
        You are selected!
        <|Date|>
'''

print(lr.replace("<|Name|>", "Shohan").replace("<|Date|>", "20/29/2843"))
