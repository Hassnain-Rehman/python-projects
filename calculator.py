def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main():
    while True:
        x = get_number("What's x? ")
        y = get_number("What's y? ")
        operator = input("Choose +, -, *, or /: ").strip()

        if operator == "+":
            result = x + y
        elif operator == "-":
            result = x - y
        elif operator == "*":
            result = x * y
        elif operator == "/":
            if y == 0:
                print("You cannot divide by zero.")
                continue
            result = x / y
        else:
            print("Invalid operator.")
            continue

        print(f"Result: {result}")

        again = input("Calculate again? (y/n): ").strip().lower()

        if again != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
