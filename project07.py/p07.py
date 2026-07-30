rooms = []
class Room:
    def __init__(self,Rno,Room_type,price):
        self.Rno=Rno
        self.Room_type=Room_type
        self.price=price
        self.status="Available"
    def show_details(self):
        print("-"*15)
        print("Room Number:",self.Rno)
        print("Room Type:",self.Room_type)
        print("Price:",self.price)
        print("Status:",self.status)
while True:
    print("===== HOTEL ROOM MANAGEMENT =====")

    print("1. Add Room")
    print("2. View Rooms")
    print("3. Search Room")
    print("4. Book Room")
    print("5. Checkout Room")
    print("6. Delete Room")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ")
    if choice == "1":
        rn = int(input("Enter room number: "))
        rt = input("Enter room type: ")
        p = int(input("Enter room price:"))
        room = Room(rn,rt,p)
        print("Room status:",room.status)
        rooms.append(room)
    elif choice == "2":
        for room in rooms:
            room.show_details()
    elif choice == "3":
        sr = int(input("Enter room number to be searched:"))
        found = False
        for room in rooms:
            if room.Rno == sr:
                print("room found successfully!")
                room.show_details()
                found = True
                break
        if not found:
            print("Invalid room number!")
    elif choice == "4":
        br = int(input("Enter room number to be booked:"))
        found = False
        for room in rooms:
            if room.Rno == br:
                if room.status == "Available":
                    room.status = "Booked"
                    room.show_details()
                    print("Room booked successfully!")
                    found = True
                    break
        if not found:
            print("Room already bookes!")
    elif choice == "5":
        roomn = int(input("Enter room number to do checkout:"))
        found = False
        for room in rooms:
            if room.Rno == roomn:
                if room.status == "Booked":
                    room.status = "Available"
                    print("Checkout successfully!")
                    found = True
                    break
        if not found:
            print("Room is already available!")
    elif choice == "6":
        dr = int(input("Enter room number to be deleted:"))
        found = False
        for room in rooms:
            if room.Rno == dr:
                rooms.remove(room)
                print("Room deleted successfully!")
                found = True
                break
        if not found:
            print("Room number not found!")
    elif choice == "7":
        print("Exit...")
        break
    else:
        print("Invalid choice")

