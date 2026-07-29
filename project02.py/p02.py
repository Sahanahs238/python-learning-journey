books = []
class Book :
    def __init__(self,name,author,copies):
        self.name=name
        self.author=author
        self.copies=copies
    def show_details(self):
        print("Name:",self.name)
        print("author:",self.author)
        print("copies:",self.copies)

while True:
    print("===== LIBRARY MANAGEMENT =====")

    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ")
    if choice == "1":
        n = input("Enter the book name:")
        a = input("enter the book author:")
        c = int(input("enter the number of copies:"))
        book = Book(n,a,c)
        books.append(book)
    elif choice == "2":
        for book in books:
            book.show_details()
    elif choice == "3":
        wanted_book = input("enter the book name:")
        for book in books:
            if book.name == wanted_book:
                book.show_details()
            else:
                print("Invalid book")
    elif choice == "4":
        user = input("enter the book you wanted to borrow:")
        for book in books:
            if book.copies >0:
                book.copies-=1
                print("remaining copies:",book.copies)
            else:
                print("book not found!")
    elif choice == "5":
        remov = input("enter the book to be returned:")
        book.copies+=1
        print("remailning copies:",book.copies)
        
    
    elif choice == "6":
        remove = input("enter the book to be deleted:")
        for book in books:
            if book.name == remove:
                books.remove(book)
                print("the book deleted successfully!")

    elif choice == "7":
        print("Exit...")
        break
    else:
        print("Invalid choice")
        


