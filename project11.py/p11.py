students = []
class Student:
    def __init__(self,sname,sid,cource_name,c_duration):
        self.sname=sname
        self.sid=sid
        self.cource_name=cource_name
        self.c_duration=c_duration
    def show_details(self):
        print("-"*15)
        print("Student Name:",self.sname)
        print("Student ID:",self.sid)
        print("Cource Name:",self.cource_name)
        print("Cource Duration:",self.c_duration)
        print("-"*15)
        print(" "*15)

while True:
    print("===== ONLINE COURSE ENROLLMENT =====")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Course")
    print("5. Calculate Course Fee")
    print("6. Delete Student")
    print("7. Exit")
    choice = input("Enter you choice (1-7): ")
    if choice == "1":
        n = input("Enter student name to be added: ")
        stid = int(input("Enter student ID: "))
        cn = input("Enter cource name (Python/Java/Web Development): ")
        cd = int(input("Enter cource duration: "))
        if cn == "Python" or cn == "Java" or cn == "Web Development":
            student = Student(n, stid, cn, cd)
            students.append(student)
        else:
            print("Invalid Course!")
    elif choice == "2":
        for student in students:
            student.show_details()
    elif choice == "3":
        ss = int(input("Enter student ID to be searched: "))
        found = False
        for student in students:
            if student.sid == ss:
                student.show_details()
                print("Student found successfully!")
                found = True
                break
        if not found:
            print("Invalid student ID!")
    elif choice == "4":
        ids = int(input("Enter student ID whose cource to be updated: "))
        new_cource = input("Enter the new cource:")
        found = False
        for student in students:
            if student.sid == ids:
                student.cource_name = new_cource
                student.show_details()
                print("Cource updated successfully!")
                found = True
                break
        if not found:
            print("Invalid student ID!")
    elif choice == "5":
        ss = int(input("Enter student ID whose fee has to be calculated: "))
        found = False
        for student in students:
            if student.sid == ss:
                if student.cource_name == "Python":
                    fee = student.c_duration * 5000
                elif student.cource_name == "Java":
                    fee = student.c_duration * 6000
                elif student.cource_name == "Web Development":
                    fee = student.c_duration * 7000
                else:
                    print("Invalid Cource!")

                print("Student Name",student.sname)
                print("student ID:",student.sid)
                print("Cource:",student.cource_name)
                print("Duration:",student.c_duration)
                print("Total fee:",fee)

                found = True
                break
        if not found:
            print("Invalid student ID!")
    elif choice == "6":
        d = int(input("Enter student id to be deleted: "))
        found = False
        for student in students:
            if student.sid == d:
                students.remove(student)
                student.show_details()
                print("Student deleted successfully!")
                found = True
                break
        if not found:
            print("Invalid student ID!")
    elif choice == "7":
        print("Exit...")
        break
    else:
        print("Invalid choice!")