class Account:
    #def __init__(self, name, balance):
    def __init__(self,name):
        self.name = name
        self.balance = 0

    def get_name(self):
        return self.name

    def set_balance(self,amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self.balance = amount

    def get_balance(self):
        return self.balance

    def withdraw(self):
        print('Account withdraw')

    def deposit(self, amount):
        self.balance += amount
        #print('Account deposit')



#oba = Account("oba")

oba = Account("oba")
print(oba.get_balance())
oba.set_balance(100)
print(oba.get_balance())
#oba.set_name("oba")
#oba.deposit(1500)
#print(oba.balance)

