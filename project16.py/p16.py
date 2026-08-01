books = []
class Book:
    def __init__(self,bname,bid,author,available_copies,price):
        self.bname = bname
        self.bid = bid
        self.author = author
        self.available_copies = available_copies
        self.price = price

    def show_details(self):
        print("-"*15)
        print("Book Name:",self.bname)
        print("Book ID:",self.bid)
        print("Author:",self.author)
        print("Available Copies:",self.available_copies)
        print("Price:",self.price)
        print("-"*15)
        print(" "*15)
while True:
    print("\n===== COLLEGE LIBRARY MANAGEMENT =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Update Available Copies")
    print("5. Calculate Total Book Value")
    print("6. Delete Book")
    print("7. Exit")
    choice = int(input("Enter your choice (1-7): "))
    if choice  == "1":
        bname = input("Enter Book Name: ")
        bid = input("Enter Book ID: ")
        author = input("Enter Author Name: ")
        available_copies = int(input("Enter Available Copies: "))
        price = float(input("Enter Price: "))
        book = Book(bname,bid,author,available_copies,price)
        books.append(book)
        print("Book added successfully!")
    elif choice == "2":
        if len(books) == 0:
            print("No books available.")
        else:
            for book in books:
                book.show_details()
    elif choice == "3":
        search_bid = input("Enter Book ID to search: ")
        found = False
        for book in books:
            if book.bid == search_bid:
                book.show_details()
                found = True
                break
        if not found:
            print("Book not found.")
    elif choice == "4":
        update_bid = input("Enter Book ID to update available copies: ")
        found = False
        for book in books:
            if book.bid == update_bid:
                new_copies = int(input("Enter new available copies: "))
                book.available_copies = new_copies
                book.show_details()
                print("Available copies updated successfully!")
                found = True
                break
        if not found:
            print("Book not found.")
    elif choice == "5":
        total_value = 0
        for book in books:
            total_value += book.available_copies * book.price
        print("Total Book Value: $", total_value)
    elif choice == "6":
        delete_bid = input("Enter Book ID to delete: ")
        found = False
        for book in books:
            if book.bid == delete_bid:
                books.remove(book)
                print("Book deleted successfully!")
                found = True
                break
        if not found:
            print("Book not found.")
    elif choice == "7":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")