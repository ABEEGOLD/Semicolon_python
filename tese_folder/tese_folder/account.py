import random

class Account:
    accounts = []

    def create_new_account(self, name, password, phone_number, balance=0.0):
        account_number = random.randint(10000, 60000)

        if account_number not in Account.accounts:
            account = {"account_number": account_number,"name": name, "password": password,"phone_number": phone_number,"balance": balance}
            Account.accounts.append(account)
            return account

    def deposit_fund(self, account_number, amount):
        for account in Account.accounts:
            if account["account_number"] == account_number:
                account["balance"] += amount
                return account
        print("Invalid account number")
        return None

    def withdraw_fund(self, account_number, password, amount):
        for account in Account.accounts:
            if account["account_number"] == account_number and account["password"] == password:
                if account["balance"] >= amount:
                    account["balance"] -= amount
                    return account
                else:
                    print("Insufficient balance")
                    return None
        print("Invalid account details")


    def view_balance(self, account_number, password ):
        for account in Account.accounts:
            if account["account_number"] == account_number and account["password"] == password:
                return account["balance"]
            else:
                print("Incorrect account details")
                return None

    def transfer(self, sender_account_number, receiver_account_number, password, amount):
        for account in Account.accounts:
            if account["account_number"] == sender_account_number and account["password"] == password:
                if account["balance"] >= amount:
                    if sender_account_number in Account.accounts:
                        if account.view_balance(sender_account_number) >= amount:
                            sender_account_number["balance"] -= amount
                            receiver_account_number["balance"] += amount
                            print("Successful transfer")

                            new_balance = sender_account_number["balance"]
                            print("Your new balance is " + new_balance)

                            return account