students = []
class Student:
    def __init__(self,student_name,student_id,marks,department):
        self.student_name = student_name
        self.student_id = student_id
        self.marks = marks
        self.department = department
    def show_details(self):
        print("-"*15)
        print("Student Name:",self.student_name)
        print("Student ID:",self.student_id)
        print("Marks:",self.marks)
        print("Department:",self.department)
        print("-"*15)
while True:
    print("===== STUDENT RESULT MANAGEMENT =====")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Calculate Grade")
    print("6. Delete Student")
    print("7. Exit")
    choice = input("Enter your choice(1-7): ")
    if choice == "1":
        sn = input("Enter student name: ")
        sid = int(input("Enter student ID: "))
        m = int(input("Enter student marks: "))
        d = input("Enter student department: ")
        student = Student(sn,sid,m,d)
        students.append(student)
        print("Student added successfully!")
    elif choice == "2":
        for student in students:
            student.show_details()
    elif choice == "3":
        search = input("Enter the student name to be searched:")
        found = False
        for student in students:
            if student.student_name == search:
                student.show_details()
                found = True
                break
        if not found:
            print("Student not found!")
    elif choice == "4":
        update_id = int(input("Enter the student ID to update marks: "))
        found = False
        for student in students:
            if student.student_id == update_id:
                new_marks = int(input("Enter new marks: "))
                student.marks = new_marks
                student.show_details()
                print("Marks updated successfully!")
                found = True
                break
        if not found:
            print("Student not found!")
    elif choice == "5":
        student_id = int(input("Enter student ID to calculate grade: "))
        found = False
        for student in students:
            if student.student_id == student_id:
                if student.marks >= 90:
                    grade = "A+"
                elif student.marks >= 80:
                    grade = "A"
                elif student.marks >= 70:
                    grade = "B"
                elif student.marks >= 60:
                    grade = "C"
                else:
                    grade = "F"
                print("Grade:", grade)
                found = True
                break
        if not found:
            print("Student not found!")
    elif choice == "6":
        delete_id = int(input("Enter student ID to delete: "))
        found = False
        for student in students:
            if student.student_id == delete_id:
                students.remove(student)
                print("Student deleted successfully!")
                found = True
                break
        if not found:
            print("Student not found!")
    elif choice == "7":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")