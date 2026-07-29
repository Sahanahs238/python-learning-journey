products = []

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def show_details(self):
        print("-" * 30)
        print("Product :", self.name)
        print("Price   :", self.price)
        print("Quantity:", self.quantity)


while True:
    print("\n===== SHOPPING CART =====")
    print("1. Add Product")
    print("2. View Cart")
    print("3. Search Product")
    print("4. Update Quantity")
    print("5. Remove Product")
    print("6. Calculate Total Price")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter quantity: "))

        product = Product(name, price, quantity)
        products.append(product)

        print("✅ Product added successfully!")

    elif choice == "2":
        if len(products) == 0:
            print("Cart is empty!")
        else:
            for product in products:
                product.show_details()

    elif choice == "3":
        search = input("Enter product name to search: ")

        found = False

        for product in products:
            if product.name == search:
                product.show_details()
                found = True
                break

        if not found:
            print("❌ Product not found!")

    elif choice == "4":
        update = input("Enter product name: ")

        found = False

        for product in products:
            if product.name == update:
                new_quantity = int(input("Enter new quantity: "))
                product.quantity = new_quantity
                print("✅ Quantity updated!")
                found = True
                break

        if not found:
            print("❌ Product not found!")

    elif choice == "5":
        remove = input("Enter product name: ")

        found = False

        for product in products:
            if product.name == remove:
                products.remove(product)
                print("✅ Product removed!")
                found = True
                break

        if not found:
            print("❌ Product not found!")

    elif choice == "6":
        total = 0

        for product in products:
            total += product.price * product.quantity

        print("🛒 Total Price =", total)

    elif choice == "7":
        print("Thank you! 👋")
        break

    else:
        print("Invalid choice!")