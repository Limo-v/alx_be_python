class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = 0

    def deposit(self, deposit_amount):
        return  self.account_balance + deposit_amount

    def withdraw(self, withdraw_amount):
        if withdraw_amount <= self.account_balance:
              self.account_balance - withdraw_amount
              return True
        else:
            return False

    def display_balance(self):
        print(f"Your account balance is {self.account_balance}")

