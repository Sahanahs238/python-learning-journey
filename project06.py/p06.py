employees = []
class Employee:
    def __init__(self,Ename,Eid,basic_salary):
        self.Ename=Ename
        self.Eid=Eid
        self.basic_salary=basic_salary
    def show_details(self):
        print("-"*15)
        print("Employee Name:",self.Ename)
        print("Employee ID:",self.Eid)
        print("Basic Salary:",self.basic_salary)
        print("-"*15)
        print(" "*15)

while True:
    print("===== EMPLOYEE PAYROLL MANAGEMENT =====")

    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Salary")
    print("5. Calculate Net Salary")
    print("6. Delete Employee")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ")
    if choice == "1":
        n = input("Enter employee name: ")
        i = int(input("Enter employee ID: "))
        bs = int(input("Enter basic salary: "))
        employee = Employee(n,i,bs)
        employees.append(employee)
    elif choice == "2":
        for employee in employees:
            employee.show_details()
    elif choice == "3":
        employID = int(input("enter employee ID to be searched:"))
        found = False
        for employee in employees:
            if employee.Eid == employID:
                print("Employee found successfully!")
                employee.show_details()
                found = True 
                break
        if not found:
            print("Invalid Employee!")
    elif choice == "4":
        un = input("Enter employee name whose salary has to be updated: ")
        us = int(input("Enter the salary to be updated: "))
        found = False
        for employee in employees:
            if employee.Ename == un:
                employee.basic_salary = us
                employee.show_details()
                print("Salary updated successfully!")
                found = True
                break
        if not found:
            print("Invalid employee!")
    elif choice == "5":
        ide = int(input("Enter employee id:"))
        for employee in employees:
            if employee.Eid == ide:
                net_salary = employee.basic_salary + 5000
                print("Employee Name:",employee.Ename)
                print("Basic Salary:",employee.basic_salary)
                print("Net Salary:",net_salary)
            else:
                print("Invalid Employee ID!")
    elif choice == "6":
        dm = input("Enter employee name to be deleted: ")
        found = False
        for employee in employees:
            if employee.Ename == dm:
                employees.remove(employee)
                found = True
                print("Employee deleted successfully!")
                break
        if not found:
            print("Employee not Found!")
    elif choice == "7":
        print("Exit...")
        break
    else:
        print("Invalid choice")


    
