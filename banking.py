class BankAccount:
    def __init__(self, account_number, account_holder_name, balance=0.0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self):
        return self.balance

    def __str__(self):
         return f"Account Number: {self.account_number}\nAccount Holder: {self.account_holder_name}\nBalance: ${self.balance}"

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_holder_name, initial_balance=0.0):
         if account_number not in self.accounts:
            self.accounts[account_number] = BankAccount(account_number, account_holder_name, initial_balance)
            print(f"Account {account_number} created successfully.")
         else:
            print(f"Account {account_number} already exists.")

    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            print("Account not found.")
            return None
    
    def remove_account(self,account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print(f"Account {account_number} removed successfully.")
        else:
            print("Account not found.")

# Example Usage
my_bank = Bank()
my_bank.create_account("12345", "Alice Smith", 1000)
my_bank.create_account("12345", "Alice Smith", 1000) #test case for already existing account
account1 = my_bank.get_account("12345")

if account1:
    print(account1)
    account1.deposit(500)
    account1.withdraw(200)
    print(account1)
    account1.withdraw(2000) #test case for insufficient balance
    print("Current balance:", account1.get_balance())
    
my_bank.remove_account("12345")
my_bank.remove_account("12345") #test case for non existing account after removal        







