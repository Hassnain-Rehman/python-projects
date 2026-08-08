import random
import string


def main():
    length = get_length()
    use_digits = get_yes_no("Include numbers? (y/n): ")
    use_symbols = get_yes_no("Include symbols? (y/n): ")

    password = generate_password(length, use_digits, use_symbols)
    print(f"Your password: {password}")


def get_length():
    while True:
        try:
            length = int(input("Password length: "))
            if length > 0:
                return length
            print("Length must be a positive number.")
        except ValueError:
            print("Please enter a valid number.")


def get_yes_no(prompt):
    while True:
        answer = input(prompt).lower()
        if answer in ["y", "yes"]:
            return True
        elif answer in ["n", "no"]:
            return False
        print("Please answer y or n.")


def generate_password(length, use_digits, use_symbols):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = "".join(random.choice(characters) for _ in range(length))
    return password


main()