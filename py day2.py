a = 20
b=40
print(a+b)
print(a-b)
print(a*b)
print(a/b)

age = input("Enter your age: ")
print("Your age is: " + age)
if int(age) >= 18:
    
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("fail")


a = input("Enter a number: ")
b = input("Enter another number: ")
if int (a) > int (b):
    print(a)
else:
    print(b)


password = input("Enter your password: ")
my_pass = "1234"
if password == my_pass:
    print("Access granted.")
else:
    print("Access denied.")