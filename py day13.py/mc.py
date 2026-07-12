print("1. Write Note")
print("2. Read Notes")
print("3. Exit")
choice = input("choose a number")

if choice =="1":
    file = open("notes.txt","a")
    note = input("enter a note for ur futureself honey")
    file.write(note + "\n")
    file.close()

elif choice == "2":
    file = open("notes.txt","r")
    content = file.read()
    print(content)
    file.close()

elif choice == "3":
    print("good bye")

else:
    print("Invalid choice")



