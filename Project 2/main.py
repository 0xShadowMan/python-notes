import random

# import main2
# main2.Game()

class Game:
    def __init__(self):
        self.round = 0
    def guess_num(self):
        computer = random.randint(1, 100)
        print(("="*4), " 🎯 The Perfect Guess 🎯 ", ("="*4))
        while True:
            user_input = int(input("Guess the secret number: "))
            self.round += 1
            if computer > user_input:
                print("⬆️ Higher number please!")
            elif computer < user_input:
                print("⬇️ Lower number please!")
            else:
                print("🎉 Congratulations! \nYou guessed the correct number.")
                print(f"✅ You guessed the number in {self.round} attempts.")
                break

theGame = Game()
theGame.guess_num()

