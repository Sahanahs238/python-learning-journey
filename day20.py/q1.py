try:
    num =int(input("enter a number :"))
    print(100/num)
except ZeroDivisionError:
   print("please enter a valid number")