expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        item = input("Expense name: ")
        amount = float(input("Amount: "))
        expenses.append((item, amount))
        print("Expense Added!")

    elif choice == "2":
        for item, amount in expenses:
            print(item, "-", amount)

    elif choice == "3":
        break
