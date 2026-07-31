books = []
class Book:
    def __init__(self,sname,sid,BookName,Days_Kept):
        self.sname=sname
        self.sid=sid
        self.BookName = BookName
        self.Days_Kept=Days_Kept

    def show_details(self):
        print("-"*15)
        print("Student Name:",self.sname)
        print("Student ID:",self.sid)
        print("Book Name:",self.BookName)
        print("Days Kept:",self.Days_Kept)
        print("-"*15)
        print(" "*15)

while True:
    print("===== SCHOOL LIBRARY FINE MANAGEMENT =====")

    print("1. Add Book Issue")
    print("2. View Issued Books")
    print("3. Search Student")
    print("4. Update Return Days")
    print("5. Calculate Fine")
    print("6. Delete Record")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        n = input("Enter student name: ")
        sid = int(input("Enter student ID: "))
        bn = input("Enter book name: ")
        dk = int(input("Enter days kept: "))
        book = Book(n,sid,bn,dk)
        books.append(book)
    elif choice == "2":
        for book in books:
            book.show_details()
    elif choice == "3":
        ids = int(input("enter student id to be searched: "))
        found = False
        for book in books:
            if book.sid == ids:
                book.show_details()
                print("Student Found successfully!")
                found = True
                break
        if not found:
            print("Invalid student ID!")
    elif choice == "4":
        s = int(input("Enter student ID: "))
        sdu = int(input("Enter the days to update: "))
        found = False
        for book in books:
            if book.sid == s:
                book.Days_Kept = sdu
                book.show_details()
                print("Days updated successfully!")
                found = True
                break
        if not found:
            print("Invalid student ID!")
    elif choice == "5":
        user = int(input("Enter student ID: "))
        found = False
        for book in books:
            if book.sid==user:
                if book.Days_Kept <= 7:
                     print("-"*15)
                     print("Student Name:",book.sname)
                     print("Student ID:",book.sid)
                     print("Book Name:",book.BookName)
                     print("Days Kept:",book.Days_Kept)
                     print("No fine!")
                     print("-"*15)
                     print(" "*15)
                elif book.Days_Kept > 7 :
                    extra_days = book.Days_Kept - 7
                    fine = extra_days * 10 
                    print("-"*15)
                    print("Student Name:",book.sname)
                    print("Student ID:",book.sid)
                    print("Book Name:",book.BookName)
                    print("Days Kept:",book.Days_Kept)
                    print("Extra days:",extra_days)
                    print("Fine:",fine)
                    print("-"*15)
                    print(" "*15)
                    found = True
                    break
                else:
                    print("Invalid days!")
        if not found:
            print("Student not Found!")
    elif choice == "6":
        ds = int(input("Enter student id to delete: "))
        found = False
        for book in books:
            if book.sid == ds:
                books.remove(book)
                book.show_details()
                print("student record deleted successfully!")
                found = True
                break
        if not found:
            print("Invalid student ID!")
    elif choice == "7":
        print("Exit...")
        break
    else:
        print("Invalid choice!")


                     
                    
                    