def main():
    camel = input("camel case: ")
    print(snake_case(camel))


def snake_case(camel):
    snake = ""
    for letter in camel:
        if letter.isupper():
            snake += "_" + letter.lower()
        else:
            snake += letter
    return snake


main()