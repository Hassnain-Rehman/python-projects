import secrets
import string

def check_strength(password):
    has_digit = any(character.isdigit() for character in password)
    has_symbol = any(character in string.punctuation for character in password)

    if len(password) >= 12 and has_digit and has_symbol:
        return "Strong"
    elif len(password) >= 8:
        return "Medium"
    else:
        return "Weak"

def main():
    while True:
        length = get_length()
        use_digits = get_yes_no("Include numbers? (y/n): ")
        use_symbols = get_yes_no("Include symbols? (y/n): ")

        password = generate_password(length, use_digits, use_symbols)

        if password:
            print(f"Your password: {password}")
            print(f"Password strength: {check_strength(password)}")

        again = get_yes_no("Generate another password? (y/n): ")

        if not again:
            print("okay!")
            break

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
        answer = input(prompt).strip().lower()
        if answer in ["y", "yes"]:
            return True
        elif answer in ["n", "no"]:
            return False
        print("Please answer y or n.")


def generate_password(length, use_digits, use_symbols):
    characters = string.ascii_letters
    password_parts = [secrets.choice(string.ascii_letters)]

    if use_digits:
        characters += string.digits
        password_parts.append(secrets.choice(string.digits))

    if use_symbols:
        characters += string.punctuation
        password_parts.append(secrets.choice(string.punctuation))

    if length < len(password_parts):
        print("Password length is too short for your selected options.")
        return None

    for _ in range(length - len(password_parts)):
        password_parts.append(secrets.choice(characters))

    secrets.SystemRandom().shuffle(password_parts)
    return "".join(password_parts)


if __name__ == "__main__":
    main()
