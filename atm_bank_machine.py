print("WELCOME TO PY BANK".center(90))
balance = 5600

while True:
    print("""
    1. Check Balance
    2. Deposit Amount
    3. Withdraw Amount
    4. Exit
    """)

    choice = input("Enter your choice (1-4): ")

    if not choice.isdigit():
        print("Please enter numbers only!")
        continue

    choice = int(choice)

    if choice == 1:
        print(f"Your current balance is: {balance} ₹")

    elif choice == 2:
        amount = input("Enter amount to deposit: ")
        if amount.isdigit() and int(amount) > 0:
            balance += int(amount)
            print(f"Amount deposited successfully. New balance: {balance} ₹")
        else:
            print("Enter a valid amount")

    elif choice == 3:
        amount = input("Enter amount to withdraw: ")
        if amount.isdigit():
            amount = int(amount)
            if amount <= balance:
                balance -= amount
                print(f"Please collect your cash. New balance: {balance} ₹")
            else:
                print("Insufficient balance!")
        else:
            print("Enter a valid amount")

    elif choice == 4:
        print("Thank you for using PY BANK 🙏")
        break

    else:
        print("Invalid option! Please choose between 1-4")
