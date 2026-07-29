accounts = []
class Account:
    def __init__(self, account_holder_name,accno,balance):
        self.account_holder_name = account_holder_name
        self.accno=accno
        self.balance=balance

    def show_details(self):
        print("-"*15)
        print("Name:",self.account_holder_name)
        print("Account No.:",self.accno)
        print("balance:",self.balance)
        print("-"*15)
while True:
    print("===== BANK MANAGEMENT =====")

    print("1. Create Account")
    print("2. View Accounts")
    print("3. Search Account")
    print("4. Deposit Money")
    print("5. Withdraw Money")
    print("6. Delete Account")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")
    if choice == "1":
        hn = input("Enter account holder name: ")
        Ac = int(input("Enter the account number: "))
        b = int(input("Enter the balance: "))
        account = Account(hn,Ac,b)
        accounts.append(account)
    elif choice == "2":
        for account in accounts:
            account.show_details()
    elif choice == "3":
        SA = input("Enter the account name to be searched: ")
        for account in accounts:
            if account.account_holder_name == SA:
                account.show_details()
                break
            else:
                print("Account not Found!")
    elif choice == "4":
        MN = int(input("Enter the amount to be deposited"))
        an = int(input("enter the account Number to be deposite:"))
        for account in accounts:
            if account.accno == an:
                account.balance+=MN
                account.show_details()
    elif choice == "5":
        NM = int(input("Enter the amount to be withdrawed: "))
        A = int(input("enter the account number in which accound you have to withdraw: "))
        for account in accounts:
            if account.accno == A:
                if account.balance >= NM:
                    account.balance-=NM
                    account.show_details()
                    break
                else:
                    print("Insufficient balance!")
                
            
    elif choice == "6":
        d = input("enter the account to ba deleted: ")
        found = False
        for account in accounts :
            if account.account_holder_name == d:
                accounts.remove(account)
                print("Account deleted successfully!")
                found = True
                break
        if found == True:
            print("Invalid Account!")
    elif choice == "7":
        print("Exit...")
        break
    else:
        print("Invalid choice")



