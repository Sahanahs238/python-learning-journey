balance = 0
print("===== BANK ACCOUNT =====")

print("1. Deposit")
print("2. Withdraw")
print("3. Check Balance")
print("4. Exit")

class BankAccount:
        def __init__(self):
            self.balance=0

        def deposit(self,amount):
            self.balance+=amount

        def withdraw(self,amount):
            if self.balance >= amount:
                self.balance -= amount
                print(self.balance)
            else:
                print("Insufficient balance")
        def Check_Balance(self):
            print("the balance is:")
            print(self.balance)

account = BankAccount()
account.deposit(400)
print(account.balance)
while True:
    choice = input("enter your choice (1,2,3,4): ")
    if choice == "1":
        amount = int(input("enter the amount to be deposited: "))
        account.deposit(amount)

    elif choice == "2":
        amt = int(input("enter the amount to be withdrawed: "))
        account.withdraw(amt)

    elif choice == "3":
        print("your balance is")
        print(account.balance)

    elif choice == "4":
        print("Exit")
        break
    else:
        print("Invalid choice")
     