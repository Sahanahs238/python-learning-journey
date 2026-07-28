class Person:
    def information(self,name,age):
        self.name=name
        self.age=age

class Doctor(Person):
    def information(self,name,age,specialization):
        super().information(name,age)
        self.specialization=specialization

class Patient(Person):
    def information(self,name,age,disease):
            super().information(name,age)
            self.disease=disease
doctor1=Doctor()
patient1=Patient()
def show_details():
    print(doctor1.name)
    print(doctor1.age)
    print(doctor1.specialization)
    print(patient1.name)
    print(patient1.age)
    print(patient1.disease)

while True:
    print("===== HOSPITAL MANAGEMENT =====")

    print("1. Add Doctor")
    print("2. Add Patient")
    print("3. View Details")
    print("4. Exit")

    choice = input("enter your choice(1,2,3,4): ")

    if choice == "1":
         print("enter the information of a doctor to be added: ")
         n =input("enter name: ")
         a = int(input("enter age: "))
         s = input("enter specialization:")
         doctor1.information(n,a,s)
         print("Information added successfully!")
    elif choice == "2":
         print("enter the information of a patient to be added: ")
         n =input("enter name: ")
         a = int(input("enter age: "))
         d = input("enter desiese:")
         patient1.information(n,a,d)
         print("Information added successfully!")
    elif choice=="3":
         show_details()
    elif choice == "4":
        print("exit")
        break
    else:
        print("Invalid choice")
     
     