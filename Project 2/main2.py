import random
import os

class Game:
    def __init__(self):
        self.round = 0
        self.score_file = "best_score.txt"

    def guess_num(self):
        self.round = 0
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
                self.update_best_score(self.round)
                break

    def get_best_score(self):
        if os.path.exists(self.score_file):
            with open(self.score_file, "r") as f:
                content = f.read().strip()
                return int(content) if content else None
        return None

    def update_best_score(self, attempts):
        best = self.get_best_score()
        if best is None or attempts < best:
            with open(self.score_file, "w") as f:
                f.write(str(attempts))
            print(f"🏆 New best score: {attempts} attempts!")

    def show_best_score(self):
        best = self.get_best_score()
        if best is None:
            print("📭 No best score yet. Play a game first!")
        else:
            print(f"🏆 Best score: {best} attempts")

    def reset_best_score(self):
        if os.path.exists(self.score_file):
            os.remove(self.score_file)
            print("🔄 Best score has been reset.")
        else:
            print("📭 No best score to reset.")

    def menu(self):
        while True:
            print("\n===== 🎯 Perfect Guess =====")
            print("1. Play Game")
            print("2. Show Best Score")
            print("3. Reset Best Score")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                self.guess_num()
            elif choice == "2":
                self.show_best_score()
            elif choice == "3":
                self.reset_best_score()
            elif choice == "4":
                print("👋 Thanks for playing!")
                break
            else:
                print("❌ Invalid choice, try again.")


theGame = Game()
theGame.menu()

