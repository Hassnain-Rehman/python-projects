import random


def main():
    choices = ["rock", "paper", "scissors"]

    while True:
        player = get_player_choice(choices)
        computer = random.choice(choices)

        print(f"You chose: {player}")
        print(f"Computer chose: {computer}")
        print(get_winner(player, computer))

        again = input("Play again? (y/n): ").strip().lower()

        if again != "y":
            print("Thanks for playing!")
            break


def get_player_choice(choices):
    while True:
        player = input("Rock, Paper, or Scissors? ").strip().lower()
        if player in choices:
            return player
        print("Please choose rock, paper, or scissors.")


def get_winner(player, computer):
    if player == computer:
        return "It's a tie!"

    beats = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    if beats[player] == computer:
        return "You win!"
    else:
        return "Computer wins!"


if __name__ == "__main__":
    main()

#<<<>>>
