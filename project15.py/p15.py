customers = []
class Customer:
    def __init__(self,cname,mobile_no,recharge_plan,validity):
        self.cname=cname
        self.mobile_no=mobile_no
        self.recharge_plan=recharge_plan
        self.validity=validity
    def show_details(self):
        print("-"*15)
        print("Customer Name:",self.cname)
        print("Mobile Number:",self.mobile_no)
        print("Recharge Plan:",self.recharge_plan)
        print("Validity:",self.validity)
        print("-"*15)
        print(" "*15)
while True:
    print("===== MOBILE RECHARGE MANAGEMENT =====")

    print("1. Add Customer")
    print("2. View Customers")
    print("3. Search Customer")
    print("4. Update Recharge Plan")
    print("5. Calculate Recharge Cost")
    print("6. Delete Customer")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ")
    if choice == "1":
        cn = input("Enter customer name:")
        mb = int(input("Enter mobile number: "))
        rp = input("Enter Recharge plan (Basic/Standard/Premium): ")
        v = int(input("Enter validity: "))
        if rp=="Basic" or rp=="Standard" or rp =="Premium":
            customer = Customer(cn,mb,rp,v)
            customers.append(customer)
        else:
            print("Invalid recharge Plan!")
    elif choice == "2":
        for customer in customers:
            customer.show_details()
    elif choice == "3":
        sc = int(input("Enter mobile number of the customer who has to be searched: "))
        found = False
        for customer in customers:
            if customer.mobile_no == sc:
                customer.show_details()
                print("customer found successfully!")
                found = True
                break
        if not found:
            print("Invalid customer!")
    elif choice =="4":
        h = int(input("Enter mobile number whose recharge plan has to be updated"))
        up = input("Enter recharge plan to update (Basic/Standard/Premium) :")
        found = False
        for customer in customers:
            if customer.mobile_no==h:
                if up == "Basic" or up == "Standard" or up == "Premium":
                    customer.recharge_plan = up
                    customer.show_details()
                    print("Updated successfully!")
                    found = True
                    break
                else:
                    print("Invalid Recharge Plan!")
                    found = True 
                    break
        if not found :
            print("Invalid Mobile number!")
    elif choice == "5":
        c = int(input("Enter mobine number of the customer whose recharge cost has to be calculated:"))
        found = False
        for customer in customers:
            if customer.mobile_no == c:
                if customer.recharge_plan == "Basic":
                    recharge_price = customer.validity * 10
                elif customer.recharge_plan == "Standard":
                    recharge_price = customer.validity * 20
                elif customer.recharge_plan == "Premium":
                    recharge_price = customer.validity * 30
                else:
                    print("Invalid recharge plan!")

                print("Customer Name:",customer.cname)
                print("Recharge Plan:",customer.recharge_plan)
                print("Validity:",customer.validity)
                print("Total Recharge Cost:",recharge_price)

                found = True
                break
        if not found:
            print("Invalid customer Number!")
    elif choice =="6":
        d = int(input("Enter customer mobile number to be deleted:"))
        found = False
        for customer in customers:
            if customer.mobile_no == d:
                customers.remove(customer)
                customer.show_details()
                print("Customer deleted successfully!")
                found = True
                break
        if not found:
            print("Invalid Mobile number!")
    elif choice== "7":
        print("Exit...")
        break
    else:
        print("Invalid choice!")

