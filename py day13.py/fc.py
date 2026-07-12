print("1. add student")
print("2. view student")
print("3. Exit")
choice = input("choose a number")

if choice =="1":
    file = open("student.txt","a")
    name = input("enter a student")
    file.write(name + "\n")
    file.close()

elif choice == "2":
    file = open("student.txt","r")
    content = file.read()
    print(content)
    file.close()

elif choice == "3":
    print("good bye")

else:
    print("Invalid choice")



