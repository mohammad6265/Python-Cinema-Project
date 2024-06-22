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


b1 = BankAccount("123", "3000", "622", "62659393")
print(b1.account_number)
