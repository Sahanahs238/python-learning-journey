contacts = {}
while True:
    print("===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    choice = input("Enter your choice (1,2,3,4,5): ")
    if choice == "1":
        number = input("Enter the contact number: ")
        print(number)
        name = input("Enter the name: ")
        print(name)
        contacts[name] = number
        print("contact added successfully:")
    elif choice == "2":
        if contacts == {}:
            print("There are no contacts")
        else:
            print(contacts.items())
    elif choice == "3":
        name1=input("Enter the contact name you need: ")
        if name1 in contacts:
            print(number)
        else:
            print("conract not found")
    elif choice == "4":
        delete = input("enter the contact name to be deleted: ")
        if delete == name:
            del contacts[delete]
        else:
            print("invalid name")
    elif choice == "5":
        print("exit")
        break
    else:
        print("invalid choice")



