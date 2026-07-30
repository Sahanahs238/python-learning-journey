movies = []
class Movie:
    def __init__(self,mname,tprice,AVL_seats):
        self.mname = mname
        self.tprice=tprice
        self.AVL_seats=AVL_seats


    def show_details(self):
        print("-"*15)
        print("Movie Name:",self.mname)
        print("Ticket Price:",self.tprice)
        print("Available Seats:",self.AVL_seats)
        print("-"*15)
while True:
    print("===== MOVIE TICKET BOOKING =====")

    print("1. Add Movie")
    print("2. View Movies")
    print("3. Search Movie")
    print("4. Book Tickets")
    print("5. Cancel Tickets")
    print("6. Delete Movie")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ")
    if choice == "1":
        n = input("Enter movie name:")
        p = int(input("Enter movie price: "))
        AS = int(input("Enter available seats: "))
        movie = Movie(n,p,AS)
        movies.append(movie)
    elif choice == "2":
        for movie in movies:
            movie.show_details()
    elif choice == "3":
        sm = input("Enter movie name to ba searched: ")
        found = False
        for movie in movies:
            if movie.mname == sm:
                movie.show_details()
                print("Movie Found!")
                found = True
                break
        if not found:
            print("Invalid movie name!")
    elif choice == "4":
        mn = input("Enter movie name to be booked:")
        tickets = int(input("Enter number of tickets: "))
        found = False
        for movie in movies:
            if movie.mname == mn:
                found = True
                if movie.AVL_seats >= tickets:
                    movie.AVL_seats -= tickets
                    movie.show_details()
                    print("Movie booked successfully!")
                else:
                    print("seats unavailable")
                    break
        if not found:
            print("movie not found!")
    elif choice == "5":
        cn = input("Enter movie name to be cancelled: ")
        ticket = int(input("Enter tickets to cancel: "))
        found = False
        for movie in movies:
            if movie.mname == cn:
                movie.AVL_seats+=ticket
                movie.show_details()
                print("Movie cancelled successfully!")
                found = True
                break

        if not found:
            print("Invalid movie!")
    elif choice == "6":
        dn = input("Enter movie name to be deleted:")
        found = False
        for movie in movies:
            if movie.mname == dn:
                movies.remove(movie)
                print("Movie deleted successfully!")
                movie.show_details()
                found = True
                break
        if not found:
            print("Invalid movie!")
    elif choice == "7":
        print("Exit...")
        break
    else:
        print("Invalid choice")


                


