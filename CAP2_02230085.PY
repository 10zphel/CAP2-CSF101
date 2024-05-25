################################
# Your Name: Tenzin Chophel
# Your Section: 1 Electrical
# Your Student ID Number: 02230085
################################
# REFERENCES
# Links that you referred while solving
# the problem
# http://link.to.an.article/video.com
################################
# SOLUTION
# Withdrawal successful. New balance: 3200000
# Personal Account Balance after transfer: 2600000
################################

import random

# Define the base class for a bank account
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number  # Unique account number
        self.balance = balance  # Current balance

    def deposit(self, amount):
        self.balance += amount  # Add deposited amount to balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount  # Subtract withdrawn amount from balance
            return True
        else:
            print("Insufficient funds.")
            return False

# Define subclasses for personal and business accounts
class PersonalAccount(BankAccount):
    def __init__(self, account_number, balance=0):
        super().__init__(account_number, balance)
        self.account_type = 'Personal'  # Mark account as personal type

class BusinessAccount(BankAccount):
    def __init__(self, account_number, balance=0):
        super().__init__(account_number, balance)
        self.account_type = 'Business'  # Mark account as business type

# Define the bank class to manage accounts and transactions
class Bank:
    def __init__(self):
        self.accounts = {}  # Dictionary to store accounts

    def create_account(self, account_type):
        account_number = random.randint(10000000, 99999999)  # Generate random account number
        if account_type.lower() == 'personal':
            account = PersonalAccount(account_number)  # Create personal account
        elif account_type.lower() == 'business':
            account = BusinessAccount(account_number)  # Create business account
        self.accounts[account_number] = account  # Add account to dictionary
        return account_number

    def login(self, account_number):
        return self.accounts.get(account_number)  # Return account object if found

    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]  # Delete account if found
            print("Account deleted successfully.")
        else:
            print("Account not found.")

    def transfer_money(self, sender_account_number, receiver_account_number, amount):
        sender_account = self.accounts.get(sender_account_number)  # Get sender account object
        receiver_account = self.accounts.get(receiver_account_number)  # Get receiver account object
        if sender_account and receiver_account:
            if sender_account.withdraw(amount):  # Withdraw from sender's account
                receiver_account.deposit(amount)  # Deposit into receiver's account
                print("Money transferred successfully.")
        else:
            print("Sender or receiver account not found.")

# Main function to test the application
def main():
    bank = Bank()  # Create bank object

    # Create a personal account
    personal_account_number = bank.create_account("personal")
    print("Personal Account Created. Account Number:", personal_account_number)

    # Login to the personal account
    account = bank.login(personal_account_number)
    if account:
        print("Logged in as Personal Account:", account.account_number)
        # Deposit money
        account.deposit(4000000)
        print("Deposit successful. New balance:", account.balance)
        # Withdraw money
        account.withdraw(800000)
        print("Withdrawal successful. New balance:", account.balance)

    # Create a business account
    business_account_number = bank.create_account("business")
    print("Business Account Created. Account Number:", business_account_number)

    # Transfer money from personal account to business account
    bank.transfer_money(personal_account_number, business_account_number, 600000)
    print("Personal Account Balance after transfer:", bank.login(personal_account_number).balance)
    print("Business Account Balance after transfer:", bank.login(business_account_number).balance)

    # Delete personal account
    bank.delete_account(personal_account_number)

main()
