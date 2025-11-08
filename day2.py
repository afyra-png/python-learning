#expense tracker

expenses = []

while True:
    print("\n1. Add expense")
    print("2. View expenses")
    print("3. Save and exit")
    choice = input("Choose an option (1-3): ")

    if choice == "1":
        name = input ("What did you spend on? > ")
        amount = float(input("How much? > "))
        expenses.append((name, amount))
        print("Expenses added!")

    elif choice == "2":
        if not expenses:
            print("No expenses yet.")
        else:
            for item in expenses:
                print(f"{item[0]} - ${item[1]}")

    elif choice == "3":
        print("Saving and exiting...")
        break
    
    else:
        print("Invalid choice. Try again.")

