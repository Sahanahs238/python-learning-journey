employees = []

class Employee:
    def __init__(self, name, age, department, salary):
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Department:", self.department)
        print("Salary:", self.salary)
        print("-" * 30)


while True:
    print("\n===== EMPLOYEE MANAGEMENT =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Remove Employee")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print("\nEnter Employee Details")
        name = input("Name: ")
        age = int(input("Age: "))
        department = input("Department: ")
        salary = float(input("Salary: "))

        emp = Employee(name, age, department, salary)
        employees.append(emp)

        print("Employee added successfully!")

    elif choice == "2":
        if len(employees) == 0:
            print("No employees found.")
        else:
            print("\nEmployee Details:")
            for emp in employees:
                emp.show_details()

    elif choice == "3":
        search_name = input("Enter employee name to search: ")
        found = False

        for emp in employees:
            if emp.name.lower() == search_name.lower():
                emp.show_details()
                found = True
                break

        if not found:
            print("Employee not found.")

    elif choice == "4":
        remove_name = input("Enter employee name to remove: ")
        found = False

        for emp in employees:
            if emp.name.lower() == remove_name.lower():
                employees.remove(emp)
                print("Employee removed successfully!")
                found = True
                break

        if not found:
            print("Employee not found.")

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")