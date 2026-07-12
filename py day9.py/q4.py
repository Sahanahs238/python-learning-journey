try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    operator = input("Enter an operator (+, -, *, /): ")
    if operator == "+":
        result=a+b
        print(result)

    elif operator == "-":
        result=a-b
        print(result)

    elif operator == "*":
        result=a*b
        print(result)

    elif operator == "/":
        result=a/b
        print(result)
    else:
        print("Invalid operator. Please enter a valid operator.")

except ValueError:
    print("Invalid input. Please enter a valid integer.")