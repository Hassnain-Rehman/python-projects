#Math-Quiz Project..
import random

def get_numbers(difficulty):
    if difficulty == "1":
        return random.randint(1, 15), random.randint(1, 15)
    elif difficulty == "2":
        return random.randint(15, 50), random.randint(15, 50)
    elif difficulty == "3":
        return random.randint(50, 100), random.randint(50, 100)

def get_operation(difficulty):
    if difficulty == "1":
        return random.choice(["+", "-"])
    elif difficulty == "2":
        return random.choice(["+", "-", "*"])
    elif difficulty == "3":
        return random.choice(["+", "-", "*", "/"])

def calculate_answer(num1, num2, operation):
    match operation:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2

def generate_question(difficulty, question_number):
    print(f"question {question_number} of 5")
    num1, num2 = get_numbers(difficulty)
    operation = get_operation(difficulty)

    if operation == "-" and num1 < num2:
        num1, num2 = num2, num1

    if operation == "/":
        num2 = random.randint(1, 10)
        num1 = num2 * random.randint(1, 10)

    answer = calculate_answer(num1, num2, operation)

    while True:
        try:
            user_answer = float(input(f"What is {num1} {operation} {num2}? "))
            break
        except ValueError:
            print("Please enter a number! ")

    if user_answer == answer:
        print("Correct!")
        return True
    else:
        print("Incorrect!")
        print(f"The correct answer was {answer}.")
        return False

def main():
    name = input("What's your name? ")
    print(f"Hello, {name}! Welcome to the Math Quiz. " )

    while True:
        difficulty = choose_difficulty()
        score = 0

        for i in range(5):
            if generate_question(difficulty, i + 1):
                score += 1

        print(f"your score: {score}/5")
        if score ==  5:
            print("Excellent!")
        elif score >= 3:
            print("Good job!")
        else:
            print("Keep practicing!")


        play_again = input("Would you like to play again? (y/n): ").strip().lower()

        while play_again not in ["y", "n"]:
            play_again = input("Please enter y or n: ").strip().lower()


        if play_again == "n":
            print("Thanks for playing!")
            break
        elif play_again == "y":
             continue


def is_valid_difficulty(choice):
    return choice in ["1", "2", "3"]

def choose_difficulty():
    print("1.  Easy")
    print("2.  Medium")
    print("3.  Hard")

    difficulty = input("choose difficulty: ")

    while not is_valid_difficulty (difficulty):
        print("Invalid choice. please choose between 1, 2, or 3.")
        difficulty = input("Choose difficulty: ")

    if difficulty == "1":
        print("Easy Selected")
    elif difficulty == "2":
        print("Medium Selected")
    elif difficulty == "3":
        print("Hard selected")

    return difficulty

if __name__ == "__main__":
    main()

           #<><><>#
           
