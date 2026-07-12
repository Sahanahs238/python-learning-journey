try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a/b
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    print("Execution completed.")