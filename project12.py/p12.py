orders = []
class Order:
    def __init__(self,customer_name,order_id,food_item,quantity):
        self.customer_name=customer_name
        self.order_id=order_id
        self.food_item=food_item
        self.quantity=quantity
    def show_details(self):
        print("-"*15)
        print("Customer Name:",self.customer_name)
        print("Order ID:",self.order_id)
        print("Food Item:",self.food_item)
        print("Quantity:",self.quantity)
        print("-"*15)
        print(" "*15)
while True:
    print("===== RESTAURANT ORDER MANAGEMENT =====")

    print("1. Add Order")
    print("2. View Orders")
    print("3. Search Order")
    print("4. Update Quantity")
    print("5. Calculate Bill")
    print("6. Delete Order")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ")
    if choice == "1":
        cn = input("enter customer name: ")
        oid = int(input("Enter order ID: "))
        fi = input("Enter food item (Pizza/Burger/Pasta): ")
        q = int(input("Enter the quantity: "))
        if fi == "Pizza" or fi == "Burger" or fi=="Pasta":
            order = Order(cn,oid,fi,q)
            orders.append(order)
        else:
            print("This Food is Unavailable!")
    elif choice == "2":
        for order in orders:
            order.show_details()
    elif choice == "3":
        sr = int(input("Enter the order ID to be searched:"))
        found = False
        for order in orders:
            if order.order_id == sr:
                order.show_details()
                print("order found successfully!")
                found = True
                break
        if not found:
            print("Invalid order ID!")
    elif choice == "4":
        uq = int(input("enter order ID to be updated:"))
        new_q = int(input("Enter the quantity to be updated:"))
        found = False
        for order in orders:
            if order.order_id == uq:
                order.order_id = new_q
                order.show_details()
                print("Quantity updated successfully!")
                found = True
                break
        if not found:
            print("Invalid order ID!")
    elif choice == "5":
        o = int(input("Enter order ID whose bill has to be calculated"))
        found = False
        for order in orders:
            if order.order_id == o:
                if order.food_item == "Pizza":
                    total_bill = order.quantity * 300
                elif order.food_item == "Burger":
                    total_bill = order.quantity * 150
                elif order.food_item == "Pasta":
                    total_bill = order.quantity * 250
                else:
                    print("Food Item Unavailable!")

                print("Customer Name:",order.customer_name)
                print("Food Item:",order.food_item)
                print("Quantity:",order.quantity)
                print("Total Bill:",total_bill) 
                found = True
                break
        if not found:
            print("Invalid order ID:")
    elif choice == "6":
        d = int(input("Enter order ID to be deleted:"))
        found = False
        for order in orders:
            if order.order_id == d:
                orders.remove(order)
                order.show_details()
                print("Order cancelled successfully!")
                found = True
                break
        if not found:
            print("Invalid order ID!")
    elif choice == "7":
        print("Exit...")
        break
    else:
        print("Invalid choice!")

