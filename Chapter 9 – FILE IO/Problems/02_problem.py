def game():
    # Placeholder: replace with actual game logic
    # Must return the score as an integer
    score = int(input("Enter your score: "))
    return score


def get_high_score():
    with open("Hi-score.txt", "r") as file:
        content = file.read().strip()

    if content == "":
        return 0  # file is blank, so no high score yet
    else:
        return int(content)


def update_high_score(new_score):
    with open("Hi-score.txt", "w") as file:
        file.write(str(new_score))


# Main program
current_high_score = get_high_score()
score = game()

if score > current_high_score:
    update_high_score(score)
    print(f"🎉 New High Score! {score} beats the old record of {current_high_score}!")
else:
    print(f"Your score: {score}. High score remains: {current_high_score}")