def coke():
    total = 0
    amount_due = 50

    while total < amount_due:
        print(f"Amount Due: {amount_due - total}")
        coin = int(input("Insert Coin: "))

        if coin in [25, 10, 5]:
            total += coin

    print(f"Change Owed: {total - amount_due}")


coke()