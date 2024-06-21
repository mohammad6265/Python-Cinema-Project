class BankAccount:
    def __init__(self, account_number, balance, cvv2, password):
        self.account_number = account_number
        self.balance = balance
        self.cvv2 = cvv2
        self.password = password
        self.min_balance = 100  # Minimum balance requirement

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
            print(f'Amount {amount} withdrawn successfully.')
        else:
            print('Insufficient balance.')

    def deposit(self, amount):
        self.balance += amount
        print(f'Amount {amount} deposited successfully.')

    def transfer(self, amount, recipient):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
            recipient.balance += amount
            print(f'Amount {amount} transferred successfully to account {recipient.account_number}.')
        else:
            print('Insufficient balance for transfer.')





# Usage example
user_account = BankAccount('123456789', 500, '123', 'password123')
recipient_account = BankAccount('987654321', 1000, '456', 'securepwd')

recharge_amount = 200
recharge_wallet(user_account, user_account, recharge_amount)
