students = []
class Student:
    def __init__(self,name,rno,marks):
        self.name=name
        self.rno=rno
        self.marks=marks
    def show_details(self):
        print("-"*15)
        print("Name:",self.name)
        print("Roll Number :",self.rno)
        print("Marks:",self.marks)
while True:
    print("===== STUDENT GRADE MANAGEMENT =====")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Calculate Grade")
    print("6. Delete Student")
    print("7. Exit")
    choice = input("Enter your choice(1-7): ")
    if choice == "1":
        n = input("Enter student name: ")
        rn = int(input("Enter the roll number of the student: "))
        m = int(input("Enter student marks: "))
        if m >= 0 and m<=100:
            student = Student(n,rn,m)
            students.append(student)
        else:
            print("Invalid marks")
    elif choice =="2":
        for student in students:
            student.show_details()
    elif choice == "3":
        search = input("Enter the student name to be searched:")
        for student in students:
            if student.name == search:
                student.show_details()
            else:
                print("student not Found!")
    elif choice == "4":
        up = int(input("Enter the updated marks:"))
        n = input("Enter the name which you wanted to update: ")
        for student in students:
            if student.name == n:
                student.marks = up
                student.show_details()
                print("marks updated successfully!")
        else:
            print("student not found!")
    elif choice == "5":
        rolln = int(input("Enter student roll number: "))
        for student in students:
            if student.rno == rolln:
                if student.marks<=100 and student.marks>=90:
                    print("Grade:A+")
                elif student.marks<=89 and student.marks>=80:
                    print("Grade:A")
                elif student.marks<=79 and student.marks>=70:
                    print("Grade:B") 
                elif student.marks<=69 and student.marks>=60:
                    print("Grade:C")
                elif student.marks<60:
                    print("Grade:Fail")
                else:
                    print("Invalid marks")
            else:
                print("Invalid student")
    elif choice == "6":
        d = input("Enter student name to be deleted: ")
        for student in students:
            if student.name == d:
                students.remove(student)
                print("student deleted successfully!")
                break
            else:
                print("Invalid student")
    elif choice == "7":
        print("Exit...")
        break
    else:
        print("Invalid choice")


