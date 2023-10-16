class BankAccount:
    
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} has been deposited and the new balance is {self.balance}")

    def withdraw(self, amount):
        if (amount <= self.balance):
            self.balance -= amount
            print(f"{amount} has been withdrawn and the new balance is {self.balance}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance

    def display_account_info(self):
        print(f"The account holder is {self.account_holder} and the account balance is {self.balance}")
