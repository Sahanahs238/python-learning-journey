cars = []
class Car:
    def __init__(self,cname,cid,rent_per_day):
        self.cname = cname
        self.cid = cid
        self.rent_per_day = rent_per_day
        self.status ="Available"
    def show_details(self):
        print("-"*15)
        print("Car Name:",self.cname)
        print("Car ID:",self.cid)
        print("Rent Per Day:",self.rent_per_day)
        print("Status:",self.status)
        print("-"*15)
        print(" "*15)
while True:
    print("===== CAR RENTAL MANAGEMENT =====")

    print("1. Add Car")
    print("2. View Cars")
    print("3. Search Car")
    print("4. Rent Car")
    print("5. Return Car")
    print("6. Delete Car")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ")
    if choice == "1":
        cn = input("Enter car name: ")
        idc = int(input("Enter car ID:"))
        rpd = int(input("Enter rent per day: "))
        car = Car(cn,idc,rpd)
        print("Car Status:",car.status)
        cars.append(car)
    elif choice == "2":
        for car in cars:
            car.show_details()
    elif choice == "3":
        c = int(input("Enter car ID to be searched: "))
        found = False
        for car in cars:
            if car.cid==c:
                car.show_details()
                print("car found successfully!")
                found = True
                break
        if not found :
            print("Car ID not found!")
    elif choice == "4":
        rc = int(input("Enter car ID to be rented: "))
        found = False
        for car in cars:
            if car.cid == rc:
                if car.status == "Available":
                    car.status = "Rented"
                    car.show_details()
                    print("car rented successfully!")
                    found = True
                    break
        if not found:
            print("Invalid car ID!")
    elif choice == "5":
        rcar = int(input("Enter car id to be returned: "))
        found = False
        for car in cars:
            if car.cid == rcar:
                if car.status == "Rented":
                    car.status = "Available"
                    car.show_details()
                    print("Car returned successfully!")
                    found = True
                    break
                else:
                    print("car is already available!")
                    break
        if not found:
            print("Invalid car ID!")
    elif choice == "6":
        dc = int(input("Enter car id to be deleted: "))
        found = False
        for car in cars:
            if car.cid == dc:
                cars.remove(car)
                car.show_details()
                print("Car deleted successfully!")
                found = True
                break
        if not found:
            print("Invalid car ID!")
    elif choice == "7":
        print("Exit...")
        break
    else:
        print("Invalid choice!")







