'''
concepts:
i have 3 choices 1>snake 2>water 3>gun 
so when user inputs a choice, computer also chooses a random one using random module
if user == computer = draw, snake beats water, water beats gun, gun beats snake
'''
import random

options = ["s", "w", "g"]

names = {
    "s": "Snake",
    "w": "Water",
    "g": "Gun"
}
# WELCOME 
print("=" * 45)
print("      🐍 SNAKE • 💧 WATER • 🔫 GUN")
print("=" * 45)
print()
print("[s] 🐍 Snake")
print("[w] 💧 Water")
print("[g] 🔫 Gun")
print("Type 'q' anytime to quit.")
print("=" * 45)


def game(user_input, round_num):
    
    print(f"✅ Round {round_num}")
    computer = random.choice(options)
    # Normal variables 
    toked = f"You Chose [{names[user_input]}] and Computer Chose [{names[computer]}]"

    # CONDITIONS VARIABLES START
    draw = (user_input == computer)
    win = (
        (user_input == "s" and computer == "w") or
        (user_input == "w" and computer == "g") or
        (user_input == "g" and computer == "s")
    )
    lose = not draw and not win

    # CONDITIONS START
    if draw:
        print(toked)
        print("🤝 It's a Draw!")
        return "draw"

    elif win:
        print(toked)
        print("🎉 Congratulations! You Win!")
        return "win"

    elif lose:
        print(toked)
        print("🤖 Computer Wins! Better luck next round.")
        return "lose"


round_num = 0
user_win = 0
computer_win = 0
draw_count = 0


while True:
    user_input = input("Choose your weapon(q to quit): ").lower()
    print()

    # END THE GAME
    if user_input == "q":
        print("=" * 30)
        print("         GAME OVER       ")
        print("=" * 30)
        print(f"Rounds Played : {round_num}")
        print(f"You Won     : {user_win}")
        print(f"Computer Won: {computer_win}")
        print(f"Draws       : {draw_count}")
        print("")
        if user_win > computer_win:
                print("🏆 Final Winner: YOU!")
        else:
            print("🏆 Final Winner: Computer!")
        print("=" * 30)
        print("")
        break

    if user_input not in options:
        print("INVALID Choice!")
        continue

    # CHECKING WINS 
    round_num += 1
    result = game(user_input, round_num)

    if result == "win":
        user_win += 1
    elif result == "lose":
        computer_win += 1
    elif result == "draw":
        draw_count += 1

    print()

