patients = []
class Patient:
    def __init__(self,pname,pid,disease,no_of_days_admitted):
        self.pname=pname
        self.pid=pid
        self.disease=disease
        self.no_of_days_admitted=no_of_days_admitted
    def show_details(self):
        print("-"*15)
        print("Patient Name:",self.pname)
        print("Patient ID:",self.pid)
        print("Disease:",self.disease)
        print("No of days admitted:",self.no_of_days_admitted)
        print("-"*15)
        print(" "*15)
while True:
    print(" ===== HOSPITAL PATIENT MANAGEMENT =====")

    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Update Disease")
    print("5. Calculate Bill")
    print("6. Delete Patient")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ")
    if choice == "1":
        n = input("Enter patient name: ")
        pid = int(input("Enter patient ID: "))
        d = input("Enter the disease:")
        dd = int(input("Enter the number of days admitted: "))
        patient = Patient(n,pid,d,dd)
        patients.append(patient)
    elif choice == "2":
        for patient in patients:
            patient.show_details()
    elif choice == "3":
        sp = int(input("enter patient id to be searched:"))
        found =False
        for patient in patients:
            if patient.pid == sp:
                patient.show_details()
                found = True
                print("patient found successfully!")
                break
        if not found:
            print("Invalid patient ID!")
    elif choice == "4":
        pp = int(input("enter patient id whose disease has to be updated: "))
        nd = input("Enter the disease name: ")
        found = False
        for patient in patients:
            if patient.pid == pp:
                patient.disease = nd
                print("disease updated successfully!")
                found = True
                break
        if not found:
            print("Invalid patient ID!")
    elif choice == "5":
        pb = int(input("Enter the patient ID to calculate bill:"))
        found = False
        for patient in patients:
            if patient.pid == pb:
                Charge_per_day = 2000
                Bill = patient.no_of_days_admitted * Charge_per_day 
                print("Patient Name:",patient.pname)
                print("Disease:",patient.disease)
                print("Days Admitted:",patient.no_of_days_admitted)
                print("Total Bill:",Bill)
                print("Bill calculated successfully!")
                found = True
                break
        if not found:
            print("Invalid patient ID!")
    elif choice == "6":
        d = int(input("Enter patient ID to be deleted:"))
        found = False
        for patient in patients:
            if patient.pid == d:
                patients.remove(patient)
                print("Patient deleted successfully!")
                found = True
                break
        if not found :
            print("Invalid patient ID!")
    elif choice == "7":
        print("Exit...")
        break
    else:
        print("Invalid choice!")
               