products = []
class Product:
    def __init__(self,pname,pid,price_per_unit,quantity):
        self.pname = pname
        self.pid = pid
        self.price_per_unit = price_per_unit
        self.quantity=quantity
    def show_details(self):
        print("-"*15)
        print("Product Name:",self.pname)
        print("Product ID:",self.pid)
        print("Price Per Unit:",self.price_per_unit)
        print("Quantity:",self.quantity)
        print("-"*15)
while True:
    print("===== SUPERMARKET BILLING MANAGEMENT =====")

    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Quantity")
    print("5. Calculate Total Bill")
    print("6. Delete Product")
    print("7. Exit")
    choice = input("Enter your choice(1-7):")
    if choice == "1":
        p = input("Enter product name:")
        idp = int(input("Enter product ID:"))
        ppu = int(input("Enter price per unit:"))
        q = int(input("Enter the quantity"))
        product =Product(p,idp,ppu,q)
        products.append(product)
        print("Product added successfully!")
    elif choice == "2":
        for product in products:
            product.show_details()

    elif choice == "3":
        pro_id = int(input("Enter product ID to be searched:"))
        found = False  
        for product in products:
            if product.pid == pro_id:
                product.show_details()
                print("product found successfully:")
                found = True 
                break
        if not found:
            print("Invalid product ID!")
    elif choice == "4":
        pr_id = int(input("Enter product id whose quantity has to be updated:"))
        uq = int(input("Enter update quantity: "))
        found = False
        for product in products:
            if product.pid == pr_id:
                product.quantity = uq
                product.show_details()
                print("Product quantity updated successfully!")
                found = True
                break
        if not found:
            print("Invalid product ID!")
    elif choice == "5":
        pd_id = int(input("Enter product ID whose bill has to be calculated:"))
        found = False
        for product in products:
            if product.pid == pd_id:
                total_bill = product.price_per_unit * product.quantity

            print("Product Name:",product.pname)
            print("Product ID:",product.pid)
            print("Quantity:",product.quantity)
            print("Price Per Unit:",product.price_per_unit)
            print("Total Bill:",total_bill)

            found = True
            break
        if not found:
            print("Invalid Product ID!")
    elif choice == "6":
        d = int(input("Enter product ID to be deleted:"))
        found = False
        for product in products:
            if product.pid == d:
                products.remove(product)
                product.show_details()
                print("Product deleted successfully!")
                found = True
                break
        if not found:
            print("Invalid product ID!")
    elif choice == "7":
        print("Exit...")
        break
    else:
        print("Invalid choice!")


