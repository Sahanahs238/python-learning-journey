try:
    marks = int(input("Enter your marks: "))
    
    if int(marks) < 0 or int(marks)>100:
        print("Invalid marks. Please enter a valid marks.")
    else:
        if marks <= 35:
            print("You have failed the exam.")
        else:
            print("You have passed the exam.")
except ValueError:
    print("Invalid input. Please enter a valid integer for marks.")