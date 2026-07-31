members = []
class Member:
    def __init__(self,mname,mid,membership_plan,months):
        self.mname = mname
        self.mid = mid
        self.membership_plan = membership_plan
        self.months = months
    def show_details(self):
        print("-"*15)
        print("Member Name:",self.mname)
        print("Member ID:",self.mid)
        print("Membership Plan:",self.membership_plan)
        print("Months:",self.months)
        print("-"*15)
        print(" "*15)
while True:
    print("===== GYM MEMBERSHIP MANAGEMENT =====")

    print("1. Add Member")
    print("2. View Members")
    print("3. Search Member")
    print("4. Renew Membership")
    print("5. Calculate Membership Fee")
    print("6. Delete Member")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ")
    if choice == "1":
        mn = input("Enter member name: ")
        mid = int(input("Enter member ID: "))
        mp = input("Enter membership Plan (Basic/Premium/VIP): ")
        m = int(input("Enter months: "))
        member = Member(mn,mid,mp,m)
        members.append(member)
    elif choice == "2":
        for member in members:
            member.show_details()
    elif choice == "3":
        sm = int(input("Enter member id to be searched:"))
        found = False
        for member in members:
            if member.mid == sm:
                member.show_details()
                print("Member Found!")
                found = True
                break
        if not found:
            print("Invalid member!")
    elif choice == "4":
        rmd = int(input("Enter member ID: "))
        adm = int(input("enter additional months: "))
        found = False
        for member in members:
            if member.mid == rmd:
                member.months += adm
                member.show_details()
                print("months updated successfully!")
                found = True
                break
        if not found:
            print("Invalid member ID!")
    elif choice == "5":
        m = int(input("enter member ID: "))
        found = False
        for member in members:
            if member.mid == m:
                mm = input("enter membership plan: ")
                if member.membership_plan == "Basic":
                    fees = member.months * 1000
                elif member.membership_plan == "Premium":
                    fees = member.months * 3000
                elif member.membership_plan == "VIP":
                    fees = member.membership_plan * 10000
                else:
                    print("Invalid membership plan!")

                print("Member Name:",member.mname)
                print("Member plan:",mm)
                print("Months:",member.months)
                print("Total fee",fees)
                found = True
                break
        if not found:
            print("member not found!")
    elif choice == "6":
        d = int(input("enter member id to be deleted:"))
        found = False
        for member in members:
            if member.mid == d:
                members.remove(member)
                member.show_details()
                print("member deleted successfully!")
                found = True 
                break
        if not found:
            print("invalid member ID!")
    elif choice == "7":
        print("Exit...")
        break
    else:
        print("Invalid choice!")
        



