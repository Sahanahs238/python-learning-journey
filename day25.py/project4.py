tasks = []
while True:
    print("===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    
    choice = input("choose (1 , 2, 3 ,4): ")
    if choice =="1":
        t=input("enter the task: ")
        tasks.append(t)
        print("task added successfully!")
    elif choice =="2":
        if len(tasks) == 0:
            print("no tasks are available")
        else:
            print("the tasks are:")
            for i in range(len(tasks)):
                print(i + 1, tasks[i])
    elif choice=="3":
        print("enter the task to be removed: ")
        index = int(input("Enter task number: "))
        tasks.pop(index - 1)
        print("Task removed successfully!")
    elif choice == "4":
        print("Exit")
        break

    else:
        print("Invalid Choice")



