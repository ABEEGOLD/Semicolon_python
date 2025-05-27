import account

account_account = account.Account() 

def menu():
    print("""
        What can I help you with today?
        1 -> Create an account
        2 -> Deposit money
        3 -> Withdraw money
        4 -> View balance
        5 -> Transfer funds
        6 -> Exit
    """)

    users_input = int(input("Enter your choice: "))

    match users_input:
        case 1:
            print("CREATE ACCOUNT")
            name = input("What is your name? ")
            password = input("What is your password? ")
            phone_number = input("What is your phone number? ")
            new_account = account_account.create_new_account(name, password, phone_number, balance=0.00)
            if new_account:
                print(f"Your account has been created. Your account number is: {new_account['account_number']}")

            return menu()

        case 2:
            print("DEPOSIT MONEY")
            try:
                acc_num = int(input("Enter your account number: "))
                amount = float(input("Enter amount to deposit: "))
                result = account_account.deposit_fund(acc_num, amount)
                if result:
                    print("Deposit successful. New balance:", result["balance"])
            except ValueError:
                print("Invalid input. Try again.")

            return menu()

        case 3:
            print("WITHDRAW MONEY")
            try:
                acc_num = int(input("Enter your account number: "))
                password = input("Enter your password: ")
                amount = float(input("Enter amount to withdraw: "))
                result = account_account.withdraw_fund(acc_num, password, amount)
                if result:
                    print("Withdrawal successful. New balance:", result["balance"])
            except ValueError:
                print("Invalid input. Try again.")

            return menu()


        case 4:
            print("VIEW BALANCE")
            try:
                acc_num = int(input("Enter your account number: "))
                password = input("Enter your password: ")
                balance = account_account.view_balance(acc_num, password)
                if balance is not None:
                    print("Your current balance is:", balance)
            except ValueError:
                print("Invalid input. Try again.")

            return menu()


        case 5:
            print("TRANSFER FUNDS")
            try:
                sender = int(input("Enter your account number: "))
                password = input("Enter your password: ")
                receiver = int(input("Enter receiver's account number: "))
                amount = float(input("Enter amount to transfer: "))
                result = account_account.transfer(sender, receiver, password, amount)
                if result:
                    print("Transfer complete. Your new balance is:", result["balance"])
            except ValueError:
                print("Invalid input. Try again.")

            return menu()


        case 6:
            print("Thank you for banking with us. Goodbye!")
            exit()

        case _:
            print("Invalid choice. Please select a number from 1 to 6.")
            return menu()


name = input("What is your name? ")
print("Welcome to my bank, " + name + "!")
menu()