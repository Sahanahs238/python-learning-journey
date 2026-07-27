try:
    num1=int(input("enter the first number:"))
    num2=int(input("enter the second number"))
    ans = num1/num2
    print(+ans)
except ZeroDivisionError:
    print("cannot devide by zero")
except ValueError:
    print("enter a valid number")