class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount
    
    def withdraw(self, amount):
        self.account_balance -= amount
    
    def display_balance(self):
        return print(f"Current Balance: ${self.account_balance}")