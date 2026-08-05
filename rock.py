import random


def main():
    choices = ["rock", "paper", "scissors"]
    player = get_player_choice(choices)
    computer = random.choice(choices)

    print(f"You chose: {player}")
    print(f"Computer chose: {computer}")

    print(get_winner(player, computer))


def get_player_choice(choices):
    while True:
        player = input("Rock, Paper, or Scissors? ").lower()
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


main()