from datetime import datetime


class UserWallet:
    def __init__(self, bank_account):
        self.bank_account = bank_account
        self.wallet = 0
        self.membership = 'Bronze'
        self.free_transactions = 3
        self.free_energy_drink = False
        self.energy_drink_expiry_date = None

    def charge_wallet(self, amount):
        self.wallet += amount

    def buy_membership(self, membership_type):
        if membership_type == 'Silver':
            self.membership = 'Silver'
            self.wallet -= 100  # Assuming the cost of Silver membership is 100
        elif membership_type == 'Gold':
            self.membership = 'Gold'
            self.wallet -= 200  # Assuming the cost of Gold membership is 200

    def purchase(self, item_price, membership_discount=0):
        if self.membership == 'Silver':
            membership_discount = 0.2
        elif self.membership == 'Gold':
            membership_discount = 0.3

        discounted_price = item_price - (item_price * membership_discount)
        if self.free_transactions > 0:
            self.free_transactions -= 1
            self.wallet += discounted_price * 0.2  # Refund 20% of transaction amount
            print(f'Purchase successful. Refund: {discounted_price * 0.2}. Remaining balance: {self.wallet}')
        elif self.wallet >= discounted_price:
            self.wallet -= discounted_price
            print(f'Purchase successful. Remaining balance: {self.wallet}')
        else:
            print('Insufficient funds')

    def buy_energy_drink(self, discounted_price):
        if self.membership == 'Gold' and not self.free_energy_drink:
            self.free_energy_drink = True
            self.wallet += discounted_price * 0.5  # Add 50% of transaction amount to wallet
            self.energy_drink_expiry_date = datetime.now() + datetime.timedelta(days=30)
            """ Set expiry date to 30 days from now"""
            print(
                f'Energy drink added to wallet. Expires on: {self.energy_drink_expiry_date.strftime("%Y-%m-%d")}. Remaining balance: {self.wallet}')
        else:
            print('You do not have access to this feature')

    def use_energy_drink(self):
        if self.free_energy_drink and self.energy_drink_expiry_date > datetime.datetime.now():
            self.free_energy_drink = False
            print('Energy drink used. You can now buy another one')
        else:
            print('You do not have access to this feature or the energy drink has expired')

