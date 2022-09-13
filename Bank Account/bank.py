class BankAccount:
    def __init__(self, int_rate=0.02, balance=0): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if (self.balance >= amount):
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    # your code here
    def display_account_info(self):
        print("Balance:$" ,self.balance)

    # your code here
    def yield_interest(self):
        if (self.balance>0):
            self.balance=(self.balance*self.int_rate)+self.balance
        return self

Rabab = BankAccount(0.03, 1000) 
Mariam =  BankAccount(0.02, 2000)    
Rabab.deposit(1200).deposit(100).deposit(100).withdraw(100).yield_interest().display_account_info()
Mariam.deposit(1500).deposit(100).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()



