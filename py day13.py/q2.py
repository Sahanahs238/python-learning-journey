file = open("student.txt","a")
name = input("what is your name \n")
file.write(name + "\n")
file.close()

file = open("student.txt","r")
content = file.read()
print(content)
file.close()
