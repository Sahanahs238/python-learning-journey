customers = []
class Customer:
    def __init__(self,cname,cid,units_consumed,area):
        self.cname=cname
        self.cid=cid
        self.units_consumed=units_consumed
        self.area=area
    def show_details(self):
        print("Customer Name:",self.cname)
        print("Customer ID:",self.cid)
        print("Units Consumed:",self.units_consumed)
        print("Area:",self.area)
while True:
    print("===== ELECTRICITY BILL MANAGEMENT =====")

    print("1. Add Customer")
    print("2. View Customers")
    print("3. Search Customer")
    print("4. Update Units Consumed")
    print("5. Calculate Electricity Bill")
    print("6. Delete Customer")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ")
    if choice == "1":
        cn = input("Customer Name:")
        idc = int(input("Customer ID: "))
        uc = int(input("Units Consumed: "))
        a = input("Area (Urban/Rural): ")
        if a == "Urban" or a == "Rural":
            customer = Customer(cn,idc,uc,a)
            customers.append(customer)
        else:
            print("Invalid Area!")
    elif choice == "2":
        for customer in customers:
            customer.show_details()
    elif choice == "3":
        sc = int(input("Enter customer id to be searched: "))
        found = False
        for customer in customers:
            if customer.cid == sc:
                customer.show_details()
                print("Customer Found successfully!")
                found = True
                break
        if not found:
            print("Invalid customer ID!")
    elif choice == "4":
        u = int(input("Enter customer id whose units has to be updated: "))
        v = int(input("Ented the units for update: "))
        found = False
        for customer in customers:
            if customer.cid == u:
                customer.units_consumed = v
                customer.show_details()
                print("units updated successfully!")
                found = True
                break
        if not found :
            print("invalid customer id!")
    elif choice == "5":
        w =int(input("Enter customer id whose electricity bill has to be calculated: "))
        found = False
        for customer in customers:
            if customer.cid == w:
                if customer.area == "Urban":
                    Bill = customer.units_consumed * 8
                elif customer.area == "Rural":
                    Bill = customer.units_consumed * 5
                else:
                    print("Invalid area!")

                print("Customer Name:",customer.cname)
                print("Area:",customer.area)
                print("Units Consumed:",customer.units_consumed)
                print("Total Bill:",Bill)

                found = True
                break
        if not found:
            print("Invalid Custome ID!")
    elif choice == "6":
        dc = int(input("Enter customer ID to be deleted: "))
        found = False
        for customer in customers:
            if customer.cid == dc:
                customers.remove(customer)
                customer.show_details()
                print("Customer deleted successfully!")
                found = True
                break
        if not found:
            print("Invalid customer ID!")

    elif choice == "7":
        print("Exit...")
        break
    else:
        print("Invalid choice!")
        

