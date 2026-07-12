class BankAccount:

    def show_balance(self):
        print("Account Holder:", self.holder)
        print("Balance:", self.balance)


bank1 = BankAccount()

bank1.holder = "David"
bank1.balance = 1000

bank1.show_balance()