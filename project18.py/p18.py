buses = []
class Bus:
   def __init__(self,bus_name,bus_id,route,available_seats,ticket_price):
      self.bus_name=bus_name
      self.bus_id=bus_id
      self.route=route
      self.available_seats=available_seats
      self.ticket_price=ticket_price
      self.total_seats = available_seats
   def show_details(self):
      print("-"*15)
      print("Bus Name:",self.bus_name)
      print("Bus ID:",self.bus_id)
      print("Route:",self.route)
      print("Available seats:",self.available_seats)
      print("Ticket Price:",self.ticket_price)
      print("-"*15)
      print(" "*15)
while True:
    print("===== BUS TICKET RESERVATION =====")

    print("1. Add Bus")
    print("2. View Buses")
    print("3. Search Bus")
    print("4. Book Seats")
    print("5. Calculate Collection")
    print("6. Delete Bus")
    print("7. Exit ")
    choice = input("Enter your choice (1-7): ")
    if choice == "1":
        bn = input("Enter bus name: ")
        bid =int(input("Enter bus ID: "))
        r = input("Enter bus route:")
        s = int(input("Enter available seats:"))
        tp = int(input("Enter ticket price:"))
        bus = Bus(bn,bid,r,s,tp)
        buses.append(bus)
    elif choice == "2":
        for bus in buses:
            bus.show_details()
    elif choice == "3":
        b_id = int(input("Enter bus id to be searched:"))
        found = False
        for bus in buses:
            if bus.bus_id==b_id:
                bus.show_details()
                print("Bus found successfully!")
                found = True
                break
        if not found:
            print("Invalid bus ID!")
    elif choice == "4":
        busid = int(input("Enter bus ID to be booked:"))
        seat = int(input("Enter number of seats to be booked:"))
        found = False
        for bus in buses:
            if bus.bus_id == busid:
                if bus.available_seats > seat:
                    available_seats -= seat
                    bus.show_details()
                    print("Seats booked successfully!")
                    found = True
                    break
                else:
                    print("Not enough seats available!")
                    found = True
                    break
        if not found:
            print("Invalid bus ID!")
    elif choice == "5":
        bc = int(input("Enter bus id whose collection has to be calculated: "))
        found = False
        for bus in buses:
            if bus.bus_id==bc:
                booked = bus.total_seats - bus.available_seats
                collection = booked * bus.ticket_price
                bus.show_details()

                print("Bus Name:",bus.bus_name)
                print("Route:",bus.route)
                print("Booked Seats:",booked)
                print("Total Collection:",collection)
                found = True
                break
        if not found:
            print("Invalid bus ID!")
    elif choice == "6":
        d = int(input("Enter bus ID to be deleted:"))
        found = False
        for bus in buses:
            if bus.bus_id == d:
                buses.remove(bus)
                bus.show_details()
                print("Bus deleted successfully!")
                found = True
                break
        if not found:
            print("Invalid bus ID!")
    elif choice == "7":
        print("Exit...")
        break
    else:
        print("Invalid choice!")


    
    
    
       