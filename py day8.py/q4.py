name = input("Enter your name: ")
age = input("Enter your age: ")
dream = input("Enter your dream: ")

student = open("student.txt", "w")
student.write(name + "\n")
student.write(age + "\n")
student.write(dream + "\n")
student.close()

student = open("student.txt", "r")
content = student.read()
print(content)
student.close()