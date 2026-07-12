try:
    age = int(input("Enter your age: "))
    if age <= 0:
        print("Invalid age. Please enter a valid age.")
    else:
        print("Your age is:", age)
except ValueError:
    print("Invalid input. Please enter a valid integer for age.")
finally:
    print("Execution completed.")