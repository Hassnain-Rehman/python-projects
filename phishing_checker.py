import re

SUSPICIOUS_WORDS = [
    "urgent",
    "suspended",
    "prize",
    "win",
    "click now",
    "verify your account",
    "bit.ly",
]


def check_message(message):
    """Return the list of suspicious words found in the message."""
    message = message.lower()
    found = []
    for word in SUSPICIOUS_WORDS:
        if re.search(rf"\b{re.escape(word)}\b", message):
            found.append(word)
    return found


def show_result(found):
    """Print the verdict and the reasons."""
    score = len(found)

    if score == 0:
        print("Looks safe.")
    elif score <= 2:
        print("Suspicious. Be careful.")
    else:
        print("Dangerous! This may be a scam.")

    if found:
        print("Reasons:")
        for word in found:
            print(f"- Found suspicious word: '{word}'")


def main():
    message = input("Paste the message: ")
    found = check_message(message)
    show_result(found)


if __name__ == "__main__":
    main()

