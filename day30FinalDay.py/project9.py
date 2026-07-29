students = []

class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def show_details(self):
        print("--------------------------")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)


while True:
    print("\n===== STUDENT RESULT MANAGEMENT =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Calculate Average Marks")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        print("\nEnter Student Details")
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        marks = float(input("Enter marks: "))

        student = Student(name, age, marks)
        students.append(student)

        print("✅ Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students available.")
        else:
            print("\nStudent Details:")
            for student in students:
                student.show_details()

    elif choice == "3":
        search_name = input("Enter student name to search: ")

        found = False

        for student in students:
            if student.name.lower() == search_name.lower():
                student.show_details()
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "4":
        delete_name = input("Enter student name to delete: ")

        found = False

        for student in students:
            if student.name.lower() == delete_name.lower():
                students.remove(student)
                print("✅ Student deleted successfully!")
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "5":
        if len(students) == 0:
            print("No students available.")
        else:
            total = 0

            for student in students:
                total += student.marks

            average = total / len(students)

            print("Average Marks =", average)

    elif choice == "6":
        print("Thank you! Exiting...")
        break

    else:
        print("Invalid Choice!")