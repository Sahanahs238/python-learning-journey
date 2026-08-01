flights = []
class Flight:
    def __init__(self,fname,fid,destination,available_seats,ticket_price):
        self.fname =fname
        self.fid=fid
        self.destination=destination
        self.available_seats=available_seats
        self.ticket_price = ticket_price
        self.total_seats = available_seats
    def show_details(self):
        print("-"*15)
        print("Flight name:",self.fname)
        print("Flight ID:",self.fid)
        print("Destination:",self.destination)
        print("Ticket Price:",self.ticket_price)
        print("Total Seats:",self.total_seats)
        print("-"*15)
while True:
    print("===== FLIGHT BOOKING MANAGEMENT =====")

    print("1. Add Flight")
    print("2. View Flights")
    print("3. Search Flight")
    print("4. Book Seats")
    print("5. Calculate Revenue")
    print("6. Delete Flight")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ")
    if choice == "1":
        fn = input("Enter Flight name:")
        fid = int(input("Enter flight ID:"))
        d = input("Enter destination:")
        avl = int(input("Enter Available seats:"))
        tp = int(input("Enter ticket price:"))
        flight = Flight(fn,fid,d,avl,tp)
        flights.append(flight)
    elif choice == "2":
        for flight in flights:
            flight.show_details()
    elif choice == "3":
        sf = int(input("Enter flight id to be searched: "))
        found = False
        for flight in flights:
            if flight.fid == sf:
                flight.show_details()
                print("flight found Successfully!")
                found = True
                break
        if not found:
            print("Invalid flight id!")
    elif choice == "4":
        fli_id = int(input("Enter flight id whose seats to be booked:"))
        nb = int(input("Enter number of seats to be booked:"))
        found = False
        for flight in flights:
            if flight.fid == fli_id:
                if flight.available_seats >= nb:
                    flight.available_seats -= nb
                    flight.show_details()
                    print("Seats booked successfully!")
                    found = True
                    break
                else:
                    print("Not enough seats available!")
                    found = True
                    break
        if not found:
            print("Invalid Flight ID!")
    elif choice == "5":
        cr = int(input("Enter flight id whose revenue has to be calculated:"))
        found = False
        for flight in flights:
            if flight.fid == cr:
                booked = flight.total_seats - flight.available_seats
                revenue = booked * flight.ticket_price

                print("Flight Name:",flight.fname)
                print("Destination:",flight.destination)
                print("Booked Seats:",booked)
                print("Total Revenue:",revenue)
                found = True
                break
        if not found:
            print("Invalid Flight ID!")

    elif choice == "6":
        df = int(input("Enter flight ID to be deleted:"))
        found = False
        for flight in flights:
            if flight.fid == df:
                flights.remove(flight)
                flight.show_details()
                print("Flight deleted successfully!")
                found = True
                break
        if not found:
            print("Invalid flight ID!")
    elif choice == "7":
        print("Exit...")
        break
    else:
        print("Invalid choice!")