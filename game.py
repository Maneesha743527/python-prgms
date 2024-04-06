import random

class RockPaperScissors:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.user_score = 0
        self.computer_score = 0

    def get_user_choice(self):
        while True:
            user_choice = input("Choose rock, paper, or scissors: ").lower()
            if user_choice in self.choices:
                return user_choice
            else:
                print("Invalid choice. Please try again.")

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            return "You win!"
        else:
            return "You lose!"

    def play_game(self):
        while True:
            print("\n--- Rock, Paper, Scissors ---")
            user_choice = self.get_user_choice()
            computer_choice = self.get_computer_choice()

            print("Your choice:", user_choice)
            print("Computer's choice:", computer_choice)

            result = self.determine_winner(user_choice, computer_choice)
            print(result)

            if result == "You win!":
                self.user_score += 1
            elif result == "You lose!":
                self.computer_score += 1

            print("Your score:", self.user_score)
            print("Computer's score:", self.computer_score)

            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != "yes":
                break

game = RockPaperScissors()
game.play_game()
